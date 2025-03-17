import pickle
print('Secure password storage by Dheeraj')
print()
print('All your passwords are encrypted and saved safely with us')
print()
print('NOTE: Never use caps and space in website name')
print()
print('''1. View saved password
2. Add new password''')
print()
opt=input('Select an option to continue: ')
if opt==2:
    ans='y'
    fin=open('Passwords.dat','rb+')
    while ans=='y':
        a=input('Enter your password: ')
        c=input('Enter the associated username: ')
        d=input('Enter the associated website: ')
        b=a                                                   #here b is supposed to be our encypted password but I'm still working on the encryption
        try:
            while True:
                e=pickle.load(fin)
                if d in e:
                    for i in e:
                        if i==d:
                            e[d].append([c,b])
                            fin.seek(0)
                            pickle.dump(e,fin)
                        else:
                            e[d]=[[c,b]]
                            fin.seek(0)
                            pickle.dump(e,fin)
        except EOFError:
            fin.close()
        ans=input('Do you want to add another one (y/n): ')
        
elif opt==1:
    x=input('Enter the website: ')
    y=input('Enter the username: ')
    fin=open('Passwords.dat','rb')
    match=0
    try:
        while True:
            z=pickle.load(fin)
            for i in z:
                if i==x:
                    for j in z[x]:
                        if j[0]==y:
                            enc=j[1]
                            dec=enc                    #here b is supposed to be our decypted password but I'm still working on the decryption
                            print('Your password is: ',dec)
                            match=1
    except EOFError:
        if match==0:
            print('password not found')
        fin.close()

