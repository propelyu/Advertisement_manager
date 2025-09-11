from nicegui import ui, app
from components.header import show_header


ads = [
    {
        "cover": "assets/pool-house.jpg",
        "price": "$500,000",
        "description": "Modern Villa located at Airport residential.",
        " category": "Villa",
    },
    {
        "cover": "assets/house-1.jpg",
        "price": "$300,000",
        "description": " Simple Villa with garden and garage at Tema.",
        " category": "Villa",
    },
    {
        "cover": "assets/house-2.jpg",
        "price": "$450,000",
        "description": "Luxury villa with swimming pool and sea view at Kokrobite.",
        " category": "Villa",
    },
    {
        "cover": "assets/real-estate.jpg",
        "price": "$500,000",
        "description": "Modern 4-bedroom apartments at Sogakope.",
        " category": "Apartments",
    },
    {
        "cover": "assets/house.jpg",
        "price": "$1,000,000",
        "description": " Elite Villa (5-bedroom)located at Aburi.",
        " category": "Villa",
    },
    {
        "cover": "assets/new-home.jpg",
        "price": "$120,000",
        "description": "Classic Vila (3-bedrooms) apartment at Akosombo.",
        " category": "Homes",
    },
    {
        "cover": "assets/home.jpg",
        "price": "$120,000",
        "description": "Vicky's Villa (2-bedrooms) in the Santasi.",
        " category": "Homes",
    },
    {
        "cover": "assets/lux-estate.jpg",
        "price": "$500,000",
        "description": "Modern Villa (4-bedrooms) at Tse Addo.",
        " category": "Homes",
    },
    {
        "cover": "assets/chairs.jpg",
        "price": "$30,000",
        "description": "office space at Dzorwulu.",
        "Category": "Office",
    },
    {
        "cover": "assets/office.jpg",
        "price": "$30,000",
        "description": "office space at East legon.",
        "Category": "Office",
    },
    {
        "cover": "assets/office-1.jpg",
        "price": "$25,000",
        "description": "office space at Shiashie.",
        "Category": "Office",
    },
    {
        "cover": "assets/chairs-1.jpg",
        "price": "$120,000",
        "description": "office space at Labone.",
        "Category": "Office",
    },
    {
        "cover": "assets/events.jpg",
        "price": "$120,000",
        "description": "Claud's Events.",
        "Category": "Events Center",
    },
    {
        "cover": "assets/events-1.jpg",
        "price": "$120,000",
        "description": "VicTash Events.",
        "Category": "Events Center",
    },
    {
        "cover": "assets/events-2.jpg",
        "price": "$120,000",
        "description": "P-Kay Events.",
        "Category": "Events Center",
    },
]


@ui.page("/")
def show_event_page():
    # full-page wrapper with background
    with ui.element("div").classes(
        "min-h-screen w-full bg-gray-100 flex flex-col items-center p-10"
    ):
        ui.label("Property Listings").classes(
            "text-7xl font-bold mb-6 text-center text-gray-800"
        )

        # grid for cards
        with ui.element("div").classes(
            "grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8 w-full max-w-7xl"
        ):
            for ad in ads:
                # card
                with ui.card().classes("bg-white p-6 rounded-2xl shadow-lg"):
                    # Cover
                    with ui.element("div").classes("w-full flex justify-center"):
                        with ui.element("div").classes(
                            "w-[500px] rounded-2xl overflow-hidden"
                        ):
                            ui.image(ad["cover"]).classes(
                                "w-full h-[300px] object-cover transition-transform duration-300 hover:scale-105"
                            )

                    # price and description
                    with ui.element("div").classes("text-center mt-4"):
                        ui.label(ad["price"]).classes(
                            "text-xl font-bold text-green-600"
                        )
                        ui.label(ad["description"]).classes("text-gray-600 text-sm")

                    # purely visual buttons
                    with ui.row().classes("gap-4 justify-center mt-4 "):
                        ui.button("Edit").classes("text-white px-4 py-2 rounded-lg")
                        ui.button("Delete").classes(
                            " text-white px-4 py-2 rounded-lg bg-[green]"
                        )


ui.run()
