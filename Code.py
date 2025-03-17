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
        e=pickle.load(fin)
        for i in e:
            for j in i:
                if j==d:
                    i[j].append(a)
                    ans2=1
            if ans2==0:
                i[d]=1
    except EOFError:
        print()
    ans=input('Do you want to add another (y/n): ')