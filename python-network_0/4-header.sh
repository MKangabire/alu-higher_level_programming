#!/bin/bash
# Sends a GET request to URl argument with header values
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
