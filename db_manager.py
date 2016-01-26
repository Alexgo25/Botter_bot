__author__ = 'Alexander'
import sqlite3


connect = sqlite3.connect('db')
db_helpr = connect.cursor()

def checkUsr(usrID):
    query = 'SELECT COUNT(*) FROM user WHERE telegramID = %s;' %usrID
    db_helpr.execute(query)
    result = db_helpr.fetchone()
    print(result)
    if result == (1,):
        return True
    else:
        return False

def createUser(user_id,usrname):
    params = (user_id,usrname)
    query = 'INSERT INTO user VALUES (?,?);'
    db_helpr.execute(query,params)
    connect.commit()

def saveMsg(text,fromID,toID):
    params = (text ,fromID ,toID,)
    query = 'INSERT INTO msg VALUES (?,?,?);'
    db_helpr.execute(query,params)
    connect.commit()

def printUserInfo(usrID):
    query = 'SELECT * FROM user WHERE telegramID = %s;'  %usrID
    db_helpr.execute(query)
    print(db_helpr.fetchone())

def getUserChatID(usrname):
    query = 'SELECT telegramID FROM user WHERE username = (?);'
    db_helpr.execute(query,(usrname,))
    result = db_helpr.fetchone()
    print(result)
    return result
def getUserList():
    query = 'SELECT username FROM user'
    db_helpr.execute(query)
    result = db_helpr.fetchone()
    return result