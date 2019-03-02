# 1 Introduce what this program is and how it works
from io import BytesIO
import requests
from docx import Document
from docx.shared import Inches
from docx.shared import Pt
import time
def main():
    
    print("Welcome to the Flash Card Creator")
    time.sleep(.6)
    print("Please fill out the info....")
    name = input("Name of file: ")
    f = open(name + ".docx", "w")
    a = open(name + ".docx" , "rb")
    document = Document()
    # 2 Then ask the user how many flash cards they would like to create
    amount = int(input("How many flash cards: "))
    times = 0

    # makes sure it only makes as many flashcards as they instructed
    flashCardNum = 1

    # 3 Then have them fill each one out
    while times < amount:
        times += 1
        title = input("Title of " + str(flashCardNum) + " card: " )

        header = document.add_heading(title + "\n")
        

        sections = document.sections
        section = sections[0]
        section.page_width = Inches(5)
        body = input("line: ")
        paragraph = document.add_paragraph(body + "\n")
        paragraph.style = 'List Bullet'
        def line():
            body = input("line: ")
            paragraph = document.add_paragraph(body + "\n")
            paragraph.style = 'List Bullet'
        addLine = input("Add another line yes/no: ")
        while addLine == "yes" or addLine == "Yes":
            line()
            addLine = input("Add another line yes/no: ")

        addImg = input("Add image yes/no: ")
        

        if addImg == "yes" or addImg == "Yes":
            image = input("Image url: ")
            response = requests.get(image)  # no need to add stream=True
            binary_img = BytesIO(response.content) 
            document.add_picture(binary_img, width=Inches(2))
            document.save(name + ".docx")
        else:
            print("Okay") 
            time.sleep(.3)
            document.save(name + ".docx")

           
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