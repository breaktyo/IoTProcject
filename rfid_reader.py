import time
from mfrc522 import MFRC522
from config import *


class RfidReader:
    def __init__(self):
        self.running = True
        self.value = 0


    def detect_card_once(self):
        reader = MFRC522()
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        self.running = True
        while self.running:
            status, TagType = reader.MFRC522_Request(reader.PICC_REQIDL)
            if status == reader.MI_OK:
                status, uid = reader.MFRC522_Anticoll()
                if status == reader.MI_OK:
                    uid_num = 0
                    for i in range(len(uid)):
                        uid_num += uid[i] << (i*8)

                    now_str = time.strftime("%Y-%m-%d %H:%M:%S")
                    
                    
                    self.value = uid_num

                    while status == reader.MI_OK and self.running:
                        status, _ = reader.MFRC522_Anticoll()
                        
                    print("Karta usunięta")
                    self.running = False
                        
        
