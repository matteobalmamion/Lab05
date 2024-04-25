# Add whatever it is needed to interface with the DB Table corso
from model.studente import Studente
from database.DB_connect import get_connection
from model.corso import Corso

def iscriviStudenteInCorso(matricola,codins):
    cnx = get_connection()
    result = []
    query = """INSERT IGNORE INTO `iscritticorsi`.`iscrizione` 
            (`matricola`, `codins`) 
    VALUES(%s,%s)
    """
    if cnx is not None:
        cursor = cnx.cursor()
        cursor.execute(query, (matricola, codins,))
        cnx.commit()
        cursor.close()
        cnx.close()
        return True
    else:
        return False
def getCorsi():
    cnx=get_connection()
    result=[]
    if cnx is not None:
        cursor=cnx.cursor(dictionary=True)
        query="""SELECT * FROM corso"""
        cursor.execute(query)
        for row in cursor:
            result.append(Corso(row["codins"],row["crediti"],row["nome"],row["pd"]))
        cursor.close()
        cnx.close()
        return result
    else:
        print("Errore nell'apertura del database")
        return None


def getStudenteCorso(codins):
    cnx=get_connection()
    studenti=[]
    if cnx is not None:
        cursor=cnx.cursor(dictionary=True)
        query="""SELECT studente.* 
                FROM iscrizione, studente 
                WHERE iscrizione.matricola=studente.matricola AND iscrizione.codins=%s"""
        cursor.execute(query,(codins,))
        for row in cursor:
            studenti.append(Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))
        cursor.close()
        cnx.close()
        return studenti
    else:
        return None

def getCorsiStudente(matricola):
    cnx=get_connection()
    result=[]
    query = """ SELECT corso.* 
        FROM corso, iscrizione 
        WHERE iscrizione.codins=corso.codins AND iscrizione.matricola = %s
        """
    if cnx is not None:
        cursor=cnx.cursor(dictionary=True)
        cursor.execute(query, (matricola,))

        for row in cursor:
            result.append(Corso(row["codins"], row["crediti"], row["nome"],row["pd"]))
        cursor.close()
        cnx.close()
        return result
    else:
        return None
