import numpy as np

from dashboard_abstract.dashboard_chart import DashboardChart
import pandas as pd
import altair as alt
import streamlit as st

class ChartExtended(DashboardChart):

    def __init__(self, title, name, subtitle=""):

        super().__init__(name=name, title=title, subtitle=subtitle)



    def show(self):
        self.show_heading()

        x, y = np.meshgrid(range(-5, 5), range(-5, 5))
        z = x ** 2 + y ** 2

        # Convert this grid to columnar data expected by Altair
        source = pd.DataFrame({'x': x.ravel(),
                               'y': y.ravel(),
                               'z': z.ravel()})

        chart = alt.Chart(source).mark_rect().encode(
            x='x:O',
            y='y:O',
            color='z:Q'
        )

        st.altair_chart(chart, use_container_width=True)

        st.markdown("*Ad esempio è possibile aggiungere anche del testo dopo i grafici, oppure del codice. E' consigliato mantentere"
                    " la seguente struttura nel metodo show*")

        st.code(
                '''
                #visualizzazione di titoli e sottotitolo
                self.show_heading()
                #creazione del grafico
                chart = ...
                #stampa del grafico con i metodi di streamlit. Ad esempio
                st.altair_chart(chart, use_container_width=True)''')

        st.info(
            "E' possibile vedere una dashboard strutturata che usa questo formato al seguente link:"
            " https://share.streamlit.io/alecioc/covid-19/dashboard_script.py"
        )





