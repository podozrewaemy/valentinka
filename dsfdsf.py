import tkinter as tk
import math
import time

# Создаем окно
root = tk.Tk()
root.title("Валентинка")
canvas = tk.Canvas(root, width=400, height=400, bg='pink')
canvas.pack()

# Функция для рисования сердца
def draw_heart(size, x_center, y_center):
    points = []
    for angle in range(0, 360, 5):  # Используем угол от 0 до 360 градусов
        t = math.radians(angle)
        x = size * 16 * math.sin(t)**3
        y = -size * (13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
        points.append(x + x_center)
        points.append(y + y_center)
    return points

# Рисуем сердце
heart_id = None

# Функция для анимации пульсации сердца
def pulse_heart():
    global heart_id
    sizes = [i / 10 for i in range(8, 12)] + [i / 10 for i in range(12, 8, -1)]
    while True:
        for size in sizes:
            new_coords = draw_heart(size * 10, 200, 200)
            if heart_id is None:
                heart_id = canvas.create_polygon(new_coords, fill='red', outline='darkred')
            else:
                canvas.coords(heart_id, new_coords)
            canvas.update()
            time.sleep(0.05)

# Текст "Я тебя люблю"
text = canvas.create_text(200, 350, text="Я тебя люблю", font=("Helvetica", 24, "bold"), fill="white")

# Запускаем анимацию
pulse_heart_thread = root.after(100, pulse_heart)

# Показываем сообщение
message = canvas.create_text(200, 380, text="С Днем Святого Валентина!", font=("Helvetica", 12), fill="white")

# Запускаем главный цикл
root.mainloop()