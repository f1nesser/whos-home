#!/bin/bash
echo $1
mkdir $1-movie
cd $1-movie

sudo python3 camera.py $1
convert --delay 20 -loop 0 $1*.jpg $1.gif
