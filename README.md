# YAML_contacts
A Python3 program that maintains a list of Contacts(Name,Phone#,E-Mail) in a YAML structured file


### Installing

To install the tool, run the following commands from Command Line:

```
git clone git@github.com:adnan904/YAML_contacts.git
cd YAML_contacts
python setup.py install
```

or Download the repository from GitHub and then run the command:

```
python setup.py install
```

**On Ubuntu use the following command (after making sure pip3 is installed, which will also install setuptools):**

```
sudo python3 setup.py install
```


### Usage

A contact has the following attributes:
- name
- number
- email
- address(optional)

The Tool right now supports the following functionality:

1. **Adding a contact**
    ```
    pycontacts --add "Name" --number 1234 --email abc@xyz.com 
   ```
    - name , number & email are mandatory fields
    - name can be only Lowercase and Uppercase alphabets
    - number only allows integers with an optional leading '+' (if needed)
    - email has to be of the format `anything@anything.anything` 
    - Contacts need to have unique name + number combination, so the below contacts would be valid:
        - David, 1234 , `abc@xyz.com`
        - David, 12345, `abcd@xyz.com`
      
   **Address** can also be added to a contact using the command:
    ```
    pycontacts --add "Name" --number 1234 --email abc@xyz.com --address "Address"
   ```

2. **Showing a contact**
    ```
    pycontacts --show "Name"  
    ```
      - Displays all the contacts with name = *Name* (if any exists)

3. **Showing all contacts**
    ```
    pycontacts --list  
    ```
      - Displays all the contacts in the contacts.yaml file
      
 ### Author 
   **Adnan Manzoor**
