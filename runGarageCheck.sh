#!/bin/bash

cd /media/disk1/piBatch

COMMAND="python garageCheck.py >> /media/disk1/logs/checkGarage.log 2>&1 "
$COMMAND &


