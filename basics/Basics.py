fname = "basics/passwords.txt"

text = " "
running = True 
webname = ""
password = ""
website = ""
hashed = ""
choice = ""
numChoice = 0
list_websites = []
list_passwords = []


def reset(): 
    text = " "
    webname = ""
    password = ""
    website = ""
    hashed = ""
    choice = ""
    numChoice = 0

def readPasswords(): 
    counter = 0
    fileIN = open(fname,'r')
    text = fileIN.readline()
    while(text != ""): 
        if(counter%2 == 0): 
            list_websites.append(text)
        if(counter%2 == 1): 
            list_passwords.append(text)
        text = fileIN.readline()
        counter += 1
    fileIN.close()
    
def numOf(site, list): 
    counter = 0
    for website in list:
        if(site == website): 
            return counter
        counter += 1 
    return -1


while(running):
    reset()
    for i in range(3):
        print()
    choice = input("What do you want to do? \na to add password. \nr to retrieve password. \nl to look at a list of webiste names \nc to change password. \nf to close program.") 
    if(choice == 'f'): 
        running = False 

    if(choice == 'a'): 
        fileOUT = open(fname,'a') 
        webname = input("What is the name of the website? ") 
        password = input("What is the password? ") 
        fileOUT.write(webname + "\n")
        fileOUT.write(password + "\n") 
        fileOUT.close()

    if(choice == 'r'): 
        readPasswords()
        website = input("What is the password? ") 
        numChoice = numOf(website) 
        if(numChoice == -1): 
            print("Website does not exist. Ensure website is spelled properly and/or exists.")
        else: 
            print(list_passwords[numChoice])
        
    if(choice == 'c'): 
        readPasswords() 
        website = input("What is the website? ") 
        numChoice = numOf(password) 
        password = input("New password? ")
        
        
    if(choice == 'l'): 
        fileIN = open(fname,'r') 
        text = fileIN.readline() 
        while(text != ""): 
            print(text)
            text = fileIN.readline() 
            text = fileIN.readline() 
        fileIN.close() 