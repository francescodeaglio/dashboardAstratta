from dashboard_abstract.dashboard_screen import DashboardScreen


class ScreenWidget(DashboardScreen):
    def __init__(self, title, name, chart_list=None, subtitle="", widget_list=None):
        super().__init__(title, name, chart_list=chart_list, subtitle=subtitle, widget_list=widget_list)


    def show(self):
        self.show_heading()
        self.show_widgets()
        self.show_charts()