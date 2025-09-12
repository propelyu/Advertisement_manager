from nicegui import ui
import requests
from utils.api import base_url

def post_advert(data,files):
    response = requests.post(f"{base_url}/adverts", data=data, files=files) 
    print(response.json())

def show_add_event_page():
    image_content = None
    
    def handle_image_upload(e):
        nonlocal image_content
        image_content = e.content
        
        
    # Page title / header
    with ui.column().classes("items-center mt-10"):
        ui.label("Welcome to Propel Properties").classes(
            "text-5xl font-bold text-blue-700 mb-6 text-center"
        )

    # Card container for the form
    with ui.card().classes(
        "w-full max-w-2xl mx-auto my-10 bg-white shadow-2xl rounded-2xl p-8"
    ):
        ui.label("Post an Advert").classes("text-2xl font-bold text-blue-700 mb-6")

        # Form fields
        title = ui.input("Title").classes("w-full mb-4")

        category = ui.select(
            ["Apartment", "Villa", "Office Space", "Event center", "Others"],
            label="Category"
        ).classes("w-full mb-4")

        description = ui.textarea("Description").classes("w-full mb-6")

        price = ui.input("Price").props("type=number").classes("w-full mb-4")
        
        image = ui.upload(on_upload=handle_image_upload).props("flat bordered").classes("w-full").style("border:2px")

        # Submit button
        ui.button("Post Advert", on_click=lambda:post_advert({
            "title": title.value,"category": category.value, 
            "description":description.value,
            "price":price.value}, 
            files={"image":image_content
            }), color="blue-700").classes(
            "text-white px-6 py-3 rounded-lg w-full font-semibold hover:bg-blue-800 transition"
        )
