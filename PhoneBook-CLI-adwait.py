import os
import msvcrt as m

fileName_in = None      #making the holder for the input file name
fileName_chng = None    #making a holder for modified file name
if os.path.isdir("Contacts"):   #Checking if the Contacts fildoer is present or not
    os.chdir("Contacts")    #changing the directory to Contacts if present
else:
    os.mkdir("Contacts")    #else making the directory and then changing the directory to Contacts
    os.chdir("Contacts")

currentPath = os.getcwd()    # for getting the current working directory
    

def check_file():                   #check for the files existence
    if os.path.isfile(fileName_chng):
        print("File exists")
    else:
        print("File was not detected and will be created")

def f_in():             #input for the file name
    global fileName_in
    fileName_in = input("Enter the name of the file: ")
    
    
def c_name():               #modifing the input filename by add .txt to it
    global fileName_chng
    fileName_chng = fileName_in + ".txt"

def openWrite():            #opening the file with append option to add the contacts
    key = "b'y'"
    f = open(fileName_chng,'a')
    check_file()   
    while (key == "b'y'"):
        con_name = input("Enter the contact name: ")
        con_phone = input("Enter the cuntact number: ")
    
        if con_phone.isnumeric() and len(con_phone) == 10:  #checking if the phone number is all numeric ad has 10 digits
            f.write("------------------------------------------\n\tcontact name: " + con_name + " "+"\tcontact number: "+con_phone+"\n------------------------------------------\n")
            print("Entry written press 'y' to add more and any other key to return to the main menu")
        else:
            print("The number you entered is not a 10 digit number\nplease try again")
        key = str(m.getch())     #waiting ofr the user to press y of to press any other key

def listDir():                  #Listing all the records in the Contacts folder
    for names in os.listdir(currentPath):
        print(names)
    
def listEntry():                #listing all the entries in the selected record
    f = open(fileName_chng,"r")
    entry = f.read()
    print(entry)

def searchRecord_num(i,key):            #searching functions to search for name or number

    if i == 1:                  #searching in a specific file for the keyword
        with open(fileName_chng,"r") as f:
            for line in f:
                if key in line:
                    print(line)
    
    elif i == 2:                    #searching in all the files in the directory for the keyword
        for names in os.listdir(currentPath):
            with open(names,"r") as f:
                for lines in f:
                    if key in lines:
                        print(lines)


os.system("cls")
print("This is a PhoneBook CLI Interface made by FUNKY_doc@69\n")
while(1):
    os.system("cls")
    print("This is a PhoneBook CLI Interface made by FUNKY_doc@69\n")
    print("-:Saving ad working directory is " + currentPath+" :-\n")
    print("Please select your option:-")
    print("\t1. Start a new record\n\t2. List all the records\n\t3. List all the entries in a record")
    print("\t4. Search in a record by number\n\t5. Search in a record by name\n\t6. Exit")
    ch = int(input("Selected: "))
    if ch == 1:
        f_in()
        c_name()
        openWrite()
        os.system("cls")

    elif ch == 2:
        print("Geting current working directiry content...Done\nDisplaying\n------------\n")
        listDir()
        print("------------\nend")
        m.getch()
        print("\n")
        
        
    elif ch == 3:
        print("\n To view the contents of the record\n")
        f_in()
        c_name()
        try:
            print("Fetching entries......Done\nShowing\nstart\n---------------------\n")
            listEntry()   
            print("---------------------\nend\npress any key to continue\n...")
            m.getch()
        except FileNotFoundError:
            print("--\nThe file "+str(fileName_chng)+" does not exists\n--")
    elif ch == 4:
        key = None
        print("To search in a specific record press y or to go for all record search press any other key:")
        key = str(m.getch())
        if key == "b'y'":
            f_in()
            c_name()
            keyword = input("Enter the contact number for record search:")
            searchRecord_num(1,keyword)    
        
        else:    
            keyword = input("Enter the contact number for record search:")
            searchRecord_num(2,keyword)    
            
    elif ch == 5:
        key = None
        print("To search in a specific record press y or to go for all record search press any other key:")
        key = str(m.getch())
        if key == "b'y'":
            f_in()
            c_name()
            keyword = input("Enter the contact name for record search:")
            searchRecord_num(1,keyword)    
        
        else:    
            keyword = input("Enter the contact name for record search:")
            searchRecord_num(2,keyword)    
        
    elif ch == 6:
        print("Thank you for using the application")
        exit(0)
                
        
    else:
        print("Invalid input")