import streamlit as st
from functools import partial
from dashboard_abstract.utils import st_functional_columns

class DashboardWidgets():

    def __init__(self, location=st, widget_list=None):
        if widget_list is None:
            self.widget_list = []
        else:
            self.widget_list = widget_list
        self.location = location


    def show_widgets(self):
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

    def add_widget_multicolumn(self, widget_list):
        """
        Elenco di widget, forniti in una lista
        :param widget_list: lista di partial
        :return:
        """
        self.widget_list.append(
            partial(st_functional_columns, widget_list)
        )

    def add_widget_singlecolumn(self, widget):
        """
        :param widget: oggetto della classe partial
        :return:
        """
        self.widget_list.append(widget)

    def set_location(self, location):
        self.location = location