#Assignment 1 By Leorenzo Openano
#The input from the user has no checks this can create bugs which may be unpredictable
#The program will work correctly with precise input

#variables for usesinput and tables for entries
userinput = None
#This is the main table that holds all entries There are initial values here for testing purposes
#The program may error if the table is empty
Maintable = [{'First_Name':'Joe','Last_Name':'Rogan','CWID': '56314','ClassID':'class1'},
            {'First_Name':'Dylan','Last_Name':'Charles','CWID':'90324','ClassID':'class2'},
            {'First_Name':'Kevin','Last_Name':'Carl','CWID':'49813','ClassID':'class2'},
            {'First_Name':'Mike','Last_Name':'Johnson','CWID':'23135','ClassID':'class3'},]

#This table holds all correlations between classID and CWID
ClassCWIDtable = {'class1':{'56314'},'class2':{'90324', '49813'},'class3':{'23135'}}


#This Function Takes newly created student entries and adds them to the appropriate place on the ClassCWIDtable
def ClassCWID(studententry):
    temp = None
    for key in ClassCWIDtable:
        print(key)
        if key == studententry['ClassID']:
            temp = key
    if temp != None:
        ClassCWIDtable[temp].add(studententry['CWID'])
        return

    ClassCWIDtable.update({studententry['ClassID']:{studententry['CWID']}})



#This function creates new student entries on the maintable
def addentryfunc():
    entryamount = int(input('Please enter the amount of students you wish to add: '),10)

    for x in range(len(Maintable),len(Maintable)+entryamount):
        print('Please enter Data for student')
        uinput = input('Please enter the students CWID: ')
        Maintable.append({'CWID':uinput})
        uinput = input('Please enter the students First Name: ')
        Maintable[x].update({'First_Name':uinput})
        uinput = input('Please enter the students Last Name: ')
        Maintable[x].update({'Last_Name':uinput})
        uinput = input('Please enter the students Gender: ')
        Maintable[x].update({'Gender':uinput})
        uinput = input('Please enter the students Date of Birth: ')
        Maintable[x].update({'DOB':uinput})
        uinput = input('Please enter the students ClassID: ')
        Maintable[x].update({'ClassID':uinput})
        uinput = input('Please enter the students Grade: ')
        Maintable[x].update({'Grade':uinput})
        print('The Student Entry has been added: ')
        ClassCWID(Maintable[x])



#This function prints out every class along with its associated students
def printentriesfunc():
    print('===========================================================================================')
    for key,value in ClassCWIDtable.copy().items():
        print('The classID is '+ key)
        for setvalue in value:
            for x in Maintable:
                if x['CWID'] == setvalue and x['ClassID'] == key:
                    print('CWID: '+ setvalue+' First Name '+x['First_Name']+' Last Name '+x['Last_Name'])
    print('===========================================================================================')



#This function is the main loop of the program it will take input from the user and direct the program
while userinput != ('Quit'):
    print('===========================================================================================')
    print('Please enter a decision: ')
    print('')
    print('Enter 1 for Add student Data ')
    print('Enter 2 for Print student Data ')
    print('To End Program enter Quit')
    print('')
    userinput = input('Please enter your decision now: ')
    print('===========================================================================================')

    if userinput == '1':
        addentryfunc()
    elif userinput == '2':
        printentriesfunc()
    elif userinput == ('Quit'):
        print('Now Ending the Program ')
    else:
        print('Incorrect Input Please try again ')