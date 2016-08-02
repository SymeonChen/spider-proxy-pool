#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sqlite3
import uuid
db = 'proxylist.db'
try:
    conn = sqlite3.connect(db)
    conn.execute('''CREATE TABLE PROXY
            (UID TEXT PRIMARY KEY NOT NULL,
            ADDRESS TEXT  NOT NULL,
            PORT INT NOT NULL,
            LOCATION INT,
            PROTOCOL TEXT);''')
except sqlite3.OperationalError:
    pass
finally:
    conn.close()


def insert(address, port, location='default', protocol='default'):
    uid = str(uuid.uuid5(uuid.NAMESPACE_DNS,address))

    conn = sqlite3.connect(db)
    try:
        conn.execute("INSERT INTO PROXY VALUES (?, ?, ?, ?, ?)",[uid,address,port,location,protocol])
        print('insert: '+str(address))
        pass
    except sqlite3.IntegrityError as e:
        conn.execute("UPDATE PROXY SET ADDRESS = ?, PORT = ?, LOCATION = ?, PROTOCOL = ? WHERE UID=?",[address,port,location,protocol,uid])
        print('update: '+str(address))
        pass    

    except sqlite3.ProgrammingError as e:
        #TODO
        pass
    finally:
        conn.commit()
        conn.close()


def select(address=-1,port=-1,location=-1,protocol=-1):
    conn = sqlite3.connect(db)
    try:
        if (address,port,location,protocol)==(-1,-1,-1,-1):
            cursor = conn.execute('SELECT * FROM PROXY')
        else:
            xlist=""
            nlist=[]
            if address  != -1:
                xlist += ' ADDRESS=? AND'
                nlist.append(address)
            if port     != -1:
                xlist += ' PORT=? AND'
                nlist.append(port)
            if location != -1:
                xlist += ' LOCATION=? AND'
                nlist.append(location)
            if protocol != -1:
                xlist += ' PROTOCOL=? AND'
                nlist.append(protocol)
            
            newlist = 'SELECT * FROM PROXY WHERE'+xlist[:-3]
            #remove last 'AND'

            cursor = conn.execute(newlist,nlist)
        cursor = list(cursor)

    except Exception as e:
        print(str(e))
    finally:
        conn.close()
    
    return(cursor)


def delete(address=-1,port=-1,location=-1,protocol=-1):
    conn = sqlite3.connect(db)
    try:
        if (address,port,location,protocol)==(-1,-1,-1,-1):
            cursor = conn.execute('DELETE FROM PROXY')
        else:
            xlist=""
            nlist=[]
            if address  != -1:
                xlist += ' ADDRESS=? AND'
                nlist.append(address)
            if port     != -1:
                xlist += ' PORT=? AND'
                nlist.append(port)
            if location != -1:
                xlist += ' LOCATION=? AND'
                nlist.append(location)
            if protocol != -1:
                xlist += ' PROTOCOL=? AND'
                nlist.append(protocol)
            
            newlist = 'DELETE FROM PROXY WHERE'+xlist[:-3]
            #remove last 'AND'

            cursor = conn.execute(newlist,nlist)

    except Exception as e:
        print(str(e))
    finally:
        conn.commit()
        conn.close()
    
def selectAllAddress():
    conn = sqlite3.connect(db)
    try:
        cursor = conn.execute('SELECT ADDRESS FROM PROXY ')
        cursor = ["%s" % x for x in list(cursor)]

    except Exception as e:
        print(str(e))
    finally:
        conn.close()
    
    return cursor
    #output example
    #['117.135.250.88', '117.40.35.233', '61.143.158.238', '124.202.180.6']


