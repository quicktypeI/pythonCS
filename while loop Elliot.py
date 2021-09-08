

def aqquireName(f_name, n_name):
        name_sys = f_name + ', or ' + n_name
        return name_sys.title()
while True:
    print("\nLets get to know each other. Please tell me your name and a Nickname ")
    f_name = input("Name:")
    n_name = input("Nickname:")


    name_sys = aqquireName(f_name, n_name)
    print("Thank you for sharing that. So " + name_sys +" let's have some fun")
    if f_name or n_name == 'quit':
        break

def introF(f_name, n_name):
    greet = {'name' : f_name, 'nickname' : n_name}
    return greet
friend = introF('Elliot', 'Dot')
print("My newest friend is named " + friend['name']+ " though they sometimes go as " + friend['nickname'])
print(friend)


    
def bondT(f_name, n_name):
        convo = {'name' : f_name, 'nickname' : n_name}
        return greet
play = bondT('Elliot', 'Dot')
print("What are some games you would like to play" + play['name']

    
    
