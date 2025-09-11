from nicegui import ui
from components.header import show_header


def show_edit_event_page():
    # Page Header
    with ui.column().classes("items-center mt-10 text-center"):
        ui.label("Make your edits below").classes(
            "text-5xl font-bold text-blue-700 mb-6"
        )

    def submit_form():
        ui.notify(
            f"Advert Updated:\n"
            f"Title: {title.value}\n"
            f"Category: {category.value}\n"
            f"Price: {price.value}\n"
            f"Description: {description.value}\n"
            f"Image: {image.value}"
        )

    # Card container
    with ui.card().classes(
        "w-full max-w-2xl mx-auto my-10 bg-white shadow-2xl rounded-2xl p-8"
    ):
        ui.label("Edit an Advert").classes("text-2xl font-bold text-blue-700 mb-6")

        # Form Fields
        title = ui.input("Title").classes("w-full mb-4")

        category = ui.select(
            ["Apartment", "Villa", "Office Space", "Event space", "Others"],
            label="Category"
        ).classes("w-full mb-4")

        price = ui.input("Price").props("type=number").classes("w-full mb-4")

        description = ui.textarea("Description").classes("w-full mb-4")

        image = ui.input("Image  ").classes("w-full mb-6")

        # Submit Button
        ui.button("Update Advert", on_click=submit_form, color="blue-700").classes(
            "text-white px-6 py-3 rounded-lg w-full font-semibold hover:bg-blue-800 transition"
        )
