from nicegui import ui, app
from pages.home import*
from pages.add_events import *
from pages.view_events import *
from pages.edit_events import *


app.add_static_files("/assets", "assets")



ui.run()
