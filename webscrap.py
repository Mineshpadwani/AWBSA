import requests
from bs4 import BeautifulSoup
def webscrapping():
    print("Welcome to Web  Scrapping Tool")
    url=input("Enter the url")
    #step1: get the html
    res = requests.get(url)
    htmlContent=res.content
    #step 2: Parse the html
    soup=BeautifulSoup(htmlContent,'html.parser')
    #print(htmlContent)
    while True:
        choice = int(input("""\n please enter the type of scan you want to run
                        1) Fetch whole HTML code
                        2) Fetch Head Section
                        3) Fetch Title Tag
                        4) Fetch Comment Sections
                        5) Fetch all the paragraphs
                        6) Fetch Anchor tags 
                        7) Fetch Navigation Elements
                        8) Fetch Parent
                        9) Fetch Siblings
                        10) Download Images
                        11) exit \n"""))
        print("you have selected option: ", choice)

        #step 3: HTML tree traversal
        if(choice==1):
            print('Here is the SOUP object containing whole HTML Code')
            #print(soup) #simply print html code
            print(soup.prettify()) #print the whole preformatted html code

        elif(choice==2):
            print('<----------Here is your HEAD SECTION---------->')
            print(soup.head) #fetch the whole section
            print(type(soup.head))

        elif(choice==3):
            #fetch title tag
            print('<----------Here is your TITLE TAG---------->')
            title=soup.title #fetch title tag from html file
            print(title)   #print the title tag
            print(type(title))   #print the class of title tag bs4.element tag
            #commonly used types of object
            print(type(title)) #1. tag
            print(type(title.string)) #2.navigable string
            print(type(soup)) #3. beautifulsoup

        elif(choice==4):
            #4 Comment
            print("<----------Here is your COMMENT SECTION--------->")
            comments="<p><!-- this is a example of comment --></p>"
            soup2=BeautifulSoup(comments,'html.parser')
            print(soup2.p) #get paragraph tag written in comment
            print(soup2.p.string) # get strings written in comment block
            print(type(soup2.p.string)) #get the bs4.element.comment

        elif(choice==5):
            print('<----------Here is your PARAGRAPH SECTION---------->')
            # get first element in the html page
            print(soup.find('p'))
            #fetch all the paragraphs
            paras=soup.find_all('p')
            print(paras)
            #get classes of any element in the html page
            print(soup.find('p')['class'])
            #find all the elements with class lead
            print(soup.find_all("p", class_="lead"))
            #get the  text from the tags
            print(soup.find('p').get_text) #get text from p tag
            print(soup.get_text()) #get all the text in the html page

        elif(choice==6):
            print('<----------Here is your ANCHOR TAGS---------->')
            #get all anchor tages
            anchors=soup.find_all('a')
            all_links = set()
            print(anchors)
            #get all the links on the page
            for link in anchors:
                if(link.get('herf')!='#'):
                    linkText="https://codewithharry.com" +link.get('href')
                    all_links.add(link)
                    print(linkText)

        elif(choice==7):
            print('<----------Here is your NAVIGATION BAR---------->')
            #get navigation bar content
            menuContent=soup.find(id='navbarSupportedContent')
            for elements in menuContent.contents:
                print(elements)

            #get all the strings in navigation bar
            for item in menuContent.strings:
                print(item)

            #gether all the strings in navigation bar
            for item in menuContent.stripped_strings:
                print(item)

        elif(choice==8):
            print('<----------Here is your PARENT NAVIGATION BAR---------->')
            menuContent = soup.find(id='navbarSupportedContent')
            #get the parent of the navigation bar
            print(menuContent.parent)
            #get all the parents
            for item in menuContent.parents:
                print(item.name)

        elif(choice==9):
            print('<----------Here is your SIBLINGS SECTION---------->')
            menuContent = soup.find(id='navbarSupportedContent')
            #next and previous siblings
            print(menuContent.next_sibling.next_sibling)    #blank line is considered as next or previous sibling
            print(menuContent.previous_sibling.previous_sibling)
        elif(choice==10):
            i = 1
            for soup in soup.find_all('img'):
                source = soup.get('src')
                i += 1
                r = requests.get(source).content
                with open("{}.jpg".format(i), 'wb') as f:
                    f.write(r)
        else:
            if choice>=11:
                exit("You tried wrong attribute")

        print("Do you want to continue? y/n : ")
        if input()=="y":
            continue
        else:
            break