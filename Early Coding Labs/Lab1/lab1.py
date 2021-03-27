#Lab 1

#Name: Ankit Jain
#ID Number: 96065117
#UCI Net ID: jaina2

import math

#Problem 1: Volume of Sphere
print('Problem 1:\n')

radius=int(input('Enter Radius of Sphere: '))
pi=3.14

def volume(x):
    volume=(4/3)*(math.pi)*x*x*x
    return volume

print('Volume of Sphere:',round(volume(radius),2))

#Problem 2: User Name
print('\nProblem 2:\n')

first_name=input('Enter First Name: ')
last_name=input('Enter Last Name: ')

print(last_name,first_name)

#Problem 3: Sequence of Numbers

print('\nProblem 3:\n')

lst=[]

numbers=input('Enter a sequence of numbers separated by commas: ').split(',')
for i in numbers:
    lst.append(i)

print('List:',lst)

#Problem 4: Difference

print('\nProblem 4:\n')

number=int(input('Enter A Number: '))

def abs_difference(x):
    diff=x-8
    return abs(diff)

print('Absolute Value of the Difference:',abs_difference(number))

#Problem 5: Even Numbers

print('\nProblem 5:\n')

number_lst=''
sequence=input('Enter a sequence of numbers separated by commas: ').split(',')

for i in sequence:
    if int(i)%2==0:
        number_lst+=i+','
        
x=number_lst[:-1]

print('Even Numbers:',x)

#Problem 6: True Or False

print('\nProblem 6:\n')

num=int(input('Enter a number: '))

if num>20 and num%2==0:
    print('True')
else:
    print('False')
    
#Problem 7:

print("\nProblem 7:\n")

#Problem 7(a):

numbers=[2,4,6,8,10]
average=sum(numbers)/len(numbers)
print("(a)Average  of the five even integers from 2 to 10 =",average)

#Problem 7(b):

scores=[75,83.5,61,43]
average_score=sum(scores)/len(scores)
print("(b)Average Score =",average_score)

#Problem 7(c):

x=2**10
print("(c)2 to the power 10 =",x)

#Problem 7(d):

anteater_mass=50
anteater_velocity=15
anteater_kinetic_energy=0.5*anteater_mass*anteater_velocity*anteater_velocity
print("(d)Kinetic Energy of Anteater of \n  mass 50 kg travelling with speed 15 m/s =",anteater_kinetic_energy)

#Problem 8:

print("\nProblem 8:\n")

test_scores = '4325220523455023'

print("(a)Score of Student 1 =",test_scores[0])
print("(b)Score of Student 5 =",test_scores[4])
print("(c)Score of Student 10 =",test_scores[9])
print("(d)Score of Student 16 =",test_scores[15])

#Problem 9:

print("\nProblem 9\n")

s="anteater"

#Problem 9(a):

print("(a)",s[0]=="a")

#Problem 9(b):

print("(b)",s[-1]=="r")

#Problem 9(c):

print("(c)",s[3]=="x")

#Problem 9(d):

print("(d)",s[0]+s[1]+s[2]=="zot")

#Problem 10:

print("\nProblem 10:\n")

#Problem 10(a):

print("(a)",20+35>2**4)

#Problem 10(b):

print("(b)",'hello'!='goodbye')

#Problem 10(c):

print("(c)",10%3<=1)

#Problem 10(d):

fruits=['apple', 'orange', 'banana', 'mango']
print("(d)",len(fruits)==5)

#Problem 10(e):

print("(e)",63%2==0)

#Problem 11:

print("\nProblem 11:\n")

s='abcdefghijklmnopqrstuvwxyz'

#Problem 11(a):

print("(a)",s[3]+s[14]+s[6])

#Problem 11(b):

print("(b)",s[-7]+s[-5])

#Problem 11(c):

print("(c)",s[8]+s[2]+s[-8])

#Problem 11(d):

print("(d)",s[-6]+s[2]+s[8])
           
#Name: Ankit Jain
#ID Number: 96065117
#UCI Net ID: jaina2
