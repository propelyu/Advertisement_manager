from nicegui import ui
from components.sidebar import show_sidebar
import requests
from utils.api import base_url


@ui.page("/vendor/edit_events")
def show_edit_event_page():
    event = {}
    event_id = ui.context.client.request.query_params.get("id")
    response = requests.get(f"{base_url}/adverts/{event_id}")
    print(response.status_code, response.content)
    if response.status_code == 200:
        json_data = response.json()
        event = json_data["data"]

    def submit_form():
        ui.notify(
            f"Advert Updated:\n"
            f"Title: {title.value}\n"
            f"Category: {category.value}\n"
            f"Price: {price.value}\n"
            f"Description: {description.value}\n"
            f"image: {image.value}"
        )

    ui.query(".nicegui-row").classes("flex-nowrap")
    with ui.row().classes("w-full flex flex-row"):
        with ui.column().classes("w-[20%]"):
            show_sidebar()
        with ui.column().classes(
            "w-[80%] flex justify-center items-start p-10 overflow-y-auto"
        ):
            with ui.element("div").classes("w-full h-full flex flex-row "):
                with ui.row().classes("flex flex-col  items-center w-full"):
                    # Card container
                    with ui.card().classes(
                        "w-full max-w-2xl mx-auto my-10 bg-gray shadow-2xl rounded-2xl pl-8"
                    ):
                        ui.label("Edit an Advert").classes(
                            "text-2xl font-bold text-black mb-6"
                        )

                        # Form Fields
                        title = ui.input("Title", value=event["title"]).classes(
                            "w-full mb-4"
                        )

                        category = ui.select(
                            "category",
                            value=["category"],
                            label="Category",
                        ).classes("w-full mb-4")

                        price = (
                            ui.input("Price")
                            .props("type=number")
                            .classes("w-full mb-4")
                        )

                        description = ui.textarea("Description").classes("w-full mb-4")

                        # image = ui.upload("image").classes("w-full mb-6")
                        image = ui.upload(on_upload=lambda e: print(e.name)).classes(
                            "w-full mb-6"
                        )

                        # Submit Button
                        ui.button(
                            "Update Advert", on_click=submit_form, color="black"
                        ).classes(
                            "bg-black text-white px-6 py-3 rounded-lg w-full font-semibold hover:bg-gray-900 transition"
                        )
