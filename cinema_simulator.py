films = {
    "Infinity War": [10,5],
    "The Dictator": [18,5],
}

while True:

    choice = input("What film would you like to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())

        #checking user age

        if age >= films[choice][0]:
            #check seats

            num_seats = films[choice][1]

            if num_seats > 0:
                print("Enjoy the film")
                films[choice][1] = films[choice][1]-1
            else:
                print("Sorry, we are sold out!")
        else:
            print("You ar etoo young to see the films!")
    else:
        print("We don't have that film....")