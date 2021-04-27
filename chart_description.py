import numpy as np

from dashboard_abstract.dashboard_chart import DashboardChart
import pandas as pd
import altair as alt
import streamlit as st

class ChartDescription(DashboardChart):

    def __init__(self, title, name, subtitle="", widget_list = None, more=False):
        self.more = more
        super().__init__(name=name, title=title, subtitle=subtitle, widget_list=widget_list)



    def show(self):
        self.show_heading()
        self.show_widgets()

        if self.more:
            text = "Ad esempio, se si vuole chiamare"
            st.markdown("*"+text+"*")
            st.code('''
            st.selectbox("Dove vivi?", ["Torino", "Roma"])''')
            text = "Bisognerà creare un oggetto del tipo"
            st.markdown("*" + text + "*")
            st.code('''
            from functools import partial
            a=partial(st.selectbox, "Dove vivi?", ["Torino", "Roma"])
            #         ^- nome funzione    ^---------^---- argomenti della funzione''')
            text = "E in un secondo momento sarà possibile fare un'operazione del genere"
            st.markdown("*" + text + "*")
            st.code('''
            citta_scelta = a()''')
            text = "Così facendo verrà creata una selectbox che chiede 'dove vivi?' e il valore di ritorno immagazzinato in citta_scelta"
            st.markdown("*" + text + "*")
