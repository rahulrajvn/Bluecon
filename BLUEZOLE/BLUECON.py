
from ctypes import *
from bluetooth import *
import string
from SendKeys import *
user32=windll.user32
from ctypes.wintypes import *
import time

LEFTDOWN   = 0x00000002
LEFTUP     = 0x00000004
#  MIDDLEDOWN = 0x00000020
#  MIDDLEUP   = 0x00000040
#  MOVE       = 0x00000001
#  ABSOLUTE   = 0x00008000
RIGHTDOWN  = 0x00000008
RIGHTUP    = 0x00000010

class POINT(Structure):
     _fields_ = [("x", c_ulong),
                 ("y", c_ulong)]

def getpos():
    global pt
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return pt.x, pt.y

def move(x,y):
    windll.user32.SetCursorPos(x,y)

def up():
     x = getpos()[0]
     y = getpos()[1]
     move(x,y-10)
def down():
     x = getpos()[0]
     y = getpos()[1]
     move(x,y+10)
def left():
     x = getpos()[0]
     y = getpos()[1]
     move(x-10,y)
def rigth():
     x = getpos()[0]
     y = getpos()[1]
     move(x+10,y)

def rightclick():
     windll.user32.mouse_event(RIGHTDOWN,0,0,0,0)
     windll.user32.mouse_event(RIGHTUP,0,0,0,0)
     
def leftclick():
     windll.user32.mouse_event(LEFTDOWN,0,0,0,0)
     windll.user32.mouse_event(LEFTUP,0,0,0,0)
     
def send(data):
     if(data==97):
          SendKeys('a')
     elif(data==98):
          SendKeys('b')
     elif(data==99):
          SendKeys('c')     
     elif(data==100):
          SendKeys('d')     
     elif(data==101):
          SendKeys('e')     
     elif(data==102):
          SendKeys('f')     
     elif(data==103):
          SendKeys('g')     
     elif(data==104):
          SendKeys('h')     
     elif(data==105):
          SendKeys('i')     
     elif(data==106):
          SendKeys('j')     
     elif(data==107):
          SendKeys('k')     
     elif(data==108):
          SendKeys('l')     
     elif(data==109):
          SendKeys('m')     
     elif(data==110):
          SendKeys('n')     
     elif(data==111):
          SendKeys('o')     
     elif(data==112):
          SendKeys('p')     
     elif(data==113):
          SendKeys('q')     
     elif(data==114):
          SendKeys('r')     
     elif(data==115):
          SendKeys('s')     
     elif(data==116):
          SendKeys('t')     
     elif(data==117):
          SendKeys('u')     
     elif(data==118):
          SendKeys('v')     
     elif(data==119):
          SendKeys('w')     
     elif(data==120):
          SendKeys('x')     
     elif(data==121):
          SendKeys('y')     
     elif(data==122):
          SendKeys('z')     
     elif(data==65):
          SendKeys('A')     
     elif(data==66):
          SendKeys('B')     
     elif(data==67):
          SendKeys('C')     
     elif(data==68):
          SendKeys('D')     
     elif(data==69):
          SendKeys('E')     
     elif(data==70):
          SendKeys('F')     
     elif(data==71):
          SendKeys('G')     
     elif(data==72):
          SendKeys('H')     
     elif(data==73):
          SendKeys('I')     
     elif(data==74):
          SendKeys('J')     
     elif(data==75):
          SendKeys('K')     
     elif(data==76):
          SendKeys('L')     
     elif(data==77):
          SendKeys('M')     
     elif(data==78):
          SendKeys('N')     
     elif(data==79):
          SendKeys('O')       
     elif(data==80):
          SendKeys('P')     
     elif(data==81):
          SendKeys('Q')     
     elif(data==82):
          SendKeys('R')     
     elif(data==83):
          SendKeys('S')     
     elif(data==84):
          SendKeys('T')     
     elif(data==85):
          SendKeys('U')     
     elif(data==86):
          SendKeys('V')     
     elif(data==87):
          SendKeys('W')     
     elif(data==88):
          SendKeys('X')     
     elif(data==89):
          SendKeys('Y')     
     elif(data==90):
          SendKeys('Z')
     elif(data==48):
          SendKeys('0')     
     elif(data==49):
          SendKeys('1')     
     elif(data==50):
          SendKeys('2')     
     elif(data==51):
          SendKeys('3')     
     elif(data==52):
          SendKeys('4')     
     elif(data==53):
          SendKeys('5')     
     elif(data==54):
          SendKeys('6')     
     elif(data==55):
          SendKeys('7')     
     elif(data==56):
          SendKeys('8')     
     elif(data==57):
          SendKeys('9')     
     elif(data==43):
          SendKeys('+')     
     elif(data==45):
          SendKeys('-')     
     elif(data==42):
          SendKeys('*')
     elif(data==47):
          SendKeys('/')     
     elif(data==61):
          SendKeys('=')     
     elif(data==35):
          SendKeys('#')     
     elif(data==44):
          SendKeys(',')     
     elif(data==46):
          SendKeys('.')     
     elif(data==59):
          SendKeys(';')     
     elif(data==58):
          SendKeys(':')
     elif(data==64):
          SendKeys('@')
     elif(data==63):
          SendKeys('?')
     elif(data==32):
          SendKeys(' ')     
     elif(data==13):
          SendKeys("{ENTER}")
          leftclick()
     elif(data==8):
          SendKeys("{BACKSPACE}")
     elif(data==40):
          SendKeys('(')     
     elif(data==41):
          SendKeys(')')     
     elif(data==38):
          SendKeys('&')     
     elif(data==33):
          SendKeys('!')
     elif(data==63497):
          up()     
     elif(data==63498):
          down()     
     elif(data==63495):
          left()     
     elif(data==63496):
          rigth()
     elif(data==63557):
          leftclick()     
     elif(data==63586):
          rightclick()     

          
          
          
          

     
        
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
        send(da)
except IOError:
    pass

print "disconnected"

client_sock.close()
server_sock.close()
print "all done"

