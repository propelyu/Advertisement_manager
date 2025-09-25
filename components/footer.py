from nicegui import ui

# Load Font Awesome for icons
ui.add_head_html(
    """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
"""
)

with ui.footer().classes("bg-white border-t border-gray-200 p-12"):
    with ui.row().classes("w-full justify-between flex-wrap gap-12"):

        # Uptown column
        with ui.column().classes("w-1/5 min-w-[200px] space-y-4"):
            ui.label("Uptown").classes("text-xl font-bold")
            ui.label(
                "Far far away, behind the word mountains, far from the countries."
            ).classes("text-gray-600 text-sm")
            with ui.row().classes("gap-6 mt-4"):
                ui.link("", "#").classes("fab fa-twitter text-pink-500 text-2xl")
                ui.link("", "#").classes("fab fa-facebook-f text-pink-500 text-2xl")
                ui.link("", "#").classes("fab fa-instagram text-pink-500 text-2xl")

        # Community column
        with ui.column().classes("w-1/5 min-w-[200px] space-y-2"):
            ui.label("Community").classes("text-xl font-bold mb-2")
            for item in ["Search Properties", "For Agents", "Reviews", "FAQs"]:
                ui.link(f"→ {item}", "#").classes("text-gray-700 hover:text-pink-500")

        # About Us column
        with ui.column().classes("w-1/5 min-w-[200px] space-y-2"):
            ui.label("About Us").classes("text-xl font-bold mb-2")
            for item in ["Our Story", "Meet the team", "Careers"]:
                ui.link(f"→ {item}", "#").classes("text-gray-700 hover:text-pink-500")

        # Company column
        with ui.column().classes("w-1/5 min-w-[200px] space-y-2"):
            ui.label("Company").classes("text-xl font-bold mb-2")
            for item in ["About Us", "Press", "Contact", "Careers"]:
                ui.link(f"→ {item}", "#").classes("text-gray-700 hover:text-pink-500")

        # Contact column
        with ui.column().classes("w-1/5 min-w-[200px] space-y-4"):
            ui.label("Have a Questions?").classes("text-xl font-bold mb-2")
            with ui.row().classes("items-start gap-3"):
                ui.icon("map-marker-alt").classes(
                    "fa-solid fa-location-dot text-pink-500 mt-1"
                )
                ui.label(
                    "203 Fake St. Mountain View, San Francisco, California, USA"
                ).classes("text-gray-600 text-sm")
            with ui.row().classes("items-center gap-3"):
                ui.icon("phone").classes("fa-solid fa-phone text-pink-500")
                ui.label("+2 392 3929 210").classes("text-pink-500 text-sm")
            with ui.row().classes("items-center gap-3"):
                ui.icon("envelope").classes("fa-solid fa-envelope text-pink-500")
                ui.label("info@yourdomain.com").classes("text-pink-500 text-sm")
