from hslr import HSLR

class LoRa:
    
    def __init__(self):
        
        self.SERIAL_NUMBER = "/dev/ttyS0"
        self.FREQUENCY = 915
        self.ADDRESS = 100
        self.POWER = 22
        self.RSSI = True
        
        self.SEND_TO_WHO = 21
        
        self.node = HSLR(serial_num=self.SERIAL_NUMBER, freq=self.FREQUENCY, addr=self.ADDRESS, power=self.POWER, rssi=self.RSSI)
        
    def sendImage(self):
        imageBytes = bytearray()
        
        for i in range(0, 228):
            imageBytes += b'\x01'
                
        print(imageBytes)
        print("Image size : " + str(len(imageBytes)))
        
        # node setting
        self.node.addr_temp = self.node.ADDRESS
        self.node.set(self.node.FREQUENCY, self.SEND_TO_WHO, self.node.POWER, self.node.RSSI)
                
        # send the imageBytes
        self.node.transmitImage(imageBytes)
        
        self.node.set(self.node.FREQUENCY, self.node.ADDRESS, self.node.POWER, self.node.RSSI)
    
    def getImage(self):
        
        while True:
            imageBytes = self.node.receiveImage()
            
            if imageBytes != None:
                break
        
        return imageBytes