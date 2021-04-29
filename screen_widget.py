from dashboard_abstract.dashboard_screen import DashboardScreen


class ScreenWidget(DashboardScreen):
    def __init__(self, title, name, chart_list=None, subtitle="", widget_dict=None):
        super().__init__(title, name, chart_list=chart_list, subtitle=subtitle, widget_dict=widget_dict)


    def show(self):
        self.show_heading()
        self.show_widgets()
        self.show_charts()