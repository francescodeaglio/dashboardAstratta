import json
import os
import random
import string
from datetime import datetime, date
from dashboard_abstract.utils import get_session_id
from state import provide_state
from functools import partial
import streamlit as st

class DashboardRecoverSession():

    @provide_state
    def __init__(self, state):

        self.state = state
        #serve a fare match indice_valore nelle selectbox
        self.dict_indexed = {}

        #all'inizio è nullo, poi può essere settato
        self.status = {}

    def get_default_value(self, name):

        if get_session_id() not in self.status:
            ret = None
        else:
            ret = self.visita_ricorsiva_dict(
                self.status[get_session_id()],
                name
            )

        #gestione delle date
        if isinstance(ret, str) and "datetime" in ret:
            return date.fromisoformat(ret.split("+")[1])

        #gestione delle selectbox
        if name in self.dict_indexed[get_session_id()]:
            ret = self.get_indexed_value(name, ret)
        return ret


    def get_indexed_value(self, name, value):

        if value is None:
            return 0
        return self.dict_indexed[get_session_id()][name].index(value)

    def add_indexed(self, name, value):
        if get_session_id() not in self.dict_indexed:
            self.dict_indexed[get_session_id()] = {}
        if name not in self.dict_indexed[get_session_id()] or len(self.dict_indexed[get_session_id()][name]) < len(value):
            self.dict_indexed[get_session_id()][name] = value

    def visita_ricorsiva_dict(self, d, name):
        for key in d:
            if isinstance(d[key], dict):
                a = self.visita_ricorsiva_dict(d[key], name)
                if a is not None:
                    return a
            elif name == key:
                return d[key]

    def get_widget(self):
        return partial(self.recover_widget)

    def recover_widget(self):
        with st.sidebar:

                st.write("\n**Gestione sessioni**")
                with st.beta_expander("Salva la sessione corrente"):
                    self.salva_sessione()
                with st.beta_expander("Recupera una sessione altrui"):
                    self.recupera_sessione()


    def salva_sessione(self):
        dflt = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))


        if st.button("SALVA SESSIONE"):
              st.write("Usa il seguente codice per condividere la tua sessione")
              st.code(dflt)
              filename = os.path.join(os.curdir, "json", str(get_session_id()))
              with open(filename, "r") as fp1:
                 data = json.load(fp1)

              #tolgo le info sugli screen che non mi interessano
              for key in list(data.keys()):
                  if key != data["Scelta screen"] and key != "Scelta screen":
                            del data[key]

              if "log.json" in os.listdir(os.curdir):
                        with open("log.json", "r") as fp2:
                            total = json.load(fp2)
                            total[dflt] = data
                        with open("log.json", "w") as fp2:
                            fp2.write(json.dumps(total))
              else:
                        with open("log.json", "w") as fp2:
                            fp2.write(json.dumps({dflt:data}))
              st.success("Sessione salvata correttamente")

    def recupera_sessione(self):
        scelta = st.text_input("Inserisci il codice")

        if st.button("RECUPERA"):
            #controllo che esista
            trovato = False
            with open("log.json", "r") as fp:
                data = json.load(fp)
                if scelta in data:
                    trovato = True
            if trovato:
                self.status[get_session_id()] = data[scelta]
                st.experimental_rerun()

            else:
                st.error("Sessione inesistente")

