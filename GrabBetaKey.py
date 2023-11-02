from bs4 import BeautifulSoup
import requests
from datetime import datetime

def main():

    URL="https://forum.makemkv.com/forum/viewtopic.php?t=1053"
    html=requests.get(URL)

    #Use Bs4 to grab all the html from the webpage
    Scraper=BeautifulSoup(html.content, 'html.parser')


    #Narrow the results down by using the id
    results=Scraper.find(id='post_content3548')
    
    #The beta key is within a tag called 'code.' Take the html from 'results' and narrow it all the way down to only include what's in the 'code' tag
    BetaKeyCode=results.find('code')

    #Print the betakey code to verify
    #print(BetaKeyCode.text)


    now=datetime.now()

    year=now.strftime("%Y")
    month=now.strftime("%B")

    f=open("Keys.txt", "a")
    f.write(month + " " + year + " " + BetaKeyCode.text + "\n")
    f.close()


if __name__ == '__main__':
    main()
