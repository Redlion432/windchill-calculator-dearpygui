# app.py - My DearPyGUI windowed app
import dearpygui.dearpygui as dpg

dpg.create_context()

# Generate unique ids for all widgets we want to change in runtime
wind_id = dpg.generate_uuid()
temp_id = dpg.generate_uuid()
output_id = dpg.generate_uuid()

def callback():
    output = "Wind Value: " + str(dpg.get_value(wind_id))
    dpg.set_value(output_id, output)

dpg.create_viewport(title='WindChill Calculator', width=600, height=300)

with dpg.window(label="WindChill Calculator", width=600, height=300):
    dpg.add_text("Welcome to the WindChill Calculator")
    dpg.add_input_int(label= "Wind Speed", width=100, tag=wind_id)
    dpg.add_input_int(label= "Temperature", width=100, tag=temp_id)
    dpg.add_button(label="Calculate", callback=callback)
    dpg.add_button(label="Clear")
    dpg.add_text("", tag=output_id)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()