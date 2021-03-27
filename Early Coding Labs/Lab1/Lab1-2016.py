#Lab 1
#Name: Ankit Jain
#ID Number: 96065117
#UCI Net ID: jaina2

#Problem 1

print("Problem 1\n")

#Problem 1(a)

numbers=[2,4,6,8,10]
average=sum(numbers)/len(numbers)
print("(a)Average  of the five even integers from 2 to 10 =",average)

#Problem 1(b)

scores=[75,83.5,61,43]
average_score=sum(scores)/len(scores)
print("(b)Average Score =",average_score)

#Problem 1(c)

x=2**10
print("(c)2 to the power 10 =",x)

#Problem 1(d)

anteater_mass=50
anteater_velocity=15
anteater_kinetic_energy=0.5*anteater_mass*anteater_velocity*anteater_velocity
print("(d)Kinetic Energy of Anteater of \n  mass 50 kg travelling with speed 15 m/s =",anteater_kinetic_energy)

#Problem 2

print("\nProblem 2\n")

wall = 'w'
cannon = 'c'

#Problem 2(a)

print("(a)",wall+cannon)

#Problem 2(b)

print("(b)",wall+cannon+wall)

#Problem 2(c)

answer_c=wall*3+cannon+wall*3
print("(c)",answer_c)

#Problem 2(d)

answer_d=wall+cannon*2
print("(d)",answer_d*4)

#Problem 2(e)

answer_e=wall*3+cannon
print("(e)",answer_e*4+wall)

#Problem 2(f)

answer_f=(wall*4+cannon)*4
print("(f)",answer_f+wall*4)

#Problem 3 

print("\nProblem 3\n")
test_scores = '4325220523455023'

print("(a)Score of Student 1 =",test_scores[0])
print("(b)Score of Student 5 =",test_scores[4])
print("(c)Score of Student 10 =",test_scores[9])
print("(d)Score of Student 16 =",test_scores[15])

#Problem 4

print("\nProblem 4\n")

s="anteater"

#Problem 4(a)

print("(a)",s[0]=="a")

#Problem 4(b)

print("(b)",s[-1]=="r")

#Problem 4(c)

print("(c)",s[3]=="x")

#Problem 4(d)

print("(d)",s[0]+s[1]+s[2]=="zot")

#Problem 5

print("\nProblem 5\n")

#Problem 5(a)

pi=3.14159

print("(a)Given Value of pi =",pi)

#Problem 5(b)

make="Toyota"
model='Camry'
year="2014"
print("(b)",make,"",model,"",year)

#Problem 5(c)

ICS_majors=['Computer Science','Informatics','Computer Game Science']
print("(c)ICS Majors are",ICS_majors[0],",",ICS_majors[1],"and",ICS_majors[2])

#Problem 5(d)

odd_numbers=[3,5,7,9]
a=sum(odd_numbers)/len(odd_numbers)
print("(d)Average of Odd Numbers from 3 to 9 =",a)

#Problem 6

print("\nProblem 6\n")

#Problem 6(a)

print("(a)",20+35>2**4)

#Problem 6(b)

print("(b)",'hello'!='goodbye')

#Problem 6(c)

print("(c)",10%3<=1)

#Problem 6(d)

fruits=['apple', 'orange', 'banana', 'mango']
print("(d)",len(fruits)==5)

#Problem 6(e)

print("(e)",63%2==0)

#Problem 7

print("\nProblem 7\n")

s='abcdefghijklmnopqrstuvwxyz'

#Problem 7(a)

print("(a)",s[3]+s[14]+s[6])

#Problem 7(b)

print("(b)",s[-7]+s[-5])

#Problem 7(c)

print("(c)",s[8]+s[2]+s[-8])

#Problem 7(d)

print("(d)",s[-6]+s[2]+s[8])

#Problem 8

print("\nProblem 8\n")

import math

def distance_formula(x1:int,y1:int,x2:int,y2:int)->int:
    assert x1>=0
    assert y1>=0
    assert x2>=0
    assert y2>=0
    distance=math.sqrt((y2-y1)**2+(x2-x1)**2)
    return distance

print("Distance between points (0,0) and (3,4)=",distance_formula(0,0,3,4))

#Problem 9

print("\nProblem 9\n")

def slope_formula(x1:int,y1:int,x2:int,y2:int)->int:
    assert x1>=0
    assert y1>=0
    assert x2>=0
    assert y2>=0
    slope=(y2-y1)/(x2-x1)
    return slope

print("Slope of line with points (0,0) and (3,6)=",slope_formula(0,0,3,6))

