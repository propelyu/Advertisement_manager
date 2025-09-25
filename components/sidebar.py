from nicegui import ui, app


def show_sidebar():
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    # ui.label("sidebar goes here")
    with ui.column().classes(
        "w-[20%] h-full bg-gray-200 fixed left-0 z-50 text-white px-10 py-20 space-y-4"
    ):
        ui.label("Welcome").classes("text-2xl font-bold mb-4")
        ui.link("Overview", "#").classes(
            "hover:text-gray-300 no-underline text-white text-lg"
        )
        ui.link("My Adverts", "/vendor/my_events").classes(
            "hover:text-gray-300 no-underline text-white text-lg"
        )
        ui.link("Post New Advert", "/vendor/add_events").classes(
            "hover:text-gray-300 no-underline text-white text-lg"
        )
        ui.link("Total Adverts").classes(
            "hover:text-gray-300 no-underline text-white text-lg"
        )
        ui.link("Categories").classes(
            "hover:text-gray-300 no-underline text-white text-lg"
        )
        ui.link("Total Views").classes(
            "hover:text-gray-300 no-underline text-white text-lg"
        )
        ui.link("Settings", "#").classes(
            "hover:text-gray-300 no-underline text-white text-lg"
        )
        ui.button(
            "Logout", color="green", on_click=lambda: ui.navigate.to("/login")
        ).classes("mt-auto w-full")


# with ui.column().classes('w-4/5 p-6 space-y-6'):
