import grovepi

ledbar = 7

grovepi.pinMode(ledbar,"OUTPUT")

grovepi.ledBar_init(ledbar, 0)
while True:
    for i in range(0,11)
        grovepi.ledBar_setLevel(i)
        time.sleep(.2)
