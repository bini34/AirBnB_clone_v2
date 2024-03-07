#!/usr/bin/python3
"""script that generates a .tgz archive
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """script that generates a .tgz archive
    from the contents of the web_static
    folder of your AirBnB Clone repo
    """
    if not os.path.exists("versions"):
        local("mkdir versions")
    now = datetime.now()
    name = "versions/web_static_{}.tgz".format(
        now.strftime("%Y%m%d%H%M%S")
    )
    cmd = "tar -cvzf {} {}".format(name, "web_static")
    result = local(cmd)
    if not result.failed:
        return name
