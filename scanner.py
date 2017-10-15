'''
    Just a CLI program designed to scan for bluetooth devices surrounding
    the local machine, then pretty print the services running on them
    out onto the terminal.
'''

from bluetooth import *
from pprint import *

print 'Scanning for devices...'

try:
    for device in discover_devices(lookup_names = True):
        print '========== discovered device =========='
        pprint(device)
        print '== device services:'
        service = find_service(device)
        pprint(service)
        print '=======================================' 
except IOError:
    print 'No devices found.'
