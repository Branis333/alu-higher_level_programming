#!/bin/bash
# display Content-Length
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
