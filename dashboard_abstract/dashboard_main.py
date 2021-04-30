import streamlit as st

from dashboard_abstract.dashboard_field import DashboardField
from functools import partial
from dashboard_abstract.__init__ import r
from dashboard_abstract.dashboard_widgets import DashboardWidgets


class DashboardMain(DashboardField):
    """
            Classe principale della Dashboard. Il suo titolo e sottotitolo vengono mostrati in ogni pagina. Di default da la possibilità di scegliere
            quale Screen mostrare, attraverso un selectbox nella sidebar

            :param title: Titolo
            :param available_screen: lista di DashboardScreen
            :param subtitle: sottotitolo
            :param logo: immagine con il logo (o path o link internet)
            :param name: nome, se non passato viene usato il titolo
            :param widget_location: posizione in cui mostrare i widget. Di default nella sidebar.
            :param widget_dict: dizionario con chiave nome e valore un partial per creare i widget (optional)
            :param widget_object: oggetto della classe DashboardWidgets (optional)
            """
    def __init__(self, title, available_screen=None, subtitle = "", logo=None, widget_dict = None, widget_location = None, name="", widget_object=None, add_recover_session=False):

        if widget_location is None:
            widget_location = st.sidebar
        if name != "":
            name = title


        if available_screen is None:
            available_screen = []
        self.available_screens_list = available_screen

        if widget_dict is None:
            widget_object = DashboardWidgets(
                widget_dict={ "Scelta screen":partial(st.sidebar.selectbox, "Scegli quale schermata visualizzare", self.get_screen_names() )})


        super().__init__(widget_location=widget_location, title=title, name=name, subtitle=subtitle,
                          widget_object=widget_object)

        self.logo = logo
        self.recover = False



    def show_heading(self):
        """
        Mostrato titolo in centro, logo nella widget_location (di default sidebar) e sottotitolo in centro
        """
        if self.logo is not None:
            self.widget_location.image(self.logo)
        self.location.markdown("# "+self.title)
        if self.subtitle is not None:
            self.location.write(self.subtitle)



    def get_screen_names(self):
        """
        Ritorna i nomi degli screen disponibili. Usato per costruire il selectbox che fa scegliere lo screen.
        """
        return [ screen.get_name() for screen in self.available_screens_list]


    def show_screen(self, screen_name):
        """
        Mostra lo screen selezionato. Solleva un'eccezione se non esisite
        :param screen_name: nome dello screen da mostrare
        :return:
        """
        trovato = False
        for screen in self.available_screens_list:
            if screen.get_name() == screen_name:
                screen.show()
                trovato = True
                break
        if not trovato:
            raise Exception("Non esiste questo schermo.")

    def show(self):
        """
        In generale, c'è un unico widget che da la possibilità di scegliere quale screen mostrare.
        Altrimenti, è possibile passare nel costruttore una widget list più estesa ma questo metodo deve essere sovrascritto
        Questo metodo mostra il titolo (e eventuale sottotitolo), raccoglie la scelta dell'utente su quale screen visualizzare e la mostra
        """

        self.show_heading()

        scelto = self.show_widgets()["Scelta screen"]
        if self.recover:
            self.recover_widget()

        self.show_screen(scelto)

    def add_screen(self, screen):
        """
        Da la possibilità di aggiungere uno Screen alla lista

        :param screen: oggetto della classe DashboardScreen
        """
        self.available_screens_list.append(screen)
        self.widgets = DashboardWidgets(
                widget_dict={"Scelta screen":partial(st.sidebar.selectbox, "Scegli quale schermata visualizzare", self.get_screen_names())})


    def add_recoverer(self, recoverer):
        self.recover_widget = recoverer.get_widget()
        self.recover = True