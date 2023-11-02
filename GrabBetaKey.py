from bs4 import BeautifulSoup
import requests

def main():

    URL="https://forum.makemkv.com/forum/viewtopic.php?t=1053"
    html=requests.get(URL)

    print(html.text)
if __name__ == '__main__':
    main()
