# coding=utf-8
from multiprocessing.dummy import Pool as ThreadPool
from time import time as timer
import requests
import os
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}

try:
    os.system('clear')
    print("""
  _________________.---.______
(_(______________(_o o_(____()   C0ded By Zekkel AR
        mrf  .___.'. .'.___.    
             \ o    Y    o /   Family Attack Cyber
              \ \__   __/ /   All CMS Scanner
               '.__'-'__.'  
                   '''
 

""")    
    ganteng = input('   [ ^ ] Your Files => ')
    f= open(ganteng, 'r')
    woh = f.read().splitlines()
except IOError:
    pass
woh = list((woh))
def Domains(url):

    if '://' not in url:
        return 'http://'+url
    else:
        return url

def DetectCMS(site):
    url = Domains(site)
    Joomla = '{}/administrator/help/en-GB/toc.json'.format(url)    # "COMPONENTS_BANNERS_BANNERS"
    Joomla2 = '{}/administrator/language/en-GB/install.xml'.format(url)   # <author>Joomla!
    Joomla3 = '{}/plugins/system/debug/debug.xml'.format(url)  # <author>Joomla!
    Joomla4 = '{}/administrator/'.format(url)
    Wordpress = '{}'.format(url)  # /wp-content/ or /wp-inclues
    Wordpress2 = '{}/wp-includes/js/jquery/jquery.js'.format(url)  # (c) jQuery Foundation
    drupal = '{}/misc/ajax.js'.format(url)  # Drupal.ajax
    drupal2 = '{}'.format(url)  # /sites/default/files
    Opencart = '{}/admin/view/javascript/common.js'.format(url)  # getURLVar(key)
    osCommerce = '{}/admin/includes/general.js'.format(url)  # function SetFocus()
    vBulletin = '{}/images/editor/separator.gif'.format(url)
    vBulletin2 = '{}/js/header-rollup-554.js'.format(url)  # /js/header-rollup-554.js
    larapel = '{}/.env'.format(url)
    larapel2 = '{}/vendor/autoload.php'.format(url)
    larapel3 = '{}/vendor/'.format(url)

    a = ('[ + ] {} | JoomSkuy' .format(site))
    b = ('[ + ] {} | WordSkuy' .format(site))
    c = ('[ + ] {} | PrestaSkuy' .format(site))
    d = ('[ + ] {} | DrupSkuy' .format(site))
    e = ('[ + ] {} | oCommerSkuy' .format(site))
    f = ('[ + ] {} | vBulletSkuy' .format(site))
    g = ('[ + ] {} | OpenSKuy' .format(site))
    h = ('[ + ] {} | LaravSkuy' .format(site)) 
    try:
        CheckLaravel3 = requests.get(larapel3, timeout=10, headers=Headers)
        if 'phpunit/' in CheckLaravel3 or 'Index of /vendor' in CheckLaravel3:
            try:
                print(h)
                with open('Laravel.txt', 'a') as XW:
                    XW.write(url + '\n')
            except:
                pass
            return 'LaravSkuy'
        CheckLaravel2 = requests.get(larapel2, timeout=10, headers=Headers)
        if CheckLaravel2.status_code == 200:
            try:
                print(h)
                with open('Laravel.txt', 'a') as XW:
                    XW.write(url + '\n')
            except:
                pass
            return 'LaravSkuy'    
        CheckLaravel = requests.get(larapel, timeout=10, headers=Headers).content
        if 'DB_HOST' in str(CheckLaravel) or 'DB_PASSWORD' in str(CheckLaravel):
            try:
                print(h)
                with open('Laravel.txt', 'a') as XW:
                    XW.write(url + '\n')
            except:
                pass 
            return 'LaravSkuy'

        CheckWp = requests.get(Wordpress, timeout=10, headers=Headers).content
        if '/wp-content/' in str(CheckWp) or '/wp-inclues/' in str(CheckWp):
            try:
                print(b)
                with open('Wordpress.txt', 'a') as XW:
                    XW.write(url + '\n')
            except:
                pass
            return 'wordpress'
        CheckWp2 = requests.get(Wordpress2, timeout=10, headers=Headers).content
        if '(c) jQuery Foundation' in str(CheckWp2):
            try:
                print(b)
                with open('Wordpress.txt', 'a') as XW:
                    XW.write(url + '\n')
            except:
                pass
            return 'wordpress'
        CheckJom = requests.get(Joomla, timeout=10, headers=Headers).content
        if '"COMPONENTS_BANNERS_BANNERS"' in str(CheckJom):
            try:
                print(a)
                print('[ + ] JoomSkuy')
                with open('joomla.txt', 'a') as XW:
                    XW.write(url + '\n')
            except:
                pass
            return 'joomla'
        CheckJom2 = requests.get(Joomla2, timeout=10, headers=Headers).content
        if '<author>Joomla!' in str(CheckJom2):
            try:
                print(a)
                with open('joomla.txt', 'a') as XW:
                    XW.write(url + '\n')
            except:
                pass
            return 'joomla'
        CheckJom3 = requests.get(Joomla3, timeout=10, headers=Headers).content
        if '<author>Joomla!' in str(CheckJom3):
            try:
                print(a)
                with open('joomla.txt', 'a') as XW:
                    XW.write(url + '\n')
            except:
                pass
            return 'joomla'
        CheckJom4 = requests.get(Joomla4, timeout=10, headers=Headers).content
        if 'content="Joomla!' in str(CheckJom4):
            try:
                print(a)
                with open('joomla.txt', 'a') as XW:
                    XW.write(url + '\n')
            except:
                pass
            return 'joomla'
        CheckDrupal = requests.get(drupal, timeout=10, headers=Headers).content
        if 'Drupal.ajax' in str(CheckDrupal):
            try:
                print(d)
                with open('drupal.txt', 'a') as XW:
                    XW.write(url + '\n')
            except:
                pass
            return 'drupal'
        CheckDrupal2 = requests.get(drupal2, timeout=10, headers=Headers).content
        if '/sites/default/files' in str(CheckDrupal2):
            try:
                print(d)
                with open('drupal.txt', 'a') as XW:
                    XW.write(url + '\n')
            except:
                pass
            return 'drupal'
        CheckOpencart = requests.get(Opencart, timeout=10, headers=Headers).content
        if 'getURLVar(key)' in str(CheckOpencart):
            try:
                print(g)
                with open('opencart.txt', 'a') as XW:
                    XW.write(url + '\n')
            except:
                pass
            return 'opencart'
        CheckOsCommerce = requests.get(osCommerce, timeout=10, headers=Headers).content
        if 'function SetFocus()' in str(CheckOsCommerce):
            try:
                print(e)
                with open('oscommerce.txt', 'a') as XW:
                    XW.write(url + '\n')
            except:
                pass
            return 'oscommerce'
        Checkvb = requests.get(vBulletin, timeout=10, headers=Headers).content
        if 'GIF89a' in str(Checkvb):
            try:
                print(f)
                with open('vBulletin.txt', 'a') as XW:
                    XW.write(url + '\n')
            except:
                pass
            return 'vBulletin'
        Checkvb2 = requests.get(vBulletin2, timeout=10, headers=Headers).content
        if 'js.compressed/modernizr.min.js' in str(Checkvb2):
            try:
                print(f)
                with open('vBulletin.txt', 'a') as XW:
                    XW.write(url + '\n')
            except:
                pass
            return 'vBulletin'
        if 'content="vBulletin' in str(CheckDrupal2):
            try:
                print(f)
                with open('vBulletin.txt', 'a') as XW:
                    XW.write(url + '\n')
            except:
                pass
            return 'vBulletin'
        if 'var prestashop =' in str(CheckDrupal2):
            try:
                print(c)
                with open('prestashop.txt', 'a') as XW:
                    XW.write(url + '\n')
            except:
                pass
            return 'prestashop'
        else:
            try:
                with open('unknown.txt', 'a') as XW:
                    XW.write(url + '\n')
            except:
                pass
            return 'unknown'
    except Exception as e:
        #print('[ + ] {} | unkown' .format(url))
        pass
        #print(e)
def Run_Work(site):
    url = Domains(site)
    DetectCMS(url)

def Main():

    start = timer()
    pp = ThreadPool(500)
    pr = pp.map(Run_Work, woh)
    print('Time: ' + str(timer() - start) + ' seconds')


if __name__ == "__main__":
    Main()
