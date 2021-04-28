from dashboard_abstract.dashboard_field import DashboardField
import streamlit as st

class DashboardScreen(DashboardField):
    """    Classe intermedia. Ogni Main possiede più Screen, ogni Screen ha più Chart. Di default mostra il titolo, sottotitolo e tutti i grafici

           :param title: titolo
           :param name: nome
           :param chart_list: lista di grafici (DashboardChart)
           :param subtitle: sottotitolo
           :param widget_list: lista di partial per creare i widget (optional)
            :param widget_object: oggetto della classe DashboardWidgets (optional)
           """

    def __init__(self, title, name=None, chart_list=None, subtitle="", widget_list=None, widget_object=None):

        super().__init__(title=title, widget_location=st, name=name, subtitle=subtitle, widget_list=widget_list, widget_object=widget_object)
        if chart_list is None:
            chart_list = []
        self.chart_list = chart_list


    def show(self):
        """
        Mostra intestazione e grafici
        """
        self.show_heading()
        self.show_charts()



    def show_heading(self):
        """
        Mostra l'intestazione

        """
        self.location.markdown("## "+self.title)
        if self.subtitle is not None:
            self.location.write(self.subtitle)


    def show_charts(self):
        """
        Mostra tutti gli oggetti di tipo DashboardChart appartenenti a questo screen.
        Si è scelto di mostrarli tutti, altrimenti si può usare show_single_chart passandone il nome
        :return:
        """
        for chart in self.chart_list:
            chart.show()

    def show_single_chart(self, name):
        """
        Mostra solo uno specifico grafico. La chiave per scegliere il titolo è il nome.
        Il grafico deve essere nella chart_list, altrimenti viene sollevata un'eccezione.

        :param name: Nome del DashboardChart da mostrare.:
        """
        trovato = False
        for chart in self.chart_list:
            if chart.get_name() == name:
                chart.show()
                trovato = True

        if not trovato:
            raise Exception("Il grafico selezionato non esiste. Controlla che il titolo passato sia corretto")




    def add_chart(self, chart):
        """
        Da la possibilità di aggiungere un grafico alla lista

        :param chart: oggetto di tipo DashboardChart
        """
        self.chart_list.append(chart)
        print()



