#importing modules
from datetime import datetime
from hashlib import sha256
from random import randint

#block class
class block:
    def __init__(self, blockID, data):
        self.blockID = blockID
        self.timestamp = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.data = data
        self.nonce = randint(1,10)
        self.prev_hash = "0"
        self.concate = self.blockID+self.timestamp+self.data+str(self.nonce)+self.prev_hash
        self.hashSHA = sha256(self.concate.encode())
        self.hash = self.hashSHA.hexdigest()
    def displayDetails(self):
        print("Block Details are:")
        print("".center(50,"-"))
        print("Block ID: ",self.blockID,"\nTimestamp: ",self.timestamp,"\nData: ",self.data,"\nNonce: ",self.nonce,"\nPrevious Hash: ",self.prev_hash,"\nHash: ",self.hash)

blockID = input("Enter block ID for the block: ")
data = input("Enter data of the block: ")
b1  = block(blockID,data)
b1.displayDetails()
