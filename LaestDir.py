# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 12:05:03 2019

@author: sayan
"""

import os
import glob
cwd = os.getcwd()
print("Current dir::",cwd)
directory=cwd+"\\Result\\"
latest_res=max(glob.glob(os.path.join(directory, '*/')), key=os.path.getmtime)
print(latest_res)