#!/bin/bash
# body size
curl -sI "$1" | grep -i Content-Length | cut -d ' ' -f 2
