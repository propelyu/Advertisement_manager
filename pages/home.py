from nicegui import ui


def show_home_page():
    ui.label("Welcome to the Advertisement Manager Home Page")
    with ui.element("div").style("background-image: url(./assets/hero.jpg)").classes(
        "h-screen w-screen flex flex-col justify-center items-center bg-cover bg-center"
    ):
        ui.button("Create ads")
