from dashboard_abstract.dashboard_screen import DashboardScreen
## importing socket module
import socket
import streamlit as st

class ScreenSessione(DashboardScreen):
    def __init__(self, title, name, chart_list=None, subtitle="", widget_list=None):
        super().__init__(title, name, chart_list=chart_list, subtitle=subtitle, widget_list=widget_list)


    def show(self):
        self.show_heading()

        ## getting the hostname by socket.gethostname() method
        hostname = socket.gethostname()
        ## getting the IP address using socket.gethostbyname() method
        ip_address = socket.gethostbyname(hostname)
        ## printing the hostname and ip_address
        st.write(f"Hostname: {hostname}")
        st.write(f"IP Address: {ip_address}")