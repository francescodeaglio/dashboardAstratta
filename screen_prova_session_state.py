import random
import string

from dashboard_abstract.dashboard_screen import DashboardScreen
## importing socket module
import socket
import streamlit as st

class ScreenSessione(DashboardScreen):
    def __init__(self, title, name, chart_list=None, subtitle="", widget_list=None):
        super().__init__(title, name, chart_list=chart_list, subtitle=subtitle, widget_list=widget_list)


    def show(self):
        self.show_heading()

        dflt = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

        col1, col2 = st.beta_columns(2)
        with col1:
            st.write("**Il tuo codice di sessione è:**")
        with col2:
            st.code(dflt)
            if st.button("SALVA SESSIONE"):
                with open("log.txt", "a") as fp:
                    fp.write(dflt + "\n")



        col1, col2 = st.beta_columns(2)
        with col1:
            st.write("**Inserisci il codice per recuperare la sessione:**")
        with col2:
            scelta = st.text_input("")
            rec = st.button("RECUPERA SESSIONE")
        if rec:
            #controllo che esista
            trovato = False
            with open("log.txt", "r") as fp:
                for line in fp:
                    if line.strip() == scelta:
                        trovato=True
                        break

            if trovato:
                st.success("Sessione esistente")
            else:
                st.error("Sessione inesistente")

        with st.beta_expander("Vedi elenco sessioni"):
            st.success("Elenco sessioni")
            with open("log.txt", "r") as fp:
                for line in fp:
                    st.write(line)

