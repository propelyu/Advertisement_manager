from nicegui import ui
from components.sidebar import show_sidebar


@ui.page("/vendor/edit_event")
def show_edit_event_page():
    def submit_form():
        ui.notify(
            f"Advert Updated:\n"
            f"Title: {title.value}\n"
            f"Category: {category.value}\n"
            f"Price: {price.value}\n"
            f"Description: {description.value}\n"
            f"Image: {image.value}"
        )

    with ui.row().classes("w-full"):
        with ui.column().classes("w-[20%]"):
            show_sidebar()
        with ui.column().classes("w-[80%]"):
            with ui.column().classes("items-center mt-10 text-center"):
                # Card container
                with ui.card().classes(
                    "w-full max-w-2xl mx-auto my-10 bg-white shadow-2xl rounded-2xl p-8"
                ):
                    ui.label("Edit an Advert").classes(
                        "text-2xl font-bold text-black mb-6"
                    )

                    # Form Fields
                    title = ui.input("Title").classes("w-full mb-4")

                    category = ui.select(
                        ["Apartment", "Villa", "Office Space", "Event space", "Others"],
                        label="Category",
                    ).classes("w-full mb-4")

                    price = (
                        ui.input("Price").props("type=number").classes("w-full mb-4")
                    )

                    description = ui.textarea("Description").classes("w-full mb-4")

                    image = ui.input("Image  ").classes("w-full mb-6")

                    # Submit Button
                    ui.button(
                        "Update Advert", on_click=submit_form, color="black"
                    ).classes(
                        "bg-black text-white px-6 py-3 rounded-lg w-full font-semibold hover:bg-gray-900 transition"
                    )
