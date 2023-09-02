from component import load_user_data,save_user_data

def registerSystem(fun):
    user_data = load_user_data('deco.json')
    def wrapper():
        result = fun()
        user_data[result['username']] = {"email": result['email'],"password":result['password']}
        print(user_data)
        save_user_data(user_data,'deco.json')

    return wrapper

@registerSystem
def register():
    username = input("Username:")
    email = input("Email:")
    password = input("Password:")
    lic =  {"username": username, "password": password,'email': email}
    return  lic


register()