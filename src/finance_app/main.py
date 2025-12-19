import sqlite3
from datetime import datetime

conn = sqlite3.connect('finance.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY,
    account TEXT,
    category TEXT,
    amount REAL,
    date TEXT,
    note TEXT
)
''')
conn.commit()

def add_expense():
    account = input("Compte (Revolut / Banque Populaire / Desjardins) : ")
    category = input("Catégorie (rent / other) : ")
    amount = float(input("Montant : "))
    note = input("Note (optionnel) : ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    c.execute(
        'INSERT INTO expenses (account, category, amount, date, note) VALUES (?, ?, ?, ?, ?)',
        (account, category, amount, date, note)
    )
    conn.commit()
    print("Dépense ajoutée avec succès !\n")

def view_expenses():
    c.execute('SELECT * FROM expenses')
    rows = c.fetchall()
    total = 0
    total_rent = 0
    for row in rows:
        print(row)
        total += row[3]
        if row[2] == 'rent':
            total_rent += row[3]
    print(f"\nTotal dépenses : {total}")
    print(f"Total dépenses (loyer) : {total_rent}")
    print(f"Total dépenses (hors loyer) : {total - total_rent}\n")

def main():
    while True:
        print("1. Ajouter une dépense")
        print("2. Voir les dépenses")
        print("3. Quitter")
        choice = input("Choix : ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            break
        else:
            print("Choix invalide.\n")

if __name__ == "__main__":
    main()
