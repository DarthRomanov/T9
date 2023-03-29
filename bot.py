# #bas
contacts = {}
# WW = True
# Listen_comand = False
# comand = ""
# operand = ""


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough params"
    return inner


@input_error    
def add(*args):
    # new_number = operand
    # nn = new_number.split(" ")
    name = args[0]
    phone = args[1]
    contacts.update({name : phone})
    return f"Contact {name} with phone {phone} add successful"
    
    
def change(*args):
    # new_number = operand
    # nn = new_number.split(" ")
    name = args[0]
    new_phone = args[1]
    contacts[name] = new_phone
    
    

def phone(*args):
    return contacts[args[0]]
    # name = args[0]
    # result = contacts[name]
    # return result

def exit(*args):
    return 'Bye'

def no_command(*args):
    return 'Unknown command. Try again'


def parse_input(text):
    text_command = text.split()[0].lower()
    match text_command:
        case 'add':
            return add, text[len('add'):].split()
        case 'change':
            return change, text[len('change'):].split()
        case 'phone':
            return phone, text[len('phone'):].split()
        case 'exit':
            return exit, text[len('exit'):].split()
    return no_command, []
    

def main():
    while True:
        user_input = input(">>>")
        
        command, data = parse_input(user_input)
        
        print(command(*data))
        
        if command == exit:
            break

    # while WW == True:
    
    #     if Listen_comand == False:
            
    #         comand = str.lower(input())
    #         if comand == "hello" and Listen_comand == False:
    #             Listen_comand = True
    #             print("How can I help you?")
    #             comand = str.lower(input())
    #         else:
    #             print("listen for hello")
    #             comand = str.lower(input())
    #     while Listen_comand == True:
    #         if comand == "add":
    #             print("pleese input name and number in format 'name number'")
    #             operand = input()
    #             add()
    #             print("How can I help you?")
    #             comand = str.lower(input())
    #         elif comand == "change":
    #                 print("pleese input name andd number in format 'name number'")
    #                 operand = input()
    #                 change()
    #                 print("How can I help you?")
    #                 comand = str.lower(input())
    #         elif comand == "phone":
    #                 print("pleese input name")
    #                 operand = input()
    #                 print(f"{phone}")
    #                 print("How can I help you?")
    #                 comand = str.lower(input())
    #         elif comand == "show all":
    #                 print(f"{Contacts}")
    #                 print("How can I help you?")
    #                 comand = str.lower(input())
    #         elif comand == "good bye" or comand == "close" or comand == "exit":
    #             WW = False
    #             print("Good bye!")
    #             break
    #         else:
    #             print("How can I help you?")
    #             comand = str.lower(input())

if __name__ == '__main__':
    main()




