def register():
    file = open('password.txt','w')
    username = input('Username:')
    password = input('Password:')
    userinfo = [f"{username}\n",f'{password}\n']
    file.writelines(userinfo)
    file.close()


