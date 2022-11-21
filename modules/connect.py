import bluetooth

def scan():
    print("Scanning for bluetooth devices:")
    devices = bluetooth.discover_devices(lookup_names = True, lookup_class = True)
    number_of_devices = len(devices)

    for addr, name, device_class in devices:
        print(f"Device:")
        print(f"Device Name: {name}")
        print(f"Device MAC Address: {addr}")
        print(f"Device Class: {device_class}\n")
    return
    
def send_data(value: int):
    addr = "" # ADDRESS
    port = 1 # PORT Number
    
    sock = bluetooth.BluetoothSocket()
    sock.connect((addr, port))
    sock.send(bytes([value]))
    print("Connect")
    sock.close()