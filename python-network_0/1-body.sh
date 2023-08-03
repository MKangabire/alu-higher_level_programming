#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
curl -s -L -I "$1" -w "%{http_code}" | grep "200" -q && curl -sL "$1"
