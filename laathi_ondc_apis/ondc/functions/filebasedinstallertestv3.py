import pip
from pip._internal.req import parse_requirements
import uuid

# Path to your requirements file
# intialPath = "c:\\Users\\Omkar Bhamare\\OneDrive\\Documents\\Laathi-ONDC\\laathi_ondc_apis\\ondc\\functions\\"
requirements_file = "c:\\Users\\Omkar Bhamare\\OneDrive\\Documents\\Laathi-ONDC\\laathi_ondc_apis\\ondc\\functions\\requirements.txt"

# Parse and install the requirements
reqs = parse_requirements(requirements_file, session="my_session")
for req in reqs:
    # Use req.requirement instead of req.req
    pip.main(["install", str(req.requirement)])


import os
import json
import datetime
import logging


# Define the value you want to assign to REQUEST_BODY_PATH

request_body_path = "c:\\Users\\Omkar Bhamare\\OneDrive\\Documents\\Laathi-ONDC\\laathi_ondc_apis\\ondc\\functions\\request_body_raw_text.txt"
g = open(request_body_path, "r")
request_body_raw_text = g.read()

#print("In cryptic_utils.py")
# Parse the JSON content into a dictionary
data = json.loads(request_body_raw_text)
oldDate = data["context"]["timestamp"]
newDate = datetime.datetime.now().isoformat()
newDate = newDate[:-3]
newDate = newDate+"Z"
# print(data)
# Modify a field within the dictionary
#data["context"]["timestamp"] = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
data["context"]["timestamp"] = newDate

# Convert the dictionary back to JSON
updated_json = json.dumps(data)  # Use indent to format the JSON for better readability
  # Combine the lines into a new content
#new_content2 = "\n".join(updated_json)
# Write the updated JSON content back to the file

# Generate unique IDs for message_id and transaction_id
message_id = str(uuid.uuid4())
transaction_id = str(uuid.uuid4())

# Update message_id and transaction_id in the JSON data
data["context"]["message_id"] = message_id
data["context"]["transaction_id"] = transaction_id

with open(request_body_path, 'w') as json_file:
    json_file.write(updated_json)




# Set the environment variable
os.environ["REQUEST_BODY_PATH"] = request_body_path

# Now, REQUEST_BODY_PATH is available as an environment variable



import subprocess

# # Define the command to run your Python script
# command = ["python", "cryptic_utils.py", "generate_key_pairs"]

# # Run the command and capture its output
# result = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# # Check for any errors
# if result.returncode == 0:
#     # Print the captured output
#     print("Output:")
#     print(result.stdout)
# else:
#     # Print any errors
#     print("Error:")
#     print(result.stderr)


# results=result.stdout
# # Split the string into substrings using "\n" as the delimiter
# substrings = results.split("\n")
# i=0
# # Now, the 'substrings' list contains the 4 sub-strings
# for i in [0,1,2,3]:
#     if i==0:
#         Private_key=substrings[i]
#         Private_key=Private_key[21:]
#         print("Private_key:")
#         print(Private_key)
#     else:
#         if i==1:
#             Public_key = substrings[i]
#             Public_key= Public_key[21:]
#             print("Public_key:")
#             print(Public_key)
#         else:
#             if i==2:
#                 Crypto_private_key = substrings[i]
#                 Crypto_private_key=Crypto_private_key[21:]
#                 print("Crypto_private_key:")
#                 print(Crypto_private_key)
#             else:
#                 Crypto_public_key=substrings[i]
#                 Crypto_public_key=Crypto_public_key[21:]
#                 print("Crypto_public_key:")
#                 print(Crypto_public_key)

#     # print(substring)



# Set the environment variable
#os.environ["PRIVATE_KEY"] = Private_key
os.environ["PRIVATE_KEY"] = "JwpJm1tU4Ga9lsFfAP4NtrzrdApHeCRA2mPEqUvNTEJtGpoAKjWMC19tWqIgHTJPxexZdQ8eSsAmm5gtzXvM1w=="
signing_private_key = os.getenv("PRIVATE_KEY")
# Set the environment variable
#os.environ["PUBLIC_KEY"] = Public_key
os.environ["PUBLIC_KEY"] = "bRqaACo1jAtfbVqiIB0yT8XsWXUPHkrAJpuYLc17zNc="
signing_public_key = os.getenv("PUBLIC_KEY")

# Set the environment variable
#os.environ["CRYPTO_PRIVATE_KEY"] = Crypto_private_key
os.environ["CRYPTO_PRIVATE_KEY"] = "MC4CAQAwBQYDK2VuBCIEIIibBH5rIMraD0wVA9mhmvgE7PECEJxkQyQGL1LrWwlA"
Crypto_private_key = os.getenv("CRYPTO_PRIVATE_KEY")
# Set the environment variable
#os.environ["CRYPTO_PUBLIC_KEY"] = Crypto_public_key
os.environ["CRYPTO_PUBLIC_KEY"] = "MCowBQYDK2VuAyEAQ8Rnhy+uIv0lWJjq+odncx4xPg95QCvrKzoWPO6Q3SI="
Crypto_public_key = os.getenv("CRYPTO_PUBLIC_KEY")

os.environ["SUBSCRIBER_ID"] = "laathi.com"
os.environ["UNIQUE_KEY_ID"] = "731"
 # subscriber_id = os.getenv("SUBSCRIBER_ID", "buyer-app.ondc.org")
 # unique_key_id = os.getenv("UNIQUE_KEY_ID", "207")


# Define the command to run your Python script
logging.basicConfig(filename='my_log2.log',level=logging.DEBUG)
#command2p0 = ["logging.basicConfig(level=logging.DEBUG)"]

#result3p0 = subprocess.run(command2p0, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
cryptic_utils_path = "c:\\Users\\Omkar Bhamare\\OneDrive\\Documents\\Laathi-ONDC\\laathi_ondc_apis\\ondc\\functions\\cryptic_utils.py"

command2 = ["python", cryptic_utils_path, "create_authorisation_header"]

# Run the command and capture its output
result3 = subprocess.run(command2, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Check for any errors
if result3.returncode == 0:
    # Print the captured output
    print("Output of create_authorization_header:")
    print(result3.stdout)
else:
    # Print any errors
    print("Error of create_authorization_header:")
    print(result3.stderr)


results2=result3.stdout

# results2=results2.replace("\\",'')
# Define the command to run your Python script
results3 = 1;
command3 = ["python", cryptic_utils_path, "verify_authorisation_header", results2]

# Run the command and capture its output
result4 = subprocess.run(command3, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Check for any errors
if result4.returncode == 0:
    # Print the captured output
    print("Output of verify authorization header:")
    print(result4.stdout)
    results3=result4.returncode
else:
    # Print any errors
    print("Error of verify authorization header:")
    print(result4.stderr)





 #Define the command to run your Python script
command4 = ["python", cryptic_utils_path, "encrypt", Crypto_private_key, Crypto_public_key, "NULL"]

# Run the command and capture its output
result5 = subprocess.run(command4, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(result5)
# Check for any errors
if result5.returncode == 0:
    # Print the captured output
    print("Output of encrypt:")
    print(result5.stdout)
else:
    # Print any errors
    print("Error of encrypt:")
    print(result5.stderr)

results4=result5.stdout



 #Define the command to run your Python script
command5 = ["python", cryptic_utils_path, "decrypt", Crypto_private_key, Crypto_public_key, results4]

# Run the command and capture its output
result6 = subprocess.run(command5, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(result5)
# Check for any errors
if result6.returncode == 0:
    # Print the captured output
    print("Output of decrypt:")
    print(result6.stdout)
else:
    # Print any errors
    print("Error of decrypt:")
    print(result6.stderr)


results5=result6.stdout

import json
import requests

url = "http://127.0.0.1:5000/search"


# original_string = results2
# character_to_remove = ""
# new_string = original_string.strip(character_to_remove)
# print(new_string)


results2 = results2[1:]
results2 = results2[:-2]

print(results2)
# print(results3)

if results3 == 0:
    header = {
        'Authorization': results2,
        'Content-Type': 'application/json',
        }

    # import cryptic_utils

    with open('c:\\Users\\Omkar Bhamare\\OneDrive\\Documents\\Laathi-ONDC\\laathi_ondc_apis\\ondc\\functions\\request_body_raw_text.txt', 'r') as json_file:
        my2data = json.load(json_file)
    #Make the HTTP request with the headers
    #response = requests.post(url, headers=headers, json=data)


    data = my2data
    # with old search url:
    # when data is results4, get 500 error, Internal server error
    # when data is my2data, get 200 status
    # with new search url:
    # when data is my2data, get 500 error, something went wrong error
    # when data is results4, get 500 error, internal server error
    print("\n")
    print(data)
    print("\n")
    print(header)
    response = requests.post(url, headers=header, json=data)

    # Process the response
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.text)
    print("Requested Data:", response)
else:
    print('Invalid authorization header generated')
