import time

print("Hi and welcome to book a movie")
input("Press enter to see that what all movies are available in our PVR")
films1 = ['', 'Finding Dory', "Bourne", "Tarzan", "Avengers Endgame", "Ghost Busters", "Avengers Age of Ultron"]
for hi in films1:
    print(hi)
films = {
    "Finding Dory":[3,5],
    "Bourne":[5,50],
    "Tarzan":[7,50],
    "Ghost Busters":[5,45],
    "Avengers Endgame":[10,60],
    "Avengers Age of Ultron":[10,60]
    }
while True:
    time.sleep(0.7)
    choice = input("Hi! What movie would you like to see today?: ").strip().title()
    if choice in films:
        age = int(input("How old are you?: ").strip())
        #check user age
        if age >= films[choice][0]:
            #check enough seats
            num_seats = films[choice][1]
            if num_seats > 0:
                time.sleep(1)
                print("Enjoy your movie")
                films[choice][1] = films[choice][1] - 1
                break
            else:
                print("Oops, we are SOLD OUT")
                break
        else:
            print("Sorry... Our system has established that you're too young to see this movie!")
            break
        
    else:
        print("This movie is NOT availible yet. Please check back at a later time. Thanks")