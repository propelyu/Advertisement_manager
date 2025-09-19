from nicegui import ui
from components.header import show_header
import requests
from utils.api import base_url


@ui.page("/")
def show_home_page():
    ui.query('.nicegui-content').classes('m-0 p-0')
    show_header()

properties = []



@ui.page('/')
def show_home_page():
    show_header
    response = requests.get(f"{base_url}/adverts")
    json_data = response.json()
    properties = json_data["data"]
    
    

    # Hero
    with ui.element('section') \
        .style("background-image: url('/assets/estate.jpg');") \
        .classes('h-screen w-screen flex flex-col justify-center items-center bg-cover bg-center'):
        ui.label('WELCOME TO PROPEL PROPERTIES') \
          .classes('text-4xl font-bold text-white mb-4') \
          .style('color: gold; text-shadow: 0 0 10px #FFD700, 0 0 20px #FFA500, 0 0 30px #FF8C00;')
        ui.label('Find your dream property today') \
          .classes('text-lg text-white mb-2') \
          .style('color: gold; text-shadow: 0 0 5px #FFD700, 0 0 10px #FFA500;')
        
    # Listing
   
    ui.label('Featured Properties').classes('text-2xl font-bold mb-8 text-center')
    with ui.element('div').classes("grid grid-cols-1 md:grid-cols-3 cursor-pointer gap-8  mx-auto w-[80%] "):
                for idx, prop in enumerate(properties):
                    with ui.card().classes(' h-80 flex flex-col items-center justify-center'
                    ) as card:
                        card.on('click', lambda i=prop["id"]: ui.navigate.to(f'/view_event?id={i}'))

                        if prop.get('category'):
                            ui.label(prop['category']).classes(
                                'absolute top-2 right-2 z-10 text-xs bg-orange-100 text-orange-700 '
                                'font-semibold px-2 py-1 rounded-full shadow-sm'
                            )

                        with ui.element('div').classes('property-image-wrap'):
                            ui.element('img').classes('w-full h-40 object-cover rounded-lg').props(
                                f'src="{prop["image_url"]}" alt="{prop["title"]}"'
                            )

                        with ui.element('div').classes('p- text-left'):
                            ui.label(prop['title']).classes('text-xl font-bold text-left')
                            with ui.row().classes('items-center justify-between w-full'):
                                ui.label(f"GHS {prop['price']}").classes('text-lg text-green-600 font-semibold text-left')
