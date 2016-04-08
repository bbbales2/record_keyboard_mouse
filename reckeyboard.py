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
devices[keyboard_device.fd] = keyboard_device
devices[mouse_device.fd] = mouse_device

def print_event(e):
    #if e.type == ecodes.EV_SYN:
    #    if e.code == ecodes.SYN_MT_REPORT:
    #        print('time {:<16} +++++++++ {} ++++++++'.format(e.timestamp(), ecodes.SYN[e.code]))
    #    else:
    #        print('time {:<16} --------- {} --------'.format(e.timestamp(), ecodes.SYN[e.code]))
    #else:
    if e.type in evdev.ecodes.bytype:
        codename = evdev.ecodes.bytype[e.type][e.code]
    else:
        codename = '?'

    print e.timestamp(), e.type, evdev.ecodes.EV[e.type], e.code, codename, e.value

print('Listening for events ...\n')
while True:
    r, w, e = select(devices, [], [])

    for fd in r:
        #print devices[fd]

        for event in devices[fd].read():
        #for ev in keyboard_device.read():
            print_event(event)
