#!/bin/bash
#  Bash Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -siX OPTIONS $1 | grep "Allow:" | cut -d ' ' -f 2- 