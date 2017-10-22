'''
    Just a CLI program designed to scan for bluetooth devices surrounding
    the local machine, then pretty print the services running on them
    out onto the terminal.
'''

from bluetooth import *
from pprint import *

print 'Scanning for BT devices in range of this machine...'
print '=======================================' 

number = 0
try:
    for device in discover_devices(lookup_names = True):
        print 'Device {}:'.format(str(number))
        if device[1] == '':
            device[1] = '{unnamed device}'

        print '    Device name: {}'.format(device[1])
        print '    MAC address: {}'.format(device[0])

        print '    Device services:'
        services = find_service(device)
        if len(services) == 0:
            print '         No services found on {}.'.format(device[1])
        else:
            pprint(services)
        number += 1

except IOError:
    print 'No devices found.'
