import tkinter as tk
from tkinter import simpledialog, messagebox
import random

class RPGGameApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window properties
        self.title("Text RPG")
        self.geometry("400x400")

        # Game variables
        self.player_hp = 100
        self.monster_hp = 50

        # Game introduction
        self.label = tk.Label(self, text="Welcome to the Text RPG!\nYou encounter a monster. What will you do?", padx=10, pady=10)
        self.label.pack()

        # Fight button
        self.fight_button = tk.Button(self, text="Fight", command=self.fight)
        self.fight_button.pack()

        # Flee button
        self.flee_button = tk.Button(self, text="Flee", command=self.flee)
        self.flee_button.pack()

        # Status
        self.status = tk.Label(self, text=f"Player HP: {self.player_hp}\nMonster HP: {self.monster_hp}", padx=10, pady=10)
        self.status.pack()

    def fight(self):
        # Calculate damage dealt and taken
        damage_dealt = random.randint(10, 20)
        damage_taken = random.randint(5, 15)

        # Update HP
        self.monster_hp -= damage_dealt
        self.player_hp -= damage_taken

        # Update status
        self.status['text'] = f"Player HP: {self.player_hp}\nMonster HP: {self.monster_hp}"

        # Check for end conditions
        if self.player_hp <= 0:
            self.end_game("You have been defeated.")
        elif self.monster_hp <= 0:
            self.end_game("You have defeated the monster.")

    def flee(self):
        flee_success = random.choice([True, False])
        if flee_success:
            self.end_game("You successfully fled from the monster.")
        else:
            self.end_game("You failed to flee and were defeated.")

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.destroy()

# Run the game
if __name__ == "__main__":
    app = RPGGameApp()
    app.mainloop()