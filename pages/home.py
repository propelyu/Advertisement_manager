from nicegui import ui
from components.header import show_header
import requests
from utils.api import base_url


@ui.page('/')
def show_home_page():
    
    show_header()
    ui.query('.nicegui-content').classes('m-0 p-0')

    
    response = requests.get(f"{base_url}/adverts")
    json_data = response.json()
    properties = json_data["data"]

    #  HERO SECTION 
    with ui.element('section').classes(
        'relative h-screen w-full flex flex-col justify-center items-center overflow-hidden'
    ):
        # Background carousel
         with ui.carousel().props("arrows autoplay swipe infinite").classes(
            "absolute inset-0 w-full h-full z-0"
        ).style("width: 100%; height: 100%;"):
            ui.carousel_slide().classes("w-full h-full").style(
                "background-image: url(/assets/interior.jpg); background-size: cover; background-position: center;"
            )
            ui.carousel_slide().classes("w-full h-full").style(
                "background-image: url(/assets/architecture.jpg); background-size: cover; background-position: center;"
            )
            ui.carousel_slide().classes("w-full h-full").style(
                "background-image: url(/assets/bg_1.jpg); background-size: cover; background-position: center;"
            )
            ui.carousel_slide().classes("w-screen h-screen").style(
                "background-image: url(/assets/architecture-.jpg); background-size: cover; background-position: center;"
            )
            # ui.carousel_slide().classes("w-screen h-screen").style(
            #     "background-image: url(/assets/homee.jpg); background-size: cover; background-position: center; width: 100vw; height: 100vh;")        
        
        # Content overlay
         with ui.column().classes(
            'relative z-10 flex flex-col justify-center items-center text-black text-center p-4'
        ):
            ui.label('THE SIMPLEST').classes(
                'text-6xl font-bold mb-4'
            )
            ui.label('WAY TO FIND A PROPERTY').classes(
                'text-5xl  mb-2'
            )
            ui.label("Surrounded by nature, a peaceful retreat where modern living meets paradise").classes("text-lg mb-2")
            
            # Hero Search Bar
            with ui.row().classes(
                "bg-white rounded-full shadow-md overflow-hidden w-[500px] mt-8"
            ):
                search_input = ui.input(
                    placeholder="Search location"
                ).props("borderless").classes(
                    "flex-1 px-4 py-2 text-gray-700 focus:outline-none"
                )
                with ui.button(
                    on_click=lambda: ui.notify(f"Searching: {search_input.value}")
                ).props("flat round").classes(
                    "bg-pink-500 text-white p-6 rounded-r-full"
                ):
                    ui.icon("search").classes("text-white")
               
    with ui.element("section").classes("w-full py-5"):
             with ui.element("div"). classes('mx-auto max-w-7xl w-full px-6 text-center'):
                  ui.label("OUR SERVICES").classes("text-lg font-semibold text-pink-500 tracking-widest") 
                  ui.label("THE SMARTEST WAY TO BUY A HOME").classes("text-4xl font-bold mt-2 mb-8")
             ui.element('hr').classes('w-16 border-t-4 border-pink-500 mb-12 mx-auto')
             with ui.row().classes('w-full justify-center'):
                 with ui.column().classes('p-4 items-center text-center max-w-sm'):
                    ui.icon('savings').classes('text-pink-500 text-6xl mb-4')
                    ui.label('No Downpayment').classes('text-xl font-bold mb-2')
                    ui.label('The smartest way to buy is now the fastest: All Cash Offer, No Downpayment, and secure Locked in Pricing..').classes('text-gray-600')
                 with ui.column().classes('p-4 items-center text-center max-w-sm'):
                    ui.icon('wallet').classes('text-pink-500 text-6xl mb-4')
                    ui.label('All Cash Offer').classes('text-xl font-bold mb-2')
                    ui.label('Stop losing homes,get the leverage of an All Cash Offer and watch sellers say YES to you.').classes('text-gray-600')
                 with ui.column().classes('p-4 items-center text-center max-w-sm'):
                    ui.icon('lock').classes('text-pink-500 text-6xl mb-4')
                    ui.label('Locked in Pricing').classes('text-xl font-bold mb-2')
                    ui.label('Lock in your dream home price today. Get the certainty of Locked in Pricing and skip the financial worry.').classes('text-gray-600')
           

                            #  FEATURED PROPERTIES 
    
    with ui.element('section').classes('w-full py-16'):
            with ui.element('div').classes('max-w-7xl w-full px-6'):
                with ui.column().classes('items-center'):
                    ui.label('What we offer').classes("text-lg font-semibold text-pink-500 tracking-widest")
                    ui.label("EXCLUSIVE OFFER FOR YOU").classes("text-4xl font-bold mt-2 mb-8 items-center justify-center")
                    ui.element('hr').classes('w-16 border-t-4 border-pink-500 mb-12 mx-auto')    

            
            with ui.element('div').classes(
                'grid grid-cols-1 md:grid-cols-3 gap-8 w-full px-6 md:px-12'
            ):
                for idx, prop in enumerate(properties):
                    with ui.card().classes(
                        'h-80 flex flex-col items-center justify-center '
                        'relative cursor-pointer'
                    ) as card:
                        # Navigate on click
                        card.on('click', lambda i=prop["id"]: ui.navigate.to(f'/view_event?id={i}'))

                        # Category Tag
                        if prop.get('category'):
                            ui.label(prop['category']).classes(
                                'absolute top-2 right-2 z-10 text-xs bg-orange-100 '
                                'text-orange-700 font-semibold px-2 py-1 rounded-full shadow-sm'
                            )

                        # Property Image
                        with ui.element('div').classes('property-image-wrap w-full'):
                            ui.element('img').classes(
                                'w-full h-40 object-cover rounded-lg'
                            ).props(
                                f'src="{prop["image_url"]}" alt="{prop["title"]}"'
                            )

                        # Property Details
                        with ui.element('div').classes('p-2 text-left w-full'):
                            ui.label(prop['title']).classes('text-xl font-bold')
                            with ui.row().classes('items-center justify-between w-full'):
                                ui.label(f"GHS {prop['price']}").classes(
                                    'text-lg text-green-600 font-semibold'
                                )

    with ui.element('section').classes('w-full py-16 bg-white'):
        with ui.element('div').classes('mx-auto max-w-7xl w-full px-6 text-center'):
            # Heading and sub-heading
         ui.label('TESTIMONIAL').classes("text-lg font-semibold text-pink-500 mb-2")
         ui.label("Happy Clients").classes("text-4xl font-bold mt-2 mb-8 items-center justify-center")
         ui.element('hr').classes('w-16 border-t-4 border-pink-500 mb-12 mx-auto')
        with ui.element('div').classes('grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8 mt-12'):
                # Testimonial 1
                with ui.card().classes('p-8 bg-white shadow-lg rounded-lg'):
                    ui.label("I couldn't be happier with my new property. This platform helped me find exactly what I was looking for, at a great price, and in a fantastic location.").classes('text-gray-600 mb-6')
                    with ui.row().classes('items-center'):
                        ui.avatar('https://cdn.pixabay.com/photo/2023/01/02/06/02/woman-7691362_1280.jpg', size='md').classes('rounded-full mr-4')
                        with ui.column():
                            ui.label('Vicky Dwira').classes('font-bold text-lg')
                            ui.label('Marketing Manager').classes('text-sm text-gray-500')

                # Testimonial 2
                with ui.card().classes('p-8 bg-white shadow-lg rounded-lg'):
                    ui.label('The team was incredibly helpful and professional. They were with me every step of the way, providing expert advice that made all the difference in my home search').classes('text-gray-600 mb-6')
                    with ui.row().classes('items-center'):
                        ui.avatar('https://cdn.pixabay.com/photo/2021/07/03/20/06/woman-6384768_640.jpg', size='md').classes('rounded-full mr-4')
                        with ui.column():
                            ui.label('Tacia Tamakloe').classes('font-bold text-lg')
                            ui.label('Marketing Manager').classes('text-sm text-gray-500')

                 # Testimonial 3
                with ui.card().classes('p-8 bg-white shadow-lg rounded-lg'):
                    ui.label('Using this website was a breeze! I found my dream home in less than a week, and the process was so simple and straightforward. Highly recommended!').classes('text-gray-600 mb-6')
                    with ui.row().classes('items-center'):
                        ui.avatar('https://cdn.pixabay.com/photo/2017/08/01/01/33/beanie-2562646_1280.jpg', size='md').classes('rounded-full mr-4')
                        with ui.column():
                            ui.label('Hannah Normeshie').classes('font-bold text-lg')
                            ui.label('Marketing Manager').classes('text-sm text-gray-500') 


                        
        with ui.element('section').classes('w-full py-16'):
         with ui.element('div').classes('mx-auto max-w-7xl w-full px-6 text-center'):
             ui.label('AGENTS').classes("text-lg font-semibold text-pink-500 mb-2")
             ui.label("OUR AGENTS").classes("text-4xl font-bold mt-2 mb-8 items-center justify-center")
             ui.element('hr').classes('w-16 border-t-4 border-pink-500 mb-12 mx-auto')
             # Agents grid
             with ui.element('div').classes('grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8'):
                with ui.card().classes('flex flex-col items-center text-center p-2 rounded-lg overflow-hidden'):
                # Agent 1
                 with ui.element('div').classes('flex flex-col items-center'):
                    
                     ui.image('https://cdn.pixabay.com/photo/2017/02/16/23/10/smile-2072907_1280.jpg').classes('w-64 h-64 rounded-xl object-cover mb-4')
                     ui.label('Tacia Tamakloe').classes('text-xl font-semibold')
                     ui.label('Listing — 10 Properties').classes('text-gray-600')

                 # Agent 2
                with ui.card().classes('flex flex-col items-center text-center p-2 rounded-lg overflow-hidden'):
                    with ui.element('div').classes('flex flex-col items-center'):
                        ui.image('https://cdn.pixabay.com/photo/2018/06/04/22/55/books-3454396_1280.jpg').classes('w-64 h-64 rounded-xl object-cover mb-4')
                        ui.label('Vicky Dwira').classes('text-xl font-semibold')
                        ui.label('Listing — 10 Properties').classes('text-gray-600')

                 # Agent 3
                with ui.card().classes('flex flex-col items-center text-center p-2 rounded-lg overflow-hidden'):
                    with ui.element('div').classes('flex flex-col items-center'):
                        ui.image('https://cdn.pixabay.com/photo/2023/01/02/06/02/woman-7691362_1280.jpg').classes('w-64 h-64 rounded-xl object-cover mb-4')
                        ui.label('Claudia Agyere').classes('text-xl font-semibold')
                        ui.label('Listing — 10 Properties').classes('text-gray-600')

                # Agent 4
                with ui.card().classes('flex flex-col items-center text-center p-2 rounded-lg overflow-hidden'):
                    with ui.element('div').classes('flex flex-col items-center'):
                        ui.image('https://cdn.pixabay.com/photo/2024/01/07/00/36/woman-8492233_1280.jpg').classes('w-64 h-64 rounded-xl object-cover mb-4')
                        ui.label('Hannah Normeshie').classes('text-xl font-semibold')
                        ui.label('Listing — 10 Properties').classes('text-gray-600')


    with ui.element("footer").classes("w-full bg-gray-100 text-black py-8 mt-16"):
        with ui.element("div").classes("max-w-7xl mx-auto px-6"): 
            with ui.element("div").classes("grid grid-cols-1 sm:grid-cols-2 md:grid-cols-5 gap-8"):
                

                # Community Section
                with ui.column().classes("space-y-2"):
                    ui.label("Community").classes("text-lg font-bold text-gray-900")
                    ui.link("➜ Search Properties", "#").classes("text-pink-500 text-sm no-underline")
                    ui.link("➜ For Agents", "#").classes("text-pink-500 text-sm no-underline")
                    ui.link("➜ Reviews", "#").classes("text-pink-500 text-sm no-underline")
                    ui.link("➜ FAQs", "#").classes("text-pink-500 text-sm no-underline")

                with ui.column().classes("space-y-2"):
                 ui.label("About Us").classes("text-lg font-bold text-gray-900")
                 ui.link("➜ Our Story", "#").classes("text-pink-500 text-sm no-underline")
                 ui.link("➜ Meet the team", "#").classes("text-pink-500 text-sm no-underline")
                 ui.link("➜ Careers", "#").classes("text-pink-500 text-sm no-underline")  

                with ui.column().classes("space-y-2"):
                 ui.label("Company").classes("text-lg font-bold text-gray-900")
                 ui.link("➜ About Us", "#").classes("text-pink-500 text-sm no-underline")
                 ui.link("➜ Press", "#").classes("text-pink-500 text-sm no-underline")
                 ui.link("➜ Contact", "#").classes("text-pink-500 text-sm no-underline")
                 ui.link("➜ Careers", "#").classes("text-pink-500 text-sm no-underline") 

                with ui.column().classes("space-y-4"):
                 ui.label("Have Questions?").classes("text-lg font-bold text-gray-900")
                 with ui.row().classes("items-start space-x-2"):
                     ui.icon("place").classes("text-pink-500 text-lg")
                     ui.label("Airport Residential Area,\nAccra, Ghana").classes("text-sm text-gray-600")
                 with ui.row().classes("items-center space-x-2"):
                     ui.icon("call").classes("text-pink-500 text-lg")
                     ui.link("+233 92 3929 xxx", "tel:+233923929xx").classes("text-pink-500 text-sm no-underline")
                 with ui.row().classes("items-center space-x-2"):
                     ui.icon("email").classes("text-pink-500 text-lg")
                     ui.link("info@propelproperties.com", "mailto:info@propelproperties.com").classes("text-pink-500 text-sm no-underline")

            ui.element("hr").classes("my-8 border-gray-300")
            ui.label("© 2025 Propel. All rights reserved.").classes("text-center text-gray-400 text-sm w-full")