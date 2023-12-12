#!/usr/bin/python

# put this at the top of every script

#Joe Gutmann
#12.11.23
#Class 11 : Psutil

# install libraries through pip install  psutil. Once it has been installed you do the import psutil

import psutil

#Generate CPU times as a tuple. This can also be done print(f"CPU Time: {psutil.cpu_times()\n}).. these are called f strings
#cputime = psutil.cpu_times()
#print(cputime)

#F strong example
#val = 'Orange'
#print(f"{val} for is the first thing on the list. Please don't forget to get some {val}s.")

# Create a Python script that fetches this information using Psutil:

def ch11():
    cpu_times = psutil.cpu_times()
    return {
# Time spent by normal processes executing in user mode
        "Normal Processes": cpu_times.user,
# Time spent by processes executing in kernel mode
        "Kernal mode": cpu_times.system,
# Time when system was idle
        "Idle": cpu_times.idle,
# Time spent by priority processes executing in user mode
        "Priority processes": cpu_times.nice,
# Time spent waiting for I/O to complete.
        "Waiting time" : cpu_times.iowait,
# Time spent for servicing hardware interrupts
        "Servicing hardware": cpu_times.irq,
# Time spent for servicing software interrupts
        "Servicing Software": cpu_times.softirq,
# Time spent by other operating systems running in a virtualized environment
        "other operating systems": cpu_times.steal,
# Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
        "Running Virtual CPU for guest": cpu_times.guest,
    }

if __name__ == "__main__":
    cpu_stats = ch11()

    for stat, value in cpu_stats.items():
        print(f"{stat}: {value} seconds")

        #Chatgpt was utilized to fix errors and check concepts.