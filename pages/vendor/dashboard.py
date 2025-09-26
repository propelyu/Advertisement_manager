from nicegui import ui
from components.sidebar import show_sidebar

adverts = []


@ui.page("/vendor/dashboard")
def show_vendor_dashboard():
    ui.query(".nicegui-row").classes("flex-nowrap")
    with ui.row().classes(
        "w-full h-screen flex flex-row bg-gray justify-between items-center"
    ):
        with ui.column().classes("w-[20%] h-full"):
            show_sidebar()
        with ui.column().classes("w-[80%] h-full px-10 py-20 mt-20"):
            ui.label("Welcome, Vendor").classes("text-2xlfont-bold mb-4")
            with ui.element("div").classes(
                "w-full h-full flex justify-center items-center"
            ):
                with ui.row().classes("w-full h-full gap-6"):
                    with ui.card().classes("w-1/3 p-4 bg-gray"):
                        ui.label("Total Adverts").classes("text-lg text-gray-600")
                        ui.label("12").classes("text-3xl font-bold")
                    with ui.card().classes("w-1/3 p-4 bg-gray"):
                        ui.label("Categories").classes("text-lg text-gray-600")
                        ui.label("3").classes("text-3xl font-bold")
                    with ui.card().classes("w-1/3 p-4 bg-gray"):
                        ui.label("Total Views").classes("text-lg text-gray-600")
                        ui.label("2,340").classes("text-3xl font-bold")
            ui.label("Analytics").classes("text-2xl font-bold text-gray-800")
            with ui.card().classes("w-full h-96 p-4"):
                ui.echart(
                    {
                        "title": {"text": "Adverts by Category", "left": "center"},
                        "tooltip": {"trigger": "item"},
                        "legend": {"orient": "vertical", "left": "left"},
                        "series": [
                            {
                                "name": "Adverts",
                                "type": "pie",
                                "radius": "50%",
                                "center": ["40%", "50%"],
                                "data": [
                                    {"value": 6, "name": "office"},
                                    {"value": 4, "name": "Villa"},
                                    {"value": 2, "name": "Apartments"},
                                ],
                                "emphasis": {
                                    "itemStyle": {
                                        "shadowBlur": 10,
                                        "shadowOffsetX": 0,
                                        "shadowColor": {"color": "#e00a8e52"},
                                    }
                                },
                            }
                        ],
                    }
                ).style("width:100%; height:100%;")

            with ui.card().classes("w-full h-96 p-4"):
                ui.echart(
                    {
                        "title": {"text": "Views per Advert", "left": "center"},
                        "tooltip": {"trigger": "axis"},
                        "xAxis": {
                            "type": "category",
                            "data": ["Advert 1", "Advert 2", "Advert 3"],
                        },
                        "yAxis": {"type": "value"},
                        "series": [
                            {
                                "data": [250, 300, 50],
                                "type": "bar",
                                "barWidth": "50%",
                                "itemStyle": {"color": "#e00a8e52"},
                            }
                        ],
                    }
                ).style("width:100%; height:100%;")
                with ui.grid(rows=3, columns=3).classes(
                    "cursor-pointer w-full gap-5 items-center"
                ):
                    for advert in adverts:
                        with ui.card().classes(
                            "mx-auto w-[80%] h-80  flex flex-col justify-center bg-gray-100 items-center shadow-lg"
                        ):
                            ui.label(advert["title"]).classes("text-lg font-bold")
                            ui.label(f'GHS {advert["price"]}').classes(
                                "text-black font-semibold"
                            )
                            ui.label(f'Category: {advert["category"]}').classes(
                                "text-sm text-gray-500"
                            )

                            with ui.row().classes(
                                " mt-4 flex flex-row w-full justify-between items-center"
                            ):
                                ui.button(
                                    "✏️",
                                    on_click=lambda a=advert: ui.navigate.to(
                                        f'/edit_event?id={a["id"]}'
                                    ),
                                ).classes("bg-black text-white flex-1 w-1/3")

                                ui.button(
                                    "🗑️",
                                    on_click=lambda a=advert: ui.notify(
                                        f"Deleted {a['title']}"
                                    ),
                                ).classes("bg-black text-white flex-1 w-1/3")
                    # with ui.row().classes(" bg-black items-center "):
                    # ui.button(
                    "View All ",
                    on_click = (lambda: ui.navigate.to("/add_events"),)
            # ).classes("w-4/4 bg-black text-white ")
