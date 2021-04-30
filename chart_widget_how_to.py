from functools import partial

import numpy as np

from dashboard_abstract.dashboard_chart import DashboardChart
import pandas as pd
import altair as alt
import streamlit as st
from dashboard_abstract.__init__ import r
from dashboard_abstract.dashboard_widgets import DashboardWidgets


class ChartWidget(DashboardChart):

    def __init__(self, title, name, subtitle="", widget_dict = None, screen_name=None):
        super().__init__(name=name, title=title, subtitle=subtitle, widget_dict=widget_dict)
        self.screen_name = screen_name



    def show(self):
        self.show_heading()

        text = "E' possibile aggiungere i widget ad un componente in più modi, sia servendosi della classe DashboardWidgets che senza. Ogni classe di DashboardXYZ ha " \
               "il metodo show_widgets che mostra i widget e ritorna quanto selezionato dai widget, in un formato spiegato sotto."
        st.write("*" + text + "*")
        text = "**Attraverso il parametro widget_dict del costruttore**"
        st.write(text)
        text = "*Uno dei parametri facoltativi del costruttore è la widget list, ovvero una lista di partial contenenti metodi di streamilit. Di default" \
               " i widget vengono mostrati su più linee. Ad esempio, se viene passato nel costruttore*"
        st.write(text)
        st.code('''
wl = [ partial(st.selectbox, "Come è il meteo oggi?", ["soleggiato", "nuvoloso"]), 
        partial(st.date_input, "Quando sei nato?")]
        ''')
        text = "E poi, una volta mostrato, l'output sarà il seguente"
        st.write("*" + text + "*")
        w = DashboardWidgets()
        w.set_screen_name(self.screen_name)
        w.set_chart_name(self.name)

        w.add_widget_singlecolumn("meteo", partial(st.selectbox, "Come è il meteo oggi?", ["soleggiato", "nuvoloso"]))
        w.add_widget_singlecolumn("data_nascita", partial(st.date_input, "Quando sei nato?"))
        a = w.show_widgets()
        text = "Altrimenti è possibile incolonnare i widget usando la funzione st_functional_columns fornita da utils. Ad esempio se voglio un widget " \
               "sulla prima riga e due sulla seconda posso fare"
        st.write("*"+text+"*")
        st.code('''
wl = [ partial(st.selectbox, "Come è il meteo oggi?", ["soleggiato", "nuvoloso"]), 
           partial(st_functional_columns, [partial(st.date_input, "Quando inizi?"), 
                                            partial(st.date_input, "Quando finisci?")
                                            ])
     ]
                ''')
        w1 = DashboardWidgets()
        w1.set_screen_name(self.screen_name)
        w1.set_chart_name(self.name)
        w1.add_widget_singlecolumn("Meteo torino", partial(st.selectbox, "Come è il meteo oggi a Torino?", ["soleggiato", "nuvoloso"] ))

        w1.add_widget_multicolumn("Prima colonna", {"inizio":partial(st.date_input, "Quando inizi?"),
                                            "fine":partial(st.date_input, "Quando finisci?")}
                                                )


        b = w1.show_widgets()
        text = "Il valore di ritorno sarà come segue:"
        st.write("*" + text + "*")
        st.write("Nel caso singola colonna: ")
        st.write(a)
        st.write("Nel caso multipla colonna: ")
        st.write(b)
        text = "Quindi una tupla, contenente in ordine gli elementi riga per riga e, nel caso ci siano più colonne, " \
               "ogni elemento della colonna viene racchiuso in una tupla."
        st.write("*" + text + "*")
        text = "**Attraverso il parametro widget_object del costruttore**"
        st.write(text)
        text = "*Uno dei parametri facoltativi del costruttore è la widget_object, ovvero un oggetto della classe DashboardWidgets. Questa classe ha" \
               " come parametro del costruttore widget_dict e il comportamento è analogo al caso precedente. Altrimenti, si può istanziare un oggetto vuoto e aggiungere" \
               " widget sfruttando i metodi add_widget_singlecolumn (riceve un partial), add_widget_multicolumn (riceve un elenco di partial), " \
               "add_widget_multicolumn_list (riceve una lista di partial) e add_widget_multicolumn_with_sizes (riceve una lista e da la possibilità di settare le dimensioni delle colonne, sotto forma di tupla)." \
               "Per ricreare i widget di prima occorre, nel primo caso  *"
        st.write(text)
        st.code('''
w = DashboardWidgets()
w.add_widget_singlecolumn(partial(st.selectbox, "Come è il meteo oggi?", ["soleggiato", "nuvoloso"]))
w.add_widget_singlecolumn(partial(st.date_input, "Quando sei nato?"))
#e poi passare w al costruttore del DashboardXYZ desiderato
                ''')
        text = "Mentre per ricreare in secondo caso"
        st.write("*" + text + "*")
        st.code('''
w1 = DashboardWidgets()
w1.add_widget_singlecolumn(partial(st.selectbox, "Come è il meteo oggi a Torino?", ["soleggiato", "nuvoloso"]))
w1.add_widget_multicolumn(partial(st.date_input, "Quando inizi?"),
                          partial(st.date_input, "Quando finisci?")
                                  )
                        ''')

        text = "Il valore di ritorno sarà come nel caso precedente."
        st.write("*" + text + "*")
        text = "**Attraverso il metodo set_widgets_object**"
        st.write(text)
        text = "E' possibile aggiungere in un secondo momento i widget (se non eran stati forniti nel costruttore) o modificarli. Per far ciò, si " \
               "può utilizzare il metodo set_widgets_object che riceve come parametro un oggetto della classe DashboardWidgets. Ad esempio,"
        st.write(text)
        st.code('''
f = Dashboard...(...)
w = DashboardWidgets()
w.add_widget_singlecolumn(partial(st.selectbox, "Come è il meteo oggi?", ["soleggiato", "nuvoloso"]))
w.add_widget_singlecolumn(partial(st.date_input, "Quando sei nato?"))

f.set_widgets_object(w)
                        ''')
