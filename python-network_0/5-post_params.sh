#!/bin/bash
# takes a URL arg sends a POST request and displays the response
curl -s -X POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
