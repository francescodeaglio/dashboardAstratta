from dashboard_abstract.dashboard_field import DashboardField
import streamlit as st

class DashboardScreen(DashboardField):

    def __init__(self, title, name, chart_list=None, subtitle="", widget_list=None):
        super().__init__(title=title, widget_location=st, name=name, subtitle=subtitle, widget_list=widget_list)
        if chart_list is None:
            chart_list = []
        self.chart_list = chart_list


    def show(self):
        self.show_heading()
        self.show_charts()



    def show_heading(self):
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
        Il grafico deve essere nella chart_list.
        :param name: Nome del DashboardChart da mostrare.
        :return:
        """
        trovato = False
        for chart in self.chart_list:
            if chart.get_name() == name:
                chart.show()
                trovato = True

        if not trovato:
            st.exception("Il grafico selezionato non esiste. Controlla che il titolo passato sia corretto")




    def add_chart(self, chart):
        """
        Da la possibilità di aggiungere un grafico alla lista
        :param chart: oggetto di tipo DashboardChart
        :return:
        """
        self.chart_list.append(chart)
        print()



