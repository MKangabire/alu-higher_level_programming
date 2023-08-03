#!/bin/bash
# takes an argument URL and displays all allowed methods
curl -sI -X OPTIONS "$1" | grep -i allow | cut -d ' ' -f 2-
