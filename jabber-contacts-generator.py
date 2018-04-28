#!/usr/bin/env python

import os
import readline

csv_header = 'User ID, User Domain, Contact ID, Contact Domain, Nickname, Group Name \n'
csv_row = "{}, {}, {}, {},, {}\n"

def find_os():
    if os.name == 'nt':
        clear_screen = 'cls'
    else:
        clear_screen = 'clear'
    return clear_screen

def valid_domain(domain):
    is_domain = True
    try:
        domain_split = domain.split('.')
    except:
        is_domain = False
    else:
        for element in domain_split:
            if element.isalnum() == False:
                is_domain = False
    return
    
def get_input():
    clear_screen = find_os()
    getting_input = True
    contact_list = "contacts.txt"
    output_filename = "ImportList.csv"

    while getting_input:
        os.system(clear_screen)
        group_name = input("Enter a group name: ")
        if group_name.upper() == 'EXIT':
            break

        domain = input("Enter domain name: ")
        if domain.upper() == 'EXIT':
            break
        if valid_domain(domain) == False:
            print("Invalid input, try again")
        else:
            getting_input = False
    return[group_name, domain, contact_list, output_filename]
    
def generate_contacts(contacts_file="contacts.txt"):
    contact_list = []
    with open(contacts_file, 'r') as contacts:
        for line in contacts:
            new_line = line.strip('\n')
            contact_list.append(new_line)
    return contact_list
    
def write_csv(contact_list, domain, group, output_filename='ImportList.csv'):
    with open(output_filename, 'w') as contact_csv:
        contact_csv.write(csv_header)
        for user in contact_list:
            for contact in contact_list:
                if user != contact:
                    new_row = csv_row.format(user, domain, contact, domain, group)
                    contact_csv.write(new_row)
    return
    
if __name__ == '__main__':
    domain, group, contact_list, output_filename = get_input()
    contact_list = generate_contacts()
    write_csv(contact_list, domain, group)
