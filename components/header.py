from nicegui import ui, app
from pages.home import show_home_page as home_page


def show_header():
    with ui.row():
        ui.link("Home", "/home")
        ui.link("Add Event", "/add_event")
        ui.link("View Event", "/view_event")
        ui.link("Edit Event", "/edit_event")
        ui.link("Log Out", "/")
