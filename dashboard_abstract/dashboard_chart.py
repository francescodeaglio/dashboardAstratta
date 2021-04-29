from dashboard_abstract.dashboard_field import DashboardField
import streamlit as st


class DashboardChart(DashboardField):
    """
            Ultimo elemento nella scala gerarchica. Tendenzialmente mostra un grafico, ma può essere usato anche per altro (tipo report testuali).

            :param title: titolo
            :param name: nome dell'oggetto
            :param subtitle: sottotitolo
            :param widget_dict: lista di partial per creare i widget (optional)
            :param widget_object: oggetto della classe DashboardWidgets (optional)
            """

    def __init__(self, title, name=None, subtitle="", widget_dict=None, widget_object=None):

        super().__init__(title, location=st, widget_location=st, name=name, subtitle=subtitle, widget_dict=widget_dict, widget_object=widget_object)
        self.chart = None
        self.widgets.set_chart_name(self.name)


    def show_heading(self):
        """
        Mostra titolo e sottotitolo
        """
        self.location.markdown("### **" + self.title+"**")
        if self.subtitle != "":
            self.location.markdown("*" +self.subtitle+"*")

    def show(self):
        """
        Da implementare, ogni classe mostra i grafici in modo diverso. Per grafici estremamente semplici, si puo passare il partial della
        funzione di visualizzazione (col metodo add_chart) e qua viene mostrato.
        """
        self.show_heading()
        if self.chart is not None:
            self.chart()

    def get_name(self):
        return self.name

    def add_chart(self, chart):
        """
        Aggiunge un grafico.

        :param chart: partial della funzione di visualizzazione. Ad esempio, se ho un grafico di altair chiamato altchart passerò partial(st.altair_chart, altchart)
        """
        self.chart = chart