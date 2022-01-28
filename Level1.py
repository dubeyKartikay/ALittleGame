def main():
    global cwd

    def display_rules():
        print()
        print("To Open any file/folder , simply type  'OPEN' followed by its name and extension (None for folders, .txt for tetfiles)")
        time.sleep(1)
        print("to go to the previous folder , type 'BACK' ")
        time.sleep(1)
        print("If you think you have enough info to guess the password, type 'GUESS PASSWORD' and then type your guess")
        time.sleep(1)
        print("If your guess is correct you will win the level, Else you have to try again")
        time.sleep(1)
        print("To Quit the game type 'QUIT")
        time.sleep(1)
        print('')
    class Textfile:
        def __init__(self, name, content, parent=None):
            self.name = name + ".txt"
            self.content = content
            self.parent = parent

        def open(self):
            print(" "*5+self.name)
            print("\n" * 2)
            print(self.content)


    class Folder:
        def __init__(self, name, data, parent=None):
            self.name = name
            self.data = data
            self.parent = parent
            self.opened = False

        def open(self):
            if self.name != "Admin" or self.opened:
                print(" "*5+self.name)
                print("\n" * 1)
                for i in self.data:
                    print(i.name)
                print('\n')
            else:
                print("SECURITY QUESTION")
                print()
                print("What is the name of my dog??")
                s = input()
                if s.upper() == "BRUNO":
                    print("Access Granted!")
                    self.opened = True
                    print(" "*5+self.name)
                    print("\n" * 1)
                    for i in self.data:
                        print(i.name)
                    print('\n')
                else:
                    print("Wrong!" + "     Enter to go back")

                    global cwd
                    cwd = Back(self)
                    return


    def Open(name, folder):
        for i in folder.data:
            if i.name == name:
                folder = i
                # i.open()
                return folder
        else:
            print("No file named", name, "in this folder")
            return folder


    def Back(folder):
        return folder.parent


    users = Folder("Users", [])
    desktop = Folder("Desktop", [])
    WorkSpace = Folder("WorkSpace", [])

    home = Folder(name="Home", data=[users, desktop, WorkSpace])

    users.parent = home
    desktop.parent = home
    WorkSpace.parent = home

    ThisUser = Folder("ThisUser", [])
    Admin = Folder("Admin", [])
    TheOtherUser = Folder("TheOtherUser", [])

    users.data = [Admin, ThisUser, TheOtherUser]

    ThisUser.parent = users
    Admin.parent = users
    TheOtherUser.parent = users

    PasswordFile = Textfile("#PASSWORD", "Password For the Employee Files is : kdboquh7238", Admin)
    Admin.data = [PasswordFile]

    Files_ThisUser = Folder("Files", [])
    Downloads_ThisUser = Folder("Downloads", [])

    ThisUser.data = [Files_ThisUser, Downloads_ThisUser]

    Files_ThisUser.parent = ThisUser
    Downloads_ThisUser.parent = ThisUser

    BankPasswords = Textfile("BankPasswords", "pass", Files_ThisUser)
    Alias = Textfile("Alias", "Chantel Beach"+"\n"+" Arooj Sutton"+"\n"+" Ramone Joseph "+"\n"+"Jason Aguirre"+"\n"+" Ayat Iles"+"\n"+" Mehmet Mcmahon"+"\n"+" Areebah Mendoza "+"\n"+"Pamela Dixon"+"\n"+" Eloisa Greig "+"\n"+"Sophia-Rose Newman", Files_ThisUser)
    Target = Textfile("Target", 'From Admin /Boss-'+'\n'+'The Target for this month is 100k. Bring it home', Files_ThisUser)

    Files_ThisUser.data = [BankPasswords, Alias, Target]

    ArticleONBlackholes = Textfile("Blackhole's_Image_Captured!",
                                   "Accomplishing what was previously thought to be impossible, "+"\n"+
                                   "a team of international astronomers has captured an image "+"\n"+
                                   "of a black hole’s silhouette. Evidence of the existence of "+"\n"+
                                   "black holes – mysterious places in space where nothing, "+"\n"+
                                   "not even light, can escape – has existed for quite some "+"\n"+
                                   "time, and astronomers have long observed the effects on the "+"\n"+
                                   "surroundings of these phenomena. In the popular "+"\n"+
                                   "imagination, it was thought that capturing an image of a "+"\n"+
                                   "black hole was impossible because an image of something "+"\n"+
                                   "from which no light can escape would appear completely "+"\n"+
                                   "black. For scientists, the challenge was how, "+"\n"+
                                   "from thousands or even millions of light-years away, "+"\n"+
                                   "to capture an image of the hot, glowing gas falling into a "+"\n"+
                                   "black hole. An ambitious team of international astronomers "+"\n"+
                                   "and computer scientists has managed to accomplish both. "+"\n"+
                                   "Working for well over a decade to achieve the feat, "+"\n"+
                                   "the team improved upon an existing radio astronomy "+"\n"+
                                   "technique for high-resolution imaging and used it to detect "+"\n"+
                                   "the silhouette of a black hole – outlined by the glowing "+"\n"+
                                   "gas that surrounds its event horizon, the precipice beyond "+"\n"+
                                   "which light cannot escape. Learning about these mysterious "+"\n"+
                                   "structures can help students understand gravity and the "+"\n"+
                                   "dynamic nature of our universe, all while sharpening their "
                                   "math skills", Downloads_ThisUser)

    ArticleOnMaths = Textfile("Most_easy_Difficult_Maths_Theorem", "In number theory, Fermat's Last Theorem (sometimes called "+ "\n" +
                                                          "Fermat's conjecture, especially in older texts) states that no "+ "\n" +
                                                          "three positive integers a, b, and c satisfy the equation an + "+ "\n" +
                                                          "bn = cn for any integer value of n greater than 2. The cases n "+ "\n" +
                                                          "= 1 and n = 2 have been known since antiquity to have an "+ "\n" +
                                                          "infinite number of solutions" + "\n" +
                              "The proposition was first conjectured by Pierre de Fermat in "+ "\n" +
                              "1637 in the margin of a copy of Arithmetica; Fermat added that "+ "\n" +
                              "he had a proof that was too large to fit in the margin. However, "+ "\n" +
                              "there were doubts that he had a correct proof because his claim "+ "\n" +
                              "was published by his son without his consent and after his "+ "\n" +
                              "death.[2] After 358 years of effort by mathematicians, "+ "\n" +
                              "the first successful proof was released in 1994 by Andrew Wiles, "+ "\n" +
                              "and formally published in 1995; it was described as a 'stunning "+ "\n" +
                              "advance' in the citation for Wiles's Abel Prize award in 2016.["+ "\n" +
                              "3] It also proved much of the modularity theorem and opened up "+ "\n" +
                              "entire new approaches to numerous other problems and "+ "\n" +
                              "mathematically powerful modularity lifting techniques."+ "\n" ,
                              Downloads_ThisUser)

    Downloads_ThisUser.data = [ArticleONBlackholes, ArticleOnMaths]
    Files_TheOtherUser = Folder("Files", [])
    Downloads_TheOtherUser = Folder("Downloads", [])

    TheOtherUser.data = [Files_TheOtherUser, Downloads_TheOtherUser]

    Files_TheOtherUser.parent = TheOtherUser
    Downloads_TheOtherUser.parent = TheOtherUser

    BankPasswords_theother = Textfile("BankPasswords", "pass", Files_TheOtherUser)
    Alias_theother = Textfile("Alias", "Alias", Files_TheOtherUser)
    Target_theother = Textfile("Target", '1', Files_TheOtherUser)
    MessageFromUser6 = Textfile("MessageFromUser6", "Uh! The new Boss Is so mean!!" + "\n" + "I had the best record for "
                                                                                             "'sales' this month and Instead "
                                                                                             "of getting "
                                + "Of getting A heafty Bonus "
                                  "What did I get ??" + "\n" + " NOTHING" + "\n" + "Its Ridiculous" + "\n" + "And You won't believe what happened the day after that." + "\n" + "He brought his dog bruno to Work! Bastard Knows that I'm Allergic!" + "\n" + "I'm filing for him to get fired. You In?",
                                Files_TheOtherUser)

    Files_TheOtherUser.data = [BankPasswords_theother, Alias_theother, Target_theother, MessageFromUser6]

    ArticleONBStarSystems = Textfile("Star_Systems", "A star system or stellar system is a small number of stars that "+"\n"+
                                                     "orbit each other, bound by gravitational attraction. A large group "+"\n"+
                                                     "of stars bound by gravitation is generally called a star cluster or "+"\n"+
                                                     "galaxy, although, broadly speaking, they are also star systems. "+"\n"+
                                                     "Star systems are not to be confused with planetary systems, "+"\n"+
                                                     "which include planets and similar bodies (such as comets)",
                                     Downloads_TheOtherUser)
    ArticleOnphysics = Textfile("Quantum_Mechanics", "Quantum mechanics, science dealing with the behaviour of matter and "+"\n"+
                                                     "light on the atomic and subatomic scale. It attempts to describe "+"\n"+
                                                     "and account for the properties of molecules and atoms and their "+"\n"+
                                                     "constituents—electrons, protons, neutrons, and other more esoteric "+"\n"+
                                                     "particles such as quarks and gluons. These properties include the "+"\n"+
                                                     "interactions of the particles with one another and with "+"\n"+
                                                     "electromagnetic radiation (i.e., light, X-rays, and gamma rays).",
                                Downloads_TheOtherUser)

    Downloads_TheOtherUser.data = [ArticleONBStarSystems, ArticleOnphysics]

    Schedule = Textfile("Schedule", "9:00 to 12:00 - work"+"\n"+"12:00 to 13:00 - lunch" +"\n"+"13:00 to 17:00 - work"+"\n"
                        +"I hate This", desktop)
    import random
    Pending = Textfile("Potential_victims", 'Harley Foreman '+str(random.randint(9000000000,100000000000-1))+'\n'+' Tayler Perkins '+str(random.randint(9000000000,100000000000-1))+'\n'+' Emilio Hansen '+str(random.randint(9000000000,100000000000-1))+'\n'+'Humaira Carlson '+str(random.randint(9000000000,100000000000-1))+'\n'+'Louisa Bullock '+str(random.randint(9000000000,100000000000-1))+'\n'+' '
                                            'Brad Wilkins '+str(random.randint(9000000000,100000000000-1))+'\n'+' Carley Hale '+str(random.randint(9000000000,100000000000-1))+'\n'+' Kingston Thorpe '+str(random.randint(9000000000,100000000000-1))+'\n'+'Violet Lloyd '+str(random.randint(9000000000,100000000000-1))+'\n'+'Ryder Montoya '+str(random.randint(9000000000,100000000000-1)), desktop)

    desktop.data = [Schedule, Pending]

    cwd = home
    run = True
    cwd.open()
    while run:
        s = input()

        if "OPEN" in s.upper():
            query = s.split()[1]
            cwd = Open(query, cwd)
        elif "BACK" in s.upper():
            cwd = Back(cwd)
        elif "GUESS PASSWORD" in s.upper():
            guess = s.split()[2]
            if guess == "kdboquh7238":
                print("")
                break
        elif "HELP" in s.upper():
            display_rules()
        cwd.open()
if __name__== "__main__":
    main()
