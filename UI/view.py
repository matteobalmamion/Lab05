import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        #Row 1
        self.ddCorso=ft.Dropdown(label="Corso", hint_text="Selezionare un corso",options=[],width=700,autofocus=True,on_change=self._controller.handleCambioCorso)
        self._controller.addCorsi()
        self.btnCercaIscritti=ft.ElevatedButton(text="Cerca iscritti", on_click=self._controller.handleCercaIscritti)
        row1=ft.Row([self.ddCorso,self.btnCercaIscritti],alignment=ft.MainAxisAlignment.CENTER)
        #Row 2
        self.txtMatricola=ft.TextField(hint_text="matricola")
        self.txtNome = ft.TextField(hint_text="nome",read_only=True)
        self.txtCognome = ft.TextField(hint_text="cognome",read_only=True)
        row2=ft.Row([self.txtMatricola,self.txtNome,self.txtCognome],alignment=ft.MainAxisAlignment.CENTER)
        #Row 3
        self.btnCercaStudenti=ft.ElevatedButton(text="Cerca studente", on_click=self._controller.handleCercaStudenti)
        self.btnCercaCorsi = ft.ElevatedButton(text="Cerca corsi", on_click=self._controller.handleCercaCorsi)
        self.btnIscrivi = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handleIscrivi)
        row3=ft.Row([self.btnCercaStudenti,self.btnCercaCorsi,self.btnIscrivi],alignment=ft.MainAxisAlignment.CENTER)
        #Row 4
        self.txtOut=ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        self._page.add(row1,row2,row3,self.txtOut)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
