#!/bin/sh unzip file, and save in where zip files located 
for f in `find . -name *.zip`
do
	n=(`echo $f | tr '.' ' '`)
	unzip $f -d .${n[0]}
done

