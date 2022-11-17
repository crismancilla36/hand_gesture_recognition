import bluetooth

def scan():
    print("Scanning for bluetooth devices:")
    devices = bluetooth.discover_devices(lookup_names = True, lookup_class = True)
    print(devices)
    number_of_devices = len(devices)
    print(f"{number_of_devices} devices found")

    for addr, name, device_class in devices:
        print(f"Device:")
        print(f"Device Name: {name}")
        print(f"Device MAC Address: {addr}")
        print(f"Device Class: {device_class}\n")
    return
    
def send_data(value: int):
    addr = "8C:E5:C0:00:E3:DA" # ADDRESS
    port = 1 # PORT Number

    sock = bluetooth.BluetoothSocket()
    sock.connect((addr, port))
    sock.send(value)
    print("Connect")
    sock.close()

if __name__ == '__main__':
    scan()
    send_data(5)