from src.sensors.futek import IPM650
import serial.tools.list_ports

def main():
    futek_port = r"/dev/tty.usbserial-811647"
    # futek_port = 'COM4'

    loadcell = IPM650(port = futek_port, baudrate = 115200, timeout = 1)
    loadcell.open_connection()
    for i in range(5):
        loadcell.start_test(5, print_vals = True)
    # print(loadcell.data)
    loadcell.close_connection()
    loadcell.store_data(False)

def test():
    pass

if __name__ == "__main__":
    main()
    # test() 