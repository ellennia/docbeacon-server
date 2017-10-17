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
        return services
    else:
        return services

'''
    Connect to a detected DocBeacon.

    Returns a connection.
'''
def connect_to(beacon):
    # Get information about the beacon we are connecting to.
    device_name = beacon["name"]
    connection_host = beacon["host"]
    connection_port = beacon["port"] 

    print("Connecting to device:{} on host:{}".format(device_name, connection_host))
    sock = BluetoothSocket(RFCOMM)
    connection = sock.connect((connection_host, connection_port))
 
'''
    Prints a command line selection menu
'''
def print_selector(selection_list):
    choice = 1

    while True:
        count = 1
        list_length = len(selection_list)
        # Print out detected DocBeacon list
        for selection in selection_list:
            print('{}: {}'.format(str(count), selection[1]))
            count+=1
        choice = int(raw_input('> '))

        # Whoops! These aren't options...
        if choice > list_length or choice < 1:
            print('{} is not an option. Try again?'.format(choice))
        else:
            return choice
 
''' Formats a manual for a user to read. '''
def format_entry(entry):
    print('====================================================')
    print('== Page name: {}'.format(entry[0]))
    print('----------------------------------------------------')
    print(entry[1])
    print('====================================================')
    return connection

''' Startup '''
print('DocBeacon client application Pre-alpha')
options = ["Scan for beacons", "Exit"]
result = int(print_selector(options))
if result == 1:
    print('Scanning for nearby DocBeacons (this may take a while)... ')
    clients = do_search()
    print('Search complete. {} DocBeacons found'.format(len(clients)))
    clients = ['Hihi', 'Cutey']

    print('Choose beacon: ')
    choice = print_selector(clients)
    # DocBeacon list
    print('You have chosen beacon {}.'.format(choice))
    connect_to(clients[choice]) 
elif result == 2:
    sys.exit(0)
