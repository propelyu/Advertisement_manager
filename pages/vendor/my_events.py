from nicegui import ui
from components.sidebar import show_sidebar

adverts = [
    {"id": 1, "title": "Modern Apartment", "price": 1200, "category": "Apartment"},
    {"id": 2, "title": "Luxury Villa", "price": 4500, "category": "Villa"},
    {
        "id": 3,
        "title": "Office Space Downtown",
        "price": 2000,
        "category": "Office Space",
    },
    {"id": 4, "title": "Event Center Hall", "price": 1500, "category": "Event Center"},
    {"id": 5, "title": "Cozy Studio", "price": 800, "category": "Apartment"},
]


@ui.page("/vendor/my_events")
def show_vendor_events():
    ui.query(".nicegui-row").classes("flex-nowrap")
    with ui.row().classes("w-full"):
        with ui.column().classes("w-[20%]"):
            show_sidebar()
        with ui.column().classes("w-[80%] h-full px-10 py-5"):
            # ui.label("dashboard content goes here")
            with ui.element("div").classes(
                "w-full h-full flex justify-center items-center"
            ):
                with ui.row().classes("flex flex-col  items-center w-full"):
                    ui.label("Your Adverts").classes(
                        "text-2xl font-semibold mb-4 items-center"
                    )
                with ui.grid(rows=3, columns=3).classes(
                    "cursor-pointer w-full gap-5 items-center"
                ):
                    for advert in adverts:
                        with ui.card().classes(
                            "mx-auto w-[80%] h-80  flex flex-col justify-center bg-gray-100 items-center shadow-lg"
                        ):
                            ui.label(advert["title"]).classes("text-lg font-bold")
                            ui.label(f'GHS {advert["price"]}').classes(
                                "text-green-600 font-semibold"
                            )
                            ui.label(f'Category: {advert["category"]}').classes(
                                "text-sm text-gray-500"
                            )

                            with ui.row().classes(
                                " mt-4 flex flex-row w-full justify-between items-center"
                            ):
                                ui.button(
                                    "✏️",
                                    on_click=lambda a=advert: ui.navigate.to(
                                        f'/edit_event?id={a["id"]}'
                                    ),
                                ).classes(
                                    "bg-yellow-500 text-white pink-500 flex-1 w-1/3"
                                )

                                ui.button(
                                    "🗑️",
                                    on_click=lambda a=advert: ui.notify(
                                        f"Deleted {a['title']}"
                                    ),
                                ).classes("bg-red-600 pink-500 text-white flex-1 w-1/3")
    ui.button(
        "➕ Post New Advert", on_click=lambda: ui.navigate.to("/vendor/add_events")
    ).classes("w-full max-w-xs mx-auto bg-black text-white mb-8")
