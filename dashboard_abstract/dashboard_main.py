import streamlit as st

from dashboard_abstract.dashboard_field import DashboardField
from functools import partial

from dashboard_abstract.dashboard_widgets import DashboardWidgets


class DashboardMain(DashboardField):

    def __init__(self, title, available_fields=None, subtitle = "", logo=None, widget_list = None, widget_location = st.sidebar, name=""):

        if name != "":
            name = title

        if available_fields is None:
            available_fields = []
        self.available_screens_list = available_fields

        if widget_list is None:
            widget_list = [partial(st.sidebar.selectbox, "Scegli quale schermata visualizzare", self.get_screen_names())]

        super().__init__(widget_location=widget_location, title=title, name=name, subtitle=subtitle,
                         widget_list=widget_list)

        self.logo = logo



    def show_heading(self):
        if self.logo is not None:
            self.widget_location.image(self.logo)
        self.location.markdown("# "+self.title)
        if self.subtitle is not None:
            self.location.write(self.subtitle)



    def get_screen_names(self):
        return [ screen.get_name() for screen in self.available_screens_list]


    def show_screen(self, screen_name):

        for screen in self.available_screens_list:
            if screen.get_name() == screen_name:
                screen.show()
                break

    def show(self):
        """
        In generale, c'è un unico widget che da la possibilità di scegliere quale screen mostrare.
        Altrimenti, è possibile passare nel costruttore una widget list più estesa ma questo metodo deve essere sovrascritto
        Questo metodo mostra il titolo (e eventuale sottotitolo), raccoglie la scelta dell'utente su quale screen visualizzare e la mostra
        :return:
        """

        self.show_heading()
        scelto = self.show_widgets()[0]
        self.show_screen(scelto)

    def add_screen(self, screen):
        self.available_screens_list.append(screen)
        self.widgets = DashboardWidgets(location = self.widget_location)
        self.widgets.add_widget_singlecolumn(partial(st.sidebar.selectbox, "Scegli quale schermata visualizzare", self.get_screen_names()))
