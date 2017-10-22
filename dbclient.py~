'''
DocBeacon client application Pre-alpha

Command line tool for finding nearby DocBeacons
and interacting with them.
'''

# Imports
from bluetooth import *
import sys
# End imports

class Beacon:

    def __init__(self):
        pass

    def detect_service():
        pass

'''
    Scan the airwaves for nearby DocBeacons.
    Return a list of the DocBeacons found if
    any are. Be warned: This function will end
    the program if none are found.
'''
def do_search():
    # Randomized UUID, same as the server. UUID of the service that we are looking for.
    # Otherwise this search would return a lot of unwanted BT devices.
    service_uuid = 'a82d9aba-3cfb-4edd-9a81-b653a1e9b749'
    # Locates BT services using this UUID in range.
    services = find_service(uuid = service_uuid, address = None)
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
    Prints a command line selection menu.
    Accepts an array of objects for the menu options,
    the string representations of which are printed out.
'''
def print_selector(selection_list):
    # Loop until the user picks a valid option.
    while True:
        list_length = len(selection_list)
        choice = 1
        count = 1

        # Print out the list of options.
        for selection in selection_list:
            print('{}: {}'.format(str(count), selection))
            count+=1

        # Query the user for their numeric selection.
        choice = int(raw_input('> '))

        # Whoops! These aren't options in the list...
        if choice < 1 or choice > list_length:
            print('{} is not an option. Try again?'.format(choice))
        else: # But these are.
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
