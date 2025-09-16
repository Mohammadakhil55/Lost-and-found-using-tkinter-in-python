import os
from datetime import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.listview import ListView
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout

# Data storage
lost_items = []
found_items = []
user_info = {"name": "", "college": ""}

class LostFoundApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical')
        self.login_screen()
        return self.root

    def login_screen(self):
        self.clear_screen()
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(Label(text="Enter Your Name:"))
        self.name_input = TextInput(multiline=False)
        layout.add_widget(self.name_input)

        layout.add_widget(Label(text="Select Your College:"))
        self.college_input = TextInput(multiline=False)
        layout.add_widget(self.college_input)

        login_button = Button(text="Login")
        login_button.bind(on_press=self.login)
        layout.add_widget(login_button)

        self.root.add_widget(layout)

    def login(self, instance):
        name = self.name_input.text.strip()
        college = self.college_input.text.strip()
        if name and college:
            user_info["name"] = name
            user_info["college"] = college
            self.main_screen()
        else:
            self.show_popup("Error", "Please enter both name and college.")

    def main_screen(self):
        self.clear_screen()
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        lost_button = Button(text="Report Lost Item")
        lost_button.bind(on_press=self.report_lost_item)
        layout.add_widget(lost_button)

        found_button = Button(text="Report Found Item")
        found_button.bind(on_press=self.report_found_item)
        layout.add_widget(found_button)

        self.root.add_widget(layout)

    def report_lost_item(self, instance):
        self.report_item(lost_items)

    def report_found_item(self, instance):
        self.report_item(found_items)

    def report_item(self, item_list):
        self.clear_screen()
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        layout.add_widget(Label(text="Item Name:"))
        item_name_input = TextInput(multiline=False)
        layout.add_widget(item_name_input)

        layout.add_widget(Label(text="Location:"))
        location_input = TextInput(multiline=False)
        layout.add_widget(location_input)

        layout.add_widget(Label(text="Contact Info:"))
        contact_input = TextInput(multiline=False)
        layout.add_widget(contact_input)

        image_button = Button(text="Attach Image")
        image_button.bind(on_press=lambda instance: self.attach_image())
        layout.add_widget(image_button)

        submit_button = Button(text="Submit")
        submit_button.bind(on_press=lambda instance: self.submit_item(item_list, item_name_input, location_input, contact_input))
        layout.add_widget(submit_button)

        self.root.add_widget(layout)

    def submit_item(self, item_list, item_name_input, location_input, contact_input):
        item_name = item_name_input.text.strip()
        location = location_input.text.strip()
        contact = contact_input.text.strip()
        if item_name and location and contact:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            item_list.append((user_info["name"], user_info["college"], item_name, location, contact, timestamp, self.image_path))
            self.show_popup("Success", "Item reported successfully.")
            self.main_screen()
        else:
            self.show_popup("Error", "Please fill in all fields.")

    def attach_image(self):
        filechooser = FileChooserIconView()
        filechooser.bind(on_selection=self.on_image_selected)
        popup = Popup(title="Select Image", content=filechooser, size_hint=(0.9, 0.9))
        popup.open()

    def on_image_selected(self, instance, value):
        if value:
            self.image_path = value[0]
            self.show_popup("Image Selected", f"Image path: {self.image_path}")

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.6, 0.3))
        popup.open()

    def clear_screen(self):
        self.root.clear_widgets()

if __name__ == '__main__':
    LostFoundApp().run()
