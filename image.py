from PIL import Image, ImageTk
import tkinter as tk

# Создаем основное окно
root = tk.Tk()
root.title("Tkinter Image Example")

# Задаем размеры окна
window_width = 600
window_height = 400
root.geometry(f"{window_width}x{window_height}")

# Загружаем изображение и изменяем его размер
original_image = Image.open("1.png")
resized_image = original_image.resize((window_width, window_height), Image.Resampling.LANCZOS)
background_image = ImageTk.PhotoImage(resized_image)

# Создаем фрейм
frame_main = tk.Frame(root)
frame_main.pack(fill='both', expand=True)

# Создаем Canvas для размещения фона и виджетов
canvas_main = tk.Canvas(frame_main, width=window_width, height=window_height)
canvas_main.pack(fill="both", expand=True)

# Устанавливаем изображение в качестве фона
canvas_main.create_image(0, 0, image=background_image, anchor="nw")

# Пример добавления кнопки на Canvas
button1 = tk.Button(frame_main, text="Fetch Books", width=15, height=5)
canvas_main.create_window(window_width // 2 - 75, window_height // 2, window=button1)

root.mainloop()
