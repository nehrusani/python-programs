import ast
import json
import os
import platform
import random
import sys
import time
from datetime import datetime

#!/usr/bin/env python3
"""
A multipurpose CLI utility featuring:
- Calculator with math functions
- Todo list manager
- Notes system
- Number guessing game
- Quick haiku generator
- System info
"""


DATA_DIR = os.path.dirname(os.path.abspath(__file__))
TODO_FILE = os.path.join(DATA_DIR, "todos.json")
NOTES_FILE = os.path.join(DATA_DIR, "notes.json")


# -------------------------
# Utilities
# -------------------------
def load_json(path, default):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def save_json(path, data):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print("Save error:", e)


def pause():
    input("\nPress Enter to continue...")


# -------------------------
# Safe calculator
# -------------------------
ALLOWED_NODES = {
    ast.Expression,
    ast.BinOp,
    ast.UnaryOp,
    ast.Num,
    ast.Constant,  # for Python 3.8+
    ast.Add,
    ast.Sub,
    ast.Mult,
    ast.Div,
    ast.Pow,
    ast.Mod,
    ast.USub,
    ast.UAdd,
    ast.FloorDiv,
    ast.Load,
    ast.Call,
    ast.Name,
    ast.Attribute,
    ast.Tuple,
    ast.List,
}


SAFE_NAMES = {
    "pi": 3.141592653589793,
    "e": 2.718281828459045,
    "sqrt": lambda x: x ** 0.5,
    "abs": abs,
    "round": round,
    "min": min,
    "max": max,
    "pow": pow,
}


def is_safe(node):
    if type(node) not in ALLOWED_NODES:
        return False
    for child in ast.iter_child_nodes(node):
        if not is_safe(child):
            return False
    # Disallow names that are not in SAFE_NAMES
    if isinstance(node, ast.Name):
        return node.id in SAFE_NAMES
    # Disallow attribute access
    if isinstance(node, ast.Attribute):
        return False
    if isinstance(node, ast.Call):
        if not isinstance(node.func, (ast.Name, ast.Attribute)):
            return False
        if isinstance(node.func, ast.Name) and node.func.id not in SAFE_NAMES:
            return False
    return True


def safe_eval(expr):
    try:
        tree = ast.parse(expr, mode="eval")
    except Exception:
        raise ValueError("Invalid expression")
    if not is_safe(tree):
        raise ValueError("Unsafe or unsupported expression")
    compiled = compile(tree, "<safe>", "eval")
    return eval(compiled, {"__builtins__": {}}, SAFE_NAMES)


def calculator():
    print("\n-- Smart Calculator --")
    print("You can use + - * / // % ** and functions: sqrt, abs, round, min, max, pow, pi, e")
    while True:
        expr = input("Enter expression (or 'back'): ").strip()
        if expr.lower() in {"back", "b", "quit", "q", ""}:
            return
        try:
            result = safe_eval(expr)
            print("= ", result)
        except Exception as e:
            print("Error:", e)


# -------------------------
# Todo list
# -------------------------
def list_todos(todos):
    if not todos:
        print("No todos yet.")
        return
    for i, item in enumerate(todos, 1):
        status = "✓" if item.get("done") else " "
        created = item.get("created", "")
        print(f"{i}. [{status}] {item.get('text')} (created: {created})")


def todo_menu():
    todos = load_json(TODO_FILE, [])
    while True:
        print("\n-- Todo List --")
        list_todos(todos)
        print("\nOptions: (a)dd  (t)oggle  (d)elete  (c)lear done  (b)ack")
        cmd = input("Choose: ").strip().lower()
        if cmd in {"b", "back"}:
            save_json(TODO_FILE, todos)
            return
        if cmd in {"a", "add"}:
            text = input("Todo text: ").strip()
            if text:
                todos.append({"text": text, "done": False, "created": datetime.now().isoformat()})
        elif cmd in {"t", "toggle"}:
            idx = input("Index to toggle: ").strip()
            if idx.isdigit() and 1 <= int(idx) <= len(todos):
                i = int(idx) - 1
                todos[i]["done"] = not todos[i].get("done", False)
            else:
                print("Invalid index.")
        elif cmd in {"d", "delete"}:
            idx = input("Index to delete: ").strip()
            if idx.isdigit() and 1 <= int(idx) <= len(todos):
                todos.pop(int(idx) - 1)
            else:
                print("Invalid index.")
        elif cmd in {"c", "clear"}:
            todos = [t for t in todos if not t.get("done")]
        else:
            print("Unknown command.")


# -------------------------
# Notes
# -------------------------
def list_notes(notes):
    if not notes:
        print("No notes.")
        return
    for i, note in enumerate(notes, 1):
        ts = note.get("created", "")
        title = note.get("title", "") or "(untitled)"
        print(f"{i}. {title} — {ts}")


def notes_menu():
    notes = load_json(NOTES_FILE, [])
    while True:
        print("\n-- Notes --")
        list_notes(notes)
        print("\nOptions: (v)iew  (a)dd  (s)earch  (d)elete  (b)ack")
        cmd = input("Choose: ").strip().lower()
        if cmd in {"b", "back"}:
            save_json(NOTES_FILE, notes)
            return
        if cmd in {"a", "add"}:
            title = input("Title: ").strip()
            print("Enter note body. End with a single '.' on a line.")
            lines = []
            while True:
                line = input()
                if line == ".":
                    break
                lines.append(line)
            body = "\n".join(lines).strip()
            notes.append({"title": title, "body": body, "created": datetime.now().isoformat()})
        elif cmd in {"v", "view"}:
            idx = input("Index to view: ").strip()
            if idx.isdigit() and 1 <= int(idx) <= len(notes):
                n = notes[int(idx) - 1]
                print(f"\n--- {n.get('title','(untitled)')} ---\n{n.get('body')}\n---")
            else:
                print("Invalid index.")
        elif cmd in {"s", "search"}:
            q = input("Search query: ").strip().lower()
            results = [n for n in notes if q in (n.get("title","").lower() + " " + n.get("body","").lower())]
            if not results:
                print("No matches.")
            else:
                for i, n in enumerate(results, 1):
                    print(f"{i}. {n.get('title')} ({n.get('created')})")
        elif cmd in {"d", "delete"}:
            idx = input("Index to delete: ").strip()
            if idx.isdigit() and 1 <= int(idx) <= len(notes):
                notes.pop(int(idx) - 1)
            else:
                print("Invalid index.")
        else:
            print("Unknown command.")


# -------------------------
# Guessing game
# -------------------------
def guessing_game():
    print("\n-- Guess the Number --")
    low, high = 1, 100
    secret = random.randint(low, high)
    tries = 0
    print(f"I'm thinking of a number between {low} and {high}. Try to guess it!")
    while True:
        guess = input("Your guess (or 'q' to quit): ").strip().lower()
        if guess in {"q", "quit", "exit"}:
            print(f"The number was {secret}.")
            return
        if not guess.isdigit():
            print("Please enter a number.")
            continue
        tries += 1
        g = int(guess)
        if g < secret:
            print("Too low.")
        elif g > secret:
            print("Too high.")
        else:
            print(f"Correct! You got it in {tries} tries.")
            return


# -------------------------
# Creative generator
# -------------------------
ADJECTIVES = ["silent", "bright", "ancient", "swift", "gentle", "wild", "bold", "calm"]
NOUNS = ["river", "forest", "star", "cloud", "mountain", "ocean", "city", "dream"]
VERBS = ["whispers", "glows", "wanders", "sleeps", "dances", "breathes", "flies", "rises"]


def generate_haiku():
    # Very small haiku-like generator (not strict syllables)
    a1 = random.choice(ADJECTIVES)
    n1 = random.choice(NOUNS)
    v = random.choice(VERBS)
    a2 = random.choice(ADJECTIVES)
    n2 = random.choice(NOUNS)
    print("\n-- Tiny Haiku --")
    print(f"{a1.capitalize()} {n1} {v},")
    print(f"{a2} {n2} in the night,")
    print(f"{random.choice(NOUNS).capitalize()} sleeps.")


# -------------------------
# System info
# -------------------------
def system_info():
    print("\n-- System Info --")
    print("Platform:", platform.platform())
    print("Python:", platform.python_version())
    print("Time:", datetime.now().isoformat())


# -------------------------
# Main menu
# -------------------------
def main_menu():
    random.seed()
    while True:
        print("\n=== Best Program Ever ===")
        print("1) Calculator")
        print("2) Todo List")
        print("3) Notes")
        print("4) Guessing Game")
        print("5) Tiny Haiku")
        print("6) System Info")
        print("7) Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            calculator()
        elif choice == "2":
            todo_menu()
        elif choice == "3":
            notes_menu()
        elif choice == "4":
            guessing_game()
        elif choice == "5":
            generate_haiku()
            pause()
        elif choice == "6":
            system_info()
            pause()
        elif choice == "7" or choice.lower() in {"q", "quit", "exit"}:
            print("Goodbye.")
            time.sleep(0.3)
            return
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
        try:
            sys.exit(0)
        except SystemExit:
            pass