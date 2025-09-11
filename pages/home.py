from nicegui import ui


def show_home_page():
    ui.label("Welcome to the Advertisement Manager Home ")
    ui.label("").classes("text-white font-bold")
    with ui.header().classes('bg-white text- p-4 flex   shadow-lg'):
        ui.label("PropelU").classes("text-black font-bold")
        with ui.element("div").style("background-image: url(./assets/house3.jpg)").classes(
        "h-screen w-screen flex flex-col justify-center items-center bg-cover bg-center m-0 p-0"
    ):
         ui.label("Welcome to Propel Properties").classes("text-white text-5xl font-bold")
