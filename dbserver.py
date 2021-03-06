'''
 DocBeacon Management Software (DBMS) Pre-alpha
 Startup file, called when DBMS starts.
 This runs a DocBeacon information server.

 DocBeacons are meant to be small Bluetooth devices that broadcast
 using Bluetooth Low-Energy, the purpose of physical objects and spaces.
 They are designed to be used with mobile apps that allow users to quickly
 see the locations and purposes of their physical environments.
 See README for more information.

 Despite the fact that is is supposed to be BLE, this is using the normal
 BT protocol currently for simplicity and will be ported over in the future.
 This is the part of code that is intended to be ran on a beacon and send
 manual data to clients, such as those running on phones, laptops, or watches.

 It uses a sqlite3 database to store manuals for later retrieval.
 This table has the following fields:

 MANUALS TABLE
 | name (TEXT) | body (TEXT) | revision (DATE) | write_id (TEXT) | read_id (TEXT) |

 The name is the name of the manual. The body, is the actual text of it.
 write_id is the id of the group that can edit this text. read_id is the group
 that can see it.
 
 When someone connects to a DocBeacon server, they must provide a public key
 with which to identify themselves. If they present a blank public key,
 then they are part of the implicit group 'public', which has the group id
 0 on every DocBeacon. Therefore, if the read_id of a manual is marked as 0,
 then anyone can connect and read one of these manual. If it is set to 1, and
 a random person connects, then they will be unable to read the manual, as only
 people who provide a public key matching the private key linked with group 1
 will be able to read it. The same applies to the write id, which determines who can write a manual.

 There are two premade groups:
 GROUPS:
 -1: The Administrator Group
 0: The Public Group
 {1-255}: Custom groups

 Whether or not a public user can create manuals is up to the global policy settings of the DocBeacon, which can be changed in the file docbeacon.rc. The setting pcreate = False must be changed to pcreate = True for public users to create new manuals- otherwise they are restricted to only interacting with existing ones. In this mode, only the administrator group can create new manuals.

 # Manuals
    Manuals themselves should be encoded in markdown, not html. The full featureset of HTML is not needed in manuals, and frankly isn't wanted (at least by the developer).

 # Style info
    Pls don't use P2.7 style prints i.e. print '' with no parenthesis.

 # Developer
     As of this point, it has been completely written by Ellen Hebert.
'''

''' Imports '''
import sqlite3
from dbinterface import *
from bluetooth import *
from flask import *
''' End imports '''

''' BT uuid '''
application_uuid = 'a82d9aba-3cfb-4edd-9a81-b653a1e9b74'

'''
    Waits for bt clients to connect, and responds accordingly when they do.
    rfcomm
'''
def listen_for_connections(uuid):
    uuid = '94f39d29-7d6d-437d-973b-fba39e49d4ee'
    server_socket = BluetoothSocket(RFCOMM)
    port = PORT_ANY
    server_socket.bind(("", port))
    server_socket.listen(1)
    advertise_service(server_socket, "DocBeacon server", uuid,
            service_classes = [uuid, SERIAL_PORT_CLASS],
            profiles = [ SERIAL_PORT_PROFILE ])

    print('Advertising and waiting for connections at channel {}'.format(port))
    client_socket, client_info = server_socket.accept()
    print("Accepted connection from", client_info)

    try:
        while True:
            data = client_socket.recv(1024)
            if len(data) == 0: break
            print("received [%s]" % data)

'''
                            USER INTERFACE
'''

''' Formats a manual for a user to read. '''
def format_entry(entry):
    print('====================================================')
    print('== Page name: {}'.format(entry[0]))
    print('----------------------------------------------------')
    print(entry[1])
    print('====================================================')


'''
                            BEGIN STARTUP
'''
app = Flask(__name__)

''' Used to view a manual. '''
@app.route('/<string>')
def dochome(string):
    print string
    if not len(string) == 0:
        return render_template('{}.html'.format(string))
    else:
        return 'Welcome to view home'

''' Used to submit changes to a manual. '''
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass

print('DocBeacon Management Software, Alpha')
listen_for_connections(application_uuid)
print('Waiting for bluetooth connections...')

#cr = make_db()

#print("Made db")
