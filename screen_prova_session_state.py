import json
import random
import string

from dashboard_abstract.dashboard_screen import DashboardScreen
## importing socket module
import socket
import streamlit as st
import os
class ScreenSessione(DashboardScreen):
    def __init__(self, title, name, chart_list=None, subtitle="", widget_dict=None):
        super().__init__(title, name, chart_list=chart_list, subtitle=subtitle, widget_dict=widget_dict)


    def show(self):
        self.show_heading()

        dflt = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

        col1, col2 = st.beta_columns(2)
        with col1:
            st.write("**Il tuo codice di sessione è:**")
        with col2:
            st.code(dflt)
            if st.button("SALVA SESSIONE"):
                with open("globallog.json", "r") as fp1:
                    data = json.load(fp1)
                    if "log.json" in os.listdir(os.curdir):
                        with open("log.json", "r") as fp2:
                            total = json.load(fp2)
                            total[dflt] = data
                        with open("log.json", "w") as fp2:
                            fp2.write(json.dumps(total))
                    else:
                        with open("log.json", "w") as fp2:
                            fp2.write(json.dumps({dflt:data}))


        col1, col2 = st.beta_columns(2)
        with col1:
            st.write("**Inserisci il codice per recuperare la sessione:**")
        with col2:
            scelta = st.text_input("")
            rec = st.button("RECUPERA SESSIONE")
        if rec:
            #controllo che esista
            trovato = False
            with open("log.json", "r") as fp:
                data = json.load(fp)
                if scelta in data:
                    trovato = True

            if trovato:
                st.success("Sessione esistente")
                st.write(data[scelta])
            else:
                st.error("Sessione inesistente")

        with st.beta_expander("Vedi elenco sessioni"):
            st.success("Elenco sessioni")
            with open("log.json", "r") as fp:
                for line in fp:
                    st.write(line)

        with open("globallog.json", "r") as fp:
            data = json.load(fp)
            st.write(data)
