# Copyright 2025 Ashu Choudhury
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import wx
import json
import os
from gemini import AI

app = wx.App()
class ChatApp(wx.Frame):
    def __init__(self, settings=None):
        # Load settings from file or use the provided settings (if any)
        self.settings = settings if settings else self.load_settings()

        super().__init__(None, title="send message", size=(500, 400))

        self.panel = wx.Panel(self)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Chat display
        self.chat_display = wx.ListBox(self.panel, style=wx.LB_SINGLE)
        self.main_sizer.Add(self.chat_display, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        # Input box and send button
        self.input_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.input_box = wx.TextCtrl(self.panel, style=wx.TE_PROCESS_ENTER, size=(350, -1))
        self.send_button = wx.Button(self.panel, label="Send")
        self.settings_button = wx.Button(self.panel, label="Settings")

        self.input_sizer.Add(self.input_box, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        self.input_sizer.Add(self.send_button, flag=wx.ALL, border=5)
        self.input_sizer.Add(self.settings_button, flag=wx.ALL, border=5)

        # Layout setup for main interface
        self.main_sizer.Add(self.input_sizer, flag=wx.EXPAND)

        self.panel.SetSizer(self.main_sizer)

        # Settings panel components (initially hidden)
        self.settings_panel = wx.Panel(self.panel)
        self.settings_sizer = wx.BoxSizer(wx.VERTICAL)
        self.mute_checkbox = wx.CheckBox(self.settings_panel, label="Mute Mic")
        self.mute_checkbox.SetValue(self.settings.get("mute", False))  # Bind to dictionary value

        self.ai_name_label = wx.StaticText(self.settings_panel, label="AI Name:")
        self.ai_name_input = wx.TextCtrl(self.settings_panel, size=(200, -1), value=self.settings.get("ai_name", ""))

        self.save_button = wx.Button(self.settings_panel, label="Save")
        self.cancel_button = wx.Button(self.settings_panel, label="Cancel")

        self.settings_sizer.Add(self.mute_checkbox, flag=wx.EXPAND | wx.ALL, border=5)
        self.settings_sizer.Add(self.ai_name_label, flag=wx.EXPAND | wx.ALL, border=5)
        self.settings_sizer.Add(self.ai_name_input, flag=wx.EXPAND | wx.ALL, border=5)
        self.settings_sizer.Add(self.save_button, flag=wx.EXPAND | wx.ALL, border=5)
        self.settings_sizer.Add(self.cancel_button, flag=wx.EXPAND | wx.ALL, border=5)

        self.settings_panel.SetSizer(self.settings_sizer)
        self.settings_panel.Hide()  # Initially hidden

        # Event bindings
        self.send_button.Bind(wx.EVT_BUTTON, self.send_message)
        self.input_box.Bind(wx.EVT_TEXT_ENTER, self.send_message)
        self.settings_button.Bind(wx.EVT_BUTTON, self.toggle_settings)
        self.save_button.Bind(wx.EVT_BUTTON, self.save_settings)
        self.cancel_button.Bind(wx.EVT_BUTTON, self.cancel_settings)
        self.Bind(wx.EVT_KEY_DOWN, self.on_key_press)

        # Add buttons for Close and Exit Program
        self.close_button = wx.Button(self.panel, label="Close Window")
        self.exit_button = wx.Button(self.panel, label="Exit Program")

        self.main_sizer.Add(self.close_button, flag=wx.ALL, border=5)
        self.main_sizer.Add(self.exit_button, flag=wx.ALL, border=5)

        self.close_button.Bind(wx.EVT_BUTTON, self.on_close_window)
        self.exit_button.Bind(wx.EVT_BUTTON, self.on_exit_program)

    def send_message(self, event):
        """Send a message from the input box to the chat display."""
        message = self.input_box.GetValue()
        if message.strip():  # Ensure the message is not empty
            self.chat_display.Append(f"You: {message}")
            text=AI(isGui=True, message=message)
            self.add_message(self.get_ai_name(), text)

            self.input_box.Clear()

    def add_message(self, sender, message):
        """Add a message from another source to the chat display."""
        self.chat_display.Append(f"{sender}: {message}")

    def toggle_settings(self, event):
        """Toggle between showing the settings and the chat."""
        if self.settings_panel.IsShown():
            self.settings_panel.Hide()
            self.main_sizer.ShowItems(True)
        else:
            self.settings_panel.Show()
            self.main_sizer.ShowItems(False)
        self.Layout()

    def save_settings(self, event):
        """Save the settings."""
        # Update dictionary with current UI values
        self.settings["ai_name"] = self.ai_name_input.GetValue()
        self.settings["mute"] = self.mute_checkbox.GetValue()

        # Save settings to file
        self.save_settings_to_file()

        # Hide settings panel after saving
        self.toggle_settings(event)

    def cancel_settings(self, event):
        """Cancel the settings changes."""
        self.mute_checkbox.SetValue(self.settings.get("mute", False))  # Reset mute status
        self.ai_name_input.SetValue(self.settings.get("ai_name", ""))  # Reset AI name input
        self.toggle_settings(event)  # Hide settings panel after canceling

    def on_key_press(self, event):
        """Handle key press events (e.g., Escape to hide the window)."""
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.Hide()  # Hide the app when Escape is pressed
        else:
            event.Skip()  # Otherwise, pass the event to other handlers

    def on_close_window(self, event):
        """Close the application window."""
        self.Hide()  # Hide the window, not exiting the program

    def on_exit_program(self, event):
        """Handle the exit program event with a confirmation dialog."""
        dialog = wx.MessageDialog(self, "Are you sure you want to exit the program?",
                                  "Confirm Exit", wx.YES_NO | wx.ICON_QUESTION)
        result = dialog.ShowModal()

        if result == wx.ID_YES:
            from index import exitAi
            exitAi()  # Close the program completely
        else:
            dialog.Destroy()  # Destroy the dialog if 'No' is pressed

    def load_settings(self):
        """Load settings from a file or return default settings."""
        settings_file = "settings.json"
        if os.path.exists(settings_file):
            with open(settings_file, "r") as f:
                return json.load(f)
        return {"mute": False, "ai_name": "AI"}  # Default settings

    def save_settings_to_file(self):
        """Save the settings dictionary to a file."""
        with open("settings.json", "w") as f:
            json.dump(self.settings, f, indent=4)

    def is_muted(self):
        """Return the current mute status (True/False)."""
        return self.settings.get("mute", False)

    def get_ai_name(self):
        """Return the current AI name."""
        return self.settings.get("ai_name", "AI")

    def show_ui(self):
        """Show the main UI and settings panel if needed."""
        self.Show()
        self.input_box.SetFocus()

    def hide_ui(self):
        """Hide the main UI."""
        self.Hide()


chat_app = ChatApp()
