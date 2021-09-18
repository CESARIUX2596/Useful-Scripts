#! /bin/bash
# This script changes names of all files in a folder to lowercase

for f in *;
do 
mv -v $f `echo $f | tr '[A-Z]' '[a-z]'`;
done