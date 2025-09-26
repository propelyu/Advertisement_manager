from nicegui import ui, app


def show_sidebar():
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    # ui.label("sidebar goes here")
    with ui.column().classes(
        "w-[20%] h-full bg-gray-200 fixed left-0 z-50 text-white px-10 py-20 space-y-4"
    ):
        ui.link("Total Adverts", "/vendor/dashboard").classes(
            "hover:text-gray-300 no-underline text-black text-lg"
        )
        ui.link("Categories").classes(
            "hover:text-gray-300 no-underline text-black text-lg"
        )
        ui.link("Analytics", "/vendor/my_events").classes(
            "hover:text-gray-300 no-underline text-black text-lg"
        )
        ui.link("My Adverts", "/vendor/my_events").classes(
            "hover:text-gray-300 no-underline text-black text-lg"
        )
        ui.link("Post New Advert", "/vendor/add_events").classes(
            "hover:text-gray-300 no-underline text-black text-lg"
        )
        ui.link("Total Views", "/vendor/dashboard").classes(
            "hover:text-gray-300 no-underline text-black text-lg"
        )
        ui.link("Settings", "/vendor/dashboard").classes(
            "hover:text-gray-300 no-underline text-black text-lg"
        )
        ui.button("Logout", on_click=lambda: ui.navigate.to("/login")).classes(
            "mt-auto w-full bg-black"
        )


# with ui.column().classes('w-4/5 p-6 space-y-6'):
