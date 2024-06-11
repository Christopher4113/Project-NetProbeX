import unittest
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.base import EventLoop


from home import Home

class TestHomeApp(unittest.TestCase):
    
    def setUp(self):
        # Set up the Kivy app
        self.app = Home()
        EventLoop.ensure_window()
        self.app.build()
        
    def test_close_button(self):
        # Simulate the pressing of the close button
        close_button = self.app.root.children[1]  # Assuming close_button is the second widget added
        close_button.trigger_action(duration=0.1)
        
        # Check if the confirmation popup is shown
        popup = self.app.root_window.children[0] if isinstance(self.app.root_window.children[0], Popup) else None
        self.assertIsNotNone(popup, "Close confirmation popup did not appear.")
        
        # Simulate pressing 'Yes' to close the app
        yes_button = popup.content.children[1]
        yes_button.trigger_action(duration=0.1)
        
    def test_sidebar(self):
        # Simulate the pressing of the sidebar button
        sidebar_button = self.app.root.children[0]  # Assuming sidebar_button is the first widget added
        sidebar_button.trigger_action(duration=0.1)
        
        # Check if the sidebar popup is shown
        popup = self.app.root_window.children[0] if isinstance(self.app.root_window.children[0], Popup) else None
        self.assertIsNotNone(popup, "Sidebar popup did not appear.")
        
    def tearDown(self):
        # Clean up after test
        self.app.stop()
        EventLoop.window = None
        EventLoop.idle()

if __name__ == "__main__":
    unittest.main()
