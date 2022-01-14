#!/usr/bin/python3

import shutil, os

shutil.copy('/root/Dockerfile', '/root/snap')
print(os.listdir('/root/snap'))
