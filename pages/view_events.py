from nicegui import ui, app
from components.header import show_header

ads = [
    {
        "title": "3-Bedroom Apartment",
        "price": "$120,000",
        "location": "Accra",
        "image": "/assets/house-1.jpg",
    },
    {
        "title": "Luxury Villa",
        "price": "$500,000",
        "location": "Kumasi",
        "image": "/assets/house-2.jpg",
    },
    {
        "title": "Office Space",
        "price": "$3,500/month",
        "location": "Tema",
        "image": "/assets/house-3.jpg",
        "title": "Office Space",
        "price": "$1,200/month",
        "location": "Tema",
        "image": "/assets/house-3.jpg",
    },
]


def show_event_page():
    show_header()
    ui.label("🏡 Real Estate Ads").classes("text-2xl font-bold mb-6")
    with ui.grid(columns=3).classes("gap-6"):
        for ad in ads:
            with ui.card().classes("w-80 shadow-lg"):
                ui.image(ad["image"]).classes("rounded-t-lg")
                with ui.card_section():
                    ui.label(ad["title"]).classes("text-lg font-semibold")
                    ui.label(ad["location"]).classes("text-gray-500")
                    ui.label(ad["price"]).classes("text-green-600 font-bold")


ui.run()
