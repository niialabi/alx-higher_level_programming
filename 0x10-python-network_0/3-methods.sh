#!/bin/bash
#  Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -siX OPTIONS $1 | grep "Allow:" | cut -d ' ' -f 2- 
