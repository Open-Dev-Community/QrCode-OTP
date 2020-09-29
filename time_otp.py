import qrcode
import os
import shutil
import secrets
import string
from pyotp import TOTP
import random



images = 'images'

try:
    shutil.rmtree(images, ignore_errors=True)
except:
    exit()

# Folder Updation
if not os.path.isdir(images):
    os.makedirs(images, exist_ok=True)

# User Key	
def user_gen():
	"""
	Returns a randomly-chosen element from a non-empty sequence to manage a basic level of security
	"""
	x = ''.join(random.choices(string.ascii_letters, k = 10))
	return x
	

# function to timebased-OTP
def gen_rolling_code(key):
    '''
    OTP token generated gets updated every 60Secs
    '''
    totp = TOTP(key, digits=6)
    return totp.now()


def code_gen():
    '''
    input_cypher = cypher OTP to be added to the qrcode
    '''
    token = ''  # needs input random string
    img = qrcode.make(token)
    img.save("images\\"+str(token)+'.png')
