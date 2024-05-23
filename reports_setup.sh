#!/bin/bash

DIRECTORY="reports"
if [ ! -d "$DIRECTORY" ]; then
  mkdir $DIRECTORY 
fi
cd reports
touch report_frankenstein.txt
touch report_metamorphosis.txt
