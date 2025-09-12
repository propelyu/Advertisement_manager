from nicegui import ui

def show_header():
     with ui.element("header").classes(
        "w-full fixed top-0 left-0 z-50 shadow-2xl shadow-orange-50"
    ):
        with ui.row().classes(
            "flex justify-between items-center w-full h-20 px-8"
        ).style("margin:0; padding:0;"):
            
            # Brand / Logo
            with ui.element("div").classes('flex flex-row gap-2 ml-4'):
                ui.html("PROPEL").classes(
        "text-stone font-bold text-3xl text-amber-400 uppercase"
    ).style('font-family: "Story Script", sans-serif')
                # ui.icon("home").classes("text-amber-400 w-10 h-10")



            
            # Navigation links
            with ui.row().classes("flex justify-center items-center space-x-6 mr-4"):
                ui.link("Home", "/home").classes(
                    "text-amber-400 text-lg hover:text-orange-400 transition-colors uppercase no-underline "
                )
                ui.link("Add Event", "/add_event").classes(
                    "text-amber-400 text-lg hover:text-orange-500 transition-colors uppercase no-underline "
                )
                # ui.link("View Event", "/view_event").classes(
                #     "text-amber-400 text-lg hover:text-orange-500 transition-colors uppercase no-underline "
                # )
                ui.link("Edit Event", "/edit_event").classes(
                    "text-amber-400 text-lg hover:text-orange-500 transition-colors uppercase no-underline "
                )
                ui.button("Log Out") \
                    .props("flat") \
                    .classes("bg-yellow-600 hover:bg-yellow-700 text-white font-semibold px-5 py-2 rounded-full shadow-md transition-colors flex items-center justify-center") \
                    .on("click", lambda: ui.navigate.to("/"))
