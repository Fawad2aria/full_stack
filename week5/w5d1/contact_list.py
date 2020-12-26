
def load(path):

    contacts = []
    with open(path, 'r') as file:
        text = file.read() 
    lines = text.split('\n') 
    header = lines[0].split(',') 
    for i in range(1, len(lines)): 
        row = lines[i].split(',') 
        contact = dict(zip(header, row)) 
        contacts.append(contact)

    return contacts, header


def save(contacts, path, header):
    
    lines = [','.join(header)]
    for contact in contacts:
        row = ','.join(contact.values()) 
        lines.append(row)  

    csv = '\n'.join(lines) 

    with open(path, 'w') as file:
        file.write(csv)


def print_contact(contact):
  
    for key in contact:
        print(f'{key}: {contact[key]}', end='\n\n')


def find_contact(contacts, name):

    for i, contact in enumerate(contacts):
        if contact['name'] == name:
            return i
    return -1


def create(contacts, contact):

    contacts.append(contact)
    return contacts[-1]


def read(contacts, name):

    read_contact = find_contact(contacts, name)
    if read_contact > -1:
        return contacts[read_contact]


def update(contacts, name, updated_info):

    update_contact = find_contact(contacts, name)
    if update_contact > -1:
        contacts[update_contact].update(updated_info)
        return contacts[update_contact]


def delete(contacts, name):

    delete_contant = find_contact(contacts, name)
    if delete_contant > -1:
        return contacts.pop(delete_contant)


def main():

    path = 'contact_list.csv'
    contacts, header = load(path)

    while True:
        help_info = input('For more information enter help or press enter to continue... ')
        if help_info == "help":
            print('''use these commands 
            create: to create contacts 
            read: to retrieve contacts 
            update: to update contacts
            print: to print the contact list
            exit: to exit
            delete: to delete
            ''')

        command = input("What operation would you like to perform? ").strip().lower()

        if command == 'exit':
            break

        elif command == 'create' or command == 'update':
            contact = {}
            for attribute_name in header:
                attribute_value = input(f"What is the contact's {attribute_name}? ")
                contact[attribute_name] = attribute_value

            if command == 'create':
                create(contacts, contact)
            else:
                contact = {k:v for (k,v) in contact.items() if v}
                update(contacts, contact['name'], contact)

        elif command == 'read':
            contact_name = input("What is the contact's name you'd like to retrieve? ")
            contact = read(contacts, contact_name)
            if contact:
                print_contact(contact)
            else:
                print(f'{contact_name} not in contact list')

        elif command == 'delete':
            contact_name = input("What is the contact's name you'd like to delete? ")
            delete(contacts, contact_name)

        elif command == 'print':
            for contact in contacts:
                print_contact(contact)

    save(contacts, path, header)


main()