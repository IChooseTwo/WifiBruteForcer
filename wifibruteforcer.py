import time
import pywifi
from pywifi import const
import atexit
import random

#Success rate: 0.001% chance of getting the password but i mean if it does

count = 0 #This makes it loop since it was easier that way

print("Get ready in 5 seconds")
time.sleep(5) #Just gets u ready


guess_password = "" #args am i right chat
while count < 5: #Loops am I right chat?
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuwxyz1234567890" 
    guess_password = ''.join(random.choice(letters) for i in range(random.randint(8,20)))
    print(list(guess_password))
    time.sleep(1)

wifi = pywifi.PyWiFi()

iface = wifi.interfaces()[0]

iface.disconnect()
time.sleep(1)
assert iface.status() in\
    [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

profile = pywifi.Profile()
profile.ssid = 'Wifi Name' #Name of wifi #Yes I left my dog name in there by mistake
profile.auth = const.AUTH_ALG_OPEN
profile.akm.append(const.AKM_TYPE_WPA2PSK)
profile.cipher = const.CIPHER_TYPE_CCMP
profile.key = guess_password

iface.remove_all_network_profiles()
tmp_profile = iface.add_network_profile(profile)

iface.connect(tmp_profile)
time.sleep(30)
assert iface.status() == const.IFACE_CONNECTED
atexit.register(print,"IF YOU SEE THIS IT WORKED AND IT HAS EXITED but i doubt it.")


iface.disconnect()
time.sleep(1)
assert iface.status() in\
    [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
