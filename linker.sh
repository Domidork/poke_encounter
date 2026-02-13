#!/bin/bash

dir=$(pwd)/main.py
ln -s $dir ~/poke && echo "Successfully linked to home!" || echo "Failed to link!"
exit
