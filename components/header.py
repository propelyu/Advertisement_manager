from nicegui import ui, app
from pages.home import show_home_page as home_page


def show_header():
    with ui.header().classes('bg-black text-white p-4 flex justify-between items-center shadow-lg'):
        ui.label("✨ Propel Properties").classes('text-lg font-bold')

        with ui.row().classes('space-x-6'):
            ui.link("Home", "/home").classes('text-white font-boldhover:text-pink-400')
            ui.link("Add Event", "/add_event").classes('hover:text-pink-400')
            ui.link("View Event", "/view_event").classes('hover:text-pink-400')
            ui.link("Edit Event", "/edit_event").classes('hover:text-pink-400')
            ui.link("Log Out", "/").classes('hover:text-pink-400')

