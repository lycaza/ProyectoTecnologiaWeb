from django.db import models
import sqlite3


class Usuario(object):

    def __init__(self, id = None, username = None):
        self.id = id
        self.username = username
    #returns Person name, ex: John Doe
    def name(self):
        return ("%s %s" % (self.id,self.username))

    @classmethod
    #returns all people inside db.txt as list of Person objects
    def getAll(self):
    	usuario = Usuario('1','lycaza')
    	#conn = sqlite3.connect('db.sqlite3')
		#c = conn.cursor()
		#result = []
		
		#for row in c.execute('SELECT * FROM auth_group '):
       	#	usuario = Usuario(row.id,row.username)
        #		result.append(usuario)
