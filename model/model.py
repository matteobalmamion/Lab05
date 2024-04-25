from database import corso_DAO
from database import studente_DAO
class Model:
    def __init__(self):
        pass

    def getCorsi(self):
        return corso_DAO.getCorsi()
    def getStudentiCorso(self,codins):
        return corso_DAO.getStudenteCorso(codins)
    def getStudente(self,matricola):
        return studente_DAO.getStudente(matricola)
    def getCorsiStudente(self,matricola):
        return corso_DAO.getCorsiStudente(matricola)
    def iscriviStudente(self,matricola,codins):
        return corso_DAO.iscriviStudenteInCorso(matricola,codins)