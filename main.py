from nicegui import ui, app
from pages.home import *
from pages.vendor.add_events import *
from pages.vendor.dashboard import *
from pages.vendor.edit_events import *
from pages.vendor.my_events import *
from pages.view_events import *
<<<<<<< HEAD
from pages.signup import *
from pages.login import *
from pages.all_adverts import *
=======
# from components.footer import show_footer
>>>>>>> 9dfc5f9399f6c00823a9441c724be59558b42192


app.add_static_files("/assets", "assets")


<<<<<<< HEAD
ui.run(storage_secret=("iamelikemiamelikem"))
=======
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
>>>>>>> 9dfc5f9399f6c00823a9441c724be59558b42192
