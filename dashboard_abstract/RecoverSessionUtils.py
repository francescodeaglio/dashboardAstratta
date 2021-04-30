from datetime import datetime, date

from streamlit.report_thread import ReportThread
from streamlit.script_request_queue import RerunData
from streamlit.script_runner import RerunException
from streamlit.server.server import Server
from dashboard_abstract.utils import get_session_id
import streamlit.script_runner
from streamlit.script_request_queue import RerunData

from state import provide_state


class Recover():

    @provide_state
    def __init__(self, state):

        self.id = get_session_id()
        self.state = state
        #serve a fare match indice_valore
        self.dict_indexed = {}

        self.status = None

    def get_default_value(self, name):

        if self.status is None:
            ret = None
        else:

            ret = self.visita_ricorsiva_dict(
                self.status,
                name
            )

        #gestione delle date
        if isinstance(ret, str) and "datetime" in ret:
            return date.fromisoformat(ret.split("+")[1])

        #gestione delle selectbox
        if name in self.dict_indexed:
            ret = self.get_indexed_value(name, ret)


        return ret

    ##inutile
    def get_default_value_wrapped(self,  name):

        if self.status is None:
            if name in self.dict_indexed:
                return  0
            return None

        #se non è nullo nel campo Scelta screen ho lo screen scelto

        #se sto cercando il nome dello screen scelto
        print(name)
        if name in self.status:
            return self.get_indexed_value("Scelta screen", self.status[name])
        else:
            if self.status["Scelta screen"] not in self.status:
                return None
            #altrimenti scendo nello screen scelto
            for chart in self.status[self.status["Scelta screen"]]:

                #chart può essere un dict o una stringa

                if isinstance(self.status[self.status["Scelta screen"]][chart], dict):
                    #se è un dict è di un grafico
                    for widget in self.status[self.status["Scelta screen"]][chart]:

                        #qua il widget può essere una stringa o un dict se su più colonne
                        if isinstance(self.status[self.status["Scelta screen"]][chart][widget], dict):
                            #qua è un dict
                            for widget_col in self.status[self.status["Scelta screen"]][chart][widget]:

                                if widget_col == name:
                                    if name in self.dict_indexed:
                                        return self.get_indexed_value(name,
                                                                      self.status[self.status["Scelta screen"]][chart][widget][
                                                                          name])

                                    return self.status[self.status["Scelta screen"]][chart][widget][name]

                        #questo è un widget del chart
                        if widget == name:
                            if name in self.dict_indexed:
                                return self.get_indexed_value(name, self.status[self.status["Scelta screen"]][chart][name])
                            return self.status[self.status["Scelta screen"]][chart][name]
                elif chart == name:
                    #qua è un widget dello screen
                    if name in self.dict_indexed:
                        return self.get_indexed_value(name, self.status[self.status["Scelta screen"]][chart])
                    return self.status[self.status["Scelta screen"]][chart]





    def get_indexed_value(self, name, value):

        if value is None:
            return 0
        return self.dict_indexed[name].index(value)

    def add_indexed(self, name, value):
        if name not in self.dict_indexed or len(self.dict_indexed[name]) < len(value):
            self.dict_indexed[name] = value


    def visita_ricorsiva_dict(self, d, name):
        for key in d:
            if isinstance(d[key], dict):
                a = self.visita_ricorsiva_dict(d[key], name)
                if a is not None:
                    return a
            elif name == key:
                return d[key]
