# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.studente import Studente
def getStudente(matricola):
    cnx=get_connection()
    studente=None
    query="""   select *
                from studente 
                where matricola ==%s"""
    if cnx is not None:
        cursor=cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM studente WHERE matricola = %s", (matricola,))
        row=cursor.fetchone()
        if row is not None:
            studente=Studente(row["matricola"], row["nome"],row["cognome"], row["CDS"])
        cursor.close()
        cnx.close()
        return studente
    else:
        print("Errore nell'apertura del database")
        return None
