import tkinter as tk
import random

# Örnek kelimeler
words = {
    "A1": [
        {"en": "apple", "tr": "elma"},
        {"en": "book", "tr": "kitap"},
        {"en": "car", "tr": "araba"},
        {"en": "dog", "tr": "köpek"},
        {"en": "sun", "tr": "güneş"}
    ],
    "A2": [
        {"en": "garden", "tr": "bahçe"},
        {"en": "market", "tr": "pazar"},
    ]
}

class WordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("İngilizce-Türkçe Kelime Testi")
        self.root.geometry("450x400")
        self.root.configure(bg="#f0f0f0")

        self.level = None
        self.score = 0
        self.total_questions = 0
        self.current_question = {}
        self.questions = []
        self.feedback_label = None

        self.create_start_screen()

    def create_start_screen(self):
        self.clear_screen()

        title = tk.Label(self.root, text="Kelime Test Uygulamasına Hoşgeldiniz", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
        title.pack(pady=30)

        subtitle = tk.Label(self.root, text="Seviyeni Seç", font=("Helvetica", 14), bg="#f0f0f0")
        subtitle.pack(pady=10)

        for level in words.keys():
            button = tk.Button(self.root, text=level, font=("Helvetica", 12), width=15, bg="#4caf50", fg="white",
                                command=lambda l=level: self.start_quiz(l))
            button.pack(pady=5)

    def start_quiz(self, level):
        self.level = level
        self.questions = random.sample(words[level], len(words[level]))
        self.total_questions = len(self.questions)
        self.score = 0
        self.ask_question()

    def ask_question(self):
        self.clear_screen()

        if not self.questions:
            self.show_result()
            return

        self.current_question = self.questions.pop()

        question_frame = tk.Frame(self.root, bg="#f0f0f0")
        question_frame.pack(pady=30)

        question_label = tk.Label(
            question_frame,
            text=f"'{self.current_question['en']}' kelimesinin Türkçesi nedir?",
            font=("Helvetica", 14),
            bg="#f0f0f0"
        )
        question_label.pack()

        options = self.generate_options()

        for option in options:
            button = tk.Button(
                self.root,
                text=option,
                font=("Helvetica", 12),
                width=20,
                bg="#2196f3",
                fg="white",
                command=lambda o=option: self.check_answer(o)
            )
            button.pack(pady=5)

        self.feedback_label = tk.Label(self.root, text="", font=("Helvetica", 12), bg="#f0f0f0")
        self.feedback_label.pack(pady=10)

    def generate_options(self):
        options = [self.current_question["tr"]]
        while len(options) < 4:
            random_word = random.choice(random.choice(list(words.values())))
            if random_word["tr"] not in options:
                options.append(random_word["tr"])
        random.shuffle(options)
        return options

    def check_answer(self, selected_option):
        if selected_option == self.current_question["tr"]:
            self.score += 1
            self.feedback_label.config(text="✅ Doğru!", fg="green")
        else:
            self.feedback_label.config(text=f"❌ Yanlış! Doğru cevap: {self.current_question['tr']}", fg="red")

        self.root.after(1000, self.ask_question)  # 1 saniye sonra yeni soru

    def show_result(self):
        self.clear_screen()

        success_rate = (self.score / self.total_questions) * 100

        result_label = tk.Label(
            self.root,
            text=f"Test Tamamlandı!\n\nDoğru Sayısı: {self.score}/{self.total_questions}\nBaşarı: %{success_rate:.1f}",
            font=("Helvetica", 16),
            bg="#f0f0f0"
        )
        result_label.pack(pady=40)

        restart_button = tk.Button(
            self.root,
            text="Yeni Test",
            font=("Helvetica", 12),
            width=15,
            bg="#4caf50",
            fg="white",
            command=self.create_start_screen
        )
        restart_button.pack(pady=10)

        exit_button = tk.Button(
            self.root,
            text="Çıkış",
            font=("Helvetica", 12),
            width=15,
            bg="#f44336",
            fg="white",
            command=self.root.quit
        )
        exit_button.pack(pady=5)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = WordApp(root)
    root.mainloop()
