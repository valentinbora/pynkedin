from pynkedin import Company
from pynkedin.auth import AuthSession

from pprint import pprint as pp

token = 'AQWz2WLJFZi1UGA80mreylqeH9da3kyW4r2KidA80K2q03rtqELBrWDooVNoxMShHiomdALu7jCZngm0Z7nD_Wl8QxxuahrXR7bXDoZTRK_7X1JrZnT3pg2FcFSvAksrXmsdcA3VFTMWUv-KDeYyMe1GlbuPt_nmWv76tjZ3h5w6PNXuLhY'

AuthSession(client_id='hbm5ioyd4zvu',
            client_secret='1kDH3xYwW2D5Qwa3', 
            access_token=token)

#company = Company(company_id=2418271)
company = Company(company_id=1703, cache=True)

#print company.updates.all()
print company.updates.filter(snid='s5750272081627451398')[0].comments
#company.updates.filter(snid=213).comments.all()
