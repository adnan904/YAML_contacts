#!/usr/bin/env python

import yaml
import os
import argparse
import re


yaml_path = 'contacts.yaml'

class Contacts:

    def add_contact(self,contact):
        #Checking if the contact already exists or not, we only add new contacts based on a unique name and phone number combination
        if os.path.exists(yaml_path):
            if self.contact_exists(contact['name'],contact['phone']):
                print("Contact exists already, Try with a new name and phone number combination!",flush=True)
                exit(255)
        #Dumping the new contact to the yaml file, If the file doesnt exist it will create one automatically
        with open(yaml_path, "a") as file_desc:
                yaml.dump(contact, file_desc, default_flow_style=False, explicit_start=True)


    #Prints to the stdout the contact details(if it exists)
    def show_contact(self,name):
        if not os.path.exists(yaml_path):
            print("No Contact present Yet!",flush=True)
            exit(0)

        with open(yaml_path, "r") as file_desc:
            loaded = yaml.safe_load_all(file_desc)
            flag=0
            for contact in loaded:
                if contact['name'] == name:
                    print(yaml.safe_dump(contact, default_flow_style=False))
                    flag=1
            if flag==0:
                print("Contact does not exist")

    #Prints to the stdout all the existing contacts
    def show_all_contacts(self):
        if not os.path.exists(yaml_path):
            print("No Contact present Yet!",flush=True)
            exit(0)
        with open(yaml_path, "r") as file_desc:
            loaded = yaml.safe_load_all(file_desc)
            print(yaml.safe_dump_all(loaded, default_flow_style=False))

    #Checks whether the contact by the provided name exists or not
    def contact_exists(self,name,phone):
        with open(yaml_path, "r") as file_desc:
            loaded = yaml.safe_load_all(file_desc)
            for contact in loaded:
                if contact['name'] == name and contact['phone'] == phone:
                    return True
            return False

    #Regular Expression matching to validate input
    def isAccordingToExpr(self, expression, input):
        if (re.match(expression, input) is None):
            return False
        else:
            return True

    #This function handles the inputs from command line
    def handle_request(self,args):
        if args.add:
            if (not args.number or not args.email):
                print("Invalid Input! '--add' needs '--number' and '--email'", flush=True)
                exit(255)
            #validating Input Name, Only lowercase and uppercase alphabets allowed
            if not self.isAccordingToExpr("^[a-zA-Z ]+$",args.add):
                print("Invalid Name",flush=True)
                exit(255)

            #validating Number , Only Integers with an option of leading + allowed
            if not self.isAccordingToExpr("^[+]?[0-9]+$", args.number):
                print("Invalid Number",flush=True)
                exit(255)

            #Validating E-mail address
            if not self.isAccordingToExpr("^[^@]+@[^@]+\.[^@]+$", args.email):
                print("Invalid E-mail",flush=True)
                exit(255)


            if not args.address:
                data = {'name': args.add, 'phone': args.number, 'email': args.email}
            else:
                data = {'name': args.add, 'phone': args.number, 'email': args.email, 'address' : args.address}

            self.add_contact(data)
            print("Contact Added", flush=True)

        if args.list:
            self.show_all_contacts()

        if args.show:
            self.show_contact(args.show)

def main():
    try:
        parser = argparse.ArgumentParser()
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--show', type=str, help="Shows the contact based on the given name provided as argument")
        group.add_argument('--list', action='store_true', help= "Prints all the contacts")
        group.add_argument('--add', type=str, help="Adds a new contact by this name")
        parser.add_argument('--number', help="The Phone Number  for the new contact")
        parser.add_argument('--email', type=str, help="Email address for the new contact")
        parser.add_argument('--address', type=str, help="Address for the new contact")
        args = parser.parse_args()
        contact = Contacts()
        contact.handle_request(args)
    except argparse.ArgumentTypeError as e:
        print(e,flush=True)

if __name__ == '__main__':
    main()