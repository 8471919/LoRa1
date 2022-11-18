def removeGarbageInJson(payload):
    
    # to remove the garbage value
    braceByte = "}".encode()
    processed = payload.split(braceByte)
    processed.pop()
    processed.append(braceByte)
    processed = ("".encode()).join(processed)
    
    return processed
            
def addHeader(self, sequenceNum, flag, payload, Checksum):
        if len(payload) > 228:
           print("payload size is over")
           exit()
        
        header = bytearray(12)
        
        # change int to byte
        sequenceNum = sequenceNum.to_bytes(2, 'big')
        flag = flag.to_bytes(1, 'big')
        payloadSize = len(payload).to_bytes(1, 'big')
        
        header[0:6] = self.DEST_MAC
        header[6:8] = sequenceNum
        header[8:9] = flag
        header[9:10] = payloadSize
        
        print("header 0~9 : " + str(header[0:10]))
        
        # calculate checksum
        # add the each 16bit of the packet
        sum = 0
        for i in range(0, 10, 2):
            #cast each portion of the header into an integer from bytes
            int_val = int.from_bytes(header[i:i+2], 'big')
            #return the binary string of the sum + int_val, remove the first two characters
            sum = bin(sum + int_val)[2:]
            #if the sum is more than 2 bytes, deal with carryout...
            if len(sum) > 16:
                #then remove the first character from the sum binary string, cast to a binary integer, add one
                sum = int(sum[1:], 2) + 1
            else:
                #if less than 16, then just cast sum to a binary integer
                sum = int(sum, 2)
        
        for i in range(0, len(payload), 2):
            int_val = int.from_bytes(payload[i:i+2], 'big')
            sum = bin(sum + int_val)[2:]
            if len(sum) > 16:
                sum = int(sum[1:], 2) + 1
            else:
                sum = int(sum, 2)
        
        print("sum : " + str(sum))
        
        for i in CheckSum:
        if(i == '1'):
            ReceiverChecksum += '0'
        else:
            ReceiverChecksum += '1'
        
        return ReceiverChecksum

        
        checkSum = sum.to_bytes(2, 'big')
        
        print("checksum : " + str(checkSum))
                
        header[10:12] = checkSum
        
        return header + payload