import hashlib 
fname = "passwords.txt"

text = " "
running = True 
webname = ""
password = ""
hashed = ""
choice = ""
list_websites = []
list_passwords = []

def reset(): 
    text = " "
    webname = ""
    password = ""
    hashed = ""
    choice = ""

while(running):
    choice = input("What do you want to do? \na to add password. \nr to retrieve password. \nl to look at a list of webiste names \nc to change password. \nf to close program.") 
    if(choice == 'f'): 
        running = False 
    if(choice == 'a'): 
        fileOUT = open(fname,'a') 
        webname = input("What is the name of the website?") 
        password = input("What is the password?") 
        fileOUT.write(webname)
        fileOUT.write(password) 
        fileOUT.close()

    if(choice == 'r'): 
        print(1)
        
    if(choice == 'c'): 
        print(1)
        
    if(choice == 'l'): 
        fileIN = open(fname,'r') 
        text = fileIN.readline() 
        while(text != ""): 
            print(text)
            text = fileIN.readline() 
            text = fileIN.readline() 
        fileIN.close() 

    reset()
