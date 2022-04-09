import random


def generate_new_pswd(pswds):
    count = 0
    new_pswd = []
    while count < 3:
        select = random.choice(pswds)
        new_pswd.append(select)
        count+=1
    print(new_pswd)


def password_combination(password):
    passwords = []
    for i in password[:4]:
        for j in password[4:8]:
            for k in password[8:]:
                result = (i,j,k)
                passwords.append(result)
    generate_new_pswd(passwords)
    return passwords

    
password_combination('12@17y017g3sa?')
