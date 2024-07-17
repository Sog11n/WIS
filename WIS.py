import customtkinter as ctk
from tkinter import messagebox
import webbrowser

class WindowsSetupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WIS")
        self.root.geometry("600x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.center_window(600, 600)
        self.create_widgets()

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        title_frame = ctk.CTkFrame(self.root)
        title_frame.pack(pady=10)

        title = ctk.CTkLabel(title_frame, text="ㅤWindows Initial Setupㅤ", font=("Helvetica", 36, "bold"), text_color="#00BFFF")
        title.pack()    
        subtitle = ctk.CTkLabel(title_frame, text="by: Windows House", font=("Helvetica", 16), text_color="#00BFFF")
        subtitle.pack()

        self.tab_control = ctk.CTkTabview(self.root, width=550, height=350)
        self.tab_windows_10 = self.tab_control.add("Windows 10")
        self.tab_windows_11 = self.tab_control.add("Windows 11")
        self.tab_control.pack(expand=1, fill='both', padx=20, pady=20)

        self.create_windows_10_tab()
        self.create_windows_11_tab()

        social_frame = ctk.CTkFrame(self.root)
        social_frame.pack(pady=10)

        discord_btn = self.create_social_button(social_frame, "Discord", self.open_discord, 0)
        website_btn = self.create_social_button(social_frame, "Website", self.open_website, 1)
        github_btn = self.create_social_button(social_frame, "GitHub", self.open_github, 2)

        exit_btn = ctk.CTkButton(self.root, text="Exit", command=self.root.quit, width=100, height=40, corner_radius=10, fg_color="#FF6347", hover_color="#FF4500")
        exit_btn.pack(pady=10)

    def create_windows_10_tab(self):
        self.create_buttons(self.tab_windows_10)

    def create_windows_11_tab(self):
        self.create_buttons(self.tab_windows_11)

    def create_buttons(self, tab):
        buttons = [
            ("Update System and Drivers", self.update_system),
            ("Windows Settings", self.configure_settings),
            ("Disable surveillance in Windows", self.disable_tracking),
            ("Fast performance in Windows", self.optimize_performance),
            ("Windows Activation", self.install_software)
        ]

        for text, command in buttons:
            btn = ctk.CTkButton(tab, text=text, command=command, width=350, height=40, corner_radius=10)
            btn.pack(pady=10)

    def create_social_button(self, frame, text, command, column):
        button = ctk.CTkButton(frame, text=text, command=command, width=100, height=40, corner_radius=10)
        button.grid(row=0, column=column, padx=10)
        return button

    def update_system(self):
        self.show_message("Update System", "System updated successfully!")

    def install_software(self):
        self.show_message("Install Software", "DirectX and .NET Framework installed successfully!")

    def configure_settings(self):
        self.show_message("Configure Settings", "Settings configured successfully!")

    def disable_tracking(self):
        self.show_message("Disable Tracking", "Tracking disabled successfully!")

    def optimize_performance(self):
        self.show_message("Optimize Performance", "System performance optimized successfully!")

    def show_message(self, title, message):
        popup = ctk.CTkToplevel(self.root)
        popup.title(title)
        popup.geometry("300x200")
        self.center_popup(popup, 300, 200)
        label = ctk.CTkLabel(popup, text=message, font=("Helvetica", 16), text_color="#FFFFFF")
        label.pack(pady=40)
        ok_button = ctk.CTkButton(popup, text="OK", command=popup.destroy, width=100, height=40, corner_radius=10)
        ok_button.pack(pady=20)

    def center_popup(self, window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

    def open_discord(self):
        webbrowser.open("https://discord.gg/VtaHyu2X6D")

    def open_website(self):
        webbrowser.open("https://windowshose.vercel.app")

    def open_github(self):
        webbrowser.open("https://github.com/Sog11n/winset")

if __name__ == "__main__":
    root = ctk.CTk()
    app = WindowsSetupApp(root)
    root.mainloop()
