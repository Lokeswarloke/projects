import tkinter as tk
from tkinter import scrolledtext, simpledialog
import json
import random
import time
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ChatApplication:
    def __init__(self, master):
        self.master = master
        master.title("Chat Application")

        # Load chatbot data
        with open('pro.json') as file:
            self.data = json.load(file)

        # Extract patterns and responses
        self.patterns = []
        self.responses = []
        for intent in self.data['intents']:
            for pattern in intent['patterns']:
                self.patterns.append(pattern)
                self.responses.append(intent['responses'])

        # Initialize CountVectorizer and cosine similarity
        self.vectorizer = CountVectorizer()
        self.X = self.vectorizer.fit_transform(self.patterns)
        self.cosine_sim = cosine_similarity(self.X, self.X)

        # Create heading
        self.heading = tk.Label(master, text="Chat Application", bg="blue", fg="white", font=("TimesNewRoman", 18, "bold"))
        self.heading.pack(fill="x", pady=10)

        # Create scrolled text widget to display conversation
        self.conversation_display = scrolledtext.ScrolledText(master, width=80, height=35, state='disabled',
                                                              bg="lightgreen")
        self.conversation_display.pack(padx=10, pady=5)

        # Create input field for user
        self.input_field = tk.Entry(master, width=50, font=("TimesNewRoman", 12))
        self.input_field.pack(pady=5)
        self.input_field.insert(tk.END, "Enter any question...")
        self.input_field.bind("<FocusIn>", self.clear_placeholder)
        self.input_field.bind("<Return>", self.process_input)

    def generate_response(self, user_input):
        user_input_vector = self.vectorizer.transform([user_input])
        similarity_scores = cosine_similarity(user_input_vector, self.X)
        max_index = similarity_scores.argmax()
        response = random.choice(self.responses[max_index])
        return response

    def update_display(self, message, is_user=False):
        self.conversation_display.config(state='normal')
        if is_user:
            self.conversation_display.insert(tk.END, message + "\n", "user")
        else:
            self.typing_effect("Bot: " + message)
        self.conversation_display.see(tk.END)
        self.conversation_display.config(state='disabled')

    def typing_effect(self, message):
        for char in message:
            time.sleep(0.05)  # Adjust typing speed here
            self.conversation_display.insert(tk.END, char)
            self.conversation_display.see(tk.END)
            self.conversation_display.update()
        self.conversation_display.insert(tk.END, "\n")

    def process_input(self, event):
        user_input = self.input_field.get()
        self.update_display("You: " + user_input, is_user=True)
        if user_input.lower() == 'quit':
            self.master.quit()
        else:
            response = self.generate_response(user_input)
            self.update_display(response)
        self.input_field.delete(0, tk.END)

    def clear_placeholder(self, event):
        self.input_field.delete(0, tk.END)


def main():
    root = tk.Tk()
    app = ChatApplication(root)
    root.mainloop()


if __name__ == "__main__":
    main()
