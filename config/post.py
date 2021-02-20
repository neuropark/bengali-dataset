import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name("config/creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open('Bengali Dataset (Responses)').sheet1

with open('entries.txt', 'r', encoding='utf8') as f:
    for entry in f.readlines():
        sheet.insert_row(['', entry.replace('\n', '')],3)
