from Gmail.Gmail import GmailService
from bs4 import BeautifulSoup
from urllib.request import urlopen

sender = '<your_email>'
to = '<default_receiver>'
credentials_path = './credentials.json'
token_path = './token.pickle'

def send():
    gmail = GmailService('./credentials.json', './token.pickle')
    html_content = '<h4>Hello World</h4>'
    message = gmail.createMessageHtml(sender, to, "Hello World", html_content, "Hello World")
    gmail.sendMail("me", message)

if __name__ == "__main__":
    send()