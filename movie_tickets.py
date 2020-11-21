prompt = "apki umar kitni hai?"
prompt += "\nEnter 'quit' when you are finished. "


while True:
    age = input(prompt)

    if age == 'quit':
        break
    age = int(age)


    if age <=3:
        print("   Ticket is free")
    elif  age<13:
        print("   Ticket 12 rs ki hai")
    else:
        print("   15rs lagega")

