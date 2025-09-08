from nicegui import ui, app
from pages.view_events import show_event_page
from pages.edit_events import show_edit_event_page
from pages.add_events import show_add_event_page
from pages.home import show_home_page, show_home_page
from components.header import show_header


@ui.page("/")
def home_page():
    show_header()
    show_home_page()

    ui.label("Welcome to the Main Page")
    ui.button("Go to Home Page", on_click=lambda: app.open("/home"))
    ui.button("Go to Add Event Page", on_click=lambda: app.open("/add_event"))
    ui.button("Go to Edit Event Page", on_click=lambda: app.open("/edit_event"))
    ui.button("Go to View Event Page", on_click=lambda: app.open("/view_event"))


@ui.page("/home")
def home_page():
    from pages.home import show_home_page

    show_home_page()


@ui.page("/add_event")
def add_event_page():
    from pages.add_events import show_add_event_page

    show_add_event_page()


@ui.page("/edit_event")
def edit_event_page():
    from pages.edit_events import show_edit_event_page

    show_edit_event_page()


@ui.page("/view_event")
def view_event_page():
    from pages.view_events import show_event_page

    show_event_page()


ui.run()
