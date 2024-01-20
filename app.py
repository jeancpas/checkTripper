import requests
import easygui
import webbrowser
from bs4 import BeautifulSoup

URL = "https://www.tripper.nl/deal/speeltegoed-gamestate-50-euro-9-locaties-korting"
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'html.parser')
button = soup.find('div', class_="deal-button")
text = button.get_text()
if "Uitverkocht!" not in text:
    easygui.msgbox("TIME TO BUY!", title="ALERT")
    webbrowser.open(URL, new=0, autoraise=True)
else: easygui.msgbox("SAD PEPE", title="ALERT")
