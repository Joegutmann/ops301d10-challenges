#!/usr/bin/python

#Joe Gutmann
#12.12.23
#Class 12 : Ops Challenge Python Requests Library

import requests
from colorama import init, Fore, Style

# Initialize colorama for colored text. I wanted to pretty up the code so I utilized chatgpt to 
# figure out how to add some colors. I still was not happy with the simplicity so I figured out
# how to add the status codes to explain what the 200/401 and what not were so I didn't have
# to keep looking them up. 
init(autoreset=True)

# Function to get user input with colored prompt
def get_input(prompt, color):
    return input(f"{color}{Style.BRIGHT}{prompt}{Style.RESET_ALL}: ")

# Function to do the above translatin
def translate_status_code(status_code):
    status_codes = {
        200: "OK",
        201: "Created",
        204: "No Content",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Site not found",
        500: "Internal Server Error",
    }
    return status_codes.get(status_code, "Not a valid choice")

# Prompt the user for the destination URL. I forgot to add the https portion
# but after getting bad results I added the https:// portion to prevent user error.

address = get_input("Type your desired URL (format: google.com)", Fore.CYAN)
user_url = str('https://' + address)  # Create the complete URL

# Prompt the user to fulfil the challenge requirements here.
http_methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"]
print(f"Select an HTTP Method:")
for i, method in enumerate(http_methods, start=1):
    print(f"{i}. {method}")

choice = get_input("Please enter the number of your choice", Fore.GREEN)

# Validate the input, user error is no good
try:
    choice = int(choice)
    if choice < 1 or choice > len(http_methods):
        raise ValueError("Invalid choice")
except ValueError:
    print(f"{Fore.RED}Invalid choice. Please select again (1-{len(http_methods)}).")
else:
    selected_method = http_methods[choice - 1]

# Print the entire request to confirm before executing it.
print(f"\nYou are about to send the following request:")
print(f"URL: {user_url}")  # Use the user's complete URL
print(f"HTTP Method: {selected_method}")

# get confirmation before we continue on
confirmation = get_input("Do you want to proceed? (yes/no)", Fore.YELLOW)

if confirmation.lower() == "yes":
    # Perform the request
    try:
        response = requests.request(selected_method, user_url)  # Use the complete URL
        # Translatgoogle status code
        status_text = translate_status_code(response.status_code)

        print(f"\nResponse Information:")
        print(f"Status Code: {response.status_code} - {status_text}")
        print(f"Response Headers:\n{response.headers}")
    except requests.RequestException as e:
        print(f"{Fore.RED}An error occurred while making the request: {str(e)}")
else:
    print(f"{Fore.RED}Request cancelled by the user.")

# end of challenge 12. I don't think i got the colors to work throughout, but it was
#worth a shot but I think I went wrong somewhere in this attempt.