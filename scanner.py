from bluetooth import *
from pprint import *

print 'Scanning for devices...'

try:
    for device in discover_devices(lookup_names = True):
        print '===================='
        pprint(device)
        service = find_service(device)
        pprint(service)
except IOError:
    print 'No devices found.'
