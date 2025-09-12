from nicegui import ui
import requests
from utils.api import base_url

# Sample property data
properties = []

# Hover zoom effect and card polish (HOVER SECTION)
ui.add_head_html('''
<style>
/* Card hover animation */
.property-card {
    border-radius: 16px;
    overflow: hidden;
    background: #fff;
    transition: box-shadow .25s ease, transform .25s ease;
}
.property-card:hover {
    box-shadow: 0 12px 28px rgba(0,0,0,.16);
    transform: translateY(-2px);
    cursor: pointer;
}
/* Image zoom hover effect */
.property-image-wrap { position: relative; height: 16rem; overflow: hidden; }
.property-image {
    width: 100%; height: 100%;
    object-fit: cover; display: block;
    transform: scale(1.0);
    transition: transform .5s ease;
}
.property-card:hover .property-image { transform: scale(1.06); }
</style>
''')

@ui.page('/')
def show_home_page():
    response = requests.get(f"{base_url}/adverts")
    json_data = response.json()
    properties = json_data["data"]
    
    ui.query('.nicegui-content').classes('m-0 p-0')

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
    with ui.element('section').classes('w-full py-16'):
        with ui.element('div').classes('mx-auto max-w-7xl w-full px-6 '):
            ui.label('Featured Properties').classes('text-2xl font-bold mb-8 text-center')

            with ui.row().classes('w-full justify-center gap-8 flex-wrap'):
                for idx, prop in enumerate(properties):
                    with ui.element('div').classes(
                        'property-card w-96 shadow-xl transition-shadow duration-300 relative hover:scale-105 rounded-2xl'
                    ).props('role=link tabindex=0 aria-label="View property"') as card:
                        card.on('click', lambda i=prop["id"]: ui.navigate.to(f'/view_event?id={i}'))

                        if prop.get('category'):
                            ui.label(prop['category']).classes(
                                'absolute top-2 right-2 z-10 text-xs bg-orange-100 text-orange-700 '
                                'font-semibold px-2 py-1 rounded-full shadow-sm'
                            )

                        with ui.element('div').classes('property-image-wrap'):
                            ui.element('img').classes('property-image').props(
                                f'src="{prop["image_url"]}" alt="{prop["title"]}"'
                            )

                        with ui.element('div').classes('p-4 text-left'):
                            ui.label(prop['title']).classes('text-xl font-bold text-left')
                            with ui.row().classes('items-center justify-between w-full'):
                                ui.label(f"GHS {prop['price']}").classes('text-lg text-green-600 font-semibold text-left')
