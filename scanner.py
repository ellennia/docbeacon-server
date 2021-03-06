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
    devices_found = discover_devices(duration = 15, lookup_names = True)

    for device in devices_found:
        device_name = device[1]
        mac_address = device[0]
        print 'Device {}:'.format(str(number))

        if device_name == '' or device_name == None:
            device_name = 'unnamed device'
        print '    Device name: {}'.format(device_name)
        print '    MAC address: {}'.format(mac_address)

        print '    Device services:'
        services = find_service(device)
        if len(services) == 0:
            print '         No services found on {}.'.format(device[1])
        else:
            pprint(services)
        number += 1

except IOError:
    print 'No devices found.'
