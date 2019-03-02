# 1 Introduce what this program is and how it works
import time
def main():
    
    print("Welcome to the Flash Card Creator")
    time.sleep(.6)
    print("Please fill out the info....")
    name = input("Name of file: ")
    a = open(name + ".txt" , "a")
    # 2 Then ask the user how many flash cards they would like to create
    amount = int(input("How many flash cards: "))
    times = 0

    # makes sure it only makes as many flashcards as they instructed
    flashCardNum = 1

    # 3 Then have them fill each one out
    while times < amount:
        times += 1
        title = input("Title of " + str(flashCardNum) + " card: " )
        a.write(title + "\n")
        body = input("Body: ")
        a.write(body + "\n")
        a.write("\n")
        flashCardNum += 1
        # 4 Finally save all of that data to a text file so they can print it out
    a.close()
    
    another = input("Would you like to make another set yes/no: ")
    if another == "yes" or another == "Yes":
        main()
    else:
        print("Thanks so much for using Flash Card Creator!")
        time.sleep(1)
        exit()  
        


# 5 Thank them for using your program 

if __name__ == "__main__":
    main()