#Lab 2

print('Lab 2:')

#Ankit Jain jaina2 96065117

#Problem 1

print('\nProblem 1:\n')

year=int(input('Enter a year: '))

def leapYear(year:int)->int:

    '''Function checks if the year entered
    is a leap year by checking it's divisibility
    with 4 and 400 and non divisibility with 100'''
    
    if year%400==0:
        print(' ')
        print(year,'is a leap year')
        return True  
    elif year%100==0:
        print(year,'is not a leap year')
        return False    
    elif year%4==0:
        print(' ')
        print(year,'is a leap year')
        return True
    else:
        print(year,'is not a leap year')
        return False

leapYear(year)

#Problem 2

import random

print('\nProblem 2:\n')

random_num=random.randrange(1,101)

print('Guessing my number between 1 and 100.')

user_input=int(input('\nEnter a Number: '))

def guessGame(user_input:int)->None:

    '''Function checks whether the number the user entered
    is same as that of the one randomized by the computer.
    It adds 1 to the number of guesses each time the numbers
    are not the same, till the numbers become equal'''

    guesses=1

    while user_input!=random_num:
        guesses=guesses+1
        if user_input>random_num:
            user_input=int(input('Too high. Try again: '))
        elif user_input<random_num:
            user_input=int(input('Too low. Try again: '))

    if user_input==random_num:
        print('\nCongratulations! You got it in',guesses,'guesses.')

guessGame(user_input)

#Problem 3

print('\nProblem 3:\n')

entry=int(input('Enter a number: '))

factors=[]

def largestFactor(x:int)->int:

    '''Function divides the entered number
    by every number from the range of 1 to one minus the
    number entered. For whenever the remainder so obtained
    is zero, it adds it to a list. The function then removes
    the number itself from the list and adds 1, and returns
    the maximum value present in the list.'''

    for i in range(1,x):
        
        y=int(x/i)
        if x%i==0:
            factors.append(y)
        
    factors.append(1)
    factors.remove(x)

    return int(max(factors))

print('Largest Factor is',largestFactor(entry))

#Problem 4:

print('\nProblem 4:\n')

num=int(input('Enter a number: '))

def addDigits(num:int)->int:

    '''Function takes in a number, converts
    it to a string. It then takes each element
    of the string, converts it to a integer and
    adds to list. The function returns the value
    of the sum of the elements in the list.'''

    digits=[]

    number=str(num)
    for x in number:
        y=int(x)
        digits.append(y)

    digits_sum=sum(digits)
    
    return digits_sum

print('Digit Sum is',addDigits(num))

Problem 5:

print('\nProblem 5:\n')

nums=[]
differences=[]
sequence=input('Enter a sequence seperated by commas: ').split(',')

def largestDiff(sequence:str)->int:

    '''This function takes in a sequence of numbers
    entered by user and appends each number to a list.
    It then subtracts the consective elements and adds each
    difference to another list. The function then returns the maximum
    value of this list'''

    for i in sequence:
        y=int(i)
        nums.append(y)

    for i in range(0,len(nums)-1):
        num1=nums[i+1]
        num2=nums[i]
        z=num1-num2
        differences.append(z)

    return max(differences)

print('Largest consecutive difference is',largestDiff(sequence))
    
#Problem 6:

print('\nProblem 6:\n')

grades=[]
grade_sequence=input('Enter a sequence of grades: ').split(',')

for i in grade_sequence:
        m=int(i)
        grades.append(m)

def adjustedAvg(grades:list)->float:

    '''This function takes in a list of grades
    ,removes the maximum and the minimum value so
    present in the list. It then adds all the values
    present in the list then, divides the sum by the new
    length of the list, and returns this value as a result.
    If the function has no decimal value, it returns a integer
    result, but if not then a float value rounded to 2 places.'''
    
    max_grade=max(grades)
    min_grade=min(grades)
    grades.remove(max_grade)
    grades.remove(min_grade)
    average=float(sum(grades)/len(grades))

    if average%1==0:
        return int(average)
    else:
        return average

print('Adjusted Average is',round(adjustedAvg(grades),2))

#Problem 7:

print('\nProblem 7:\n')

x,y=input('Enter two strings: ').split(' ')

def atEnd(x:str,y:str)->str:
    len_1=len(x)
    len_2=len(y)

    '''The function checks the end of the longer word as per the
    length of the shorter word, and matches it so to the shorter
    word. It returns True if they are the same, and False if not'''

    if len_1>len_2:
        if x[-len_2:]==y:
            print('One string is at the end of the other string')
            return True
        elif x[-len_2:]!=y:
            print('One string is not at the end of the other string')
            return False

    if len_1<len_2:
        if x==y[-len_1:]:
            print('One string is at the end of the other string')
            return True
        elif x!=y[-len_1:]:
            print('One string is not at the end of the other string')
            return False
       
atEnd(x,y)

#Problem 8:

print('\nProblem 8:\n')

def findHarris(entry:str)->bool:

    '''This function checks if the string
    'harris' is present in the entered string
    and returns True if present and not precedded
    by a period. It returns False if 'harris' is not
    there or if 'harris' is precedded by a string'''
    
    if '.harris' in entry:
        return False
    elif 'harris' in entry:
        return True
    else:
        return False 
    
entry=input('Enter a string: ')

print(findHarris(entry))

#Problem 9

print('\nProblem 9:\n')

entry_numbers=input('Enter a sequence of numbers: ').split(',')
entry_list=[]
rounded_numbers=[]

for i in entry_numbers:
        x=float(i)
        entry_list.append(x)

def myAvg(entry_list:list)->int:

    '''This function rounds off each number present
    in the entered list of numbers and adds it to
    another list. It then divides the sum of the new
    list by the length of the same list and returns this
    value, according to the presence of decimal or not.'''

    for i in entry_list:
        m=i-0.5
        z=int(m)
        round_number=z+1
        rounded_numbers.append(round_number)
        avg=sum(rounded_numbers)/len(rounded_numbers)

    if avg%1==0:
        return int(avg)
    else:
        return "%.2f"%avg

print('Average is',myAvg(entry_list))

#Problem 10:

print('\nProblem 10:\n')

def pieNum(x:int,y:int,z:int)->int:

    '''This function checks in the input of apples
    ,oranges, and pickles and checks the possibilities
    of the number of pies to be made with each ingredient
    separetely. It then adds the possibilities to a different
    list and returns the minimum value of this list.'''

    pies_num=[]
    
    pie_pickle=int(z/3)
    pie_orange=int(y/2)
    pie_apple=int(x/1)
    
    pies_num.append(pie_pickle)
    pies_num.append(pie_orange)
    pies_num.append(pie_apple)

    return min(pies_num)

apples=int(input('How many apples?: '))
oranges=int(input('How many oranges?: '))
pickles=int(input('How many pickles?: '))

print(' ')
print(pieNum(apples,oranges,pickles),'pies can be made')



