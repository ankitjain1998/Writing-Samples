#Lab 5

#Name: Ankit Jain
#UCI Net ID: jaina2
#ID Number: 96065117

#Imported Modules, Dictionaries and Room Class

from collections import namedtuple
import re
import os

rooms_dictionary={}
playerInventory={}

'''
Global variables(dictionary) used
in the program
'''

class Room:

    '''
    Class initializes the details of each room
    as instance variables 
    '''

    def __init__(self,room_nums,description):
        self.room_nums=room_nums
        self.description=description
        self.room_num=int(room_nums[0])
        self.North=int(room_nums[1])
        self.South=int(room_nums[2])
        self.East=int(room_nums[3])
        self.West=int(room_nums[4])
        self.roomInventory={}

#Functions Used
        
def loaddungeon(entry_room:str)->list:

    '''
    Checks whether file exists, opens if yes and then
    adds each individual line to a list. For each line
    then the details are extracted using cthe room class
    and stored in a dictionary, with the room number as
    the key. The details of the first room inside the file
    is returned at the end of the function, as a tuple.
    '''

    if os.path.isfile(entry_room)==True:

        rooms_list=[]
        
        room_details=open(entry_room,'r').read().strip().split('\n')
        blank=''
        while blank in room_details:
            room_details.remove(blank)

        for i in room_details:

            description=wordselector(i)
            room_nums=numselector(i)
            room_i=Room(room_nums,description)

            room_detail=(room_i.room_num,room_i.description,room_i.North,room_i.South,room_i.East,room_i.West,room_i.roomInventory)
            rooms_list.append(room_detail)

            rooms_dictionary[room_i.room_num]=room_detail[1:]

        initial_room=rooms_list[0][1:]
        
        print(initial_room[0])
        room_contents(initial_room[5])

        return initial_room

    elif os.path.isfile(entry_room)==False:
        pass

def loaditems(items_file:str):

    '''
    Checks whether items file exists. If exists,
    it extracts each item and their number separetely.
    It then adds each item to the playerInventory dictionary
    with the item name as the key.
    '''
    
    if os.path.isfile(items_file)==True:
        
        items=open(items_file,'r').read().strip().split(' ')
        item_names = [item for item in items if not item.isdigit()]
        item_numbers = [item for item in items if item.isdigit()]
        number_of_items=int(len(items)/2)

        for i in item_names:
            if i in playerInventory.keys():
                playerInventory[i]=playerInventory[i]+1
            elif i not in playerInventory.keys():
                for j in range(0,number_of_items):
                    playerInventory[item_names[j]]=int(item_numbers[j])
        
    elif os.path.isfile(items_file)==False:
        pass
    
def goto(entry:int)->list:

        '''
        Takes in room number as
        entry and returns the tuple so
        associated with the entry as
        a key. Prints the description
        of the room associated with the
        room number.
        '''
        
        new_room=rooms_dictionary[entry]
        print(new_room[0])
        return new_room

def wordselector(string:str)->str:

    '''
    Extracts all characters within
    the hashtags and returns the
    extracted substring in a list
    '''
    
    description_string=re.findall(r'\#(.*?)\#',string)
    description=description_string[0]
    
    return description

def numselector(string:str)->list:

    '''
    Selects all characters in the
    string which are numbers
    and returns a list with them.
    '''

    numbers_needed=re.findall(r"[-+]?\d*\.\d+|[-+]?\d+",string)

    return numbers_needed

def room_contents(inventory:dict)->None:

    '''
    Takes all the room inventory initialized
    by the class room for each separate room
    and prints the contents from the dictionary
    as with the key and its number. If room has
    no items, it passes.
    '''

    keys=[]
    values=[]
    contents=[]
    room_inventory=''

    for i in inventory.keys():
        keys.append(i)
    for i in inventory.values():
        values.append(i)

    if len(keys)!=0:

        for i in range(0,len(keys)):
            
            x=keys[i]
            y=str(values[i])
            content='('+x+' '+y+')'
            contents.append(content)

        for i in contents:
            room_inventory+=i

        all_contents='This room contains'+room_inventory
        print(all_contents)

    elif len(keys)==0:
        pass

    return None

def playerInventoryContents(inventory:dict)->None:

    '''
    Prints all the items present in the player
    inventory at the time.
    '''

    keys=[]
    values=[]
    contents=[]
    all_contents=''

    for i in inventory.keys():
        keys.append(i)
    for i in inventory.values():
        values.append(i)

    if len(keys)!=0:

        for i in range(0,len(keys)):
            
            x=keys[i]
            y=str(values[i])
            content= x+' '+y
            contents.append(content)

        for content in contents:
            all_contents+=content+','

        x=all_contents[:-1]
        print(x)

    elif len(keys)==0:
        print('Player has no items in inventory.')

    return None

def dropitem(item:str,roomInventory:dict)->dict:

    '''
    This function removes the item from the
    playerInventory to the inventory of the
    room the user is currently in, if the item
    is present in the inventory.
    '''

    keys=[]
    room_keys=[]
    
    for key in playerInventory.keys():
        keys.append(key)
        
    for key in roomInventory.keys():
        room_keys.append(key)
        
    if item in keys:
        playerInventory[item]=playerInventory[item]-1
        if item in room_keys:
            roomInventory[item]=roomInventory[item]+1
        elif item not in room_keys:
            new={item:1}
            roomInventory.update(new)
            
    if item not in keys:
        print('You do not have the item')

    return roomInventory

def takeitem(item:str,roomInventory:dict)->None:

    '''
    This function takes an item from the
    inventory of the room the user is
    currently in and adds it to the playerInventory,
    if the item is present in the room.
    '''

    keys=[]
    room_keys=[]
    
    for key in playerInventory.keys():
        keys.append(key)
        
    for key in roomInventory.keys():
        room_keys.append(key)
        
    if item in room_keys:
        roomInventory[item]=roomInventory[item]-1
        if item in keys:
            playerInventory[item]=playerInventory[item]+1
        elif item not in keys:
            new={item:1}
            playerInventory.update(new)
            
    if item not in room_keys:
        print('The item is not in this room')

    return None

#Main Function 

def StartDungeon()->None:

    command=[]
    commands=input('$ ').split()

    for i in commands:
        x=i.strip()
        command.append(x)
            
    while command[0]!='quit':

        '''
        Calls different functions as per
        the argument so entered
        '''
    
        if command[0]=='loaddungeon':
            x=loaddungeon(command[1])
            command=input('$ ').split()
            m=x

        elif command[0]=='north':
            y=int(m[1])
            if int(y)!=-1:
                m=goto(y)
                room_contents(m[5])
                command=input('$ ').split()
            elif int(y)==-1:
                print('You can’t go there.')
                command=input('$ ').split()

        elif command[0]=='south':
            y=int(m[2])
            if int(y)!=-1:
                m=goto(y)
                room_contents(m[5])
                command=input('$ ').split()
            elif int(y)==-1:
                print('You can’t go there.')
                command=input('$ ').split()

        elif command[0]=='east':
            y=int(m[3])
            if int(y)!=-1:
                m=goto(y)
                room_contents(m[5])
                command=input('$ ').split()
            elif int(y)==-1:
                print('You can’t go there.')
                command=input('$ ').split()

        elif command[0]=='west':
            y=int(m[4])
            if int(y)!=-1:
                m=goto(y)
                room_contents(m[5])
                command=input('$ ').split()
            elif int(y)==-1:
                print('You can’t go there.')
                command=input('$ ').split()

        elif command[0]=='loaditems':
            loaditems(command[1])
            command=input('$ ').split()

        elif command[0]=='roomcontents':
            room_contents(m[5])
            command=input('$ ').split()

        elif command[0]=='inventory':
            playerInventoryContents(playerInventory)
            command=input('$ ').split()

        elif command[0]=='drop':

            keys=[]
            dropitem(command[1],m[5])

            for key in playerInventory.keys():
                keys.append(key)
            
            if command[1] in keys:
                if playerInventory[command[1]]==0:
                    del playerInventory[command[1]]

            command=input('$ ').split()

        elif command[0]=='take':
            
            keys=[]
            takeitem(command[1],m[5])

            for key in m[5].keys():
                keys.append(key)
            
            if command[1] in keys:
                if m[5][command[1]]==0:
                    del m[5][command[1]]
                    
            command=input('$ ').split()
            
        else:
            command=input('$ ').split()

StartDungeon()    

'''
Calls the main function 
'''    
