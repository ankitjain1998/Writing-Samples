#Lab 4

#Name: Ankit Jain
#UCI Net ID: jaina2
#ID Number: 96065117

#Imported Modules and Dictionary

from collections import namedtuple
import re
import os

rooms_dictionary={}

'''
Dictionary storing all the rooms
so available in the text file.
'''

#Functions to be used

def loaddungeon(entry_room:str)->tuple:

    '''
    Opens file and adds each individual line to a list.
    All the numbers in each line are then added to a list
    and the list is added to another list. The same is done
    with the description wordings. A named tuple is so made
    out of the details so available for all the rooms.
    The room number is then selected as the key for the
    rest of the details in the dictionary. It finally
    prints the description of the first room and returns
    a tuple with its details from the dictionary.
    '''
    
    if os.path.isfile(entry_room)==True:
        
        room_details=open(entry_room,'r').read().strip().split('\n')
        blank=''
        while blank in room_details:
            room_details.remove(blank)
            
        room_descriptions=[]
        room_nums=[]
        rooms_list=[]

        Room=namedtuple('Room','Room_Number Room_Description North_Room South_Room East_Room West_Room')
          
        for i in range(0,len(room_details)):

            description=wordselector(room_details[i])
            room_descriptions.append(description)

            det=room_details[i].replace(room_descriptions[i][0][0],'')
            nums=numselector(det)
            room_nums.append(nums)

            room_tuple=Room(room_nums[i][0],room_descriptions[i][0][0],room_nums[i][1],room_nums[i][2],room_nums[i][3],room_nums[i][4])
            
            rooms_list.append(room_tuple)

        for i in range(0,len(rooms_list)):
            x=int(rooms_list[i][0])
            rooms_dictionary[x]=rooms_list[i][1:]
 
        print(room_descriptions[0][0][0])

        x=int(room_nums[0][0])
        room_1=rooms_dictionary[x]

        return room_1

    elif os.path.isfile(entry_room)==False:
        pass



def goto(entry:int)->tuple:

    '''
    Takes in room number as
    entry and returns the tuple so
    associated with the entry as
    a key. Prints the description
    of the room associated with the
    room number.
    '''
    
    x=rooms_dictionary[entry]
    print(x[0])

    return x



def passfunction():
    try:
        pass
    except IndexError:
        pass
        


def wordselector(string:str)->str:

    '''
    Extracts all characters within
    the hashtags and returns the
    extracted substring in a list
    '''

    description_list=[]
    
    description_string=re.findall(r'\#(.*?)\#',string)
    
    description_list.append(description_string)

    return description_list



def numselector(string:str)->list:

    '''
    Selects all characters in the
    string which are numbers
    and returns a list with them.
    '''

    numbers_needed=re.findall(r"[-+]?\d*\.\d+|[-+]?\d+",string)

    return numbers_needed

#Main Function

def StartDungeon()->None:

    command=[]
    commands=input('$ ').split()

    for i in commands:
        x=i.strip()
        command.append(x)
            
    while command[0]!='quit':

        '''
        Calls functions according
        to the argument so entered
        '''

        if len(command)>1:
            if command[0]=='loaddungeon':
                x=loaddungeon(command[1])
                command=input('$ ').split()
                m=x

        if command[0]=='north':
            y=int(m[1])
            if int(y)!=-1:
                m=goto(y)
                command=input('$ ').split()
            elif int(y)==-1:
                print('You can’t go there.')
                command=input('$ ').split()

        elif command[0]=='south':
            y=int(m[2])
            if int(y)!=-1:
                m=goto(y)
                command=input('$ ').split()
            elif int(y)==-1:
                print('You can’t go there.')
                command=input('$ ').split()

        elif command[0]=='east':
            y=int(m[3])
            if int(y)!=-1:
                m=goto(y)
                command=input('$ ').split()
            elif int(y)==-1:
                print('You can’t go there.')
                command=input('$ ').split()

        elif command[0]=='west':
            y=int(m[4])
            if int(y)!=-1:
                m=goto(y)
                command=input('$ ').split()
            elif int(y)==-1:
                print('You can’t go there.')
                command=input('$ ').split()

        if command[0]==None:
            command=input('$ ').split()   
            
        else:
            command=input('$ ').split()
  
StartDungeon()
'''
Calls the game function
'''    
    
