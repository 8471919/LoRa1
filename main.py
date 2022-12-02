from hslr import HSLR
from lora import LoRa

def main():
    lora = LoRa()
    print("----- LoRa Open -----")
    lora.sendImage()

    # lora = HSLR(serial_num='/dev/ttyS0', freq=915, addr=21, power=22, rssi=True)
    
    # a = b'\xe4_\x01\xda\xabx'

    # packet = lora.addHeader(sequenceNum=1, flag=1, payload=a)
    
    # print(packet)
    
    # print("parse")
    
    # res = lora.check(packet)
    
    # print(res)

if __name__=="__main__":
    main()