from bs4 import BeautifulSoup
import requests

def main():

    URL="https://forum.makemkv.com/forum/viewtopic.php?t=1053"
    html=requests.get(URL)

    Scraper=BeautifulSoup(html.content, 'html.parser')

    #print(html.text)

    results=Scraper.find(id='post_content3548')
    #print(results)
    BetaKeyCode=results.find('code')


    print(BetaKeyCode.text)


if __name__ == '__main__':
    main()
