from nicegui import ui


def show_header():
    with ui.element("header").classes("bg-white w-full fixed top-0 left-0 z-50 s"):
        with ui.row().classes(
            "flex justify-between items-center w-full h-20 px-8"
        ).style("margin:0; padding:0;"):

            # Brand / Logo
            with ui.element("div").classes("flex flex-row items-center gap-2 ml-4"):
                ui.html("PROPEL").classes(
                    "text-stone font-bold text-lg text-black uppercase"
                ).style('font-family: "Story Script", sans-serif')

                ui.icon("apartment").classes("text-3xl text-pink-300")

            # Navigation links
            with ui.row().classes("flex justify-center items-center space-x-4 mr-4"):
                ui.link("Home", "/").classes(
                    "text-black text-sm transition-colors uppercase no-underline "
                )
                ui.link("create Event", "/vendor/add_events").classes(
                    "text-black text-sm hover:text-pink-500 transition-colors uppercase no-underline "
                )
                # ui.link("View Event", "/view_event").classes(
                #     "text-amber-400 text-lg hover:text-orange-500 transition-colors uppercase no-underline "
                # )
                # ui.link("edit Event", "/edit_event").classes(
                #     "text-black text-lg hover:text-orange-500 transition-colors uppercase no-underline "
                # )
                ui.button("LOGIN").props("flat").classes(
                    "bg-pink-400 hover:bg-yellow-700 text-white font-semibold px-5 py-2 rounded-full shadow-md transition-colors flex items-center justify-center"
                ).on("click", lambda: ui.navigate.to("/login"))
