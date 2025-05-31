import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
'v','w','x','y','z']
#letters=["abcdefghijklmnopqrstuvwxyz"]
symbols=['!','@','#','$','%','^','&','*','(,)','_','-','=','+','`','~']

numbers=['0','1','2','3','4','5','6','7','8','9']

print("Welcome to password generator")
no_letters=int(input("Enter no of letters you want in your password:"))
no_symbols=int(input("Enter no of symbols you want in your password:"))
no_numbers=int(input("enter no of numbers you want in your password:"))

#empty string
password_list=[]
#looping for letters
for i in range(1,no_letters+1):
    char=random.choice(letters)
    password_list+=char
#print(password)

#looping for symbols
for i in range(1,no_symbols+1):
    char=random.choice(symbols)
    password_list+=char
#print(password)

#looping for numbers
for i in range(1,no_numbers+1):
    char=random.choice(numbers)
    password_list+=char
print("the genearted list:",password_list)

#for strong password shuffing the letters
print("the shuffled list:",end="")
random.shuffle(password_list)
print(password_list)

#convert to  string for that fecth letter from list and add to empty string
password=""
for i in password_list:
    password=password+i
print("the generated password is:",password)
