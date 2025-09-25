from nicegui import ui

adverts = [
    {"id": 1, "title": "Modern Apartment", "price": 1200, "category": "Apartment"},
    {"id": 2, "title": "Luxury Villa", "price": 4500, "category": "Villa"},
    {
        "id": 3,
        "title": "Office Space Downtown",
        "price": 2000,
        "category": "Office Space",
    },
    {"id": 4, "title": "Event Center Hall", "price": 1500, "category": "Event Center"},
    {"id": 5, "title": "Cozy Studio", "price": 800, "category": "Apartment"},
]


@ui.page("/all_adverts")
def show_all_adverts_page():
    # show_header()
    with ui.row():
        ui.label("All Adverts").classes("text-2xl font-bold text-center items-center")

        with ui.row().classes("mb-6 rounded-lg justify-end w-4/5 flex items-center"):
            search = (
                ui.input(placeholder="Search adverts...")
                .props("outlined rounded")
                .classes("w-[70%]")
            )

        # Search icon button
        ui.button(icon="search", on_click=lambda: apply_filter()).classes(
            "bg-blue-600 text-white rounded-full p-2 hover:bg-blue-700"
        )
        category_filter = ui.select(
            ["All", "Apartment", "Villa", "Office Space", "Event center", "Others"],
            value="All",
            label="Filter by category",
        ).classes("w-48 rounded-lg")

    # Grid container for adverts
    adverts_container = ui.element("div").classes(
        "grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 mx-auto w-[80%]  items-center"
    )

    # function to filter and show adverts
    def apply_filter():
        adverts_container.clear()
        query = search.value.lower()
        category = category_filter.value

        filtered = [
            a
            for a in adverts
            if (query in a["title"].lower())
            and (category == "All" or a["category"] == category)
        ]

        for advert in filtered:
            with adverts_container:
                with ui.card().classes(
                    "p-4 w-64 h-48 cursor-pointer hover:shadow-lg transition"
                ) as card:
                    ui.label(advert["title"]).classes("font-bold")
                    ui.label(f"GHS {advert['price']}")
                    ui.label(advert["category"]).classes("text-sm text-gray-500")

                    card.on(
                        "click",
                        lambda e, i=advert["id"]: ui.navigate.to(
                            f"/view_events?id={i}"
                        ),
                    )

    # Reaction
    search.on("input", lambda e: apply_filter())
    category_filter.on("change", lambda e: apply_filter())

    apply_filter()
