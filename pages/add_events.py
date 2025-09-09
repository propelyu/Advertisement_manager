from nicegui import ui

def show_add_event_page():
    ui.label("Welcome to the Add Event Page -Tacia Simon")
    
    def submit_form():
        ui.notify(f"Advert Posted:\nTitle: {title.value}\nDescription: {description.value}\nPrice: {price.value}\nCategory: {category.value}")

    with ui.card().classes('w-[500px] p-6 shadow-lg space-y-4'):
        ui.label("Post an Advert").classes('text-3xl font-bold text-blue-700 mb-4')

        title = ui.input("Title").classes('w-full')
        description = ui.textarea("Description").classes('w-full')
        price = ui.input("Price").props('type=number').classes('w-full')
        
        category = ui.select(
            ["1 Bedroom apartment", "2 Bedroom apartment", "3 Bedroom apartment", "Luxury Villa", "Office Space", "Others"], 
            label="Category"
        ).classes('w-full')

        ui.button("Post Advert", on_click=submit_form, color="blue-700").classes('text-white px-4 py-2 rounded-lg w-full')
