import time
import Level1
class Textfile:
    def __init__(self, name,content):
        self.name =name
        self.content = content
    

    def open(self):
        print(self.name)
        print("\n"*5)
        print(self.content)

class Folder:
    def __init__(self,name,data,parent):
        self.name = name
        self.data = data
        self.parent = parent
    def open(self):
        print(self.name)
        print("\n"*5)
        for i in data:
            print(i)

def Open(name, folder):
    if name in folder.data:
        name.open
    else:
        print("No file named",name,"in this folder")

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
def main():
    print("Hello!")
#    time.sleep(1)
    print("You are The best ethical hacker the govenment currently has")
 #   time.sleep(0.5)
    print("and it's your job to shut down a Scam Call Center in Mumbai")
  #  time.sleep(3)
    print("You have gained acess to one of their computers using your skill and can shut down their entire operation")
   # time.sleep(3)
    print("But there's one problem ... the file that contains all the information about their employees is password protected and you cannot hack it.")
   # time.sleep(3)
    print("Now you have to guess the password in order to obtain the file")
   # time.sleep(0.5)
    print("Browse through his computer files and look for clues that can help you guess the password")
   # time.sleep(0.5)
    print("Good Luck!")
    #\time.sleep(1)
    print(r"P.S -------> if you are stuck somewhere type 'help'")
    display_rules()
    print(" "*5 + "USER5 COMPUTER")
    print()
    print()
   # Level1.main()
    print("Congratulations! you have sucessfully retieved the files! mission 1 Complete!")
    time.sleep(3)
    print("Now it's time for your next assingment")
    time.sleep(3)
    print("We need you to hack into a computer, but it uses the Latest security... which makes it impossible to hack")
    time.sleep(1)
    print("So you will have to guess the password")
    time.sleep(1)
    print("Enter ONE character at a time to check if it's in the actual password")
    time.sleep(1)
    print("You can only enter a total of 10 worng guesses")
    time.sleep(1)
    print("Good Luck!")
    import Level2
    sucessful = Level2.main()
    if sucessful:
        print("Congratulations,you Have done it!")
    else:
        print("you Failed")
main()
