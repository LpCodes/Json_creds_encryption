## Json_creds_encryption

This script is designed to create and manage user accounts using JSON file as a database. It uses the json and pathlib modules to read and write data to a JSON file. The cryptocode module is used to encrypt and decrypt user passwords.

### Getting Started
To use this script, you will need to have Python installed on your machine. You can download it from the official website (https://www.python.org/downloads/).

Once you have installed Python, you can clone the repository or copy the script to your local machine.

Before running the script, you should make sure that you have the json and pathlib modules installed. If you don't have them, you can install them using pip:

```
pip install pathlib
You will also need to install the cryptocode module to encrypt and decrypt user passwords:
```

### How to Use
To use this script, open the terminal or command prompt and navigate to the directory where the script is saved. Then run the script using the command:
```
python script_name.py
```
When the script is run, it checks if the JSON file sample.json exists. If the file exists, it loads the data from the file into a dictionary. If the file does not exist, it creates a new file and writes an empty dictionary to the file.

The script then asks the user to enter their username. If the username is found in the dictionary, the script asks the user to enter their password. If the password is correct, the script logs in the user. If the password is incorrect, the script allows the user to retry entering their password up to three times. If the user enters the wrong password three times, the script displays an error message and exits.

If the username is not found in the dictionary, the script asks the user if they want to create an account. If the user chooses to create an account, the script asks the user to enter their username and password. The script then encrypts the username and password using cryptocode and adds the encrypted data to the dictionary. The dictionary is then written to the JSON file. If the user chooses not to create an account, the script exits.
