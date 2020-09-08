import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")

try:
      for item in c.streaming_range(10, 20, 2):
           print item
except Exception, e:
      print "An error occurred: %s" % e 