def main():
    sucessful = True
    movielist= ["La La Land","Hacksaw Ridge","Manchester by the Sea","Arrival","Fences","Fantastic Beasts and Where to Find Them"
                ,"The Jungle Book","OJ Made in America","Piper","The Salesman","Suicide Squad"]
    import random
    i = random.randint(0,len(movielist)-1)
    movie = movielist[i]
    known_characters = ["A","E","I","O","U"]
    def display(s,known_characters):
        isdone = True
        for i in s:
            if i.upper() in known_characters:
                print(i ,end=" ")
                continue
            if i == " ":
                print("/",end=" ")
                continue
            else:
                isdone = False
                print("_",end=" ")
        print()
        return isdone
    guess= 10

    while True:

        won = display(movie,known_characters)
        if won:
            break
        if guess<=0:
            sucessful = False
            break
        s=input("Enter a Character :  ")
        if len(s) > 1:
            print("Heavy Data Flow, Intrusion Detected!  ")
            print("Initiating LockDown")
            sucessful = False
            break
        else:
            if s.upper() in movie.upper() and s not in known_characters:
                known_characters.append(s.upper())
            else:
                guess -= 1
                print("Remaining Wrong Guesses = ",guess)
    return sucessful
