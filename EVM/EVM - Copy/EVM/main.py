import eel
import MySQLdb
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint

db = MySQLdb.connect(host="localhost",user="jgan",
                     passwd="1234",
                     db="EVM")
# you must create a Cursor object. It will let you execute all the queries you need
cur = db.cursor()
# Initializing GUI Library
eel.init('gui')

@eel.expose
def check_rfid():
	reader = SimpleMFRC522()
    try:
            id, text = reader.read()
            print(id)
            print(text)

    finally:
            GPIO.cleanup()
	pass

	try:
           cur.execute("Select Numpad from test Where RFID='(%s'", id))
           # print all the first cell of all the rows
           for row in cur.fetchall():
               db_id =(row[0])
               if id == db_id:
                   print "RFID Matches"
               else:
                   print("RFID ERROR!", db_id)
                   # clear `entry`
               db.close()

               e.delete('0', 'end')
    except:
             print("RFID Except!", db_id)

@eel.expose
def check_pin(pin):


    # inform function to use external/global variable
    global pin

    if value == 'C':
        # remove last number from `pin`
        pin = pin[:-1]
        # remove all from `entry` and put new `pin`
        e.delete('0', 'end')
        e.insert('end', pin)

    elif value == 'E':
        # check pin
        try:
            cur.execute("Select Numpad from test Where pin='(%s'", pin))
            # print all the first cell of all the rows
            for row in cur.fetchall():
                stored_pin =(row[0])
                print stored_pin
                print pin
                if pin == stored_pin:
                    print "PIN OK"
                    pass
                else:
                    print("PIN ERROR!", stored_pin)
                    # clear `pin`
                    pin = ''
                    # clear `entry`
                db.close()

                e.delete('0', 'end')
        except:
             print("PIN Except!", stored_pin)

    else:
        # add number to pin
        pin += value
        # add number to `entry`
        e.insert('end', value)

    print("Current:", pin)

def check_finger():
    ## Search for a finger
##

## Tries to initialize the sensor
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

        if ( f.verifyPassword() == False ):
            raise ValueError('The given fingerprint sensor password is wrong!')

    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        exit(1)

    ## Gets some sensor information
    print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

    ## Tries to search the finger and calculate hash
    try:
        print('Waiting for finger...')

        ## Wait that finger is read
        while ( f.readImage() == False ):
            pass

        ## Converts read image to characteristics and stores it in charbuffer 1
        f.convertImage(0x01)

        ## Searchs template
        result = f.searchTemplate()

        positionNumber = result[0]
        accuracyScore = result[1]

        if ( positionNumber == -1 ):
            print('No match found!')
            exit(0)
        else:
            print('Found template at position #' + str(positionNumber))
            print('The accuracy score is: ' + str(accuracyScore))

        ## OPTIONAL stuff
        ##

        ## Loads the found template to charbuffer 1
        f.loadTemplate(positionNumber, 0x01)

        ## Downloads the characteristics of template loaded in charbuffer 1
        characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')

        ## Hashes characteristics of template
        print('SHA-2 hash of template: ' + hashlib.sha256(characterics).hexdigest())

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)

eel.start('index.html', size=(1000,600))
