usernames={"user1@gmail.com" : "user123"}
email = input("enter your email")
if email in usernames:
    print("this email is already taken")
else:
    print("this email is not in our database")