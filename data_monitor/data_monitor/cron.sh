#!/bin/bash

line="0 9 * * * python path/to/data_monitor.py"
(crontab -e; echo "$line" ) | crontab -e