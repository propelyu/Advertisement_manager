from nicegui import ui, app
from pages.home import *
from pages.vendor.add_events import *
from pages.vendor.dashboard import *
from pages.vendor.edit_events import *
from pages.vendor.adverts import *
from pages.view_events import *


app.add_static_files("/assets", "assets")


ui.run()
