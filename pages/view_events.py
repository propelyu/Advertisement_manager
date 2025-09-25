from nicegui import ui
from components.header import show_header
import requests
from utils.api import base_url


@ui.page("/view_events")
def show_view_events_page():
    show_header()


# Delete function
def delete_property(id: str):
    try:
        response = requests.get(f"{base_url}/adverts/{id}")
        if response.status_code == 200:
            ui.notify("Advert deleted!", color="red")
            ui.navigate.to("/home")  # reload the listing page
    except IndexError:
        ui.notify("Error: Property not found", color="orange")


# Property Listing Page
def show_view_events_page():
    q = ui.context.client.request.query_params
    prop_id = q.get("id")

    response = requests.get(f"{base_url}/adverts/{prop_id}")
    json_data = response.json()
    # print(json_data)
    prop = json_data["data"]

    with ui.element("section").classes("w-full py-16 bg-gray-50"):
        with ui.element("div").classes("mx-auto max-w-6xl w-full px-6"):
            with ui.column().classes("w-full space-y-16"):
                with ui.element("div").classes(
                    "grid grid-cols-1 md:grid-cols-2 gap-12 items-center"
                ):
                    # Left: Bigger Image
                    ui.image(prop["image_url"]).classes(
                        "w-[500px] h-[500px] object-cover rounded-2xl shadow-xl"
                    )

                    # Right: Centered Info
                    with ui.element("div").classes(
                        "flex flex-col justify-center items-start gap-4"
                    ):
                        ui.label(prop["title"]).classes(
                            "text-3xl font-bold text-gray-800"
                        )
                        # ui.label(prop['location']).classes('text-lg text-gray-600')
                        ui.label(f"GHS {prop['price']}").classes(
                            "text-2xl text-green-600 font-semibold"
                        )

                        # Action Buttons
                        with ui.row().classes("gap-4 mt-4"):
                            ui.button("Edit").classes(
                                "bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
                            )
                            ui.button(
                                "Delete", on_click=lambda: delete_property(prop["id"])
                            ).classes(
                                "bg-red-600 text-white px-4 py-2 rounded-lg hover:bg-red-700"
                            )
