from colorama import Fore

from pynkedin.lib.auth import AuthService

client_id = 'hbm5ioyd4zvu'
client_secret = '1kDH3xYwW2D5Qwa3'

print Fore.YELLOW + '---- START TOKEN RETRIEVING OPERATION ----' + Fore.RESET
#scope         = raw_input(Fore.RED + 'Define a scope: ' + Fore.RESET)
#redirect_uri  = raw_input(Fore.RED + 'Use a redirect url: ' + Fore.RESET)
scope = 'r_fullprofile'
redirect_uri = 'http://linkedin.gosimplysocial.com'


service = AuthService(client_id, client_secret, redirect_uri)

url = service.get_authorize_url(scope)
print Fore.GREEN + 'Access this url and retrieve the token: ' + Fore.RESET + url 

auth_code = raw_input(Fore.GREEN + 'Paste the code from the redirected url: ' + Fore.RESET)
access_token = service.get_access_token(auth_code)
print Fore.GREEN + 'Acess TOKEN: ' + Fore.RESET + access_token 

api = service.create_session(access_token)

#Do stuff with your session
