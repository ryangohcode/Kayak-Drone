#!/usr/bin/env python
'''To turn on white LED'''

import zerorpc
import time

relay = {'horn':['U45Y4',1] , 
                    'sensor':['5SA7G',1],
                    'whiteLED':['5SA7G',2],
                    'greenLED':['X6SVH',1],
                    'redLED':['X6SVH',2] }


c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4243")

def onDevice(rpcClient, device):
     if device in relay:
         rpcClient.openOneRelayChannel(relay[device][0],relay[device][1],)
         print("whiteLED is on")
     else:
         print("No such device: %s" % device )


try:
     onDevice(c,'whiteLED')

except Exception, e:
      print "An error occurred: %s" % e 
