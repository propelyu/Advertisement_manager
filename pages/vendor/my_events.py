from nicegui import ui, app
from components.sidebar import show_sidebar
import requests
from utils.api import base_url


@ui.page("/vendor/my_events")
def show_vendor_events():
    response = requests.get(
        f"{base_url}/adverts/vendor",
        headers={"Authorization": f"Bearer {app.storage.user.get("access_token")}"},
    )
    # print(response.status_code, response.content)
    properties = []
    if response.status_code == 200:
        json_data = response.json()
        properties = json_data["data"]
    elif response.status_code == 401:
        return ui.navigate.to("/login")
    ui.query(".nicegui-row").classes("flex-nowrap")
    with ui.row().classes("w-full"):
        with ui.column().classes("w-[20%]"):
            show_sidebar()
        with ui.column().classes("w-[80%] h-full px-10 py-5 bg-gray-100"):

            with ui.element("div").classes(
                "w-full h-full flex justify-center items-center "
            ):
                with ui.row().classes("flex flex-col  items-center w-full"):
                    ui.label("Your Adverts").classes(
                        "text-2xl font-semibold mb-4 items-center"
                    )
                with ui.grid(rows=3, columns=3).classes("w-full gap-5 items-center"):
                    for idx, prop in enumerate(properties):
                        with ui.card().classes(
                            "h-80 flex flex-col items-center justify-center "
                            "relative cursor-pointer"
                        ) as card:
                            # Navigate on click
                            # card.on(
                            #     "click",
                            #     lambda i=prop["id"]: ui.navigate.to(
                            #         f"/view_events?id={i}"
                            #     ),
                            # )

                            # Category Tag
                            if prop.get("category"):
                                ui.label(prop["category"]).classes(
                                    "absolute top-2 right-2 z-10 text-xs bg-orange-100 "
                                    "text-orange-700 font-semibold px-2 py-1 rounded-full shadow-sm"
                                )

                            # Property Image
                            with ui.element("div").classes(
                                "property-image-wrap w-full"
                            ):
                                ui.element("img").classes(
                                    "w-full h-40 object-cover rounded-lg"
                                ).props(
                                    f'src="{prop["image_url"]}" alt="{prop["title"]}"'
                                )

                            # Property Details
                            with ui.element("div").classes("p-2 text-left w-full"):
                                ui.label(prop["title"]).classes("text-xl font-bold")
                                with ui.row().classes(
                                    "items-center justify-between w-full"
                                ):
                                    ui.label(f"GHS {prop['price']}").classes(
                                        "text-lg text-green-600 font-semibold"
                                    )
                                ui.button(
                                    "Edit",
                                    on_click=lambda p=prop: ui.navigate.to(
                                        f"/vendor/edit_events?id={p['id']}"
                                    ),
                                ).classes("bg-black")

                                ui.button(
                                    "Delete",
                                    on_click=lambda a=prop: ui.notify(
                                        f"Deleted {a['title']}"
                                    ),
                                ).classes("bg-black text-white flex-1 w-1/3")
    ui.button(
        "➕ Post New Advert", on_click=lambda: ui.navigate.to("/vendor/add_events")
    ).classes("w-full max-w-xs mx-auto bg-black text-white mb-8")
