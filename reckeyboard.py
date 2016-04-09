#!/usr/bin/env python
# encoding: utf-8

'''
evdev example - input device event monitor
'''


from select import select
#from evdev import ecodes, InputDevice, list_devices, AbsInfo
import evdev

devices = {}
keyboard_device = evdev.InputDevice('/dev/input/event3')
mouse_device = evdev.InputDevice('/dev/input/event12')
devices[keyboard_device.fd] = (keyboard_device, 'keyboard')
devices[mouse_device.fd] = (mouse_device, 'mouse')

def print_event(devicename, e):
    if e.type in evdev.ecodes.bytype:
        codename = evdev.ecodes.bytype[e.type][e.code]
    else:
        codename = '?'

    print devicename, e.timestamp(), e.type, evdev.ecodes.EV[e.type], e.code, codename, e.value

print('Listening for events ...\n')
while True:
    r, w, e = select(devices, [], [])

    for fd in r:
        #print devices[fd]
        device, devicename = devices[fd]

        for event in device.read():
        #for ev in keyboard_device.read():
            print_event(devicename, event)
