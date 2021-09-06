# Telephone Book

my_teleBook = {'1111111111': 'Amal', '2222222222': 'Mohammed', '3333333333': 'Khadijah', '4444444444': 'Abdullah', '5555555555': 'Rawan', '6666666666': 'Faisal', '7777777777': 'Layla'}


def searchByPhone():
    print('********* Search by phone *********')
    while True:
            phone_number = input('Enter the phone number: (10 digits) ')
            if not phone_number.isdigit():
                print('This is invalid number!')
            elif len(phone_number) != 10:
                print('This is invalid number!')
                continue
            else:
                name = getName(phone_number)
                if name == None:
                    print('Sorry, the number is not found..')
                else:
                    print(name)
                break

def searchByName():
    print('********* Search by name *********')
    while True:
            name = input('Enter the name: ')
            if not name.isalpha():
                print('incorrect name! please try again')
            else:
                phone = getPhone(name)
                if phone == None:
                    print('Sorry, the name is not found..')
                else:
                    print(phone)
                break

def addNew():
    print('********* Add new *********')
    while True:
            new_number = input('Enter the phone number: (10 digits) ')
            if not new_number.isdigit():
                print('This is invalid number!')
            elif len(new_number) != 10:
                print('This is invalid number!')
                continue
            else:
                exist = getName(new_number)
                if exist == None:
                    name = input('Enter the name: ')
                    if not name.isalpha():
                        print('incorrect name! please try again')
                    else:
                        my_teleBook[new_number] = name
                else:
                    print('The phone number already exist...')
                break

def getName(phone):
    if phone in my_teleBook:
        return my_teleBook.get(phone, None)

def getPhone(name):
    for phone, n in my_teleBook.items():
        if n == name:
            return phone
            break





print('\n*******************************************************')
print('****************** My Telephone Book ******************')
print('*******************************************************')

ans = True
while ans:
    print('''
1. Search by the phone number.
2. Search by name.
3. Add a new phone number.
4. Exit.\n ''')
    ans = input("What would you like to do? ")
    if ans == "1":
        searchByPhone()
    elif ans == "2":
        searchByName()
    elif ans == "3":
        addNew()
    elif ans == "4":
        print("\n Goodbye")
        ans = False
    elif ans != "":
        print("\n Not Valid Choice Try again")









