import numpy as np

from Chart_extended import ChartExtended
from chart_description import ChartDescription
from dashboard_abstract.dashboard_chart import DashboardChart
from dashboard_abstract.dashboard_main import DashboardMain
from dashboard_abstract.dashboard_screen import DashboardScreen
import pandas as pd
import altair as alt
from functools import partial
import streamlit as st

from screen_widget import ScreenWidget

main = DashboardMain(
    title="Questo è il titolo del Main",
    subtitle="Questo il sottotitolo del Main. Titolo e sottotitolo verranno mostrati in tutte le pagine della dashboard."
             " Il Main ha a disposizione più screen, ed è possibile accedervi utilizzando il selectbox nella sidebar."
             " Inoltre, è possibile aggiungere un logo che verrà mostrato anch'esso nella sidebar.",
    logo="http://ciaologo.com/timthumb.php?src=upload/167/266/0_20130106090123_4aab79d75c.png&h=250&w=400&zc=2&b=15"
)

screen1 = DashboardScreen(
    title="Questo è il titolo del primo screen",
    name = "Primo Screen",
    subtitle="Questo invece è il sottotitolo del primo screen. Titolo e sottotitolo variano in base alla pagina scelta. "
             "Ogni Screen ha dei grafici. Vengono mostrati tutti una volta che lo screen è stato selezionato."
)

chart1 = DashboardChart(
    title="Questo è invece un grafico",
    name="Primo",
    subtitle="Questo è il sottotitolo del grafico. Qua sotto viene mostrato un grafico. Essendo tutti diversi i grafici è consigliato "
             "creare una classe concreta che implementi questa classe astratta. In alternativa, è possibile usare il metodo add_chart passando un grafico "
             "wrappato dentro una functools.partial"
)

#esempio di grafico dalla documentazione di altair
x = np.arange(100)
source = pd.DataFrame({
  'x': x,
  'f(x)': np.sin(x / 5)
})

alt_chart = alt.Chart(source).mark_line().encode(
    x='x',
    y='f(x)'
)

chart1.add_chart(partial(st.altair_chart, alt_chart, True))
screen1.add_chart(chart1)

chart2 = ChartExtended(title="Questo è un grafico più avanzato",
                       name="Secondo",
                       subtitle="Facendo l'override si può intervenire sul metodo show e stampare qualsiasi grafico si voglia. Anche qua riporto un esempio "
                                "preso dalla documentazione di Altair")
screen1.add_chart(chart2)
chart3 = DashboardChart("Sono nato Chart ma mi hanno fatto versatile",
                         "",
                         "Le classi che implementano DashboardChart possono essere ben di più di un grafico. "
                         "E' possibile creare report, testi, decrizioni e infitinte altre cose modificando il metodo show. Lo screen sui widget è realizzzato così." )

screen1.add_chart(chart3)

screen2 = ScreenWidget(
    title="Qua si gioca con i widget",
    name = "Widget",
    subtitle="Se sei arrivato qua di sicuro hai già usato un widget, quindi siamo a buon punto. In questo Screen ci sono alcuni hint su come usarli.",
    chart_list = [
        ChartDescription(
            "Ecco un po' di esempi",
            "",
            "Sopra di me ci sono i widget dello Screen, ciò che viene scelto qua influisce su tutti i Chart. Nella sidebar c'è un multiselect,"
            " è di proprietà del Main e ti consente di navigare tra più Screen. Inoltre, ogni Chart può avere i suoi widget. Puoi vedere un esempio sotto di me",
            widget_list = [
                partial(st.slider,"Scegli un numero", 1, 12, 5)
            ]
        ),
        ChartDescription(
            "Partial",
            "",
            "Questa struttura si basa sulla programmazione funzionale. Quando sto scrivendo questa riga di codice, non voglio che mi venga mostrato"
            " in questo punto il grafico ma voglio che venga fatto in uno specifico momento. Pertanto tornano comodi i puntatori a funzioni. Purtroppo, "
            "tutte le funzioni di streamlit richiedono almeno un argomento quindi non possiamo usare semplicemente il puntatore. Per poter creare la funzione, e quindi "
            "il widget dobbiamo usare il metodo partial di functools. ",
            more=True
        )
        ],
    widget_list=[
        partial(st.selectbox,"Qual'è il tuo mese preferito?", ["Gennaio", "Febbraio"])
    ]
)


main.add_screen(screen1)
main.add_screen(screen2)


main.show()