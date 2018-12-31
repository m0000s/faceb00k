#Coded by grap3
#HailBQ
#Based in a MRX tool
#

import os
import datetime
import mechanicalsoup
import getpass
from time import sleep

print('Please wait. Loading ... ')
browser          = mechanicalsoup.StatefulBrowser()
loginPage        = browser.open('http://facebook.com/login.php')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
#Data login
emailUser        = input('Input email   : ')
passUser         = getpass.getpass('Input password: ')
#Login data fill
def login():
    print('[+] Logging...')
    loginSection     = browser.select_form('form[id=\"login_form\"]') #Locating form section
    browser['email'] = emailUser
    browser['pass']  = passUser
    browser.submit_selected() #Submit login session changes

#Parsing profile url

def enter_profile():
    urlProfile       = browser.get_current_page().find_all('a',class_='_2s25 _606w')[0]['href']
    profile          = browser.open(urlProfile) #Opening profile url
def select_photo():
    print('[+] Posting photo...')
    getProfile       = browser.get(browser.get_current_page().find_all('a',class_='_2s25 _606w')[0]['href'])
    upload           = getProfile.soup.select('input[class="_n _5f0v"]')
    print(getProfile.get_current_page().findAll('input',class_='_n _5f0v'))
    upload[0]['name']   = os.path.join(APP_ROOT,'grap3.jpg')
    target = upload['name']
    uploadFinal      = browser.post(target,profile.url)
    print(uploadFinal)

#<a href="#" class="_156p _1o5e" ajaxify="/profile/picture/menu_dialog/?context_id=u_0_13&amp;profile_id=100025252275340" rel="dialog" role="button" id="u_0_1d"><div class="_3-95"><i class="_1din _156q _1o6f img sp_E0oHonVlduq sx_c610f4"></i></div>Actualizar</a>
#<input class="_n _5f0v" title="Elige un archivo para subir" accept="image/*, image/heic, image/heif" autofocus="1" id="js_as" name="photo" type="file">
#<button data-testid="profilePicSaveButton" class="_4jy0 _4jy3 _4jy1 _51sy selected _42ft" type="submit" value="1">Guardar</button>
login()
print('[*] Succes logged in.')
enter_profile()
select_photo()
print('[*] Succes photo upload.')
print('[*] Succes!.')
