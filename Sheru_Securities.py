known_users = ["Harman","Snimar", "Antar", "Sehaj", "Ajay", "Armaan", "Jazz"]

print(len(known_users))

while True:
    print("Hi! I'm Sheru! Security guard (^.^)")
    name = input("What is your name?: ").strip()

    if name in known_users:
        print("Hello {}. You are authorised to enter the Dark zone.").format(name)
    else:
        print("Your name is not recognised. Get out before I throw you outta here")
        