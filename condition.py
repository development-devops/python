age=int(input('enter your age:'));
is_member=True;

if age>=18:
    if is_member:
        print("You are eligible for voting with member discount.");
        print(2+4 )
    else:
        print("You are eligible for voting without member discount.");
else:
    print("You are not eligible for voting.");