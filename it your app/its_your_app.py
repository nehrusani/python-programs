import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

class RobloxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Roblox App")
        self.root.geometry("700x500")
        self.root.configure(bg="#1e1e1e")
        self.root.resizable(False, False)
        self.games = []
        # Header
        class RobloxApp:
            def __init__(self, root):
                self.root = root
                self.root.title("Roblox App")
                self.root.geometry("700x500")
                self.root.configure(bg="#1e1e1e")
                self.root.resizable(False, False)
                self.games = []
                # Header
                header = tk.Label(
                    root,
                    text="🎮 ROBLOX",
                    font=("Arial", 32, "bold"),
                    bg="#1e1e1e",
                    fg="#00a2ff"
                )
                header.pack(pady=20)
                
                # Game list frame with scrollbar
                container = tk.Frame(root, bg="#1e1e1e")
                container.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
                
                tk.Label(container, text="Popular Games:", bg="#1e1e1e", fg="white", font=("Arial", 12, "bold")).pack(anchor=tk.W, pady=(0, 10))
                
                games = {
                    "Adopt Me!": "https://www.roblox.com/games/920587237",
                    "Bloxburg": "https://www.roblox.com/games/185655149",
                    "Murder Mystery": "https://www.roblox.com/games/142823291",
                    "Jailbreak": "https://www.roblox.com/games/606849621"
                }
                
                for game, url in games.items():
                    btn = tk.Button(
                        container,
                        text=f"▶ {game}",
                        bg="#00a2ff",
                        fg="white",
                        font=("Arial", 11, "bold"),
                        relief=tk.RAISED,
                        padx=10,
                        pady=8,
                        cursor="hand2",
                        command=lambda u=url: webbrowser.open(u)
                    )
                    btn.pack(fill=tk.X, pady=6)
                    btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#0088cc"))
                    btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#00a2ff"))
                
                # Footer
                footer = tk.Label(
                    root,
                    text="© 2024 Roblox Corporation",
                    bg="#1e1e1e",
                    fg="#666666",
                    font=("Arial", 8)
                )
                footer.pack(side=tk.BOTTOM, pady=10)

        if __name__ == "__main__":
            root = tk.Tk()
            app = RobloxApp(root)
            root.mainloop()
        header.pack(pady=20)
        
        # Game list frame with scrollbar
        container = tk.Frame(root, bg="#1e1e1e")
        container.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        tk.Label(container, text="Popular Games:", bg="#1e1e1e", fg="white", font=("Arial", 12, "bold")).pack(anchor=tk.W, pady=(0, 10))
        
        games = ["Adopt Me!", "Bloxburg", "Murder Mystery", "Jailbreak"]
        for i, game in enumerate(games):
            btn = tk.Button(
                container,
                text=f"▶ {game}",
                bg="#00a2ff",
                fg="white",
                font=("Arial", 11, "bold"),
                relief=tk.RAISED,
                padx=10,
                pady=8,
                cursor="hand2",
                command=lambda g=game: messagebox.showinfo("Game", f"Opening {g}!")
            )
            btn.pack(fill=tk.X, pady=6)
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#0088cc"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#00a2ff"))
        
        # Footer
        footer = tk.Label(
            root,
            text="© 2024 Roblox Corporation",
            bg="#1e1e1e",
            fg="#666666",
            font=("Arial", 8)
        )
        footer.pack(side=tk.BOTTOM, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = RobloxApp(root)
    root.mainloop()