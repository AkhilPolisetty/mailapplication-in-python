import tkinter as tk
from tkinter import messagebox

class MailApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mail Application")

        # Create UI components
        self.email_text = tk.Text(self, height=10, width=50)
        self.login_button = tk.Button(self, text="Login", command=self.show_login_screen)
        self.inbox_button = tk.Button(self, text="Inbox", command=self.show_inbox)
        self.compose_button = tk.Button(self, text="Compose", command=self.show_compose)

        # Pack UI components
        self.email_text.pack(pady=10)
        self.login_button.pack()
        self.inbox_button.pack()
        self.compose_button.pack()

        # Hide inbox and compose buttons initially
        self.inbox_button.pack_forget()
        self.compose_button.pack_forget()

        # Variables to store email data
        self.emails = []

    def show_login_screen(self):
        # Create login screen
        login_screen = tk.Toplevel(self)
        login_screen.title("Login")
        login_text = tk.Text(login_screen, height=5, width=30)
        login_text.pack(padx=10, pady=10)

        email_label = tk.Label(login_text, text="Email:")
        email_label.pack(anchor="w")
        email_entry = tk.Entry(login_text)
        email_entry.pack()

        password_label = tk.Label(login_text, text="Password:")
        password_label.pack(anchor="w")
        password_entry = tk.Entry(login_text, show="*")
        password_entry.pack()

        login_button = tk.Button(login_text, text="Login", command=lambda: self.login(email_entry.get(), password_entry.get()))
        login_button.pack()

    def login(self, email, password):
        # Perform authentication logic
        if email == "intern@codeclause.com" and password == "password":
            messagebox.showinfo("Login", "Login successful!")
            self.show_inbox_button()
        else:
            messagebox.showerror("Login", "Invalid email or password")

    def show_inbox_button(self):
        self.login_button.pack_forget()
        self.inbox_button.pack()
        self.compose_button.pack()

    def show_inbox(self):
        # Clear email content in the Text widget
        self.email_text.delete(1.0, tk.END)

        # Logic to fetch inbox emails
        self.emails = self.fetch_inbox_emails()

        # Display email content in the Text widget
        for email in self.emails:
            self.email_text.insert(tk.END, f"From: {email.sender}\n")
            self.email_text.insert(tk.END, f"Subject: {email.subject}\n")
            self.email_text.insert(tk.END, f"Content: {email.content}\n\n")

    def fetch_inbox_emails(self):
        # Logic to fetch and return inbox emails
        return [
            Email("intern1@codeclause.com", "Hello", "This is the first email"),
            Email("intern2@codeclause.com", "Greetings", "This is the second email"),
            Email("intern3@codeclause.com", "Important Notice", "This is the third email"),
        ]

    def show_compose(self):
        # Create compose mail screen
        compose_screen = tk.Toplevel(self)
        compose_screen.title("Compose Mail")

        compose_text = tk.Text(compose_screen, height=10, width=50)
        compose_text.pack(padx=10, pady=10)

        recipient_label = tk.Label(compose_text, text="Recipient:")
        recipient_label.pack(anchor="w")
        recipient_entry = tk.Entry(compose_text)
        recipient_entry.pack()

        subject_label = tk.Label(compose_text, text="Subject:")
        subject_label.pack(anchor="w")
        subject_entry = tk.Entry(compose_text)
        subject_entry.pack()

        content_label = tk.Label(compose_text, text="Content:")
        content_label.pack(anchor="w")
        content_entry = tk.Text(compose_text, height=5, width=40)
        content_entry.pack()

        send_button = tk.Button(compose_text, text="Send", command=lambda: self.send_mail(recipient_entry.get(), subject_entry.get(), content_entry.get("1.0", tk.END)))
        send_button.pack()

    def send_mail(self, recipient, subject, content):
        # Logic to send the composed email
        messagebox.showinfo("Compose Mail", "Mail sent successfully!")

class Email:
    def __init__(self, sender, subject, content):
        self.sender = sender
        self.subject = subject
        self.content = content

if __name__ == "__main__":
    app = MailApplication()
    app.mainloop()
