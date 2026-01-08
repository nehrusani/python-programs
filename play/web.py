import tkinter as tk
from tkinterweb import HtmlFrame  # make sure tkinterweb is installed

def load_page():
    url = url_entry.get()
    if not url.startswith("http"):
        url_with_http = "https://" + url
    else:
        url_with_http = url
    browser.load_website(url_with_http)

root = tk.Tk()
root.title("Mini Chrome in Tkinter")
root.geometry("1000x700")

top_bar = tk.Frame(root)
top_bar.pack(side="top", fill="x")

url_entry = tk.Entry(top_bar, width=80)
url_entry.pack(side="left", padx=5, pady=5)

go_button = tk.Button(top_bar, text="Go", command=load_page)
go_button.pack(side="left", padx=5)

browser = HtmlFrame(root)
browser.pack(fill="both", expand=True)

# load a default page
browser.load_website("https://www.google.com")

root.mainloop()
