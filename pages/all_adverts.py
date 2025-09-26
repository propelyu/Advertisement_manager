from nicegui import ui
from components.header import show_header
import requests
from utils.api import base_url


@ui.page("/all_adverts")
def show_all_adverts_page():
    show_header()
    response = requests.get(f"{base_url}/adverts?limit=0")
    json_data = response.json()
    properties = json_data["data"]
    with ui.row().classes(
        "bg-white rounded-full shadow-md overflow-hidden w-[80%] mt-20"
    ):
        search_input = (
            ui.input(placeholder="Search Properties")
            .props("borderless")
            .classes("flex-1 px-4 py-2 text-gray-700 focus:outline-none")
        )
        with ui.button(
            on_click=lambda: ui.notify(f"Searching: {search_input.value}")
        ).props("flat round").classes("bg-pink-500 text-white p-6 rounded-r-full"):
            ui.icon("search").classes("text-white")

    with ui.element("section").classes("w-full py-16"):
        with ui.element("div").classes("max-w-7xl w-full px-6"):
            with ui.column().classes("items-center"):
                ui.label("What we offer").classes(
                    "text-lg font-semibold text-pink-500 tracking-widest"
                )
                ui.label("EXCLUSIVE OFFER FOR YOU").classes(
                    "text-4xl font-bold mt-2 mb-8 items-center justify-center"
                )
                ui.element("hr").classes(
                    "w-16 border-t-4 border-pink-500 mb-12 mx-auto"
                )

        with ui.element("div").classes(
            "grid grid-cols-1 md:grid-cols-3 gap-8 w-full px-6 md:px-12"
        ):
            for idx, prop in enumerate(properties):
                with ui.card().classes(
                    "h-80 flex flex-col items-center justify-center "
                    "relative cursor-pointer"
                ) as card:
                    # Navigate on click
                    card.on(
                        "click",
                        lambda i=prop["id"]: ui.navigate.to(f"/view_events?id={i}"),
                    )

                    # Category Tag
                    if prop.get("category"):
                        ui.label(prop["category"]).classes(
                            "absolute top-2 right-2 z-10 text-xs bg-orange-100 "
                            "text-orange-700 font-semibold px-2 py-1 rounded-full shadow-sm"
                        )

                    # Property Image
                    with ui.element("div").classes("property-image-wrap w-full"):
                        ui.element("img").classes(
                            "w-full h-40 object-cover rounded-lg"
                        ).props(f'src="{prop["image_url"]}" alt="{prop["title"]}"')

                    # Property Details
                    with ui.element("div").classes("p-2 text-left w-full"):
                        ui.label(prop["title"]).classes("text-xl font-bold")
                        with ui.row().classes("items-center justify-between w-full"):
                            ui.label(f"GHS {prop['price']}").classes(
                                "text-lg text-green-600 font-semibold"
                            )
