##def get_Fullname(first_name, last_name):
##    full_name = first_name + ' ' + last_name
##    return full_name.title()
##while True:
##    print("\nPlease Inupt your name to Continue:")
##    f_name = input("first name:")
##    l_name = input("last name:")
##
##    formatted_name = get_Fullname(f_name, l_name)
##    print("welcome " + formatted_name)
##    if f_name or l_name == 'quit':
##        break
##
##def build_person(hair_c, eye_c):
##    person = {'hair' : hair_c, 'eyes' : eye_c}
##    return person
##red = build_person('Red hair', 'Brown eyes')
##print(red)

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
    


    
    
