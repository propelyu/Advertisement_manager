from nicegui import ui, run, app
from components.sidebar import show_sidebar
import requests
from utils.api import base_url

_create_event_btn: ui.button = None


def _run_create_event(data, files, token):
    return requests.post(
        f"{base_url}/adverts",
        data=data,
        files=files,
        headers={"Authorization": f"Bearer {token}"},
    )


async def _create_event(data, files):
    _create_event_btn.props(add="disable loading")
    response = await run.cpu_bound(
        _run_create_event, data, files, app.storage.user.get("access_token")
    )
    print(response.status_code, response.content)
    _create_event_btn.props(remove="disable loading")
    if response.status_code == 403:
        ui.navigate.to("/login")
    elif response.status_code == 200:
        ui.navigate.to("/vendor/my_event")


@ui.page("/vendor/add_events")
def show_add_event_page():
    ui.query(".nicegui-row").classes("flex-nowrap")
    global _create_event_btn
    image_content = None

    def handle_image_upload(e):
        nonlocal image_content
        image_content = e.content

    with ui.row().classes("w-full flex flex-row"):
        with ui.column().classes("w-[20%]"):
            show_sidebar()
        with ui.column().classes(
            "w-[80%] flex justify-center items-start p-10 overflow-y-auto"
        ):
            with ui.element("div").classes("w-full h-full flex flex-row "):
                with ui.row().classes("flex flex-col  items-center w-full"):

                    # Card container for the form
                    with ui.card().classes(
                        "w-full max-w-2xl mx-auto my-10 bg-gray shadow-2xl rounded-2xl pl-8"
                    ):
                        ui.label("Post an Advert").classes(
                            "text-2xl font-bold text-black-700 mb-6"
                        )

                        # Form fields
                        title = (
                            ui.select(
                                [
                                    "Apartment",
                                    "Villa",
                                    "Office Space",
                                    "Event center",
                                    "Others",
                                ],
                                label="Title",
                            )
                            .classes("w-full ")
                            .props("outlined")
                        )

                        category = (
                            ui.select(
                                [
                                    "High demand (A)",
                                    "Medium demand (B)",
                                    "Low demand (C)",
                                ],
                                label="Category",
                            )
                            .props("outlined")
                            .classes("w-full")
                        )
                        description = ui.textarea("Description").classes("w-full")

                        price = ui.input("GH¢ ").props("type=number").classes("w-full")
                        location = ui.textarea("location").classes("w-full")

                        image = (
                            ui.upload(on_upload=handle_image_upload)
                            .props("flat bordered ")
                            .classes("w-full ")
                            .style("border:2px")
                        )

                        # Submit button
                        _create_event_btn = ui.button(
                            "Post Advert",
                            on_click=lambda: _create_event(
                                {
                                    "title": title.value,
                                    "category": category.value,
                                    "description": description.value,
                                    "price": price.value,
                                    "location": location.value,
                                },
                                files={"image": image_content},
                            ),
                            color="black",
                        ).classes(
                            "text-white px-6 py-3 rounded-lg w-full font-semibold hover:bg-blue-800 transition"
                        )
