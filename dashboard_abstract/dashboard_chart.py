from dashboard_abstract.dashboard_field import DashboardField
import streamlit as st


class DashboardChart(DashboardField):

    def __init__(self, title, name, subtitle="", widget_list=None):
        super().__init__(title, location=st, widget_location=st, name=name, subtitle=subtitle, widget_list=widget_list)
        self.chart = None


    def show_heading(self):
        self.location.markdown("### **" + self.title+"**")
        self.location.markdown("*" +self.subtitle+"*")

    def show(self):
        """
        Da implementare, ogni classe astratta mostra i grafici in modo diverso. Lo implemento per esempio
        :return:
        """
        self.show_heading()
        if self.chart is not None:
            self.chart()

    def get_name(self):
        return self.name

    def add_chart(self, chart):
        self.chart = chart