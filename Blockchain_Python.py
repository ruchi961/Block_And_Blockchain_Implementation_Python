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


no_blocks = int(input("How many blocks to create: "))
print("".center(80,"*"))
blocks_list=[]

#accepting blocks information and forming blockchain
for i in range(no_blocks):
    print()
    print("".center(50,"-"))
    print("Block ",i+1)
    print("".center(50,"-"))
    flag=True
    while flag:
        blockID = input("Enter block ID for the block: ")
        
        if len(blocks_list)!=0:
            if int(blockID) == blockID_sequence_remember:
                flag = False
            else:
                print("Block id must be in increasing order, and non-repetative.")
                #checking repetition of block id code not required if block id is sequential above if will do
##            for j in blocks_list:
##                if j.blockID == blockID:
##                    print("Block id already entered, enter a new block id.")
##                    break
##                else:
##                    flag= False
##                    break
        else:
            if int(blockID) != 1:
                print("Block ID must start from 1.")
            else:
                flag=False
    blockID_sequence_remember = int(blockID) +1
    data = input("Enter data of the block: ")
    block_obj = block(blockID,data)
    if i!=0:
        block_obj.prev_hash = blocks_list[-1].hash
    print("block Created")
    blocks_list.append(block_obj)
print("".center(80,"*"))

#displaying blocks details
for j in blocks_list:
    print("".center(50,"-"))
    print("Block ",i+1)
    print("".center(50,"-"))
    j.displayDetails()
