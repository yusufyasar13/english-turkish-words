import tkinter as tk

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Kelime Öğrenme Uygulaması")
        self.size(400,300)
        self.configure(bg="lightblue")
        self.main_screen()


    def size(self,window_width,window_height):
        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2 - 100)

        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.resizable(False, False)


    def main_screen(self):

        self.main_frame = tk.Frame(self, bg="lightblue")

        self.main_label_frame = tk.Frame(self.main_frame, bg="blue", height=200)
        
        self.title_label = tk.Label(self.main_label_frame, 
                                    text="Welcome to the dictionary app.\nPlease press to button for starting!\n\nSözlük uygulamasına hoşgeldiniz.\nBaşlamak için lütfen butona tıklayınız!", 
                                    font=("Arial", 18), bg="lightblue",
                                    wraplength=400,
                                    justify=tk.CENTER,
                                    anchor=tk.CENTER)
        self.title_label.pack(expand=True, anchor=tk.CENTER)

        self.main_label_frame.pack(expand=True, fill=tk.BOTH, side=tk.TOP, padx=5, pady=5)
        self.main_label_frame.pack_propagate(False)


        self.main_button_frame = tk.Frame(self.main_frame, bg="red", height=100)

        self.start_button = tk.Button(self.main_button_frame, text="Başla", command=self.start_game, font=("Arial", 16), bg="lightblue", width=10, height=2, cursor="hand2")
        self.start_button.pack(expand=True, anchor=tk.CENTER, padx=5, pady=5)

        self.main_button_frame.pack(expand=True, fill=tk.BOTH, side=tk.BOTTOM, padx=5, pady=5)
        self.main_button_frame.pack_propagate(False)


        self.main_frame.pack(expand=True, fill=tk.BOTH)
        self.main_frame.pack_propagate(False)

    def start_game(self):
        
        self.size(400, 400)
        self.main_frame.destroy()
        self.start_frame = tk.Frame(self, bg="lightblue")
        
        self.start_label_frame = tk.Frame(self.start_frame, bg="blue", height=100)
        self.start_choice_label = tk.Label(self.start_label_frame, bg="lightblue",
                                           text="Lütfen başlamak istediğiniz seviyeyi seçiniz.\nPlease select the level you want to start with.", 
                                           font=("Arial", 16), wraplength=400, 
                                           justify=tk.CENTER, anchor=tk.CENTER)
        self.start_choice_label.pack(expand=True, anchor=tk.CENTER, padx=5, pady=5)
        self.start_choice_label.pack_propagate(False)
        self.start_label_frame.pack(expand=True, fill=tk.BOTH, side=tk.TOP, padx=5, pady=5)
        self.start_label_frame.pack_propagate(False)

        self.start_choice_frame = tk.Frame(self.start_frame, bg="purple", height=150)

        self.level_frame = tk.Frame(self.start_choice_frame, bg="orange")
        self.buttons = ["a1", "a2", "b1", "b2", "c1"]
        for button in self.buttons:
            btn = tk.Button(self.level_frame, text=button.upper(), font=("Arial", 10), bg="lightblue", width=6, height=2, cursor="hand2")
            btn.pack(expand=True, fill=tk.BOTH, side=tk.LEFT, padx=5, pady=5)
            btn.pack_propagate(False)

        self.level_frame.pack(expand=True, fill=tk.BOTH, side=tk.TOP, padx=5, pady=5)
        self.level_frame.pack_propagate(False)

        self.language_frame = tk.Frame(self.start_choice_frame, bg="yellow")
        self.language_buttons = ["İngilizce --> Türkçe", "Türkçe --> İngilizce"]
        for button in self.language_buttons:
            btn = tk.Button(self.language_frame, text=button, font=("Arial", 10), bg="lightblue", width=20, height=2, cursor="hand2")
            btn.pack(expand=True, fill=tk.BOTH, side=tk.LEFT, padx=5, pady=5)
            btn.pack_propagate(False)
        self.language_frame.pack(expand=True, fill=tk.BOTH, side=tk.BOTTOM, padx=5, pady=5)
        self.language_frame.pack_propagate(False)
        
        self.start_choice_frame.pack(expand=True, fill=tk.BOTH, side=tk.TOP, padx=5, pady=5)
        self.start_choice_frame.pack_propagate(False)

        self_start_letsgo_frame = tk.Frame(self.start_frame, bg="green", height=50)
        self_start_letsgo_frame.pack(expand=True, fill=tk.BOTH, side=tk.BOTTOM, padx=5, pady=5)   
        self_start_letsgo_frame.pack_propagate(False)

        self.start_frame.pack(expand=True, fill=tk.BOTH)
        self.start_frame.pack_propagate(False)



if __name__ == "__main__":
    app = App()
    app.mainloop()