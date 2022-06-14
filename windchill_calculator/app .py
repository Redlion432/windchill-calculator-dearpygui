# app.py - My DearPyGUI windowed app
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='WindChill Calculator', width=600, height=300)

with dpg.window(label="WindChill Calculator", width=600, height=300):
    dpg.add_text("Welcome to the WindChill Calculator")
    dpg.add_input_int(label= "Wind Speed")
    dpg.add_input_int(label= "Temperature")
    dpg.add_button(label="Calculate")
    dpg.add_button(label="Clear")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()