# Are you there? We’ve opened up a communications link to The Fender‘s secret computer. We need you to write a program that will read in the compromised usernames and passwords that are stored in a file called "passwords.csv". First import the CSV module, since we’ll be needing it to parse the data.
import csv

# We need to create a list of users whose passwords have been compromised, create a new list and save it to the variable compromised_users.
compromised_users = []

# Next we’ll need you to open up the file itself. Store it in a file object called password_file.
with open("passwords.csv") as password_file:
  # Pass the password_file object holder to our CSV reader for parsing. Save the parsed csv.DictReader object as password_csv.
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    #Inside your for loop, print out password_row['Username']. This is the username of the person whose password was compromised. Run your code, do you see a list of usernames?
    # print(password_row['Username'])
    # Remove the print statement. We want to add each username to the list of compromised_users. Use the list’s .append() method to add the username to compromised_users instead of printing them.
    compromised_users.append(password_row['Username'])

# Exit out of your with block for "passwords.csv". We have all the data we need from that file. 
# Start a new with block, opening a file called compromised_users.txt. Open this file in write-mode, saving the file object as compromised_user_file.
with open("compromised_users.txt", "w") as compromised_user_file:
  # Inside the new context-managed block opened by the with statement start a new for loop. Iterate over each of your compromised_users.
  for compromised_user in compromised_users:
    # Write the username of each compromised_user in compromised_users to compromised_user_file.
    compromised_user_file.write(compromised_user)



# Your boss needs to know that you were successful in retrieving that compromised data. We’ll need to send him an encoded message over the internet. Let’s use JSON to do that.
# First we’ll need to import the json module.
import json

# Open a new JSON file in write-mode called boss_message.json. Save the file object to the variable boss_message.
with open("boss_message.json", "w") as boss_message:
  boss_message_dict = {
    "recipient": "The Boss",
    "message": "Mission Success"
  }
  json.dump(boss_message_dict, boss_message)
  
# Now that we’ve safely recovered the compromised users we’ll want to remove the "passwords.csv" file completely.
# Create a new with block and open "new_passwords.csv" in write-mode. Save the file object to a variable called new_passwords_obj.
with open("new_passwords.csv", "w") as new_passwords_obj:
  slash_null_sig = """
   _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
  """
  new_passwords_obj.write(slash_null_sig)
