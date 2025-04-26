import tkinter as tk
from tkinter import messagebox, ttk
import json
import random

# words.json dosyasını oku
with open('words.json', 'r', encoding='utf-8') as file:
    kelimeler = json.load(file)

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Challenge!")
        self.bg_colors = ["#a1c4fd", "#fbc2eb", "#fceabb", "#d4fc79", "#ff9a9e"]
        self.root.configure(bg=self.bg_colors[0])

        self.score = 0
        self.question_count = 0
        self.word_list = []
        self.direction = None
        self.selected_levels = []

        self.xp = 0
        self.level = 1

        self.create_language_selection_screen()

    def create_language_selection_screen(self):
        self.clear_screen()

        title = tk.Label(self.root, text="Ne çalışmak istersin?", font=("Comic Sans MS", 24, "bold"), bg=self.bg_colors[0], pady=20)
        title.pack(pady=30)

        self.lang_frame = tk.Frame(self.root, bg=self.bg_colors[0])
        self.lang_frame.pack(pady=20)

        self.lang_buttons = {}

        langs = [("🇬🇧 İngilizce -> Türkçe", "en_to_tr"), ("🇹🇷 Türkçe -> İngilizce", "tr_to_en")]
        for idx, (text, value) in enumerate(langs):
            btn = tk.Button(self.lang_frame, text=text, font=("Comic Sans MS", 16), width=25, height=2,
                            bg="#ffffff", fg="#333333", relief="ridge", bd=4,
                            command=lambda v=value: self.select_language(v))
            btn.pack(pady=10)
            self.lang_buttons[value] = btn

    def select_language(self, value):
        self.direction = value
        for v, btn in self.lang_buttons.items():
            btn.config(bg="#ffffff")
        self.lang_buttons[value].config(bg="#90ee90")
        self.create_level_selection_screen()

    def create_level_selection_screen(self):
        self.clear_screen()

        title = tk.Label(self.root, text="Seviye Seç (Birden fazla seçebilirsin!)", font=("Comic Sans MS", 20, "bold"), bg=self.bg_colors[0], pady=20)
        title.pack(pady=20)

        self.level_frame = tk.Frame(self.root, bg=self.bg_colors[0])
        self.level_frame.pack(pady=20)

        self.level_buttons = {}

        levels = ["A1", "A2", "B1", "B2", "C1"]
        level_colors = {
            "A1": "#77dd77",  # yeşil
            "A2": "#77dd77",  # yeşil
            "B1": "#4682b4",  # mavi
            "B2": "#4682b4",  # mavi
            "C1": "#ff6961"   # kırmızı
        }

        for level in levels:
            btn = tk.Button(self.level_frame, text=level, font=("Comic Sans MS", 16), width=10, height=2,
                            bg=level_colors[level], fg="#333333", relief="ridge", bd=4,
                            command=lambda l=level: self.toggle_level(l))
            btn.pack(side=tk.LEFT, padx=10, pady=10)
            self.level_buttons[level] = btn

        start_btn = tk.Button(self.root, text="🚀 Teste Başla!", command=self.start_test, font=("Comic Sans MS", 18, "bold"), bg="#ff758c", fg="white", width=20, relief="ridge", bd=5)
        start_btn.pack(pady=40)

        # Ekran boyutunu içeriğe göre ayarlayalım
        self.adjust_window_size()

    def toggle_level(self, level):
        if level in self.selected_levels:
            self.selected_levels.remove(level)
            # Butonun arka planını ilk haline döndür
            self.level_buttons[level].config(bg=self.get_initial_button_color(level))
        else:
            self.selected_levels.append(level)
            # Seçili buton rengi değişir
            self.level_buttons[level].config(bg="#add8e6")  # Seçildiğinde renk değişir

    def get_initial_button_color(self, level):
        """Seviye butonunun ilk rengini döndüren fonksiyon."""
        level_colors = {
            "A1": "#77dd77",  # yeşil
            "A2": "#77dd77",  # yeşil
            "B1": "#4682b4",  # mavi
            "B2": "#4682b4",  # mavi
            "C1": "#ff6961"   # kırmızı
        }
        return level_colors.get(level, "#ffffff")

    def start_test(self):
        if not self.selected_levels:
            messagebox.showwarning("Uyarı", "En az bir seviye seçmelisiniz.")
            return

        self.word_list = []
        for lvl in self.selected_levels:
            self.word_list.extend(kelimeler[lvl])

        random.shuffle(self.word_list)

        self.score = 0
        self.question_count = 0
        self.xp = 0
        self.level = 1

        self.create_test_screen()

    def create_test_screen(self):
        self.clear_screen()

        self.word_label = tk.Label(self.root, text="", font=("Comic Sans MS", 24, "bold"), bg=self.bg_colors[0], pady=20)
        self.word_label.pack(pady=20)

        self.option_buttons = []
        colors = ["#ffb347", "#ff6961", "#77dd77", "#aec6cf"]
        for i in range(4):
            btn = tk.Button(self.root, text="", font=("Comic Sans MS", 16, "bold"), width=20, height=2,
                            bg=colors[i], fg="black", command=lambda b=i: self.check_answer(b))
            btn.pack(pady=10)
            self.option_buttons.append(btn)

        self.info_frame = tk.Frame(self.root, bg=self.bg_colors[0])
        self.info_frame.pack(pady=20)

        self.score_label = tk.Label(self.info_frame, text="Skor: 0", font=("Comic Sans MS", 16), bg=self.bg_colors[0])
        self.score_label.grid(row=0, column=0, padx=10)

        self.xp_label = tk.Label(self.info_frame, text="XP: 0/50", font=("Comic Sans MS", 16), bg=self.bg_colors[0])
        self.xp_label.grid(row=0, column=1, padx=10)

        self.level_label = tk.Label(self.info_frame, text="Seviye: 1", font=("Comic Sans MS", 16), bg=self.bg_colors[0])
        self.level_label.grid(row=0, column=2, padx=10)

        # Progress Bar ekle
        self.xp_bar = ttk.Progressbar(self.root, orient="horizontal", length=400, mode="determinate", maximum=50)
        self.xp_bar.pack(pady=20)
        self.xp_bar["value"] = 0

        self.next_question()

    def next_question(self):
        self.selected_word = random.choice(self.word_list)

        if self.direction == "en_to_tr":
            word = self.selected_word["english"]
            correct_answer = self.selected_word["turkish"]
            options = [correct_answer] + [random.choice(self.word_list)["turkish"] for _ in range(3)]
        else:
            word = self.selected_word["turkish"]
            correct_answer = self.selected_word["english"]
            options = [correct_answer] + [random.choice(self.word_list)["english"] for _ in range(3)]

        random.shuffle(options)

        self.correct_index = options.index(correct_answer)

        self.word_label.config(text=word)
        for i in range(4):
            self.option_buttons[i].config(text=options[i])

    def check_answer(self, selected_index):
        self.question_count += 1
        if selected_index == self.correct_index:
            self.score += 1
            self.xp += 10

            if self.xp >= 50:
                self.level += 1
                self.xp -= 50
                self.root.configure(bg=random.choice(self.bg_colors))
                messagebox.showinfo("🎉 Level Up!", f"Tebrikler! Seviye {self.level} oldun!")

            messagebox.showinfo("✅ Doğru!", "Tebrikler doğru cevap!")
        else:
            messagebox.showerror("❌ Yanlış", "Yanlış cevap :(")

        self.update_info_labels()
        self.next_question()

    def update_info_labels(self):
        self.score_label.config(text=f"Skor: {self.score}/{self.question_count}")
        self.xp_label.config(text=f"XP: {self.xp}/50")
        self.level_label.config(text=f"Seviye: {self.level}")
        self.xp_bar["value"] = self.xp

    def adjust_window_size(self):
        """Ekran boyutunu içeriğe göre dinamik ayarlamak için fonksiyon."""
        screen_width = self.root.winfo_width()
        screen_height = self.root.winfo_height()
        # Ekranın boyutunu içeriğe göre ayarlayalım
        self.root.geometry(f"{screen_width + 50}x{screen_height + 50}")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Başlat
if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
