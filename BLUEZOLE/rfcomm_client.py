

from bluetooth import *
import string
from SendKeys import SendKeys as sk
#import SendKeys

parseStr = lambda x: x.isalpha() and x or x.isdigit() and int(x) or x.isalnum() and x or len(set(string.punctuation).intersection(x)) == 1 and x.count('.') == 1 and float(x) or x
server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "BLUECONTROL",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ],
#                   protocols = [ OBEX_UUID ]
                    )
                   
print "Waiting for connection on RFCOMM channel %d" % port

client_sock, client_info = server_sock.accept()
print "Accepted connection from ", client_info

try:
    while True:
        data = client_sock.recv(1024)
        if len(data) == 0: break
        da=parseStr(data)
        print "received [%s]" % (data)
        print "received         [%d]" % (da*2)
        sk(%d %'data')
except IOError:
    pass

print "disconnected"

client_sock.close()
server_sock.close()
print "all done"

