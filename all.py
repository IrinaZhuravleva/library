import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2
from PIL import Image, ImageTk

# Функция для выполнения запроса и получения списка книг
def fetch_books():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="myuser",
            password="mypassword",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT book_id, title, author_id, status_id FROM book")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except psycopg2.Error as e:
        print("Ошибка при подключении к базе данных:", e)
        return []

# Функция для получения списка статусов
def fetch_statuses():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="myuser",
            password="mypassword",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT status_id, name_status FROM status")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except psycopg2.Error as e:
        print("Ошибка при подключении к базе данных:", e)
        return []

# Функция для удаления книги
def delete_book(book_id):
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="myuser",
            password="mypassword",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        cursor.execute("DELETE FROM book WHERE book_id = %s", (book_id,))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Информация", "Книга успешно удалена!")
        show_books_page()
    except psycopg2.Error as e:
        print("Ошибка при удалении книги:", e)
        messagebox.showerror("Ошибка", "Не удалось удалить книгу.")

# Функция для изменения статуса книги
def change_book_status(book_id, new_status):
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="myuser",
            password="mypassword",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        cursor.execute("UPDATE books SET status = %s WHERE book_id = %s", (new_status, book_id))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Информация", "Статус книги успешно обновлен!")
        show_books_page()
    except psycopg2.Error as e:
        print("Ошибка при обновлении статуса книги:", e)
        messagebox.showerror("Ошибка", "Не удалось обновить статус книги.")

# Функция для перехода на главную страницу
def show_main_page():
    frame_books.pack_forget()
    frame_main.pack(fill='both', expand=True)

# Функция для перехода на страницу с книгами
def show_books_page():
    frame_main.pack_forget()
    for widget in frame_books.winfo_children():
        widget.destroy()

    books = fetch_books()
    statuses = fetch_statuses()

    # Заголовок страницы
    label_title = tk.Label(frame_books, text="Список книг", font=("Helvetica", 16), bg='white')
    label_title.grid(row=0, column=0, columnspan=5, pady=10)

    # Заголовки таблицы
    headers = ["ID", "Название", "Автор", "Статус", "Действия"]
    for idx, header in enumerate(headers):
        tk.Label(frame_books, text=header, font=("Helvetica", 12, "bold"), bg='white').grid(row=1, column=idx, padx=5, pady=5)

    # Отображение книг
    for i, book in enumerate(books, start=2):
        book_id, title, author, status_id = book
        tk.Label(frame_books, text=str(book_id), bg='white').grid(row=i, column=0, padx=5, pady=5)
        tk.Label(frame_books, text=title, bg='white').grid(row=i, column=1, padx=5, pady=5)
        tk.Label(frame_books, text=author, bg='white').grid(row=i, column=2, padx=5, pady=5)

        # Отображение текущего статуса книги
        status_name = next((name for id_, name in statuses if id_ == status_id), "Unknown")
        tk.Label(frame_books, text=status_name, bg='white').grid(row=i, column=3, padx=5, pady=5)

        # Кнопка удаления
        btn_delete = tk.Button(frame_books, text="Удалить", command=lambda book_id=book_id: delete_book(book_id))
        btn_delete.grid(row=i, column=4, padx=5, pady=5)

        # Кнопка изменения статуса
        btn_change_status = tk.Button(frame_books, text="Изменить статус", command=lambda book_id=book_id: open_status_change_window(book_id))
        btn_change_status.grid(row=i, column=5, padx=5, pady=5)

    # Кнопка возврата на главную страницу
    btn_back = tk.Button(frame_books, text="Назад", command=show_main_page)
    btn_back.grid(row=len(books) + 2, column=0, columnspan=5, pady=10)

    frame_books.pack(fill='both', expand=True)

# Открывает окно для изменения статуса книги
def open_status_change_window(book_id):
    status_window = tk.Toplevel(root)
    status_window.title("Изменение статуса книги")
    status_window.geometry("300x150")

    tk.Label(status_window, text="Выберите новый статус:").pack(pady=10)

    statuses = fetch_statuses()
    status_var = tk.StringVar(value=statuses[0][1])

    for status_id, status_name in statuses:
        tk.Radiobutton(status_window, text=status_name, variable=status_var, value=status_name).pack(anchor='w')

    def on_status_change():
        new_status_name = status_var.get()
        new_status_id = next((id_ for id_, name in statuses if name == new_status_name), None)
        if new_status_id:
            change_book_status(book_id, new_status_id)
        status_window.destroy()

    btn_confirm = tk.Button(status_window, text="Подтвердить", command=on_status_change)
    btn_confirm.pack(pady=10)

# Создание главного окна
root = tk.Tk()
root.title("Tkinter Buttons Example")
root.minsize(600, 400)

# Загрузка изображения для фона
image = Image.open("background.jpg")
background_image = ImageTk.PhotoImage(image)

# Фрейм для главного меню
frame_main = tk.Frame(root)
frame_main.pack(fill='both', expand=True)

# Фрейм для отображения книг
frame_books = tk.Frame(root)

# Создание Canvas для размещения фона и виджетов
canvas_main = tk.Canvas(frame_main, width=600, height=400)
canvas_main.pack(fill="both", expand=True)

# Установка изображения в качестве фона
canvas_main.create_image(0, 0, image=background_image, anchor="nw")

# Создание первой кнопки для перехода на страницу с книгами
button1 = tk.Button(frame_main, text="Fetch Books", width=15, height=5, command=show_books_page)
button1_window = canvas_main.create_window(150, 150, window=button1)

# Создание второй кнопки (например, для будущих функций)
button2 = tk.Button(frame_main, text="Button 2", width=15, height=5)
button2_window = canvas_main.create_window(450, 150, window=button2)

# Настройка сетки фрейма для центрирования
frame_main.update_idletasks()
frame_width = frame_main.winfo_width()
frame_height = frame_main.winfo_height()
root.geometry(f"{frame_width}x{frame_height}+{(root.winfo_screenwidth() - frame_width) // 2}+{(root.winfo_screenheight() - frame_height) // 2}")

# Запуск главного цикла обработки событий
root.mainloop()
