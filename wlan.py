
def connect():
    import network

    ssid = "esp8266"
    password = "4esp8266"

    wlan = network.WLAN(network.STA_IF)

    if wlan.isconnected() == True:
        print("Alerady connected")
        return
    wlan.active(True)
    wlan.connect(ssid, password)

    while wlan.isconnected() == False:
        pass
        
    print("Connection successful")
    print(wlan.ifconfig())






