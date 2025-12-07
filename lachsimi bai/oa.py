import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk

# --- Main Window ---
root = tk.Tk()
root.title("Rani Lakshmibai – The Brave Queen of Jhansi")
root.geometry("800x700")
root.configure(bg="white")

# --- Load Image ---
try:
    image = Image.open("ls.jpeg")
    image = image.resize((300, 300))  # Resize for better display
    photo = ImageTk.PhotoImage(image)

    img_label = tk.Label(root, image=photo, bg="white")
    img_label.image = photo  # Keep reference
    img_label.pack(pady=10)

except FileNotFoundError:
    img_label = tk.Label(root, text="Error: ls.jpeg not found", fg="red", bg="white")
    img_label.pack(pady=10)

# --- Full Story of Rani Lakshmibai ---
story_text = """
Rani Lakshmibai, one of the greatest heroines of India’s freedom struggle, was born on 19 November 1828 in Varanasi.
Her childhood name was Manikarnika, lovingly called “Manu.” Her father, Moropant Tambe, worked in the court of
the Peshwa at Bithoor, and her mother, Bhagirathi Sapre, was a simple and educated woman.

Manu grew up in the Peshwa’s court, where she played with boys, learned archery, horse riding, sword fighting, 
and other martial arts. Even as a child, she showed extraordinary courage, a sharp mind, and a fearless spirit.

Marriage and Becoming the Queen of Jhansi:
At the age of 14, Manu was married to Maharaja Gangadhar Rao, the king of Jhansi.
After her marriage, she was named Rani Lakshmibai. She became loved by the people for her kindness, wisdom,
and desire to help the poor.

In 1851, the royal couple had a son, but the child died soon after. Saddened, they adopted a boy named Damodar Rao,
as their legal heir. But soon after, Maharaja Gangadhar Rao died, leaving Lakshmibai as the queen and mother
to the young prince.

Conflict with the British – Doctrine of Lapse:
The British East India Company introduced a law called the Doctrine of Lapse, which said that if a king died 
without a biological son, the British could take over the kingdom—even if an adopted son existed.

Using this rule, the British refused to accept Damodar Rao as the heir and ordered Lakshmibai to leave her palace 
and surrender Jhansi.

This was when Rani Lakshmibai said her famous words:
“Main apni Jhansi nahi doongi!” (“I shall not give up my Jhansi!”)

Preparation for War:
Lakshmibai began preparing for battle:
- Assembled an army of men and women
- Trained them in sword fighting and horseback riding
- Strengthened the fort of Jhansi
- Personally practiced war drills

The Revolt of 1857:
In 1857, a major rebellion broke out across India. Jhansi became one of the strongest centers of the uprising.
The British laid siege to Jhansi, attacking with thousands of soldiers. But Lakshmibai fought with unmatched bravery.
She rode on horseback with her infant son tied to her back and attacked the British forces fearlessly.

The Final Battle:
On 18 June 1858, in Gwalior, Lakshmibai fought her final battle. She dressed as a soldier, leading her troops 
from the front. Surrounded by British soldiers, she continued fighting courageously until she was fatally wounded.

Legacy:
Rani Lakshmibai remains an eternal symbol of courage, patriotism, sacrifice, women empowerment, and fearless leadership.
Her life inspires millions even today. She proved that a woman is capable of defending her land, her people, and her honor.
"""

# --- Scrollable Text Widget ---
story_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=20, font=("Arial", 12))
story_box.insert(tk.END, story_text)
story_box.config(state=tk.DISABLED)  # Make it read-only
story_box.pack(padx=20, pady=10)

# --- Start Tkinter Loop ---
root.mainloop()

