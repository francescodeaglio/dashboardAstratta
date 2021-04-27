import streamlit as st
from dashboard_abstract.dashboard_widgets import DashboardWidgets

class DashboardField():

    def __init__(self, title="", location=st, widget_location=st, name=None, subtitle="", widget_list=None, widget_object=None):
        if widget_list is None:
            widget_list = []
        self.title = title
        self.location = location
        self.widget_location = widget_location
        if name is None:
            self.name = title
        else:
            self.name = name
        self.subtitle = subtitle

        if widget_list is None and widget_object is None:
            w = DashboardField(self.widget_location)
        elif widget_list is None and widget_object is not None:
            w = widget_object
        elif widget_list is not None and widget_object is None:
            w = DashboardWidgets(location=widget_location,widget_list=widget_list)
        else:
            st.error("Errore. Non puoi passare contemporaneamente l'oggetto Widget e la lista di widget")
        self.widgets = w
    def show_heading(self):
        """
        Mostra titolo e eventuale sottotitolo. I titoli sono i markdown con il numero di # che dipende dall'importanza
        :return:
        """

    def show_widgets(self):
        return self.widgets.show_widgets()


    def get_name(self):
        return self.name