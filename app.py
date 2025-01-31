import customtkinter as ctk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import threading
from rfid_reader import RfidReader
from PIL import Image, ImageTk 
import datetime
import json

CATEGORIES = ['Action', 'Sci-Fi', 'Fantasy', 'Horror', 'Biography', 'History']

"""books = {
    'Action' : [
    {
        "id": 1,
        "title": "Jurassic Park",
        "status": "available",
        "borrower": None,
        "image": 'hobbit.png',
        "time": datetime.datetime.now()
    },
    {
        "id": 2,
        "title": "Hobbit",
        "status": "not available",
        "borrower": 714757691636,
        "image": 'hobbit.png',
        "time": datetime.datetime.now() 
    },
    {
        "id": 3,
        "title": "Hunger Games",
        "status": "available",
        "borrower": None,
        "image": 'hobbit.png',
        "time": datetime.datetime.now() 
    },
    {
        "id": 4,
        "title": "Divergent",
        "status": "not available",
        "borrower": 714757691636,
        "image": 'hobbit.png',
        "time": datetime.datetime.now() 
    },
    {
        "id": 5,
        "title": "Treasure Islands",
        "status": "not available",
        "borrower": 101,
        "image": 'hobbit.png',
        "time": datetime.datetime.now() 
    }
],
'Sci-Fi': [
    {
        "id": 6,
        "title": "Dune",
        "status": "available",
        "borrower": None,
        "image": 'hobbit.png',
        "time": datetime.datetime.now()  
    },
    {
        "id": 7,
        "title": "Hyperion",
        "status": "available",
        "borrower": None,
        "image": 'hobbit.png',
        "time": datetime.datetime.now()  
    },
    {
        "id": 8,
        "title": "Foundation",
        "status": "available",
        "borrower": None,
        "image": 'hobbit.png',
        "time": datetime.datetime.now()  
    },
    {
        "id": 9,
        "title": "Neuromancer",
        "status": "not available",
        "borrower": 928285915686,
        "image": 'hobbit.png',
        "time": datetime.datetime.now()   
    },
    {
        "id": 10,
        "title": "Star Wars: Empire Strikes Back",
        "status": "not available",
        "borrower": 714757691636,
        "image": 'hobbit.png',
        "time": datetime.datetime.now()  
    }
],
'Fantasy': [
    {
        "id": 11,
        "title": "Rangers Apprentice",
        "status": "available",
        "borrower": None,
        "image": 'hobbit.png',
        "time": datetime.datetime.now()  
    },
    {
        "id": 12,
        "title": "Fablehaven",
        "status": "not available",
        "borrower": 714757691636,
        "image": 'treasure.png',
        "time": datetime.datetime.now()  
    },
    {
        "id": 13,
        "title": "DragonWatch",
        "status": "available",
        "borrower": None,
        "image": 'ship.png',
        "time": datetime.datetime.now()  
    },
    {
        "id": 14,
        "title": "Harry Potter and Philosopher's stone",
        "status": "available",
        "borrower": None,
        "image": 'hobbit.png',
        "time": datetime.datetime.now()  
    },
    {
        "id": 15,
        "title": "Harry Pottem",
        "status": "not available",
        "borrower": 928285915686,
        "image": 'hobbit.png',
        "time": datetime.datetime.now()  
    }
],
'Horror': [
    {
        "id": 16,
        "title": "Scary Movie",
        "status": "available",
        "borrower": None,
        "image": 'treasure.png',
        "time": datetime.datetime.now()  
    },
    {
        "id": 17,
        "title": "Scary Movie 2",
        "status": "not available",
        "borrower": 101,
        "image": 'hobbit.png',
        "time": datetime.datetime.now()  
    },
    {
        "id": 18,
        "title": "Scary Movie 3",
        "status": "available",
        "borrower": None,
        "image": 'ship.png',
        "time": datetime.datetime.now()  
    },
    {
        "id": 19,
        "title": "Scary Movie 4",
        "status": "not available",
        "borrower": 714757691636,
        "image": 'ring.png',
        "time": datetime.datetime.now()  
    },
    {
        "id": 20,
        "title": "Scary Movie 5",
        "status": "not available",
        "borrower": 714757691636,
        "image": 'hobbit.png',
        "time": datetime.datetime.now()  
    }
],
'Biography': [
    {
        "id": 21,
        "title": "Tesla",
        "status": "available",
        "borrower": None,
        "image": 'ship.png',
        "time": datetime.datetime.now()  
    },
    {
        "id": 22,
        "title": "Newton",
        "status": "not available",
        "borrower": 928285915686,
        "image": 'ring.png',
        "time": datetime.datetime.now()  
    },
    {
        "id": 23,
        "title": "Einstein",
        "status": "available",
        "borrower": None,
        "image": 'hobbit.png',
        "time": datetime.datetime.now()  
    },
    {
        "id": 24,
        "title": "Ronaldo",
        "status": "not available",
        "borrower": 928285915686,
        "image": 'treasure.png',
        "time": datetime.datetime.now()  
    },
    {
        "id": 25,
        "title": "Messi",
        "status": "available",
        "borrower": None,
        "image": 'hobbit.png',
        "time": datetime.datetime.now()  
    }
],
'History': [
    {
        "id": 26,
        "title": "Columbus",
        "status": "available",
        "borrower": None,
        "image": 'treasure.png',
        "time": datetime.datetime.now()  
    },
    {
        "id": 27,
        "title": "World Wat II",
        "status": "not available",
        "borrower": 714757691636,
        "image": 'ship.png',
        "time": datetime.datetime.now()  
    },
    {
        "id": 28,
        "title": "Medival Times",
        "status": "available",
        "borrower": None,
        "image": 'hobbit.png',
        "time": datetime.datetime.now()  
    },
    {
        "id": 29,
        "title": "Ancient Egypt",
        "status": "not available",
        "borrower": 928285915686,
        "image": 'ship.png',
        "time": datetime.datetime.now()  
    },
    {
        "id": 30,
        "title": "Aztecs",
        "status": "available",
        "borrower": None,
        "image": 'treasure.png',
        "time": datetime.datetime.now()  
    }
]
}"""

rfid = RfidReader()
with open('books.json', 'r') as file:
    books = json.load(file)
    for type in books.values():
        for film in type:
            tempStr = film['time']
            film['time'] = datetime.datetime.strptime(tempStr, '%Y-%m-%d %H:%M:%S.%f')
"""books = data"""









class LibraryApp(ctk.CTk):
    def __init__(self):
        super().__init__()


        self.title("Library System")
        self.geometry("500x450")

        ctk.set_appearance_mode("dark")

        self.available_img = ImageTk.PhotoImage(Image.new("RGB", (20, 20), "green"))
        self.unavailable_img = ImageTk.PhotoImage(Image.new("RGB", (20, 20), "red"))

        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        self.show_main_view()

    def show_main_view(self):
        for widget in self.container.winfo_children():
            widget.destroy()
        self.geometry("500x450")

        title = ctk.CTkLabel(self.container, text="Library System", font=("Arial", 18))
        title.pack(pady=20)

        show_categories_btn = ctk.CTkButton(self.container, 
            text="Show categories", 
            height=50, width=250, 
            font=("Arial Bold", 16), 
            corner_radius=25, 
            fg_color="#0078D7",
            hover_color="#0056A3",
            command=self.show_categories_view)
        show_categories_btn.pack(pady=5)

        check_books_btn = ctk.CTkButton(self.container, text="Check Lent Books", command=self.check_lent_books, height=40, width=250, corner_radius=20, fg_color="#0078D7")
        check_books_btn.pack(pady=5)

        save_books_btn = ctk.CTkButton(self.container, text="Save data", command=self.save_data_to_json, height=20, width=150, corner_radius=20, fg_color="#0078D7")
        save_books_btn.pack(side="bottom", pady=5)

        

    def show_categories_view(self):
        for widget in self.container.winfo_children():
            widget.destroy()

        title = ctk.CTkLabel(self.container, text="Book Categories", font=("Arial", 18))
        title.pack(pady=10)

        for category in CATEGORIES:
            btn = ctk.CTkButton(self.container, text=category, command=lambda c=category: self.show_books_in_category(c), height=40, width=250, corner_radius=20, fg_color="#0078D7")
            btn.pack(pady=5)

        back_btn = ctk.CTkButton(self.container, text="Back", fg_color='red', command=self.show_main_view, height=40, width=250, corner_radius=20)
        back_btn.pack(pady=10)

    def show_books_in_category(self, category):
        for widget in self.container.winfo_children():
            widget.destroy()

        title = ctk.CTkLabel(self.container, text=f"Books in {category}", font=("Arial", 18))
        title.pack(pady=10)

        books_in_category = books[category]

        for book in books_in_category:
            frame = ctk.CTkFrame(self.container)
            frame.pack(fill="x", pady=5, padx=10)

           
            book_btn = ctk.CTkButton(frame, text=book["title"], fg_color="transparent", text_color="white",
                                     command=lambda b=book: self.show_book_detail(b, category), anchor='w')
            book_btn.pack(side="left", padx=10)

            img_label = ctk.CTkLabel(frame, image=self.available_img if book["borrower"]==None else self.unavailable_img, text="")
            img_label.pack(side="right", padx=10)

        back_btn = ctk.CTkButton(self.container, text="Back", command=self.show_categories_view)
        back_btn.pack(pady=10)






    def show_book_detail(self, book, category):
            for widget in self.container.winfo_children():
                widget.destroy()

            

            title = ctk.CTkLabel(self.container, text=book["title"], font=("Arial", 18))
            title.pack(pady=10)

            img = Image.open(book['image']).resize((80, 100))
            self.img = ImageTk.PhotoImage(img) 
            img_label = ctk.CTkLabel(self.container, image=self.img, text="")  
            img_label.pack(pady=10)

            availability_text = "Status: " + book['status']
            availability_label = ctk.CTkLabel(self.container, text=availability_text, font=("Arial", 14))
            availability_label.pack(pady=5)

            owner_text = 'Current owner: ' + (str(book['borrower']) if book['borrower']!=None else 'does not exist')
            owner_label = ctk.CTkLabel(self.container, text=owner_text, font=("Arial", 14))
            owner_label.pack(pady=5)

            if book['borrower']==None:
                lend_button = ctk.CTkButton(self.container, text='Lend', command=lambda: self.lend(book, category), height=40, width=200, corner_radius=20, fg_color="green")
                lend_button.pack(pady=5)
            else:
                giveback_button = ctk.CTkButton(self.container, text='Return', command=lambda: self.giveback(book, category), height=40, width=200, corner_radius=20, fg_color="green")
                giveback_button.pack(pady=5)

            back_btn = ctk.CTkButton(self.container, text="Back", command=lambda: self.show_books_in_category(category), height=40, width=200, corner_radius=20, fg_color="red")
            back_btn.pack(pady=10)


    def lend(self, book, category):
        rfid.detect_card_once()
        value = rfid.value
        book['borrower'] = value
        book['status'] = 'not available'
        book['time'] = datetime.datetime.now()
        for widget in self.container.winfo_children():
            widget.destroy()
        self.show_book_detail(book, category)


    def giveback(self, book, category):
        rfid.detect_card_once()
        value = rfid.value
        if book['borrower']!=value:
            for widget in self.container.winfo_children():
                widget.destroy()
            self.show_book_detail(book, category)
            print("You are not the owner")
        else:
            book['borrower'] = None
            book['status'] = 'available'
            for widget in self.container.winfo_children():
                widget.destroy()
            self.show_book_detail(book, category)
            print(f"You returned {book['title']}")
            print(f"You had the book for {datetime.datetime.now() - book['time']}")









    def check_lent_books(self):
        for widget in self.container.winfo_children():
                widget.destroy()

        self.geometry("500x600")
        title = ctk.CTkLabel(self.container, text='Place your card and check what books you have lent:', font=("Arial", 18))
        title.pack(pady=10)

        rfid.detect_card_once()
        value = rfid.value

        borrowed = getBooks(value)

        for book in borrowed:
            frame = ctk.CTkFrame(self.container)
            frame.pack(fill="x", pady=5, padx=10)

            wholeMessage = "You own this book for: " + str(datetime.datetime.now()-book['time'])

            book_btn = ctk.CTkLabel(frame, text=book["title"], fg_color="transparent", text_color="white")
            book_btn.pack(side="left", padx=10)

            date_btn = ctk.CTkLabel(frame, text=wholeMessage, fg_color="transparent", text_color="white")
            date_btn.pack(side="left", padx=10)
           
            img_label = ctk.CTkLabel(frame, image=self.available_img if book["borrower"]==None else self.unavailable_img, text="")
            img_label.pack(side="right", padx=10)

        back_btn = ctk.CTkButton(self.container, text="Back", command=self.show_main_view, height=40, width=200, corner_radius=20, fg_color="red")
        back_btn.pack(pady=10) 

    def save_data_to_json(self):
        with open('books.json', 'w') as f:
            json.dump(books, f, default=str)
        print("Data saved to JSON file")

    

def getBooks(UID):
    borrowed = []
    for category in CATEGORIES:
         for book in books[category]:
              if book['borrower']==UID:
                   borrowed.append(book)

    return borrowed


if __name__ == "__main__":
    app = LibraryApp()
    app.mainloop()
