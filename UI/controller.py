import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCercaIscritti(self,e):
        corso=self._view.ddCorso.value
        if corso is None or corso == "":
            self._view.create_alert("Inserire il corso")
            return
        studenti=self._model.getStudentiCorso(corso)
        for studente in studenti:
            self._view.txtOut.controls.append(ft.Text(studente))
        self._view.update_page()
    def handleCercaStudenti(self,e):
        name=self._view.txtMatricola.value
        if name is None or name == "":
            self._view.create_alert("Inserire la matricola")
            return None
        studente=self._model.getStudente(name)
        if studente is None or name == "":
            self._view.create_alert("La matricola inserita non è presente nel database")
            return None
        self._view.txtNome.value=studente.nome
        self._view.txtCognome.value=studente.cognome
        self._view.update_page()

    def handleCercaCorsi(self, e):
        matricola=self._view.txtMatricola.value
        if matricola is None or matricola == "":
            self._view.create_alert("Inserire la matricola")
            return None
        corsi=self._model.getCorsiStudente(matricola)
        if corsi is None or corsi==[]:
            self._view.create_alert("Lo studente non è immatricolato a nessun corso")
            return None
        self._view.txtOut.controls.append(ft.Text(f"Risultano {len(corsi)} corsi"))
        for corso in corsi:
            self._view.txtOut.controls.append(ft.Text(corso))
        self._view.update_page()
    def handleIscrivi(self,e):
        matricola=self._view.txtMatricola.value
        studente=self._model.getStudente(matricola)
        if studente is None:
            self._view.create_alert("La matricola inserita non è presente nel database")
            self._view.update_page()
            return None
        corso=self._view.ddCorso.value
        if matricola is None or matricola == "":
            self._view.create_alert("Inserire la matricola")
            self._view.update_page()
            return None
        if corso is None:
            self._view.create_alert("Inserire il corso")
            self._view.update_page()
            return None
        esito=self._model.iscriviStudente(matricola,corso)
        if esito:
            self._view.txtOut.controls.append(ft.Text("Iscrizione riuscita"))
            self._view.update_page()
            return None
        self._view.txtOut.controls.append(ft.Text("Iscrizione fallita"))
        self._view.update_page()
        return None
    def addCorsi(self):
        corsi=self._model.getCorsi()
        for corso in corsi:
            self._view.ddCorso.options.append(ft.dropdown.Option(key=corso.codins,text=corso))
        self._view.update_page()
    def handleCambioCorso(self,e):
        self.corso_selezionato = self._view.ddCorso.value
