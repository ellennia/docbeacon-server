import sqlite3

debug = True

def make_db():
    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS pages (name text, body text, edit_gid Integer, read_gid Integer)")
    return cursor

def make_entry(db_cursor, manual_name, new_text, read_gid, write_gid):
    db_cursor.execute("INSERT INTO pages VALUES ('{}', '{}', '{}', '{}')".format(manual_name, new_text, str(read_gid), str(write_gid)))

    if debug: print('Created new entry.')

def update_entry(db_cursor, manual_name, new_text, gid):
    db_cursor.execute("INSERT INTO pages VALUES ('{}', '{}', '{}', '{}')".format(manual_name, new_text, str(gid), str(gid)))

def retrieve_entry(db_cursor, manual_name, gid):
    container = db_cursor.execute("SELECT * FROM pages WHERE name = '{}' AND read_gid = '{}'".format(manual_name, str(gid)))
    return container.fetchone()


# Debug Functions
def dump_db(db_cursor):
    container = db_cursor.execute('SELECT * FROM pages')
    print '================= Database contents: '
    for entry in container:
        print entry

