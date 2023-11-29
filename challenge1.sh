#!/bin/bash

# Script Name:                  Ops Challenge - Append; Date and Time
# Author:                       Joe Gutmann
# Date of latest revision:      11NOV2023
# Purpose:                      Ops Challenge 301: Class 02

# how to show date and time

#running the date command from terminal to give a general output
# copies /var/log/syslog to the current directory

cp /var/log/syslog .

# appends the current date and time to the filename

cp /var/log/syslog "syslog_$(date +'%Y-%m-%d_%H-%M-%S').log"

# echo 'date'

# assign variables

#year='date +%Y'
# echo "We are currently in the year of $year"

# month='date +%m'
# echo "The month is $month"

# day='date +%d'
# echo "Today is the $day"

#put it all together
# echo "current date: $(date)"

# "current date: $day-$month-$year"
# "Current Date: $(date +%d=%m-%Y)"

#how to append this to a file The >> double carrrot will append to the file. > just overwrites the whole thing

# echo "My new string with date: $(date +%d=%m-%Y)" >> test.txt

# to add to the name mv test.txt test-$(date +%d=%m-%Y).txt