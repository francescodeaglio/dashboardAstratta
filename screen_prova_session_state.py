import random
import string

from dashboard_abstract.dashboard_screen import DashboardScreen
## importing socket module
import socket
import streamlit as st

class ScreenSessione(DashboardScreen):
    def __init__(self, title, name, chart_list=None, subtitle="", widget_list=None):
        super().__init__(title, name, chart_list=chart_list, subtitle=subtitle, widget_list=widget_list)
        self.elenco_scelti = []


    def show(self):
        self.show_heading()

        dflt = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        while dflt in self.elenco_scelti:
            dflt = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

        col1, col2 = st.beta_columns(2)
        with col1:
            st.write("Il tuo codice di sessione è:")
        with col2:
            st.code(dflt)
            if st.button("SALVA SESSIONE"):
                self.elenco_scelti.append(dflt)
                with open("log.txt", "a") as fp:
                    fp.write(dflt + "\n")





        st.success("Elenco sessioni")
        with open("log.txt", "r") as fp:
            for line in fp:
                st.write(line)

