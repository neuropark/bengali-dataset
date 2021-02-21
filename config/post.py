import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name("config/creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open('Bengali Dataset (Responses)').sheet1
with open('config/mail.json') as f:
    data = dict(json.load(f))

if data["email"] == "ENTER YOUR EMAIL INSIDE THE QUOTE" or "" or "":
    print("please enter a valid email adderss\nGo to config folder. Open the mail.json file and \nenter your email inside the quote containing 'ENTER YOUR EMAIL INSIDE THE QUOTE'")

else:
    with open('entries.txt', 'r', encoding='utf8') as f:
        for entry in f.readlines():
            sheet.insert_row(['', entry.replace('\n', ''), data["email"]],3)
            print('DONE!')
