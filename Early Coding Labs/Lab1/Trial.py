number_lst=''
sequence=input('Enter a sequence of numbers separated by commas:').split(',')

for i in sequence:
    if int(i)%2==0:
        number_lst+=i+','
        
x=number_lst[:-1]

print('Even Numbers:',x)
