#!/bin/bash
# script that takes a url, sends a request to the url and
# display the size of the body of the response
curl -s "$1" | wc -c
