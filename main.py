from nicegui import ui, app
from pages.home import *
from pages.vendor.add_events import *
from pages.vendor.dashboard import *
from pages.vendor.edit_events import *
from pages.vendor.my_events import *
from pages.view_events import *
from pages.signup import *
from pages.login import *
from pages.all_adverts import *


app.add_static_files("/assets", "assets")


ui.run(storage_secret=("iamelikemiamelikem"))
