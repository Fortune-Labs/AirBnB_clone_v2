#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from web_static folder
"""
from fabric.api import local
from datetime import datetime
from os.path import exists


def do_pack():
    """
    Generates a .tgz archive from web_static folder
    Returns the path of the archive if successful, None otherwise
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(timestamp)

    local("mkdir -p versions")
    result = local("tar -cvzf {} web_static".format(archive_name))

    if exists(archive_name):
        print("web_static packed: {} -> {}Bytes".format(archive_name, result.stdout.split()[-2]))
        return archive_name
    else:
        return None
