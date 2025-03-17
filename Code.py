import pickle
print('Secure password storage by Dheeraj')
print()
print('All your passwords are encrypted and saved safely with us')
print()
print('NOTE: Never use caps and space in website name')
ans='y'
a=[]
fin=open('Passwords.dat','rb+')
while ans=='y':
    b=input('Enter your password: ')
    c=input('Enter the associated username: ')
    d=input('Enter the associated website: ')
    a=[c,b]
    print(a)
    ans2=0
    try:
        while True:
            e=pickle.load(fin)
            if d in e:
                print()
            else:
                e[d]=[c,b]
                fin.seek(0)
                pickle.dump(e,fin)
    except EOFError:
        fin.close()
    ans=input('Do you want to add another (y/n): ')


fin1=open('Passwords.dat','rb')
try:
    while True:
        g=pickle.load(fin1)
        print(g)
except EOFError:
    fin1.close()
