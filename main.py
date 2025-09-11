from nicegui import ui, app
from pages.view_events import show_view_events_page
from pages.edit_events import show_edit_event_page
from pages.add_events import show_add_event_page
from pages.home import show_home_page
from components.header import show_header


app.add_static_files("/assets", "assets")

ui.add_head_html('''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/all.min.css" integrity="sha512-2SwdPD6INVrV/lHTZbO2nodKhrnDdJK9/kg2XD1r9uGqPo1cUbujc+IYdlYdEErWNu69gVcYgdxlmVmzTWnetw==" crossorigin="anonymous" referrerpolicy="no-referrer" />
''')


@ui.page("/")
def home_page():
    show_header()
    show_home_page()


@ui.page("/home")
def home_page():
    show_header()
    show_home_page()


@ui.page("/add_event")
def add_event_page():
    show_header()
    show_add_event_page()


@ui.page("/edit_event")
def edit_event_page():
    show_header()
    show_edit_event_page()


@ui.page("/view_event")
def view_events_page():
    show_header()
    show_view_events_page()


ui.run()
