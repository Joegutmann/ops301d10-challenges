#!/bin/bash

# Script Name:                  Ops Challenge - Challenge: Conditionals in Menu Systems
# Author:                       Joe Gutmann
# Date of latest revision:      30NOV2023
# Purpose:                      Ops Challenge 301: Class 04

#make it do the loopdydo
while :
do
# menu option where the user selects one of these 3 choices.
echo "Choose from one of the below 3 choices to run the command."

#This is to allow the user a chance to read the statement and hopefully understand before printing the three choices
sleep 2 

# Hello world prints to the screen

echo "a) Hello world prints to the screen"

# Ping self using loopback addy

echo "b) Use the Ping command on this computer"

# IP info (print the network adapter info for this computer)

echo "c) Get information about the network adapter of this computer"

#user input - takes the users choice and then launches that script.
read choice

# make it so either A or a works
case "$choice" in

"a" | "A")
echo "Hello world"
;;
"b" | "B")
ping -c 1 127.0.0.1
;;
"c" | "C")
ip a
;;
*)
echo "That was not an option. Choose a, b, or c."
;;
esac
done
#loop continues on and on and on...