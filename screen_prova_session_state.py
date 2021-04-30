import json
import random
import string

from streamlit.script_runner import RerunException

from dashboard_abstract.dashboard_screen import DashboardScreen
## importing socket module
import socket
import streamlit as st
from dashboard_abstract.__init__ import r
from dashboard_abstract.utils import get_session_id
import os
class ScreenSessione(DashboardScreen):
    def __init__(self, title, name, chart_list=None, subtitle="", widget_dict=None):
        super().__init__(title, name, chart_list=chart_list, subtitle=subtitle, widget_dict=widget_dict)


    def show(self):
        self.show_heading()

        dflt = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

        col1, col2 = st.beta_columns(2)

        filename = os.path.join(os.curdir, "json", str(get_session_id()))

        with col1:
            st.write("**Premi per salvare la sessione, ti verrà fornito un codice:**")
        with col2:
            if st.button("SALVA SESSIONE BIS"):
                st.code(dflt)
                with open(filename, "r") as fp1:
                    data = json.load(fp1)

                    #tolgo le info sugli screen che non mi interessano
                    for key in list(data.keys()):
                        st.write(key)
                        if key != data["Scelta screen"] and key != "Scelta screen":
                            del data[key]
                            st.write("RIMOSSA")

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
            rec = st.button("RECUPERA SESSIONE BIS")
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
                r.status = data[scelta]
                raise st.script_runner.RerunException(st.script_request_queue.RerunData(None))

            else:
                st.error("Sessione inesistente")

        with st.beta_expander("Vedi elenco sessioni"):
            st.success("Elenco sessioni")
            with open("log.json", "r") as fp:
                for line in fp:
                    st.write(line)

        with open(filename, "r") as fp:
            data = json.load(fp)
            st.write(data)

        if st.button("Pulisci il file di log"):
            os.remove("log.json")

