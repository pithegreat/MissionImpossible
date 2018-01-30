import os

def sensor():
    for i in os.listdir("/sys/bus/w1/devices"):
        if i != "w1_bus_master1":
            aerial = i
    return aerial

def read(serial):
    location = "/sys/bus/w1/devices/" + serial + "/w1_slave"
    tfile = open(location)
    text = tfile.read()
    tfile.close
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperaturedata = float(temperaturedata[2:])
    celsius = temperature / 1000
    farenheit = (celsius * 1.8) + 32
    return celsius, farenheit

def loop(serial):
    while True:
        if read(serial) != None:
            print "%0.2f C" % read(serial)[0]
            print "%0.2f F" % read(serial)[1]

def kill():
    quit()

if __name__ == "__main__":
    try:
        serial = sensor()
        loop(serial)
    except KeyBoardInterrupt:
        kill()

