#!/usr/bin/python3


"""
 ****************************** THIS SCRIPT CREATES COPIES FILES ADDING AN UNIQUE NUBER TO EACH******************************
"""
import shutil

for i in range(600):
    shutil.copy('path/documentName.txt',
                'newpath/newdocumentName{}.txt'.format(i+1))
