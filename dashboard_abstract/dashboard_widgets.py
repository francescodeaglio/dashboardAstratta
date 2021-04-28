import streamlit as st
from functools import partial
from dashboard_abstract.utils import st_functional_columns

class DashboardWidgets():
    """
            Permette di inserire widget nei vari campi. Una spiegazione dettagliata è data nell'esempio su streamlit

            :param location: posizione in cui vengono mostrati i widget, di default al centro (altre possibili st.sidebar, st.beta_expander ecc)
            :param widget_list: lista di partial, uno per ogni widget
            """
    def __init__(self, location=None, widget_list=None):

        if location is None:
            location = st
        if widget_list is None:
            self.widget_list = []
        else:
            self.widget_list = widget_list
        self.location = location


    def show_widgets(self):
        """
        Mostra i widget e ritorna quanto scelto.

        :return: Quanto scelto dell'utente. Viene ritornata una tupla, dove ogni elemento è quanto ritornato su ogni riga. Se una riga presenta più colonne, vengono inseriti in un ulteriore tupla
        Ad esempio, se il layout è: prima riga: selectbox (a), seconda riga: due date_input (b,c), terza riga: del testo allora verrà ritornato (ret(a), (ret(b), ret(c)), None), dove ret(x) è quanto selezionato dal widget x.
        """
        ret = []
        if self.location != st:
            with self.location:
                for widget in self.widget_list:
                    r = widget()
                    ret.append(r)
        else:
            for widget in self.widget_list:
                r = widget()
                ret.append(r)

        return tuple(ret)

    def add_widget_multicolumn(self, *widget_list):
        """
        Elenco di widget, forniti in un elenco

        :param widget_list: elenco di partial (chiamata del tipo nome.add_widget_multicolumn(partial(..), partial(..))
        """
        self.widget_list.append(
            partial(st_functional_columns, widget_list)
        )
    def add_widget_multicolumn_list(self, widget_list):
        """
        Elenco di widget, forniti in una lista

        :param widget_list: lista di partial (chiamata del tipo nome.add_widget_multicolumn([partial(..), partial(..)])
        """
        self.widget_list.append(
            partial(st_functional_columns, widget_list)
        )
    def add_widget_multicolumn_with_sizes(self, widget_list, sizes):

        """
        Elenco di widget, forniti in una lista, e relativa dimensione.

        :param widget_list: lista di partial (chiamata del tipo nome.add_widget_multicolumn([partial(..), partial(..)], (0.1, 0.9))
        """
        self.widget_list.append(
            partial(st_functional_columns, widget_list, sizes)
        )
    def add_widget_singlecolumn(self, widget):
        """
        Aggiunge un widget (su una nuova riga)

        :param widget: oggetto della classe partial
        """
        self.widget_list.append(widget)

    def set_location(self, location):
        """
        Possibile cambaire la posizione del widget
        :param location: posizione (st, st.sidebar, st.beta_expander...)
        :return:
        """
        self.location = location
