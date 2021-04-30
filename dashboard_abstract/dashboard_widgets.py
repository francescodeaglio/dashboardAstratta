import streamlit as st
from functools import partial
from dashboard_abstract.__init__ import recoverer
from dashboard_abstract.logger import Logger
from dashboard_abstract.utils import st_functional_columns

class DashboardWidgets():
    """
            Permette di inserire widget nei vari campi. Una spiegazione dettagliata è data nell'esempio su streamlit

            :param location: posizione in cui vengono mostrati i widget, di default al centro (altre possibili st.sidebar, st.beta_expander ecc)
            :param widget_dict: dizionario con chiave nome e valore un partial per creare i widget (optional)
            """
    def __init__(self, location=None, widget_dict=None):

        if location is None:
            location = st
        if widget_dict is None:
            self.widget_dict = {}
        else:
            self.widget_dict = widget_dict

            #questo mi interessa solo se c'è un recoverer

            if recoverer is not None:
                for widget_name in widget_dict:
                    widget_dict[widget_name] = self.stato_iniziale(widget_name, widget_dict[widget_name])
        self.location = location
        self.screen_name = None
        self.chart_name = None

    def show_widgets(self):
        """
        Mostra i widget e ritorna quanto scelto.

        :return: Quanto scelto dell'utente. Viene ritornata una tupla, dove ogni elemento è quanto ritornato su ogni riga. Se una riga presenta più colonne, vengono inseriti in un ulteriore tupla
        Ad esempio, se il layout è: prima riga: selectbox (a), seconda riga: due date_input (b,c), terza riga: del testo allora verrà ritornato (ret(a), (ret(b), ret(c)), None), dove ret(x) è quanto selezionato dal widget x.
        """

        ret = {}
        if self.location != st:
            with self.location:
                for widget_name in self.widget_dict:

                    r = self.widget_dict[widget_name]()
                    ret[widget_name] = r
        else:
            for widget_name in self.widget_dict:
                r = self.widget_dict[widget_name]()
                ret[widget_name] = r

        if len(ret) != 0:
            Logger(ret, self.screen_name, self.chart_name)
        return ret

    def add_widget_multicolumn(self,name, widget_dict, sizes=None):
        """
        Elenco di widget, forniti in un elenco

        :param widget_dict: elenco di partial (chiamata del tipo nome.add_widget_multicolumn(partial(..), partial(..))
        """
        if recoverer is not None:
            for widget_name in widget_dict:
                widget_dict[widget_name] = self.stato_iniziale(widget_name, widget_dict[widget_name])

        self.widget_dict[name] = partial(st_functional_columns, widget_dict, sizes)



    def add_widget_singlecolumn(self, name, widget):
        """
        Aggiunge un widget (su una nuova riga)

        :param widget: oggetto della classe partial
        """
        if recoverer is not None:
            self.widget_dict[name] = self.stato_iniziale(name, widget)
        else:
            self.widget_dict[name] = widget

    def set_location(self, location):
        """
        Possibile cambaire la posizione del widget
        :param location: posizione (st, st.sidebar, st.beta_expander...)
        :return:
        """
        self.location = location


    def set_screen_name(self, name):
        self.screen_name = name

    def set_chart_name(self, name):
        self.chart_name = name

    def stato_iniziale(self, name, widget):

        param = widget.args
        func = widget.func


        if "SelectboxMixin.selectbox" in str(func):
            recoverer.add_indexed(name, param[1])

        return partial(func, *param, recoverer.get_default_value(name))

