usernames = []
if usernames :
  for user in usernames :
    if user == 'admin':
        print("Hello " + user.title() + " would you like to see a status report?")
    else:
        print("Hello " + user.title() + ", thank you for loging in again.")
else :
    print("We  need to find some users!")

