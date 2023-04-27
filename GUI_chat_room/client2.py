import tkinter as tk
from PIL import Image, ImageTk

class ChatClientGUI:
    def __init__(self):
        # Define window
        self.root = tk.Tk()
        self.root.title("Chat Client")
        icon = ImageTk.PhotoImage(Image.open("./icons/messageIcon.png"))
        self.root.iconphoto(True, icon)
        self.root.geometry("700x700")
        self.root.resizable(0,0)

        # Define fonts and colors
        self.my_font = ('SimSun', 14)
        self.black = "#010101"
        self.light_green = "#1fc742"
        self.root.config(bg=self.black)

        # Create Frames
        self.info_frame = tk.Frame(self.root, bg=self.black)
        self.output_frame = tk.Frame(self.root, bg=self.black)
        self.input_frame = tk.Frame(self.root, bg=self.black)
        self.info_frame.pack()
        self.output_frame.pack(pady=10)
        self.input_frame.pack()

        # Create widgets
        self.name_label = tk.Label(self.info_frame, text="Client Name:", font=self.my_font, fg=self.light_green, bg=self.black)
        self.name_entry = tk.Entry(self.info_frame, borderwidth=3, font=self.my_font)
        self.ip_label = tk.Label(self.info_frame, text="Host IP:", font=self.my_font, fg=self.light_green, bg=self.black)
        self.ip_entry = tk.Entry(self.info_frame, borderwidth=3, font=self.my_font)
        self.port_label = tk.Label(self.info_frame, text="Port Num:", font=self.my_font, fg=self.light_green, bg=self.black)
        self.port_entry = tk.Entry(self.info_frame, borderwidth=3, font=self.my_font, width=10)
        self.connect_button = tk.Button(self.info_frame, text="Connect", font=self.my_font, bg=self.light_green, borderwidth=5, command=self.connect)
        self.disconnect_button = tk.Button(self.info_frame, text="Disconnect", font=self.my_font, bg=self.light_green, borderwidth=5, width=10, state=tk.DISABLED, command=self.disconnect)

        # Grid widgets
        self.name_label.grid(row=0, column=0, padx=2, pady=10)
        self.name_entry.grid(row=0, column=1, padx=2, pady=10)
        self.port_label.grid(row=0, column=2, padx=2, pady=10)
        self.port_entry.grid(row=0, column=3, padx=2, pady=10)
        self.ip_label.grid(row=1, column=0, padx=2, pady=5)
        self.ip_entry.grid(row=1, column=1, padx=2, pady=5)
        self.connect_button.grid(row=1, column=2, padx=4, pady=5)
        self.disconnect_button.grid(row=1, column=3, padx=4, pady=5)

    def run(self):
        self.root.mainloop()

    def connect(self):
        # TODO: Implement connection functionality
        self.disconnect_button.config(state=tk.NORMAL)
        self.connect_button.config(state=tk.DISABLED)

    def disconnect(self):
        # TODO: Implement disconnection functionality
        self.connect_button.config(state=tk.NORMAL)
        self.disconnect_button.config(state=tk.DISABLED)

if __name__ == '__main__':
    chat_client_gui = ChatClientGUI()
    chat_client_gui.run()
