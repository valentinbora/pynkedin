from colorama import Fore

from pynkedin.lib.auth import Auth

client_id = 'hbm5ioyd4zvu'
client_secret = '1kDH3xYwW2D5Qwa3'

linkedin = Auth(client_id, client_secret)

print Fore.YELLOW + '---- START TOKEN RETRIEVING OPERATION ----' + Fore.RESET

scope         = raw_input(Fore.RED + 'Define a scope: ' + Fore.RESET)
redirect_uri  = raw_input(Fore.RED + 'Use a redirect url: ' + Fore.RESET)

url = linkedin.get_token_url(scope, redirect_uri)
print Fore.GREEN + 'Access this url and retrieve the token: ' + Fore.RESET + url 

token = raw_input(Fore.GREEN + 'Paste the token from redirected url: ' + Fore.RESET)
linkedin.set_token(token)

#Do stuff with your tokens
