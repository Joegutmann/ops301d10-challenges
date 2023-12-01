#!/bin/bash

# Script Name:                  Ops Challenge - File Permissions
# Author:                       Joe Gutmann
# Date of latest revision:      29NOV2023
# Purpose:                      Ops Challenge 301: Class 03

#Declare variables : // ls is all files //  ls -a includes hidden files // ls -la showsa bunch of info 

# create a file test with.. you can use chmod 777 class03.sh to give all users max permissions. can use +x to add -x to remove

#prompt the user for input for the directory path they want to create

echo "Please enter in the name of the directory you wish to create..."
read DN

mkdir "$DN"

echo "The directory "$DN" has been created"

#what permission level do they want

echo "Please enter in the permissions numer you want, in this case enter in 777 to perform a chmod 777"
read PN
# chmod 777 "$DN"
chmod -R $PN $DN 
# navigate to the directory // print to the screen the directory contents and the new permissions settings of everything in the dir
cd "$DN"
ls -la "$DN"

#watch class video 11.30.23 if you need to review and fix the assignment. This here is not exactly what was uploaded to canvas. or github as of 1158 11.30.23