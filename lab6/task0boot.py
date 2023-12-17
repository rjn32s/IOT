import network
ssid = '6IOT'
password = '123456789'
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid = ssid , password = password)
print(ap.ifconfig())