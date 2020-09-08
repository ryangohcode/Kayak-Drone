#!/usr/bin/env python
import zerorpc
import time

relay = {'horn':['U45Y4',1] , 
                    'sensor':['5SA7G',1],
                    'whiteLED':['5SA7G',2],
                    'greenLED':['X6SVH',1],
                    'redLED':['X6SVH',2] }


c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4243")

def runContinuousCycle(rpcClient, device,delay):
     if device in relay:
         rpcClient.runContinuousCycle(relay[device][0], relay[device][1], delay)
     else:
         print("No such device: %s" % device )
     
     
def stopContinuousCycle(rpcClient, device):
     if device in relay:
         rpcClient.stopContinuousCycle(relay[device][0], relay[device][1])
     else:
         print("No such device: %s" % device )
     

try:
      runContinuousCycle(c,'horn',1)
      time.sleep(2)
      stopContinuousCycle(c,'horn')
     
except Exception, e:
      print "An error occurred: %s" % e 
