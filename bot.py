#bas
Contacts = {}
WW = True
Listen_comand = False
comand = ""
operand = ""


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough params"
    return inner
@input_error    
def add(*args):
    new_number = operand
    nn = new_number.split(" ")
    a = nn[0]
    b = nn[1]
    Contacts.update({a : b})
    
    
    

def change(*args):
    new_number = operand
    nn = new_number.split(" ")
    a = nn[0]
    b = nn[1]
    Contacts[a] = b
    
    

def phone(*args):
    name = operand
    result = Contacts[name]
    return result


def main():

    while WW == True:
    
        if Listen_comand == False:
            
            comand = str.lower(input())
            if comand == "hello" and Listen_comand == False:
                Listen_comand = True
                print("How can I help you?")
                comand = str.lower(input())
            else:
                print("listen for hello")
                comand = str.lower(input())
        while Listen_comand == True:
            if comand == "add":
                print("pleese input name and number in format 'name number'")
                operand = input()
                add()
                print("How can I help you?")
                comand = str.lower(input())
            elif comand == "change":
                    print("pleese input name andd number in format 'name number'")
                    operand = input()
                    change()
                    print("How can I help you?")
                    comand = str.lower(input())
            elif comand == "phone":
                    print("pleese input name")
                    operand = input()
                    print(f"{phone}")
                    print("How can I help you?")
                    comand = str.lower(input())
            elif comand == "show all":
                    print(f"{Contacts}")
                    print("How can I help you?")
                    comand = str.lower(input())
            elif comand == "good bye" or comand == "close" or comand == "exit":
                WW = False
                print("Good bye!")
                break
            else:
                print("How can I help you?")
                comand = str.lower(input())

main()




