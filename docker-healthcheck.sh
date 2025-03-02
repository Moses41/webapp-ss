#!/bin/bash
wget -q --spider http://localhost:4444/wd/hub/status
if [ $? -eq 0 ]; then
    exit 0
else
    exit 1
fi
