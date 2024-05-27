import tkinter as tk
from tkinter import messagebox

class HorseQuiz:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz sobre o CLThanos")

        self.question_number = 0
        self.score = 0

        self.questions = [
            {
                "question": "Qual é o maior inimigo do CLThanos?",
                "options": ["Cipriano", "Piadas do Nicolas", "PIX BET", "DRY"],
                "correct_answer": "Piadas do Nicolas"
            },
            {
                "question": "Quantas vezes por dia o CLThanos aposta?",
                "options": ["infinitas vezes", "5783", "0", "40"],
                "correct_answer": "infinitas vezes"
            },
            {
                "question": "Qual é a maior felicidade do CLThanos?",
                "options": ["Escala 6 por 1", "Uma moto", "GREEN", "se mutar em call"],
                "correct_answer": "GREEN"
            }
        ]

        self.question_label = tk.Label(master, text="", font=("Arial", 12))
        self.question_label.pack(pady=10)

        self.option_var = tk.StringVar()
        self.option_var.set(None)

        self.option_buttons = []
        for i in range(4):
            button = tk.Radiobutton(master, text="", variable=self.option_var, value="", font=("Helvetica", 10))
            self.option_buttons.append(button)
            button.pack(pady=5)

        self.next_button = tk.Button(master, text="Próxima", command=self.next_question)
        self.next_button.pack(pady=10)

        self.display_question()

    def display_question(self):
        self.question_label.config(text=self.questions[self.question_number]["question"])
        options = self.questions[self.question_number]["options"]
        for i in range(4):
            self.option_buttons[i].config(text=options[i], value=options[i])

    def check_answer(self):
        selected_answer = self.option_var.get()
        correct_answer = self.questions[self.question_number]["correct_answer"]
        if selected_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False

    def next_question(self):
        is_correct = self.check_answer()
        if is_correct:
            messagebox.showinfo("Resposta Correta", "Parabéns! Sua resposta está correta.")
        else:
            messagebox.showwarning("Resposta Incorreta", "Sua resposta está incorreta.")

        # Animação de transição de opacidade
        self.master.attributes("-alpha", 0.0)  # Inicia a transição com opacidade 0
        self.master.after(500, self.update_question)  # Chama a função para atualizar a pergunta após 500ms

    def update_question(self):
        if self.question_number < len(self.questions) - 1:
            self.question_number += 1
            self.display_question()
            self.master.attributes("-alpha", 1.0)  # Restaura a opacidade para 1
        else:
            messagebox.showinfo("Pontuação Final", f"Sua pontuação final é: {self.score}/{len(self.questions)}")
            self.master.destroy()

def main():
    root = tk.Tk()
    quiz = HorseQuiz(root)
    root.mainloop()

if __name__ == "__main__":
    main()
