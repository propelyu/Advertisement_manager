from nicegui import ui, app
from pages.home import *
from pages.vendor.add_events import *
from pages.vendor.dashboard import *
from pages.vendor.edit_events import *
from pages.vendor.adverts import *
from pages.view_events import *
# from components.footer import show_footer


app.add_static_files("/assets", "assets")


# @ui.page("/")
# def home_page():
#     show_header()
#     show_home_page()
#     # show_footer()

# @ui.page("/view_event")
# def add_view_page(id=""):
#     show_header()
#     # show_footer()

ui.run()
