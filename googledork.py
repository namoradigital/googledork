import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

class GoogleDorkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Google Dork Finder")
        self.root.geometry("600x400")

        self.label = tk.Label(root, text="Masukkan Query Google Dork:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=50, font=("Arial", 12))
        self.entry.pack(pady=10)

        self.search_button = tk.Button(root, text="Cari", width=20, font=("Arial", 12), command=self.search)
        self.search_button.pack(pady=10)

        self.result_text = tk.Text(root, width=70, height=15, font=("Arial", 10))
        self.result_text.pack(pady=10)

    def search(self):
        query = self.entry.get().strip()
        if not query:
            messagebox.showwarning("Input Error", "Silakan masukkan query Google Dork!")
            return

        url = f"https://www.google.com/search?q={query}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            results = soup.find_all('div', class_='BVG0Nb')

            self.result_text.delete(1.0, tk.END)
            if results:
                for result in results:
                    self.result_text.insert(tk.END, result.text + '\n\n')
            else:
                self.result_text.insert(tk.END, "Tidak ada hasil ditemukan.\n")
        
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Gagal mengambil hasil pencarian: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GoogleDorkApp(root)
    root.mainloop()
