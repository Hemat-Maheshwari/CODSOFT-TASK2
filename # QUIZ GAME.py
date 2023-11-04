import tkinter as tk
import random

# Define quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["a) Paris", "b) London", "c) Berlin", "d) Madrid"],
        "correct_answer": "a"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["a) Earth", "b) Mars", "c) Venus", "d) Jupiter"],
        "correct_answer": "b"
    },
    {
        "question": "What is the largest mammal in the world?",
        "choices": ["a) Elephant", "b) Blue Whale", "c) Giraffe", "d) Rhinoceros"],
        "correct_answer": "b"
    },
    {
        "question": "What is the currency of Japan?",
        "choices": ["a) Yen", "b) Dollar", "c) Euro", "d) Rupee"],
        "correct_answer": "a"
    }, 
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["a) Earth", "b) Mars", "c) Jupiter", "d) Venus"],
        "correct_answer": "c"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.score = 0
        self.current_question = 0
        self.shuffle_questions()
        
        # Add a title label to make the GUI more appealing
        self.title_label = tk.Label(root, text="Welcome to the Quiz Game", font=("Arial", 18, "bold"), pady=10)
        self.title_label.pack()
        
        self.question_label = tk.Label(root, text="", font=("Arial", 14))
        self.question_label.pack(pady=10)
        
        self.choice_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Arial", 12), command=lambda i=i: self.check_answer(i))
            self.choice_buttons.append(button)
            button.pack(pady=5)
        
        self.next_question_button = tk.Button(root, text="Next Question", font=("Arial", 12), state=tk.DISABLED, command=self.next_question)
        self.next_question_button.pack(pady=20)
        
        self.next_question()

    def shuffle_questions(self):
        random.shuffle(questions)
        
    def next_question(self):
        if self.current_question < len(questions):
            question_data = questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i in range(4):
                self.choice_buttons[i].config(text=question_data["choices"][i], state=tk.NORMAL)
        else:
            self.show_final_results()
    
    def check_answer(self, choice):
        question_data = questions[self.current_question]
        if question_data["correct_answer"] == chr(97 + choice):
            self.score += 1
        self.current_question += 1
        for button in self.choice_buttons:
            button.config(state=tk.DISABLED)
        self.next_question_button.config(state=tk.NORMAL)
    
    def show_final_results(self):
        self.title_label.config(text="Quiz completed!")
        self.question_label.config(text=f"You got {self.score} out of {len(questions)} questions correct.")
        self.next_question_button.config(text="Quit", command=self.quit_game)

    def quit_game(self):
        self.root.destroy()

# Create the main application window
root = tk.Tk()
app = QuizApp(root)
root.geometry("400x400")  # Set the window size
root.mainloop()
