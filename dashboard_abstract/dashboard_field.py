import streamlit as st
from dashboard_abstract.dashboard_widgets import DashboardWidgets
from dashboard_abstract.logger import Logger


class DashboardField():
    """
            Classe astratta da cui ereditano tutte le altre. Fornisce funzionalità di base.

            :param title: Titolo.
            :param location: posizione in cui mostrare il contenuto. Di default st (quindi centro schermo).
            :param widget_location: posizione in cui mostrare i widget. Di default st (quindi centro schermo).
            :param name: Nome dell'oggetto, se non è fornito in automatico viene preso il titolo.
            :param subtitle: Sottotitolo
            :param widget_dict: dizionario con chiave nome e valore un partial per creare i widget (optional)
            :param widget_object: oggetto della classe DashboardWidgets (optional)
    """
    def __init__(self, title="", location=None, widget_location=None, name=None, subtitle="", widget_dict=None, widget_object=None):

        if location is None:
            location = st
        if widget_location is None:
            widget_location = st

        self.title = title
        self.location = location
        self.widget_location = widget_location
        if name is None:
            self.name = title
        else:
            self.name = name
        self.subtitle = subtitle

        if widget_dict is None and widget_object is None:
            w = DashboardWidgets(location=self.widget_location)
        elif widget_dict is None and widget_object is not None:
            w = widget_object
        elif widget_dict is not None and widget_object is None:
            w = DashboardWidgets(location=widget_location,widget_dict=widget_dict)
        else:
            st.error("Errore. Non puoi passare contemporaneamente l'oggetto Widget e la lista di widget")

        self.widgets = w



    def __enter__(self):
        """
        Beta per usare i campi con with
        """
        self.show_heading()

    def __exit__(self, exc_type, exc_val, exc_tb):
        #nulla
        pass

    def show_heading(self):
        """
        Mostra titolo e eventuale sottotitolo. I titoli sono i markdown con il numero di # che dipende dall'importanza.
        Metodo astratto.

        """

    def show_widgets(self):
        """
        Mostra i widget

        :return: quanto selezionato dall'utente nei vari widget, sotto forma di tupla
        """

        return self.widgets.show_widgets()

    def get_name(self):
        """
        Ritorna il nome

        :return: il nome dell'oggetto
        """
        return self.name

    def set_widgets_object(self, widgets):
        """
        Permette di impostare come widget un oggetto della classe DashboardWidgets

        :param widgets: Oggetto della classe DashboardWidgets
        """
        self.widgets=widgets