from nicegui import ui
with ui.element('section').classes('h-screen w-full flex flex-col justify-center items-center bg-[url(assets/bg_1.jpg)] bg-cover bg-center'):
        ui.label('THE SIMPLEST') \
          .classes('text-6xl font-bold text-bg-black mb-4 ') \
        #   .style('color: gold; text-shadow: 0 0 10px #FFD700, 0 0 20px #FFA500, 0 0 30px #FF8C00;')
        ui.label('WAY TO FIND A PROPERTY') \
          .classes('text-5xl  mb-2') \


ui.run()
