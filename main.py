import tkinter as tk
from tkinter import messagebox
import random
import json

# Данные
citati = [
    {"text": "Простые решения редко бывают правильными.", "author": "Мудрец", "theme": "жизнь"},
    {"text": "Делай, что должен, и будь что будет.", "author": "Римская", "theme": "мотивация"},
    {"text": "Век живи — век учись.", "author": "Народная", "theme": "мудрость"},
]

try:
    with open("history.json", "r", encoding="utf-8") as f:
        istoria = json.load(f)
except:
    istoria = []

def sluchaynaya():
    cit = random.choice(citati)
    text_cit.config(text=f'"{cit["text"]}"')
    avtor_cit.config(text=f"— {cit['author']} [{cit['theme']}]")
    
    istoria.append(cit)
    with open("history.json", "w", encoding="utf-8") as f:
        json.dump(istoria, f, ensure_ascii=False, indent=4)
    
    pokazat_istoriyu()

def dobavit_novuyu():
    txt = vvod_text.get().strip()
    avt = vvod_avtor.get().strip()
    tem = vvod_tema.get().strip()
    
    if txt == "" or avt == "" or tem == "":
        messagebox.showwarning("Ошибка", "Заполни все поля!")
        return
    
    citati.append({"text": txt, "author": avt, "theme": tem})
    messagebox.showinfo("Успех", "Цитата добавлена!")
    
    vvod_text.delete(0, tk.END)
    vvod_avtor.delete(0, tk.END)
    vvod_tema.delete(0, tk.END)

# Окно
okno = tk.Tk()
okno.title("Цитатник")
okno.geometry("480x550")

tk.Label(okno, text="ГЕНЕРАТОР ЦИТАТ", font=("Arial", 16)).pack(pady=10)

text_cit = tk.Label(okno, text="", font=("Arial", 12), wraplength=450)
text_cit.pack(pady=20)

avtor_cit = tk.Label(okno, text="", fg="gray")
avtor_cit.pack()

tk.Button(okno, text="Случайная цитата", command=sluchaynaya, bg="green", fg="white").pack(pady=10)

tk.Label(okno, text="--- Добавить цитату ---").pack(pady=5)
tk.Label(okno, text="Текст:").pack()
vvod_text = tk.Entry(okno, width=50)
vvod_text.pack()

tk.Label(okno, text="Автор:").pack()
vvod_avtor = tk.Entry(okno, width=30)
vvod_avtor.pack()

tk.Label(okno, text="Тема:").pack()
vvod_tema = tk.Entry(okno, width=20)
vvod_tema.pack()

tk.Button(okno, text="Добавить", command=dobavit_novuyu, bg="orange").pack(pady=5)

tk.Label(okno, text="--- История ---").pack(pady=5)

spisok_ist = tk.Listbox(okno, width=55, height=8)
spisok_ist.pack()

def pokazat_istoriyu(spis=None):
    spisok_ist.delete(0, tk.END)
    if spis is None:
        spis = istoria
    if not spis:
        spisok_ist.insert(0, "Пусто")
    for i, c in enumerate(spis, 1):
        spisok_ist.insert(tk.END, f"{i}. {c['text'][:35]} — {c['author']}")

def ochistit():
    if messagebox.askyesno("Очистка", "Удалить всю историю?"):
        global istoria
        istoria = []
        with open("history.json", "w") as f:
            json.dump(istoria, f)
        pokazat_istoriyu()

tk.Button(okno, text="Очистить историю", command=ochistit, bg="red", fg="white").pack(pady=5)

pokazat_istoriyu()
okno.mainloop()