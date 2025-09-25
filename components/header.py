from nicegui import ui


def show_header():
<<<<<<< HEAD
    with ui.element("header").classes(
        "w-full fixed top-0 left-0 z-50 shadow-2xl shadow-orange-50"
=======
     with ui.element("header").classes(
        "bg-white w-full fixed top-0 left-0 z-50 shadow-2xl shadow-orange-50"
>>>>>>> 9dfc5f9399f6c00823a9441c724be59558b42192
    ):
        with ui.row().classes(
            "flex justify-between items-center w-full h-20 px-8"
        ).style("margin:0; padding:0;"):

            # Brand / Logo
<<<<<<< HEAD
            with ui.element("div").classes("flex flex-row gap-2 ml-4"):
                ui.html("PROPEL").classes(
                    "text-stone font-bold text-3xl text-amber-400 uppercase"
                ).style('font-family: "Story Script", sans-serif')
                # ui.icon("home").classes("text-amber-400 w-10 h-10")
=======
            with ui.element("div").classes('flex flex-row items-center gap-2 ml-4'):
                ui.html("PROPEL").classes(
        "text-stone font-bold text-lg text-black uppercase"
    ).style('font-family: "Story Script", sans-serif')
                
                ui.icon("apartment").classes('text-3xl text-pink-300')
>>>>>>> 9dfc5f9399f6c00823a9441c724be59558b42192

            # Navigation links
<<<<<<< HEAD
            with ui.row().classes("flex justify-center items-center space-x-6 mr-4"):
                ui.link("Home", "/").classes(
                    "text-amber-400 text-lg hover:text-orange-400 transition-colors uppercase no-underline "
                )
                ui.link("Add Event", "/vendor/add_events").classes(
                    "text-amber-400 text-lg hover:text-orange-500 transition-colors uppercase no-underline "
=======
            with ui.row().classes("flex justify-center items-center space-x-4 mr-4"):
                ui.link("Home", "/home").classes(
                    "text-black text-sm transition-colors uppercase no-underline "
                )
                ui.link("create Event", "/add_event").classes(
                    "text-black text-sm hover:text-pink-500 transition-colors uppercase no-underline "
>>>>>>> 9dfc5f9399f6c00823a9441c724be59558b42192
                )
                # ui.link("View Event", "/view_event").classes(
                #     "text-amber-400 text-lg hover:text-orange-500 transition-colors uppercase no-underline "
                # )
<<<<<<< HEAD
                ui.link("Edit Event", "/edit_event").classes(
                    "text-amber-400 text-lg hover:text-orange-500 transition-colors uppercase no-underline "
                )
                ui.button("Log In").props("flat").classes(
                    "bg-black hover:bg-yellow-700 text-white font-semibold px-5 py-2 rounded-full shadow-md transition-colors flex items-center justify-center"
                ).on("click", lambda: ui.navigate.to("/login"))
=======
                # ui.link("edit Event", "/edit_event").classes(
                #     "text-black text-lg hover:text-orange-500 transition-colors uppercase no-underline "
                # )
                ui.button("SIGN IN") \
                    .props("flat") \
                    .classes("bg-pink-400 hover:bg-yellow-700 text-white font-semibold px-5 py-2 rounded-full shadow-md transition-colors flex items-center justify-center") \
                    .on("click", lambda: ui.navigate.to("/"))
                
                
>>>>>>> 9dfc5f9399f6c00823a9441c724be59558b42192
