known_users = ["Harman","Snimar", "Antar", "Sehaj", "Ajay", "Armaan", "Jazz"]



while True:
    print("Hi! I'm Sheru! Security guard (^.^)")
    name = input("What is your name?: ").strip().capitalize()
    if name in known_users:
        print("Hello {}. You are authorised to enter the Dark zone.".format(name))
    else:
        print("Your name is not recognised. Get out of here!! Before I throw you outta here")