#!/usr/bin/python3

import shutil, os

shutil.copy('/root/Dockerfile', '/root/snap')
#shutil.copytree(source, destination) => copy an entire folder from sorce to destination

shutil.move('/root/secret-file', '/root/snap')
print(os.listdir('/root/snap'))
