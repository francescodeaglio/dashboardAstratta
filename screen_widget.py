from dashboard_abstract.dashboard_screen import DashboardScreen
import streamlit as st


class ScreenWidget(DashboardScreen):
    def __init__(self, title, name, chart_list=None, subtitle="", widget_dict=None):
        super().__init__(title, name, chart_list=chart_list, subtitle=subtitle, widget_dict=widget_dict)


    def show(self):
        self.show_heading()
        self.show_widgets()
        self.show_charts()

        if st.button("Rets",key = "VEDIAMO"):
            str = '''{'-1025759994563665727': id: "-1025759994563665727"
            int_value: 0
            ,
            '-1690034288893705868': id: "-1690034288893705868"
            string_array_value
            {
                data: "2021/04/29"
            }
            ,
            '-4817958842516097845': id: "-4817958842516097845"
            int_value: 1
            ,
            '-8205970098210670936': id: "-8205970098210670936"
            string_array_value
            {
                data: "2021/04/29"
            }
            ,
            '-9163863398167826010': id: "-9163863398167826010"
            int_value: 0
            ,
            '218599046741165752': id: "218599046741165752"
            string_array_value
            {
                data: "2021/04/29"
            }
            ,
            '2232552355339700821': id: "2232552355339700821"
            int_value: 0
            ,
            '8269466469198427688': id: "8269466469198427688"
            double_array_value
            {
                data: 5.0
            }
            }'''

            raise st.script_runner.RerunException(st.script_request_queue.RerunData(None, str))