import os

def find_os():
    if os.name == 'nt':
        clear_screen = 'cls'
    else:
        clear_screen = 'clear'
    return clear_screen

def valid_domain(domain):
    is_domain = True
    try:
        domain_array = domain.split('.')
    except:
        is_domain = False
    else:
        for element in domain_array:
            if element.isalnum() == False:
                is_domain = False
    return
    
def get_input():
    clear_screen = find_os()
    getting_input = True
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
    return[group_name, domain]
    
def generate_contacts():
    contact_array = []
    with open('contacts.txt' , 'r') as contacts:
        for line in contacts:
            append = line.strip('\n')
            contact_array.append(append)
    return contact_array
    
def write_csv(contact_array, domain, group):
    with open('ImportList.csv', 'w') as ImportList:
        ImportList.write('User ID, User Domain, Contact ID, Contact Domain, Nickname, Group Name \n')
        for user in contact_array:
            for contact in contact_array:
                if user != contact:
                    ctString = (user + ', ' + domain + ',' + contact + ',' + domain + ',,' + group + '\n')
                    ImportList.write(ctString)
    return
    
if __name__ == '__main__':

    domain, group = get_input()
    contact_array = generate_contacts()
    write_csv(contact_array, domain, group)
