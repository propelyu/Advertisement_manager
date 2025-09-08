from nicegui import ui
from components.header import show_header


def show_event_page():
    show_header()
    ui.label("Welcome to the Event Page")
