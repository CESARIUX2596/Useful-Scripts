#!/bin/bash

# target="D:\Stuff\Documents\Projects\Repaso_Estructura_de_Datos"
target = PATH
pushd "$target" > /dev/null
let count=0
for f in *
do
    echo $f
    let count=count+1
done
popd
echo ""
echo "Count: $count"