#Create a Python script that includes the following:

#Assign to a variable a list of ten string elements.

list = ['iceman', 'wolverine', 'rogue', 'nightcrawler', 'cyclops', 'forge', 'phoenix', 'gambit', 'archangel', 'jubilee']


#Print the fourth element of the list.

print("The fourth X-Men on the list is:", list[3])

#Print the sixth through tenth element of the list.

# print("The sixth through the tenth members on the list are: ", list[5:9])

# I did not like how the above method printed out in brackets. I utilized chatgpt to find alternative ways to print it without the []. https://chat.openai.com/share/5e903e11-329d-4cce-be19-cffdcb9ebc8c

selected_elements = list[5:10]

result_string = ', '.join(selected_elements)

print("The sixth through the tenth members on the list are: ", result_string)

#Change the value of the seventh element to “onion”. utilized the list command here and then copy pasted the above down below to show the change. If I have time I will do the
#stretch, but I have to back track and I don't know if I can tonight. 

list[6] = "magneto"

selected_elements = list[5:10]

result_string = ', '.join(selected_elements)

print("The sixth through the tenth members on the list are: ", result_string)