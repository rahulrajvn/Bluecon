import appuifw
import socket
import graphics
import e32
import btsocket as socket

keyboard_state={}
last_keycode=0

def bt_connect():
    global sock
    sock=socket.socket(socket.AF_BT,socket.SOCK_STREAM)
    target=''
    if not target:
        address,services=socket.bt_discover()
        print "Discovered: %s, %s"%(address,services)
        if len(services)>1:
            choices=services.keys()
            choices.sort()
            choice=appuifw.popup_menu([unicode(services[x])+": "+x
                                        for x in choices],u'Choose port:')
            target=(address,services[choices[choice]])
        else:
            target=(address,services.values()[0])
    print "Connecting to "+str(target)
    sock.connect(target)
    print "OK."
    
    
def callback(event):
    if event['type'] == appuifw.EEventKeyDown:
        keyboard_state[event['scancode']]=1
    elif event['type'] == appuifw.EEventKeyUp:
        keyboard_state[event['scancode']]=0
    elif event['type'] == appuifw.EEventKey:
        last_keycode=event['keycode']
        
    canvas.text((0,60),u'%s'%(last_keycode))
    sock.sendall(u'%s'%(last_keycode))
    

bt_connect()
    
canvas=appuifw.Canvas(event_callback=callback)
appuifw.app.body=canvas


lock=e32.Ao_lock()
appuifw.app.exit_key_handler=lock.signal
lock.wait()
