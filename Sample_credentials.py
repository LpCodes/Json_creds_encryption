import json
import logging
from pathlib import Path

import cryptocode

myfile = Path('sample.json')
logging.basicConfig(level=logging.INFO)

if myfile.is_file():  # checking if file exits
    logging.info("File Already Exits")
else:  # else create it
    logging.info("File not found creating one ")
    with open(myfile, 'w') as file:
        file.write("{}")  # {} required for json file

with open(myfile, 'r') as file:
    my_dict = json.load(file)  # load json  file in memory
# print(my_dict)
my_dict1 = my_dict.copy()  # copy to avoid data changes error
decrypted_dict = {}  # creating empty dict for storing decrypted data
for key, value in my_dict1.items():
    y = cryptocode.decrypt(key, '123')
    x = cryptocode.decrypt(value, '123')

    d1 = {y: x}
    decrypted_dict.update(d1)

# print(decrypted_dict)
username = input("Enter Your User Name\n")

for i in range(3):
    if username in decrypted_dict:
        # logging.info("User Exits\n")
        pwd = input("Enter Your Password\n")
        # print(pwd)
        estoredpwd = decrypted_dict[username]  # for checking correspong password to username
        # print(estoredpwd)
        if estoredpwd == pwd:
            logging.info("Login Succusseful")
            input("")
            break
        else:
            retries = str(2 - i)
            logging.warning("Incorrect Password retry remaing : " + retries)
            if retries == "0":
                logging.error("Sorry You have entered incorrect passwords")

    else:  # if user is not present get data ,encrypt,store
        c = str(input("User does not exits\nDo you want to create account if yes press y or any other key to exit\n"))
        if c == "y":
            username = input(" Enter Username: ")
            password = input(" Enter Password: ")
            eusername = cryptocode.encrypt(username, "123")
            epassword = cryptocode.encrypt(password, "123")
            my_dict.update({eusername: epassword})
            try:
                with open(myfile, 'w') as file:
                    json.dump(my_dict, file, indent=4, sort_keys=True)
                logging.info("Account created successfully")
                input("")
                break
            except Exception as e:
                print(e)
        else:
            break
