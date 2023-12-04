#!/bin/bash

#Tasks
#Write a bash script that performs the following tasks:

#Print to the screen the file size of the log files before compression

#/var/log/syslog

# Get the size of the file in bytes
size_in_bytes=$(stat -c %s /var/log/syslog)

# Convert bytes to megabytes
size_in_mb=$(echo "scale=2; $size_in_bytes / (1024 * 1024)" | bc)

# Print the size in MB
echo "Size of /var/log/syslog before compression: ${size_in_mb}MB"


#/var/log/wtmp
size_in_bytes=$(stat -c %s /var/log/wtmp)

size_in_mb=$(echo "scale=2; $size_in_bytes / (1024 * 1024)" | bc)

echo "Size of /var/log/wtmp before compression: ${size_in_mb}MB"
#The file name should contain a time stamp with the following format -YYYYMMDDHHMMSS

#Compress the contents of the log files listed below to a backup directory
timestamp=$(date "+%Y%m%d%H%M%S")

mkdir -p /var/log/backup
mv /var/log/wtmp /var/log/backup/wtmp_${timestamp}.log
gzip /var/log/backup/wtmp_${timestamp}.log
>/var/log/wtmp

#Other log file

timestamp=$(date "+%Y%m%d%H%M%S")

mkdir -p /var/log/backup
mv /var/log/syslog /var/log/syslog_${timestamp}.log
gzip /var/log/syslog_${timestamp}.log
>/var/log/syslog

#Example: /var/log/backups/syslog-20220928081457.zip
#Hint: gzip is a preinstalled Linux application for performing zip formatted compression.
#gzip -f filename (-f is for force or can be done --force)
#Clear the contents of the log file

#Print to screen the file size of the compressed file
# Get the size of the file in bytes
size_in_bytes=$(stat -c %s /var/log/syslog_${timestamp}.log)
size_in_bytes=$(stat -c %s /var/log/backup/wtmp_${timestamp}.log)
# Convert bytes to megabytes
size_in_mb=$(echo "scale=2; $size_in_bytes / (1024 * 1024)" | bc)

# Print the size in MB
echo "Size of /var/log/syslog before compression: ${size_in_mb}MB"


#Compare the size of the compressed files to the size of the original log files

mv /var/log/wtmp "$backup_dir/wtmp-$timestamp.log"
gzip "$backup_dir/wtmp-$timestamp.log"

# Clear the contents of /var/log/wtmp
>/var/log/wtmp

# Print the file size of the compressed files
