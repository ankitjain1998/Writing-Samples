#Lab 3

#Name: Ankit Jain
#UCI Net ID: jaina2
#ID Number: 96065117

#Functions to be used in program:



def addbook(books:list,command:list)->None:

    '''
    Gets rid of blank spaces,
    and adds each element to a list. The list so obtained
    is added to a bigger list, in this case, books.
    '''

    book_to_add=[]

    if len(command)==4:
        for i in command[1:]:
            space_removed=i.strip()
            book_to_add.append(space_removed)
        books.append(book_to_add)
        
    elif len(command)!=4:
        pass

    

def printbooks(books:list)->None:
    
    '''
    Prints all the elements of
    the books database, along with their details each of
    which are seperated by commas.
    '''
    
    for book in books:
        for details in book:
           print(*book,sep=", ")
           break



def deletebook(books:list,command:list)->None:

    '''
    Checks book to be removed
    from database, and removes the entered book and
    it's related details from the database.
    '''
    
    delete_book=command[1].strip()
    
    if len(command)==2:
        for i in range(0,len(books)):
            if books[i][0]==delete_book:
                books.remove(books[i])
                break
            
    elif len(command)!=2:
        pass

    

def findbook(books:list,command:list)->None:

    '''
    Checks book to be found
    from database, and prints the entered book and
    it's related details from the database.
    '''
    
    find_book=command[1].strip()
    
    if len(command)==2:
        for i in range(0,len(books)):
            if books[i][0]==find_book:
                print(*books[i],sep=", ")
                
    elif len(command)!=2:
        pass


    
def findauthor(books:list,command:list)->None:

    '''
    Checks author to be found
    from database, and prints all the books which
    matches the author name and the books
    related details from the database.
    '''
    
    find_author=command[1].strip()
    
    if len(command)==2:
        for i in range(0,len(books)):
            if books[i][2]==find_author:
                print(*books[i],sep=", ")
                
    elif len(command)!=2:
        pass



def findyear(books:list,command:list)->None:

    '''
    Checks the publication year to be found
    from database, and prints all the books which
    matches the year entered and the books
    related details from the database
    '''
    
    find_year=command[1].strip()
    
    if len(command)==2:
        for i in range(0,len(books)):
            if books[i][1]==find_year:
                print(*books[i],sep=", ")
                
    elif len(command)!=2:
        pass

#Database Program

'''Uses above functions and implements them in
the database'''

command=input('$ ').split(',')

'''Takes in user input, seperated by commas
and adds each string to a list 'command' '''

books=[]

'''This is the list or so database
in which the books so entered, are added'''

while command[0]!='quit':

    '''Program ends if quit is entered'''  
    
    if command[0]=='addbook':
        
        addbook(books,command)
        command=input('$ ').split(',')
        
    elif command[0]=='printbooks':
        
        printbooks(books)
        command=input('$ ').split(',')

    elif command[0]=='deletebook':

        deletebook(books,command)
        command=input('$ ').split(',')

    elif command[0]=='findbook':

        findbook(books,command)
        command=input('$ ').split(',')

    elif command[0]=='findauthor':

        findauthor(books,command)
        command=input('$ ').split(',')

    elif command[0]=='findyear':

        findyear(books,command)
        command=input('$ ').split(',')

    else:

        command=input('$ ').split(',')
