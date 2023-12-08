# Joe Gutmann
# 12.8.23
# Ops Challenge: Python File Handling

import os

def cndf(filename):

#Using file handling commands, create a Python script that creates a new .txt file, appends three lines, prints to the screen the first line, then deletes the .txt file.

# Create a new .txt file and appends three lines.

    with open(filename, "w") as file:
        file.write("The X-Men franchise is a popular series of superhero movies and comics.\n")
        file.write("It revolves around mutants, individuals with superhuman abilities, who are often misunderstood and face discrimination from regular humans.\n")
        file.write("Themes of acceptance, identity, and the struggle between mutants and humans are common throughout the series.\n")

#print the first line

    with open(filename, "r") as file:
        first_line = file.readline()
        print("First Line:", first_line)

#delete the .txt file

    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' deleted.")
    else:
        print(f"File '{filename}' does not exist.")

filename = input("Enter your desired filename. i.e. file.txt: ")

    #end it
cndf(filename)