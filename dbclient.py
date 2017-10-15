'''
DocBeacon client application Pre-alpha

Command line tool for finding nearby DocBeacons
and interacting with them.
'''

# Imports
from bluetooth import *
import sys
# End imports

'''
    Scan the airwaves for nearby DocBeacons.
    Return a list of the DocBeacons found if
    any are. Be warned: This function will end
    the program if none are found.
'''
def do_search():
    # Randomized UUID, same as the server.
    uuid = 'a82d9aba-3cfb-4edd-9a81-b653a1e9b749'
    # Locates BT services using this UUID in range.
    services = find_service(uuid = uuid, address = None)
    '''
        If no services are found, print this to the user
        then exit. Otherwise, return the list of services
        that have been found.
    '''
    if len(services) == 0:
        print('No DocBeacons found nearby. :(')
        sys.exit(0)
    else:
        return services

'''
    Connect to a detected DocBeacon.

    Returns a connection.
'''
def connect(beacon):
    # Get information about the beacon we are connecting to.
    device_name = beacon["name"]
    connection_host = beacon["host"]
    connection_port = beacon["port"] 

    print("Connecting to device:{} on host:{}".format(device_name, connection_host))
    sock = BluetoothSocket(RFCOMM)
    connection = sock.connect((connection_host, connection_port))

    print("Connection established to {}".format(host))
    return connection

''' Startup '''

print('DocBeacon client application Pre-alpha')

print('Scanning for nearby DocBeacons (this may take a while)... ')
clients = do_search()
print('Search complete. {} DocBeacons found'.format(len(clients)))

# Connect to the first beacon found.
connection = connect(clients[0])

