from tkinter import *
import math
import pyttsx3
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
root = Tk()
root.geometry("1200x700")
root.title("Алгебраист")

def typewriter(label, text, delay=50):
    """Выводит текст в label по одному символу с задержкой."""
    # Очищаем label перед началом анимации
    label.config(text="")
    if int(len(text)) % 2 == 1:
        text = text + " "

    def _typewriter(index=0):
        if index < len(text):
            # Устанавливаем текст от начала до текущего индекса
            current_text = text[:index + 2]
            label.config(text=current_text)
            # Планируем следующий вызов
            label.after(delay, _typewriter, index + 2)


    # Запускаем процесс
    _typewriter(0)
def error(Frame):
    for widget in Frame.winfo_children():
        widget.destroy()

# Овечает за голос
def voice(result):
    try:
        text = str(result)
        text = text.replace('=', ' равно ')
        text = text.replace('+', ' плюс ')
        text = text.replace('-', ' минус ')
        text = text.replace('x', ' икс')
        text = text.replace('*', ' умножить на ')
        text = text.replace('/', ' разделить на ')
        text = text.replace('a', ' а ')
        text = text.replace('b', ' б ')
        text = text.replace('c', ' ц ')
        text = text.replace('^2', ' в квадрате ')
        text = text.replace('√', ' квадратный корень из ')
        text = text.replace('≥', ' больше либо равен чем ')
        text = text.replace('≤', ' меньше либо равен чем ')
        text = text.replace('∈', ' принадлежит ')
        text = text.replace('∪', ' объединение ')
        text = text.replace('∞', '  бесконечности ')
        text = text.replace('[', ' от ')
        text = text.replace('(', ' от ')
        text = text.replace(';', ' до ')
        text = text.replace('0.', ' ноль целых ')
        text = text.replace('.', ' точка ')
        text = text.replace('ℝ', ' множеству действительных чисел ')

        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 200)
        engine.setProperty('volume', 1)
        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print(f"Ошибка синтеза речи: {e}")


# Отвечает за решение линейного уравнения
def lin_ur_decide_2(a, b):
    try:
        a, b = float(a), float(b)
        if a - int(a) == 0 and b - int(b) == 0:
            a, b = int(a), int(b)
        if a - int(a) == 0 and b - int(b) == 0:
            a = int(a)
            b = int(b)
        if a == 0 and b == 0:
            result = f"Ответ: x  любое число"
            result_2 = (
                f"Ответ: x  любое число\n  \nПояснение:\n1)Подставим a = 0 и b = 0.\n2)Получим уравнение вида 0x = 0.\n3)"
                f"Попробуем подставить любые значения x и увидим что всё равно получается 0.\n4)Получается, что "
                f"x  лбюое число.")
        elif a == 0:
            result = f"Ответ: нет корней"
            result_2 = (
                f"Ответ: нет корней\n  \nПояснение:\n1)Подставим a = 0 и b = {b}\n2)Получим уравнение вида 0x = {-b}.\n3)При "
                f"любом значении x левая часть уравнения будет равна нулю и никогда не будет равна {-b}.\n4)Нет "
                f"корней.")

        else:
            x1 = -b / a
            result = f"Ответ: x = {x1:.6f}"
            result_2 = (
                f"Ответ: x = {x1:.6f}\n   \nПояснение:\n1)Подставим a = {a} и b = {b}\n2)Получим уравнение вида {a}x = {-b} "
                f"\n3)Поделим обе части уравнения на {a}\n4)Получим , что x = {-b}/{a}\n5)Получается, что x = {x1:.6f}")
    except ValueError:
        result = "Ошибка: введите все числовые значения"
    error(frame_answer)
    result = result.replace(".000000", "")
    Label_answer = Label(frame_answer, text="", font=("Arial", 12), bg="white", justify='left')
    Label_answer.pack(side="left", anchor="nw")
    typewriter(Label_answer, result, delay=50)
    Button_voice = Button(frame_answer, text="Произнести голосом", bg="orange", command=lambda: voice(result))
    Button_voice.pack(side="right")

    def help(f):
        error(frame_answer)
        f = f.replace(".000000", "")
        Label_answer = Label(frame_answer, text="", font=("Arial", 12), bg="white", justify='left')
        Label_answer.pack(side="left", anchor="nw")
        typewriter(Label_answer, f, delay=50)
        Button_voice = Button(frame_answer, text="Произнести голосом", bg="orange", command=lambda: voice(f))
        Button_voice.pack(side="right")
        Button_answer_not = Button(frame_answer, text="Убрать пояснение", bg="orange",
                                   command=lambda: lin_ur_decide_2(a, b))
        Button_answer_not.pack(side="right")

    Button_answer = Button(frame_answer, text="Пояснение", bg="orange", command=lambda: help(result_2))
    Button_answer.pack(side="right")
    Button_ark = Button(frame_answer, text="Округленные значения   значения x", bg="orange",
                        command=lambda: lin_ur_decide(a, b))
    Button_ark.pack(side="right")


def lin_ur_decide(a, b):
    try:
        a, b = float(a), float(b)
        if a - int(a) == 0 and b - int(b) == 0:
            a, b = int(a), int(b)
        if a == 0 and b == 0:
            result = f"Ответ: x  любое число"
            result_2 = (
                f"Ответ: x  любое число\n  \nПояснение:\n1)Подставим a = 0 и b = 0.\n2)Получим уравнение вида 0x = 0.\n3)"
                f"Попробуем подставить любые значения x и увидим что всё равно получается 0.\n4)Получается, что "
                f"x  лбюое число.")
        elif a == 0:
            result = f"Ответ: нет корней"
            result_2 = (
                f"Ответ: нет корней\n  \nПояснение:\n1)Подставим a = 0 и b = {b}\n2)Получим уравнение вида 0x = {-b}.\n3)При "
                f"любом значении x левая часть уравнения будет равна нулю и никогда не будет равна {-b}.\n4)Нет "
                f"корней.")

        else:
            x1 = -b / a
            result = f"Ответ: x = {x1:.3f}"
            result_2 = (
                f"Ответ: x = {x1:.3f}\n   \nПояснение:\n1)Подставим a = {a} и b = {b}\n2)Получим уравнение вида {a}x = {-b} "
                f"\n3)Поделим обе части уравнения на {a}\n4)Получим , что x = {-b}/{a}\n5)Получается, что x = {x1:.3f}")
    except ValueError:
        result = "Ошибка: введите все числовые значения"
    error(frame_answer)
    result = result.replace(".000", "")
    Label_answer = Label(frame_answer, text="", font=("Arial", 12), bg="white", justify='left')
    Label_answer.pack(side="left", anchor="nw")
    typewriter(Label_answer, result, delay=50)
    Button_voice = Button(frame_answer, text="Произнести голосом", bg="orange", command=lambda: voice(result))
    Button_voice.pack(side="right")

    def help(g):
        error(frame_answer)
        g = g.replace(".000", "")
        Label_answer = Label(frame_answer, text="", font=("Arial", 12), bg="white", justify='left')
        Label_answer.pack(side="left", anchor="nw")
        typewriter(Label_answer, g, delay=50)
        Button_voice = Button(frame_answer, text="Произнести голосом", bg="orange", command=lambda: voice(g))
        Button_voice.pack(side="right")
        Button_answer_not = Button(frame_answer, text="Убрать пояснение", bg="orange",
                                   command=lambda: lin_ur_decide(a, b))
        Button_answer_not.pack(side="right")

    Button_answer = Button(frame_answer, text="Пояснение", bg="orange", command=lambda: help(result_2))
    Button_answer.pack(side="right")
    Button_ark = Button(frame_answer, text="Более точные значения x", bg="orange",
                        command=lambda: lin_ur_decide_2(a, b))
    Button_ark.pack(side="right")


# Отвечает за решение квадратного уравнения
def quar_ur_decide_2(a, b, c):
    try:
        error(frame_answer)
        a, b, c = float(a), float(b), float(c)
        if a - int(a) == 0 and b - int(b) == 0 and c - int(c) == 0:
            a, b, c = int(a), int(b), int(c)
        if a - int(a) == 0 and b - int(b) == 0 and c - int(c) == 0:
            a = int(a)
            b = int(b)
            c = int(c)
        if a == 0:
            result = "Ответ: это не квадратное уравнеие"
            result_2 = (
                "Ответ: это не квадратное уравнеие\n \nПояснение:\n1)Квадратное уравнение имеет вид ax^2 + bx + c,"
                " где a не равно нулю\n2)Так как a равно нулю то это уже не квадратное уравнение")
        else:
            D = b ** 2 - 4 * a * c
            if D > 0:
                x1 = (-b + math.sqrt(D)) / (2 * a)
                x2 = (-b - math.sqrt(D)) / (2 * a)
                result = f"Ответ: x = {x1:.6f} и x = {x2:.6f}"
                result_2 = (
                    f"Ответ: x = {x1:.6f} и x = {x2:.6f}\n \nПояснение:\n1)Сначала найдем дискриминант уравнения"
                    f"({a})x^2 {b}x {c}\n2)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n3)Найдем первый корень "
                    f"по формуле x = (-b + √D) / (2 * a) = ({-b} + √{D}) / (2 * {a}) = {x1:.6f}\n4)Найдем второй "
                    f"корень по формуле x = (-b - √D) / (2 * a) = ({-b} - √{D}) / (2 * {a}) = {x2:.6f}\n5)Следовате"
                    f"льно корни уравнения x = {x1:.6f} и x = {x2:.6f}")
            elif D == 0:
                x1 = -b / (2 * a)
                result = f"Ответ: x = {x1:.6f}"
                result_2 = (f"Ответ: x = {x1:.6f}\n \nПояснение:\n1)Сначала найдем дискриминант уравнения"
                            f"({a})x^2 + {b}x + {c}\n2)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = 0\n3)Так как дискриминант "
                            f"равен нулю, то данное уравнение имеет только один корень\n4)Найдем его по формуле "
                            f"x = (-b + 0) / (2 * a) = ({-b} + √0) / (2 * {a}) = {x1:.6f}\n5)Следователно корень "
                            f"уравнения x = {x1:.6f}")
            else:
                result = "Ответ: нет корней"
                result_2 = (f"Ответ: нет корней\n \nПояснение:\n1)Сначала найдем дискриминант уравнения "
                            f"({a})x^2 + {b}x + {c}\n2)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n3)Так как дискриминант "
                            f"меньше нуля, то данное уравнение не имеет действительных корней\n4)Следовательно нет корней")
    except ValueError:
        result = "Ошибка: введите все числовые значения"
    error(frame_answer)
    result = result.replace(".000000", "")
    Label_answer = Label(frame_answer, text="", font=("Arial", 12), bg="white", justify='left')
    Label_answer.pack(side="left", anchor="nw")
    typewriter(Label_answer, result, delay=50)
    Button_voice = Button(frame_answer, text="Произнести голосом", bg="orange", command=lambda: voice(result))
    Button_voice.pack(side="right")

    def help(f):
        error(frame_answer)
        f = f.replace(".000000", "")
        Label_answer = Label(frame_answer, text="", font=("Arial", 12), bg="white", justify='left')
        Label_answer.pack(side="left", anchor="nw")
        typewriter(Label_answer, f, delay=50)
        Button_voice = Button(frame_answer, text="Произнести голосом", bg="orange", command=lambda: voice(f))
        Button_voice.pack(side="right")
        Button_answer_not = Button(frame_answer, text="Убрать пояснение", bg="orange",
                                   command=lambda: quar_ur_decide_2(a, b, c))
        Button_answer_not.pack(side="right")

    Button_answer = Button(frame_answer, text="Пояснение", bg="orange", command=lambda: help(result_2))
    Button_answer.pack(side="right")
    Button_ark = Button(frame_answer, text="Округлённые  значения x", bg="orange",
                        command=lambda: quar_ur_decide(a, b, c))
    Button_ark.pack(side="right")


def quar_ur_decide(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)
        if a - int(a) == 0 and b - int(b) == 0 and c - int(c) == 0:
            a, b, c = int(a), int(b), int(c)
        if a == 0:
            result = "Ответ: это не квадратное уравнеие"
            result_2 = (
                "Ответ: это не квадратное уравнеие\n \nПояснение:\n1)Квадратное уравнение имеет вид ax^2 + bx + c,"
                " где a не равно нулю\n2)Так как a равно нулю то это уже не квадратное уравнение")
        else:
            D = b ** 2 - 4 * a * c
            if D > 0:
                x1 = (-b + math.sqrt(D)) / (2 * a)
                x2 = (-b - math.sqrt(D)) / (2 * a)
                result = f"Ответ: x = {x1:.3f} и x = {x2:.3f}"
                result_2 = (
                    f"Ответ: x = {x1:.3f} и x = {x2:.3f}\n \nПояснение:\n1)Сначала найдем дискриминант уравнения "
                    f"({a})x^2 + {b}x + {c}\n2)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n3)Найдем первый корень "
                    f"по формуле x = (-b + √D) / (2 * a) = ({-b} + √{D}) / (2 * {a}) = {x1:.3f}\n4)Найдем второй "
                    f"корень по формуле x = (-b - √D) / (2 * a) = ({-b} - √{D}) / (2 * {a}) = {x2:.3f}\n5)Следовате"
                    f"льно корни уравнения x = {x1:.3f} и x = {x2:.3f}")
            elif D == 0:
                x1 = -b / (2 * a)
                result = f"Ответ: x = {x1:.3f}"
                result_2 = (f"Ответ: x = {x1:.3f}\n \nПояснение:\n1)Сначала найдем дискриминант уравнения "
                            f"({a})x^2 + {b}x + {c}\n2)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = 0\n3)Так как дискриминант "
                            f"равен нулю, то данное уравнение имеет только один корень\n4)Найдем его по формуле "
                            f"x = (-b + 0) / (2 * a) = ({-b} + √0) / (2 * {a}) = {x1:.3f}\n5)Следователно корень "
                            f"уравнения x = {x1:.3f}")
            else:
                result = "Ответ: нет корней"
                result_2 = (f"Ответ: нет корней\n \nПояснение:\n1)Сначала найдем дискриминант уравнения"
                            f"({a})x^2 + {b}x + {c}\n2)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n3)Так как дискриминант "
                            f"меньше нуля, то данное уравнение не имеет действительных корней\n4)Следовательно нет корней")
    except ValueError:
        result = "Ошибка: введите все числовые значения"
    error(frame_answer)
    result = result.replace(".000", "")
    Label_answer = Label(frame_answer, text="", font=("Arial", 12), bg="white", justify='left')
    Label_answer.pack(side="left", anchor="nw")
    typewriter(Label_answer, result, delay=50)
    Button_voice = Button(frame_answer, text="Произнести голосом", bg="orange", command=lambda: voice(result))
    Button_voice.pack(side="right")

    def help(g):
        error(frame_answer)
        g = g.replace(".000", "")
        Label_answer = Label(frame_answer, text="", font=("Arial", 12), bg="white", justify='left')
        Label_answer.pack(side="left", anchor="nw")
        typewriter(Label_answer, g, delay=50)
        Button_voice = Button(frame_answer, text="Произнести голосом", bg="orange", command=lambda: voice(g))
        Button_voice.pack(side="right")
        Button_answer_not = Button(frame_answer, text="Убрать пояснение", bg="orange",
                                   command=lambda: quar_ur_decide(a, b, c))
        Button_answer_not.pack(side="right")

    Button_answer = Button(frame_answer, text="Пояснение", bg="orange", command=lambda: help(result_2))
    Button_answer.pack(side="right")
    Button_ark = Button(frame_answer, text="Более точные значения x", bg="orange",
                        command=lambda: quar_ur_decide_2(a, b, c))
    Button_ark.pack(side="right")


# Отвечает за решение линейного неравенства

def lin_nerve_decide_2(a, b, var):
    try:
        a, b = float(a), float(b)
        if a - int(a) == 0 and b - int(b) == 0:
            a, b = int(a), int(b)
        if a == 0:
            if var == ">" and b > 0:
                result = "Ответ: x  любое число"
                result_2 = (
                    f"Ответ: x  любое число\n \nПояснение:\n1)Подставим a = 0 и b = {b}\n2)Получим неравентсво "
                    f"вида 0x + {b} > 0\n3)Мы видим, что при любом значении x, всегда {b} > 0\n4)Следовательно "
                    f"x  любое число")
            elif var == ">=" and b >= 0:
                result = "Ответ: x  любое число"
                result_2 = (
                    f"Ответ: x  любое число\n \nПояснение:\n1)Подставим a = 0 и b = {b}\n2)Получим неравентсво "
                    f"вида 0x + {b} ≥ 0\n3)Мы видим, что при любом значении x, всегда {b} ≥ 0\n4)Следовательно "
                    f"x  любое число")
            elif var == "<" and b < 0:
                result = "Ответ: x  любое число"
                result_2 = (
                    f"Ответ: x  любое число\n \nПояснение:\n1)Подставим a = 0 и b = {b}\n2)Получим неравентсво "
                    f"вида 0x + {b} < 0\n3)Мы видим, что при любом значении x, всегда {b} < 0\n4)Следовательно "
                    f"x  любое число")
            elif var == "<=" and b <= 0:
                result = "Ответ: x  любое число"
                result_2 = (
                    f"Ответ: x  любое число\n \nПояснение:\n1)Подставим a = 0 и b = {b}\n2)Получим неравентсво "
                    f"вида 0x + {b} ≤ 0\n3)Мы видим, что при любом значении x, всегда {b} ≤ 0\n4)Следовательно "
                    f"x  любое число")
            else:
                result = "Ответ: нет решений"
                result_2 = (
                    f"Ответ: нет решений\n \nПояснение:\n1)Подставим a = 0 и b = {b}\n2)Получим неравентсво "
                    f"вида 0x + {b} {var} 0\n3)Мы видим, что при любом значении x, никогда не будет {b} {var} 0\n4)Следовательно "
                    f"нет решений")
        else:
            x1 = -b / a
            if a > 0:
                if var == ">":
                    result = f"Ответ: x > {x1:.6f}"
                    result_2 = (f"Ответ: x > {x1:.6f}\n \nПояснение:\n1)Подставим a = {a} и b = {b}\n2)Получим "
                                f"неравенство вида {a}x > {-b}\n3)Поделим обе части неравенства на {a}\n4)Получим, что "
                                f"x > {-b}/{a}\n5)Следовательно x > {x1:.6f}")
                elif var == ">=":
                    result = f"Ответ: x ≥ {x1:.6f}"
                    result_2 = (f"Ответ: x ≥ {x1:.6f}\n \nПояснение:\n1)Подставим a = {a} и b = {b}\n2)Получим "
                                f"неравенство вида {a}x ≥ {-b}\n3)Поделим обе части неравенства на {a}\n4)Получим, что "
                                f"x ≥ {-b}/{a}\n5)Следовательно x ≥ {x1:.6f}")
                elif var == "<":
                    result = f"Ответ: x < {x1:.6f}"
                    result_2 = (f"Ответ: x < {x1:.6f}\n \nПояснение:\n1)Подставим a = {a} и b = {b}\n2)Получим "
                                f"неравенство вида {a}x < {-b}\n3)Поделим обе части неравенства на {a}\n4)Получим, что "
                                f"x < {-b}/{a}\n5)Следовательно x < {x1:.6f}")
                elif var == "<=":
                    result = f"Ответ: x ≤ {x1:.6f}"
                    result_2 = (f"Ответ: x ≤ {x1:.6f}\n \nПояснение:\n1)Подставим a = {a} и b = {b}\n2)Получим "
                                f"неравенство вида {a}x ≤ {-b}\n3)Поделим обе части неравенства на {a}\n4)Получим, что "
                                f"x ≤ {-b}/{a}\n5)Следовательно x ≤ {x1:.6f}")
            else:
                if var == ">":
                    result = f"Ответ: x < {x1:.6f}"
                    result_2 = (f"Ответ: x < {x1:.6f}\n \nПояснение:\n1)Подставим a = {a} и b = {b}\n2)Получим "
                                f"неравенство вида {a}x > {-b}\n3)Поделим обе части неравенства на {a} и поменяем знак на противоположный\n4)Получим, что "
                                f"x < {-b}/{a}\n5)Следовательно x < {x1:.6f}")
                elif var == ">=":
                    result = f"Ответ: x ≤ {x1:.6f}"
                    result_2 = (f"Ответ: x ≤ {x1:.6f}\n \nПояснение:\n1)Подставим a = {a} и b = {b}\n2)Получим "
                                f"неравенство вида {a}x ≥ {-b}\n3)Поделим обе части неравенства на {a} и поменяем знак на противоположный\n4)Получим, что "
                                f"x ≤ {-b}/{a}\n5)Следовательно x ≤ {x1:.6f}")
                elif var == "<":
                    result = f"Ответ: x > {x1:.6f}"
                    result_2 = (f"Ответ: x > {x1:.6f}\n \nПояснение:\n1)Подставим a = {a} и b = {b}\n2)Получим "
                                f"неравенство вида {a}x < {-b}\n3)Поделим обе части неравенства на {a} и поменяем знак на противоположный\n4)Получим, что "
                                f"x > {-b}/{a}\n5)Следовательно x > {x1:.6f}")
                elif var == "<=":
                    result = f"Ответ: x ≥ {x1:.6f}"
                    result_2 = (f"Ответ: x ≥ {x1:.6f}\n \nПояснение:\n1)Подставим a = {a} и b = {b}\n2)Получим "
                                f"неравенство вида {a}x ≤ {-b}\n3)Поделим обе части неравенства на {a} и поменяем знак на противоположный\n4)Получим, что "
                                f"x ≥ {-b}/{a}\n5)Следовательно x ≥ {x1:.6f}")
    except ValueError:
        result = "Введите все числовые значения"
    error(frame_answer)
    result = result.replace(".000000", "")
    Label_answer = Label(frame_answer, text="", font=("Arial", 12), bg="white", justify='left')
    Label_answer.pack(side="left", anchor="nw")
    typewriter(Label_answer, result, delay=50)
    Button_voice = Button(frame_answer, text="Произнести голосом", bg="orange", command=lambda: voice(result))
    Button_voice.pack(side="right")

    def help(f):
        error(frame_answer)
        f = f.replace(".000000", "")
        Label_answer = Label(frame_answer, text="", font=("Arial", 12), bg="white", justify='left')
        Label_answer.pack(side="left", anchor="nw")
        typewriter(Label_answer, f, delay=50)
        Button_voice = Button(frame_answer, text="Произнести голосом", bg="orange", command=lambda: voice(f))
        Button_voice.pack(side="right")
        Button_answer_not = Button(frame_answer, text="Убрать пояснение", bg="orange",
                                   command=lambda: lin_nerve_decide_2(a, b, var))
        Button_answer_not.pack(side="right")

    Button_answer = Button(frame_answer, text="Пояснение", bg="orange", command=lambda: help(result_2))
    Button_answer.pack(side="right")
    Button_ark = Button(frame_answer, text="Округленные  значения x", bg="orange",
                        command=lambda: lin_nerve_decide(a, b, var))
    Button_ark.pack(side="right")


def lin_nerve_decide(a, b, var):
    try:
        a, b = float(a), float(b)
        if a - int(a) == 0 and b - int(b) == 0:
            a, b = int(a), int(b)
        if a == 0:
            if var == ">" and b > 0:
                result = "Ответ: x  любое число"
                result_2 = (
                    f"Ответ: x  любое число\n \nПояснение:\n1)Подставим a = 0 и b = {b}\n2)Получим неравентсво "
                    f"вида 0x + {b} > 0\n3)Мы видим, что при любом значении x, всегда {b} > 0\n4)Следовательно "
                    f"x  любое число")
            elif var == ">=" and b >= 0:
                result = "Ответ: x  любое число"
                result_2 = (
                    f"Ответ: x  любое число\n \nПояснение:\n1)Подставим a = 0 и b = {b}\n2)Получим неравентсво "
                    f"вида 0x + {b} ≥ 0\n3)Мы видим, что при любом значении x, всегда {b} ≥ 0\n4)Следовательно "
                    f"x  любое число")
            elif var == "<" and b < 0:
                result = "Ответ: x  любое число"
                result_2 = (
                    f"Ответ: x  любое число\n \nПояснение:\n1)Подставим a = 0 и b = {b}\n2)Получим неравентсво "
                    f"вида 0x + {b} < 0\n3)Мы видим, что при любом значении x, всегда {b} < 0\n4)Следовательно "
                    f"x  любое число")
            elif var == "<=" and b <= 0:
                result = "Ответ: x  любое число"
                result_2 = (
                    f"Ответ: x  любое число\n \nПояснение:\n1)Подставим a = 0 и b = {b}\n2)Получим неравентсво "
                    f"вида 0x + {b} <= 0\n3)Мы видим, что при любом значении x, всегда {b} <= 0\n4)Следовательно "
                    f"x  любое число")
            elif var != " ":
                result = "Ответ: нет решений"
                result_2 = (
                    f"Ответ: нет решений\n \nПояснение:\n1)Подставим a = 0 и b = {b}\n2)Получим неравентсво "
                    f"вида 0x + {b} {var} 0\n3)Мы видим, что при любом значении x, никогда не будет {b} {var} 0\n4)Следовательно "
                    f"нет решений")
        else:
            x1 = -b / a
            if a > 0:
                if var == ">":
                    result = f"Ответ: x > {x1:.3f}"
                    result_2 = (f"Ответ: x > {x1:.3f}\n \nПояснение:\n1)Подставим a = {a} и b = {b}\n2)Получим "
                                f"неравенство вида {a}x > {-b}\n3)Поделим обе части неравенства на {a}\n4)Получим, что "
                                f"x > {-b}/{a}\n5)Следовательно x > {x1:.3f}")
                elif var == ">=":
                    result = f"Ответ: x ≥ {x1:.3f}"
                    result_2 = (f"Ответ: x ≥ {x1:.3f}\n \nПояснение:\n1)Подставим a = {a} и b = {b}\n2)Получим "
                                f"неравенство вида {a}x ≥ {-b}\n3)Поделим обе части неравенства на {a}\n4)Получим, что "
                                f"x ≥ {-b}/{a}\n5)Следовательно x ≥ {x1:.3f}")
                elif var == "<":
                    result = f"Ответ: x < {x1:.3f}"
                    result_2 = (f"Ответ: x < {x1:.3f}\n \nПояснение:\n1)Подставим a = {a} и b = {b}\n2)Получим "
                                f"неравенство вида {a}x < {-b}\n3)Поделим обе части неравенства на {a}\n4)Получим, что "
                                f"x < {-b}/{a}\n5)Следовательно x < {x1:.3f}")
                elif var == "<=":
                    result = f"Ответ: x ≤ {x1:.3f}"
                    result_2 = (f"Ответ: x <= {x1:.3f}\n \nПояснение:\n1)Подставим a = {a} и b = {b}\n2)Получим "
                                f"неравенство вида {a}x <= {-b}\n3)Поделим обе части неравенства на {a}\n4)Получим, что "
                                f"x <= {-b}/{a}\n5)Следовательно x <= {x1:.3f}")
            else:
                if var == ">":
                    result = f"Ответ: x < {x1:.3f}"
                    result_2 = (f"Ответ: x < {x1:.3f}\n \nПояснение:\n1)Подставим a = {a} и b = {b}\n2)Получим "
                                f"неравенство вида {a}x > {-b}\n3)Поделим обе части неравенства на {a} и"
                                f" поменяем знак на противоположный\n4)Получим, что "
                                f"x < {-b}/{a}\n5)Следовательно x < {x1:.3f}")
                elif var == ">=":
                    result = f"Ответ: x ≤ {x1:.3f}"
                    result_2 = (f"Ответ: x <= {x1:.3f}\n \nПояснение:\n1)Подставим a = {a} и b = {b}\n2)Получим "
                                f"неравенство вида {a}x ≥ {-b}\n3)Поделим обе части неравенства на {a} и"
                                f" поменяем знак на противоположный\n4)Получим, что "
                                f"x <= {-b}/{a}\n5)Следовательно x <= {x1:.3f}")
                elif var == "<":
                    result = f"Ответ: x > {x1:.3f}"
                    result_2 = (f"Ответ: x > {x1:.3f}\n \nПояснение:\n1)Подставим a = {a} и b = {b}\n2)Получим "
                                f"неравенство вида {a}x < {-b}\n3)Поделим обе части неравенства на {a} и"
                                f" поменяем знак на противоположный\n4)Получим, что "
                                f"x > {-b}/{a}\n5)Следовательно x > {x1:.3f}")
                elif var == "<=":
                    result = f"Ответ: x ≥ {x1:.3f}"
                    result_2 = (f"Ответ: x ≥ {x1:.3f}\n \nПояснение:\n1)Подставим a = {a} и b = {b}\n2)Получим "
                                f"неравенство вида {a}x <= {-b}\n3)Поделим обе части неравенства на {a} и"
                                f" поменяем знак на противоположный\n4)Получим, что "
                                f"x >= {-b}/{a}\n5)Следовательно x >= {x1:.3f}")
    except ValueError:
        result = "Введите все числовые значения"
    error(frame_answer)
    result = result.replace(".000", "")
    Label_answer = Label(frame_answer, text="", font=("Arial", 12), bg="white", justify='left')
    Label_answer.pack(side="left", anchor="nw")
    typewriter(Label_answer, result, delay=50)
    Button_voice = Button(frame_answer, text="Произнести голосом", bg="orange", command=lambda: voice(result))
    Button_voice.pack(side="right")

    def help(g):
        error(frame_answer)
        g = g.replace(".000", "")
        Label_answer = Label(frame_answer, text="", font=("Arial", 12), bg="white", justify='left')
        Label_answer.pack(side="left", anchor="nw")
        typewriter(Label_answer, g, delay=50)
        Button_voice = Button(frame_answer, text="Произнести голосом", bg="orange", command=lambda: voice(g))
        Button_voice.pack(side="right")
        Button_answer_not = Button(frame_answer, text="Убрать пояснение", bg="orange",
                                   command=lambda: lin_nerve_decide(a, b, var))
        Button_answer_not.pack(side="right")

    Button_answer = Button(frame_answer, text="Пояснение", bg="orange", command=lambda: help(result_2))
    Button_answer.pack(side="right")
    Button_ark = Button(frame_answer, text="Более точные значения x", bg="orange",
                        command=lambda: lin_nerve_decide_2(a, b, var))
    Button_ark.pack(side="right")


# Отвечает за решение квадартного неравенства
def quar_nerve_decide_2(a, b, c, var):
    try:
        a, b, c = float(a), float(b), float(c)
        if a - int(a) == 0 and b - int(b) == 0 and c - int(c) == 0:
            a, b, c = int(a), int(b), int(c)
        if a == 0:
            result = "Ответ: это не квадратное неравенство"
            result_2 = (f"Ответ: это не квадратное неравенство\n \nПояснение:\n1)Квадратное неравенство имеет вид"
                        f" ax^2 + bx + c (>;<;>=;<=) 0"
                        " где a не равно нулю\n2)Так как a равно нулю то это уже не квадратное неравенство")
        else:
            D = b ** 2 - 4 * a * c
            if D > 0:
                x1 = (-b - math.sqrt(D)) / (2 * a)
                x2 = (-b + math.sqrt(D)) / (2 * a)
                if x1 > x2:
                    x1, x2 = x2, x1
                if a > 0:
                    if var == ">":
                        result = f"Ответ: x ∈ (-∞; {x1:.6f}) ∪ ({x2:.6f}; +∞)"
                        result_2 = (
                            f"Ответ: x ∈ (-∞; {x1:.6f}) ∪ ({x2:.6f}; +∞)\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения "
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n4)Найдем первый корень "
                            f"по формуле x = (-b + √D) / (2 * a) = ({-b} + √{D}) / (2 * {a}) = {x1:.6f}\n5)Найдем второй "
                            f"корень по формуле x = (-b - √D) / (2 * a) = ({-b} - √{D}) / (2 * {a}) = {x2:.6f}\n6)Следовате"
                            f"льно корни уравнения x = {x1:.6f} и x = {x2:.6f}\n7)Теперь построим ось Ox и расположим "
                            f"на ней эти корни слева на право в порядке возрастания\n8)Данные корни разбивают"
                            f" ось Ox на три интервала со знаками (+;-;+) соответсвенно\n9)Так как у нас знак "
                            f"'{var}' то нам нужны интервалы где знак '+' и в ответ не берём сами корни\n10)Выбираем соответсвующие интервалы"
                            f"и получается, что x ∈ (-∞; {x1:.6f}) ∪ ({x2:.6f}; +∞)")
                    elif var == ">=":
                        result = f"Ответ: x ∈ (-∞; {x1:.6f}] ∪ [{x2:.6f}; +∞)"
                        result_2 = (
                            f"Ответ: x ∈ (-∞; {x1:.6f}] ∪ [{x2:.6f}; +∞)\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения "
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n4)Найдем первый корень "
                            f"по формуле x = (-b + √D) / (2 * a) = ({-b} + √{D}) / (2 * {a}) = {x1:.6f}\n5)Найдем второй "
                            f"корень по формуле x = (-b - √D) / (2 * a) = ({-b} - √{D}) / (2 * {a}) = {x2:.6f}\n6)Следовате"
                            f"льно корни уравнения x = {x1:.6f} и x = {x2:.6f}\n7)Теперь построим ось Ox и расположим "
                            f"на ней эти корни слева на право в порядке возрастания\n8)Данные корни разбивают"
                            f" ось Ox на три интервала со знаками (+;-;+) соответсвенно\n9)Так как у нас знак "
                            f"'{var}', то нам нужны интервалы где знак '+' и в ответ также берём сами корни\n10)Выбираем соответсвующие интервалы"
                            f"и получается, что x ∈ (-∞; {x1:.6f}] ∪ [{x2:.6f}; +∞)")
                    elif var == "<":
                        result = f"Ответ: x ∈ ({x1:.6f}; {x2:.6f})"
                        result_2 = (
                            f"Ответ: x ∈ ({x1:.6f}; {x2:.6f})\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения "
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n4)Найдем первый корень "
                            f"по формуле x = (-b + √D) / (2 * a) = ({-b} + √{D}) / (2 * {a}) = {x1:.6f}\n5)Найдем второй "
                            f"корень по формуле x = (-b - √D) / (2 * a) = ({-b} - √{D}) / (2 * {a}) = {x2:.6f}\n6)Следовате"
                            f"льно корни уравнения x = {x1:.6f} и x = {x2:.6f}\n7)Теперь построим ось Ox и расположим "
                            f"на ней эти корни слева на право в порядке возрастания\n8)Данные корни разбивают"
                            f" ось Ox на три интервала со знаками (+;-;+) соответсвенно\n9)Так как у нас знак "
                            f"'{var}', то нам нужны интервалы где знак '-' и в ответ не берём сами корни\n10)Выбираем соответсвующие интервалы"
                            f"и получается, что x ∈ ({x1:.6f}; {x2:.6f})")
                    elif var == "<=":
                        result = f"Ответ: x ∈ [{x1:.6f}; {x2:.6f}]"
                        result_2 = (
                            f"Ответ: x ∈ [{x1:.6f}; {x2:.6f}]\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения "
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n4)Найдем первый корень "
                            f"по формуле x = (-b + √D) / (2 * a) = ({-b} + √{D}) / (2 * {a}) = {x1:.6f}\n5)Найдем второй "
                            f"корень по формуле x = (-b - √D) / (2 * a) = ({-b} - √{D}) / (2 * {a}) = {x2:.6f}\n6)Следовате"
                            f"льно корни уравнения x = {x1:.6f} и x = {x2:.6f}\n7)Теперь построим ось Ox и расположим "
                            f"на ней эти корни слева на право в порядке возрастания\n8)Данные корни разбивают"
                            f" ось Ox на три интервала со знаками (+;-;+) соответсвенно\n9)Так как у нас знак "
                            f"'{var}', то нам нужны интервалы где знак '-' и в ответ также берём сами корни\n10)Выбираем соответсвующие интервалы"
                            f"и получается, что x ∈ [{x1:.6f}; {x2:.6f}]")
                else:
                    if var == ">":
                        result = f"Ответ: x ∈ ({x1:.6f}; {x2:.6f})"
                        result_2 = (
                            f"Ответ: x ∈ ({x1:.6f}; {x2:.6f})\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения "
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n4)Найдем первый корень "
                            f"по формуле x = (-b + √D) / (2 * a) = ({-b} + √{D}) / (2 * {a}) = {x1:.6f}\n5)Найдем второй "
                            f"корень по формуле x = (-b - √D) / (2 * a) = ({-b} - √{D}) / (2 * {a}) = {x2:.6f}\n6)Следовате"
                            f"льно корни уравнения x = {x1:.6f} и x = {x2:.6f}\n7)Теперь построим ось Ox и расположим "
                            f"на ней эти корни слева на право в порядке возрастания\n8)Данные корни разбивают"
                            f" ось Ox на три интервала со знаками (-;+;-) соответсвенно\n9)Так как у нас знак "
                            f"'{var}', то нам нужны интервалы где знак '+' и в ответ не берём сами корни\n10)Выбираем соответсвующие интервалы"
                            f"и получается, что x ∈ ({x1:.6f}; {x2:.6f})")
                    elif var == ">=":
                        result = f"Ответ: x ∈ [{x1:.6f}; {x2:.6f}]"
                        result_2 = (
                            f"Ответ: x ∈ [{x1:.6f}; {x2:.6f}]\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения "
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n4)Найдем первый корень "
                            f"по формуле x = (-b + √D) / (2 * a) = ({-b} + √{D}) / (2 * {a}) = {x1:.6f}\n5)Найдем второй "
                            f"корень по формуле x = (-b - √D) / (2 * a) = ({-b} - √{D}) / (2 * {a}) = {x2:.6f}\n6)Следовате"
                            f"льно корни уравнения x = {x1:.6f} и x = {x2:.6f}\n7)Теперь построим ось Ox и расположим "
                            f"на ней эти корни слева на право в порядке возрастания\n8)Данные корни разбивают"
                            f" ось Ox на три интервала со знаками (-;+;-) соответсвенно\n9)Так как у нас знак "
                            f"'{var}', то нам нужны интервалы где знак '+' и в ответ также берём сами корни\n10)Выбираем соответсвующие интервалы"
                            f"и получается, что x ∈ [{x1:.6f}; {x2:.6f}]")
                    elif var == "<":
                        result = f"Ответ: x ∈ (-∞; {x1:.6f}) ∪ ({x2:.6f}; +∞)"
                        result_2 = (
                            f"Ответ: x ∈ (-∞; {x1:.6f}) ∪ ({x2:.6f}; +∞)\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения "
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n4)Найдем первый корень "
                            f"по формуле x = (-b + √D) / (2 * a) = ({-b} + √{D}) / (2 * {a}) = {x1:.6f}\n5)Найдем второй "
                            f"корень по формуле x = (-b - √D) / (2 * a) = ({-b} - √{D}) / (2 * {a}) = {x2:.6f}\n6)Следовате"
                            f"льно корни уравнения x = {x1:.6f} и x = {x2:.6f}\n7)Теперь построим ось Ox и расположим "
                            f"на ней эти корни слева на право в порядке возрастания\n8)Данные корни разбивают"
                            f" ось Ox на три интервала со знаками (-;+;-) соответсвенно\n9)Так как у нас знак "
                            f"'{var}', то нам нужны интервалы где знак '-' и в ответ не берём сами корни\n10)Выбираем соответсвующие интервалы"
                            f"и получается, что x ∈ (-∞; {x1:.6f}) ∪ ({x2:.6f}; +∞)")
                    elif var == "<=":
                        result = f"Ответ: x ∈ (-∞; {x1:.6f}] ∪ [{x2:.6f}; +∞)"
                        result_2 = (
                            f"Ответ: x ∈ (-∞; {x1:.6f}] ∪ [{x2:.6f}; +∞)\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения "
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n4)Найдем первый корень "
                            f"по формуле x = (-b + √D) / (2 * a) = ({-b} + √{D}) / (2 * {a}) = {x1:.6f}\n5)Найдем второй "
                            f"корень по формуле x = (-b - √D) / (2 * a) = ({-b} - √{D}) / (2 * {a}) = {x2:.6f}\n6)Следовате"
                            f"льно корни уравнения x = {x1:.6f} и x = {x2:.6f}\n7)Теперь построим ось Ox и расположим "
                            f"на ней эти корни слева на право в порядке возрастания\n8)Данные корни разбивают"
                            f" ось Ox на три интервала со знаками (-;+;-) соответсвенно\n9)Так как у нас знак "
                            f"'{var}', то нам нужны интервалы где знак '-' и в ответ также берём сами корни\n10)Выбираем соответсвующие интервалы"
                            f"и получается, что x ∈ (-∞; {x1:.6f}] ∪ [{x2:.6f}; +∞)")
            elif D == 0:
                x = -b / (2 * a)
                if a > 0:
                    if var == ">":
                        result = f"Ответ: x ∈ (-∞; {x:.6f}) ∪ ({x:.6f}; +∞)"
                        result_2 = (
                            f"Ответ: x ∈ (-∞; {x:.6f}) ∪ ({x:.6f}; +∞)\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения"
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = 0\n4)Так как дискриминант "
                            f"равен нулю, то данное уравнение имеет только один корень\n5)Найдем его по формуле "
                            f"x = (-b + 0) / (2 * a) = ({-b} + √0) / (2 * {a}) = {x:.6f}\n6)Следователно корень "
                            f"уравнения x = {x:.6f}\n7)Теперь построим ось Ox и расположим на ней этот корень"
                            f"\n8)Этот корень разбивает ось Ox на два интервала со знаками (+;+)\n9)Так как "
                            f"у нас знак '{var}', то нам нужны интервалы где знак '+' и в ответ не берём сам "
                            f"корень\n10)Выбираем соответсующие интервалы и получается, что x ∈ (-∞; {x:.6f}) ∪ ({x:.6f}; +∞)")
                    elif var == ">=":
                        result = "Ответ: x ∈ ℝ"
                        result_2 = (
                            f"Ответ: x ∈ ℝ\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения"
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = 0\n4)Так как дискриминант "
                            f"равен нулю, то данное уравнение имеет только один корень\n5)Найдем его по формуле "
                            f"x = (-b + 0) / (2 * a) = ({-b} + √0) / (2 * {a}) = {x:.6f}\n6)Следователно корень "
                            f"уравнения x = {x:.6f}\n7)Теперь построим ось Ox и расположим на ней этот корень"
                            f"\n8)Этот корень разбивает ось Ox на два интервала со знаками (+;+)\n9)Так как "
                            f"у нас знак '{var}', то нам нужны интервалы где знак '+' и в ответ также берём сам "
                            f"корень\n10)Выбираем соответсующие интервалы и получается, что x ∈ ℝ")
                    elif var == "<":
                        result = "Ответ: нет решений"
                        result_2 = (
                            f"Ответ: нет решений\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения"
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = 0\n4)Так как дискриминант "
                            f"равен нулю, то данное уравнение имеет только один корень\n5)Найдем его по формуле "
                            f"x = (-b + 0) / (2 * a) = ({-b} + √0) / (2 * {a}) = {x:.6f}\n6)Следователно корень "
                            f"уравнения x = {x:.6f}\n7)Теперь построим ось Ox и расположим на ней этот корень"
                            f"\n8)Этот корень разбивает ось Ox на два интервала со знаками (+;+)\n9)Так как "
                            f"у нас знак '{var}', то нам нужны интервалы где знак '-' и в ответ не берём сам "
                            f"корень\n10)Выбираем соответсующие интервалы и получается, что нет решений")
                    elif var == "<=":
                        result = f"Ответ: x = {x:.6f}"
                        result_2 = (
                            f"Ответ: x = {x:.6f}\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения"
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = 0\n4)Так как дискриминант "
                            f"равен нулю, то данное уравнение имеет только один корень\n5)Найдем его по формуле "
                            f"x = (-b + 0) / (2 * a) = ({-b} + √0) / (2 * {a}) = {x:.6f}\n6)Следователно корень "
                            f"уравнения x = {x:.6f}\n7)Теперь построим ось Ox и расположим на ней этот корень"
                            f"\n8)Этот корень разбивает ось Ox на два интервала со знаками (+;+)\n9)Так как "
                            f"у нас знак '{var}', то нам нужны интервалы где знак '-' и в ответ также берём сам "
                            f"корень\n10)Выбираем соответсующие интервалы и получается, что x = {x:.6f}")
                else:
                    if var == ">":
                        result = "Ответ: нет решений"
                        result_2 = (
                            f"Ответ: нет решений\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения"
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = 0\n4)Так как дискриминант "
                            f"равен нулю, то данное уравнение имеет только один корень\n5)Найдем его по формуле "
                            f"x = (-b + 0) / (2 * a) = ({-b} + √0) / (2 * {a}) = {x:.6f}\n6)Следователно корень "
                            f"уравнения x = {x:.6f}\n7)Теперь построим ось Ox и расположим на ней этот корень"
                            f"\n8)Этот корень разбивает ось Ox на два интервала со знаками (-;-)\n9)Так как "
                            f"у нас знак '{var}', то нам нужны интервалы где знак '+' и в ответ не берём сам "
                            f"корень\n10)Выбираем соответсующие интервалы и получается, что нет решений")
                    elif var == ">=":
                        result = f"Ответ: x = {x:.6f}"
                        result_2 = (
                            f"Ответ: x = {x:.6f}\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения"
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = 0\n4)Так как дискриминант "
                            f"равен нулю, то данное уравнение имеет только один корень\n5)Найдем его по формуле "
                            f"x = (-b + 0) / (2 * a) = ({-b} + √0) / (2 * {a}) = {x:.6f}\n6)Следователно корень "
                            f"уравнения x = {x:.6f}\n7)Теперь построим ось Ox и расположим на ней этот корень"
                            f"\n8)Этот корень разбивает ось Ox на два интервала со знаками (-;-)\n9)Так как "
                            f"у нас знак '{var}', то нам нужны интервалы где знак '+' и в ответ также берём сам "
                            f"корень\n10)Выбираем соответсующие интервалы и получается, что x = {x:.6f}")
                    elif var == "<":
                        result = f"Ответ: x ∈ (-∞; {x:.6f}) ∪ ({x:.6f}; +∞)"
                        result_2 = (
                            f"Ответ: x ∈ (-∞; {x:.6f}) ∪ ({x:.6f}; +∞)\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения"
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = 0\n4)Так как дискриминант "
                            f"равен нулю, то данное уравнение имеет только один корень\n5)Найдем его по формуле "
                            f"x = (-b + 0) / (2 * a) = ({-b} + √0) / (2 * {a}) = {x:.6f}\n6)Следователно корень "
                            f"уравнения x = {x:.6f}\n7)Теперь построим ось Ox и расположим на ней этот корень"
                            f"\n8)Этот корень разбивает ось Ox на два интервала со знаками (-;-)\n9)Так как "
                            f"у нас знак '{var}', то нам нужны интервалы где знак '-' и в ответ не берём сам "
                            f"корень\n10)Выбираем соответсующие интервалы и получается, что x ∈ (-∞; {x:.6f}) ∪ ({x:.6f}; +∞)")
                    elif var == "<=":
                        result = "Ответ: x ∈ ℝ"
                        result_2 = (
                            f"Ответ: x ∈ ℝ\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения"
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = 0\n4)Так как дискриминант "
                            f"равен нулю, то данное уравнение имеет только один корень\n5)Найдем его по формуле "
                            f"x = (-b + 0) / (2 * a) = ({-b} + √0) / (2 * {a}) = {x:.6f}\n6)Следователно корень "
                            f"уравнения x = {x:.6f}\n7)Теперь построим ось Ox и расположим на ней этот корень"
                            f"\n8)Этот корень разбивает ось Ox на два интервала со знаками (-;-)\n9)Так как "
                            f"у нас знак '{var}', то нам нужны интервалы где знак '-' и в ответ также берём сам "
                            f"корень\n10)Выбираем соответсующие интервалы и получается, что x ∈ ℝ")
            else:
                if a > 0:
                    if var == ">" or var == ">=":
                        result = "Ответ: x ∈ ℝ"
                        result_2 = (f"Ответ: x ∈ ℝ\n \nПояснение:\n1)Сначала найдем дискриминант уравнения"
                                    f"({a})x^2 + {b}x + {c}\n2)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n3)Так как дискриминант "
                                    f"меньше нуля, то данное уравнение не имеет действительных корней\n4)Следовательно график этого "
                                    f"уравнения располложен выше оси Ox, а так как у нас знак '{var}', то x ∈ ℝ")
                    else:
                        result = "Ответ: нет решений"
                        result_2 = (f"Ответ: нет решений\n \nПояснение:\n1)Сначала найдем дискриминант уравнения"
                                    f"({a})x^2 + {b}x + {c}\n2)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n3)Так как дискриминант "
                                    f"меньше нуля, то данное уравнение не имеет действительных корней\n4)Следовательно график этого "
                                    f"уравнения располложен выше оси Ox(коэффицент a > 0), а так как у нас знак '{var}', то нет решений")
                else:
                    if var == "<" or var == "<=":
                        result = "Ответ: x ∈ ℝ"
                        result_2 = (f"Ответ: x ∈ ℝ\n \nПояснение:\n1)Сначала найдем дискриминант уравнения"
                                    f"({a})x^2 + {b}x + {c}\n2)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n3)Так как дискриминант "
                                    f"меньше нуля, то данное уравнение не имеет действительных корней\n4)Следовательно график этого "
                                    f"уравнения располложен ниже оси Ox(коэффицент a < 0), а так как у нас знак '{var}', то x ∈ ℝ")
                    else:
                        result = "Ответ: нет решений"
                        result_2 = (f"Ответ: нет решений\n \nПояснение:\n1)Сначала найдем дискриминант уравнения"
                                    f"({a})x^2 + {b}x + {c}\n2)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n3)Так как дискриминант "
                                    f"меньше нуля, то данное уравнение не имеет действительных корней\n4)Следовательно график этого "
                                    f"уравнения располложен ниже оси Ox(коэффицент a < 0), а так как у нас знак '{var}', то нет решений")
    except ValueError:
        result = "Введите все числовые значения"
    error(frame_answer)
    result = result.replace(".000000", "")
    Label_answer = Label(frame_answer, text="", font=("Arial", 12), bg="white", justify='left')
    Label_answer.pack(side="left", anchor="nw")
    typewriter(Label_answer, result, delay=50)
    Button_voice = Button(frame_answer, text="Произнести голосом", bg="orange", command=lambda: voice(result))
    Button_voice.pack(side="right")

    def help(f):
        error(frame_answer)
        f = f.replace(".000000", "")
        Label_answer = Label(frame_answer, text="", font=("Arial", 12), bg="white", justify='left')
        Label_answer.pack(side="left", anchor="nw")
        typewriter(Label_answer, f, delay=50)
        Button_voice = Button(frame_answer, text="Произнести голосом", bg="orange", command=lambda: voice(f))
        Button_voice.pack(side="right")
        Button_answer_not = Button(frame_answer, text="Убрать пояснение", bg="orange",
                                   command=lambda: quar_nerve_decide(a, b, c, var))
        Button_answer_not.pack(side="right")

    Button_answer = Button(frame_answer, text="Пояснение", bg="orange", command=lambda: help(result_2))
    Button_answer.pack(side="right")
    Button_ark = Button(frame_answer, text="Округлённые значения x", bg="orange",
                        command=lambda: quar_nerve_decide(a, b, c, var))
    Button_ark.pack(side="right")


def quar_nerve_decide(a, b, c, var):
    try:
        a, b, c = float(a), float(b), float(c)
        if a - int(a) == 0 and b - int(b) == 0 and c - int(c) == 0:
            a, b, c = int(a), int(b), int(c)
        if a == 0:
            result = "Ответ: это не квадратное неравенство"
            result_2 = (f"Ответ: это не квадратное неравенство\n \nПояснение:\n1)Квадратное неравенство имеет вид"
                        f" ax^2 + bx + c (>;<;>=;<=) 0"
                        " где a не равно нулю\n2)Так как a равно нулю то это уже не квадратное неравенство")
        else:
            D = b ** 2 - 4 * a * c
            if D > 0:
                x1 = (-b - math.sqrt(D)) / (2 * a)
                x2 = (-b + math.sqrt(D)) / (2 * a)
                if x1 > x2:
                    x1, x2 = x2, x1
                if a > 0:
                    if var == ">":
                        result = f"Ответ: x ∈ (-∞; {x1:.3f}) ∪ ({x2:.3f}; +∞)"
                        result_2 = (
                            f"Ответ: x ∈ (-∞; {x1:.3f}) ∪ ({x2:.3f}; +∞)\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения "
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n4)Найдем первый корень "
                            f"по формуле x = (-b + √D) / (2 * a) = ({-b} + √{D}) / (2 * {a}) = {x1:.3f}\n5)Найдем второй "
                            f"корень по формуле x = (-b - √D) / (2 * a) = ({-b} - √{D}) / (2 * {a}) = {x2:.3f}\n6)Следовате"
                            f"льно корни уравнения x = {x1:.3f} и x = {x2:.3f}\n7)Теперь построим ось Ox и расположим "
                            f"на ней эти корни слева на право в порядке возрастания\n8)Данные корни разбивают"
                            f" ось Ox на три интервала со знаками (+;-;+) соответсвенно\n9)Так как у нас знак "
                            f"'{var}' то нам нужны интервалы где знак '+' и в ответ не берём сами корни\n10)Выбираем соответсвующие интервалы"
                            f"и получается, что x ∈ (-∞; {x1:.3f}) ∪ ({x2:.3f}; +∞)")
                    elif var == ">=":
                        result = f"Ответ: x ∈ (-∞; {x1:.3f}] ∪ [{x2:.3f}; +∞)"
                        result_2 = (
                            f"Ответ: x ∈ (-∞; {x1:.3f}] ∪ [{x2:.3f}; +∞)\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения "
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n4)Найдем первый корень "
                            f"по формуле x = (-b + √D) / (2 * a) = ({-b} + √{D}) / (2 * {a}) = {x1:.3f}\n5)Найдем второй "
                            f"корень по формуле x = (-b - √D) / (2 * a) = ({-b} - √{D}) / (2 * {a}) = {x2:.3f}\n6)Следовате"
                            f"льно корни уравнения x = {x1:.3f} и x = {x2:.3f}\n7)Теперь построим ось Ox и расположим "
                            f"на ней эти корни слева на право в порядке возрастания\n8)Данные корни разбивают"
                            f" ось Ox на три интервала со знаками (+;-;+) соответсвенно\n9)Так как у нас знак "
                            f"'{var}', то нам нужны интервалы где знак '+' и в ответ также берём сами корни\n10)Выбираем соответсвующие интервалы"
                            f"и получается, что x ∈ (-∞; {x1:.3f}] ∪ [{x2:.3f}; +∞)")
                    elif var == "<":
                        result = f"Ответ: x ∈ ({x1:.3f}; {x2:.3f})"
                        result_2 = (
                            f"Ответ: x ∈ ({x1:.3f}; {x2:.3f})\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения "
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n4)Найдем первый корень "
                            f"по формуле x = (-b + √D) / (2 * a) = ({-b} + √{D}) / (2 * {a}) = {x1:.3f}\n5)Найдем второй "
                            f"корень по формуле x = (-b - √D) / (2 * a) = ({-b} - √{D}) / (2 * {a}) = {x2:.3f}\n6)Следовате"
                            f"льно корни уравнения x = {x1:.3f} и x = {x2:.3f}\n7)Теперь построим ось Ox и расположим "
                            f"на ней эти корни слева на право в порядке возрастания\n8)Данные корни разбивают"
                            f" ось Ox на три интервала со знаками (+;-;+) соответсвенно\n9)Так как у нас знак "
                            f"'{var}', то нам нужны интервалы где знак '-' и в ответ не берём сами корни\n10)Выбираем соответсвующие интервалы"
                            f"и получается, что x ∈ ({x1:.3f}; {x2:.3f})")
                    elif var == "<=":
                        result = f"Ответ: x ∈ [{x1:.3f}; {x2:.3f}]"
                        result_2 = (
                            f"Ответ: x ∈ [{x1:.3f}; {x2:.3f}]\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения "
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n4)Найдем первый корень "
                            f"по формуле x = (-b + √D) / (2 * a) = ({-b} + √{D}) / (2 * {a}) = {x1:.3f}\n5)Найдем второй "
                            f"корень по формуле x = (-b - √D) / (2 * a) = ({-b} - √{D}) / (2 * {a}) = {x2:.3f}\n6)Следовате"
                            f"льно корни уравнения x = {x1:.3f} и x = {x2:.3f}\n7)Теперь построим ось Ox и расположим "
                            f"на ней эти корни слева на право в порядке возрастания\n8)Данные корни разбивают"
                            f" ось Ox на три интервала со знаками (+;-;+) соответсвенно\n9)Так как у нас знак "
                            f"'{var}', то нам нужны интервалы где знак '-' и в ответ также берём сами корни\n10)Выбираем соответсвующие интервалы"
                            f"и получается, что x ∈ [{x1:.3f}; {x2:.3f}]")
                else:
                    if var == ">":
                        result = f"Ответ: x ∈ ({x1:3f}; {x2:.3f})"
                        result_2 = (
                            f"Ответ: x ∈ ({x1:3f}; {x2:.3f})\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения "
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n4)Найдем первый корень "
                            f"по формуле x = (-b + √D) / (2 * a) = ({-b} + √{D}) / (2 * {a}) = {x1:.3f}\n5)Найдем второй "
                            f"корень по формуле x = (-b - √D) / (2 * a) = ({-b} - √{D}) / (2 * {a}) = {x2:.3f}\n6)Следовате"
                            f"льно корни уравнения x = {x1:.3f} и x = {x2:.3f}\n7)Теперь построим ось Ox и расположим "
                            f"на ней эти корни слева на право в порядке возрастания\n8)Данные корни разбивают"
                            f" ось Ox на три интервала со знаками (-;+;-) соответсвенно\n9)Так как у нас знак "
                            f"'{var}' то нам нужны интервалы где знак '+' и в ответ не берём сами корни\n10)Выбираем соответсвующие интервалы"
                            f"и получается, что x ∈ ({x1:3f}; {x2:.3f})")
                    elif var == ">=":
                        result = f"Ответ: x ∈ [{x1:.3f}; {x2:.3f}]"
                        result_2 = (
                            f"Ответ: x ∈ [{x1:.3f}; {x2:.3f}]\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения "
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n4)Найдем первый корень "
                            f"по формуле x = (-b + √D) / (2 * a) = ({-b} + √{D}) / (2 * {a}) = {x1:.3f}\n5)Найдем второй "
                            f"корень по формуле x = (-b - √D) / (2 * a) = ({-b} - √{D}) / (2 * {a}) = {x2:.3f}\n6)Следовате"
                            f"льно корни уравнения x = {x1:.3f} и x = {x2:.3f}\n7)Теперь построим ось Ox и расположим "
                            f"на ней эти корни слева на право в порядке возрастания\n8)Данные корни разбивают"
                            f" ось Ox на три интервала со знаками (-;+;-) соответсвенно\n9)Так как у нас знак "
                            f"'{var}' то нам нужны интервалы где знак '+' и в ответ также берём сами корни\n10)Выбираем соответсвующие интервалы"
                            f"и получается, что x ∈ [{x1:.3f}; {x2:.3f}]")
                    elif var == "<":
                        result = f"Ответ: x ∈ (-∞; {x1:.3f}) ∪ ({x2:.3f}; +∞)"
                        result_2 = (
                            f"Ответ: x ∈ (-∞; {x1:.3f}) ∪ ({x2:.3f}; +∞)\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения "
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n4)Найдем первый корень "
                            f"по формуле x = (-b + √D) / (2 * a) = ({-b} + √{D}) / (2 * {a}) = {x1:.3f}\n5)Найдем второй "
                            f"корень по формуле x = (-b - √D) / (2 * a) = ({-b} - √{D}) / (2 * {a}) = {x2:.3f}\n6)Следовате"
                            f"льно корни уравнения x = {x1:.3f} и x = {x2:.3f}\n7)Теперь построим ось Ox и расположим "
                            f"на ней эти корни слева на право в порядке возрастания\n8)Данные корни разбивают"
                            f" ось Ox на три интервала со знаками (-;+;-) соответсвенно\n9)Так как у нас знак "
                            f"'{var}' то нам нужны интервалы где знак '-' и в ответ не берём сами корни\n10)Выбираем соответсвующие интервалы"
                            f"и получается, что x ∈ (-∞; {x1:.3f}) ∪ ({x2:.3f}; +∞)")

                    elif var == "<=":
                        result = f"Ответ: x ∈ (-∞; {x1:.3f}] ∪ [{x2:.3f}; +∞)"
                        result_2 = (
                            f"Ответ: x ∈ (-∞; {x1:.3f}] ∪ [{x2:.3f}; +∞)\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения "
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n4)Найдем первый корень "
                            f"по формуле x = (-b + √D) / (2 * a) = ({-b} + √{D}) / (2 * {a}) = {x1:.3f}\n5)Найдем второй "
                            f"корень по формуле x = (-b - √D) / (2 * a) = ({-b} - √{D}) / (2 * {a}) = {x2:.3f}\n6)Следовате"
                            f"льно корни уравнения x = {x1:.3f} и x = {x2:.3f}\n7)Теперь построим ось Ox и расположим "
                            f"на ней эти корни слева на право в порядке возрастания\n8)Данные корни разбивают"
                            f" ось Ox на три интервала со знаками (-;+;-) соответсвенно\n9)Так как у нас знак "
                            f"'{var}' то нам нужны интервалы где знак '-' и в ответ также берём сами корни\n10)Выбираем соответсвующие интервалы"
                            f"и получается, что x ∈ (-∞; {x1:.3f}] ∪ [{x2:.3f}; +∞)")
            elif D == 0:
                x = -b / (2 * a)
                if a > 0:
                    if var == ">":
                        result = f"Ответ: x ∈ (-∞; {x:.3f}) ∪ ({x:.3f}; +∞)"
                        result_2 = (
                            f"Ответ: x ∈ (-∞; {x:.3f}) ∪ ({x:.3f}; +∞)\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения"
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = 0\n4)Так как дискриминант "
                            f"равен нулю, то данное уравнение имеет только один корень\n5)Найдем его по формуле "
                            f"x = (-b + 0) / (2 * a) = ({-b} + √0) / (2 * {a}) = {x:.3f}\n6)Следователно корень "
                            f"уравнения x = {x:.6f}\n7)Теперь построим ось Ox и расположим на ней этот корень"
                            f"\n8)Этот корень разбивает ось Ox на два интервала со знаками (+;+)\n9)Так как "
                            f"у нас знак '{var}', то нам нужны интервалы где знак '+' и в ответ не берём сам "
                            f"корень\n10)Выбираем соответсующие интервалы и получается, что x ∈ (-∞; {x:.3f}) ∪ ({x:.3f}; +∞)")
                    elif var == ">=":
                        result = "Ответ: x ∈ ℝ"
                        result_2 = (
                            f"Ответ: x ∈ ℝ\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения"
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = 0\n4)Так как дискриминант "
                            f"равен нулю, то данное уравнение имеет только один корень\n5)Найдем его по формуле "
                            f"x = (-b + 0) / (2 * a) = ({-b} + √0) / (2 * {a}) = {x:.3f}\n6)Следователно корень "
                            f"уравнения x = {x:.6f}\n7)Теперь построим ось Ox и расположим на ней этот корень"
                            f"\n8)Этот корень разбивает ось Ox на два интервала со знаками (+;+)\n9)Так как "
                            f"у нас знак '{var}', то нам нужны интервалы где знак '+' и в ответ также берём сам "
                            f"корень\n10)Выбираем соответсующие интервалы и получается, что x ∈ ℝ")
                    elif var == "<":
                        result = "Ответ: нет решений"
                        result_2 = (
                            f"Ответ: нет решений\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения"
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = 0\n4)Так как дискриминант "
                            f"равен нулю, то данное уравнение имеет только один корень\n5)Найдем его по формуле "
                            f"x = (-b + 0) / (2 * a) = ({-b} + √0) / (2 * {a}) = {x:.3f}\n6)Следователно корень "
                            f"уравнения x = {x:.6f}\n7)Теперь построим ось Ox и расположим на ней этот корень"
                            f"\n8)Этот корень разбивает ось Ox на два интервала со знаками (+;+)\n9)Так как "
                            f"у нас знак '{var}', то нам нужны интервалы где знак '-' и в ответ не берём сам "
                            f"корень\n10)Выбираем соответсующие интервалы и получается, что нет решений")
                    elif var == "<=":
                        result = f"Ответ: x = {x:.3f}"
                        result_2 = (
                            f"Ответ: x = {x:.3f}\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения"
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = 0\n4)Так как дискриминант "
                            f"равен нулю, то данное уравнение имеет только один корень\n5)Найдем его по формуле "
                            f"x = (-b + 0) / (2 * a) = ({-b} + √0) / (2 * {a}) = {x:.3f}\n6)Следователно корень "
                            f"уравнения x = {x:.6f}\n7)Теперь построим ось Ox и расположим на ней этот корень"
                            f"\n8)Этот корень разбивает ось Ox на два интервала со знаками (+;+)\n9)Так как "
                            f"у нас знак '{var}', то нам нужны интервалы где знак '-' и в ответ также берём сам "
                            f"корень\n10)Выбираем соответсующие интервалы и получается, что x = {x:.3f}")
                else:
                    if var == ">":
                        result = "Ответ: нет решений"
                        result_2 = (
                            f"Ответ: нет решений\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения"
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = 0\n4)Так как дискриминант "
                            f"равен нулю, то данное уравнение имеет только один корень\n5)Найдем его по формуле "
                            f"x = (-b + 0) / (2 * a) = ({-b} + √0) / (2 * {a}) = {x:.3f}\n6)Следователно корень "
                            f"уравнения x = {x:.6f}\n7)Теперь построим ось Ox и расположим на ней этот корень"
                            f"\n8)Этот корень разбивает ось Ox на два интервала со знаками (-;-)\n9)Так как "
                            f"у нас знак '{var}', то нам нужны интервалы где знак '+' и в ответ не берём сам "
                            f"корень\n10)Выбираем соответсующие интервалы и получается, что нет решений")
                    elif var == ">=":
                        result = f"Ответ: x = {x:.3f}"
                        result_2 = (
                            f"Ответ: x = {x:.3f}\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения"
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = 0\n4)Так как дискриминант "
                            f"равен нулю, то данное уравнение имеет только один корень\n5)Найдем его по формуле "
                            f"x = (-b + 0) / (2 * a) = ({-b} + √0) / (2 * {a}) = {x:.3f}\n6)Следователно корень "
                            f"уравнения x = {x:.6f}\n7)Теперь построим ось Ox и расположим на ней этот корень"
                            f"\n8)Этот корень разбивает ось Ox на два интервала со знаками (-;-)\n9)Так как "
                            f"у нас знак '{var}', то нам нужны интервалы где знак '+' и в ответ также берём сам "
                            f"корень\n10)Выбираем соответсующие интервалы и получается, что x = {x:.3f}")
                    elif var == "<":
                        result = f"Ответ: x ∈ (-∞; {x:.3f}) ∪ ({x:.3f}; +∞)"
                        result_2 = (
                            f"Ответ: x ∈ (-∞; {x:.3f}) ∪ ({x:.3f}; +∞)\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения"
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = 0\n4)Так как дискриминант "
                            f"равен нулю, то данное уравнение имеет только один корень\n5)Найдем его по формуле "
                            f"x = (-b + 0) / (2 * a) = ({-b} + √0) / (2 * {a}) = {x:.3f}\n6)Следователно корень "
                            f"уравнения x = {x:.3f}\n7)Теперь построим ось Ox и расположим на ней этот корень"
                            f"\n8)Этот корень разбивает ось Ox на два интервала со знаками (-;-)\n9)Так как "
                            f"у нас знак '{var}', то нам нужны интервалы где знак '-' и в ответ не берём сам "
                            f"корень\n10)Выбираем соответсующие интервалы и получается, что x ∈ (-∞; {x:.3f}) ∪ ({x:.3f}; +∞)")
                    elif var == "<=":
                        result = "Ответ: x ∈ ℝ"
                        result_2 = (
                            f"Ответ: x ∈ ℝ\n \nПояснение:\n1)Сначала приравняем левую часть"
                            f" неравенства к нулю и найдем корни уравнения\n2)Для этого найдем дискриминант уравнения"
                            f"({a})x^2 + {b}x + {c}\n3)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = 0\n4)Так как дискриминант "
                            f"равен нулю, то данное уравнение имеет только один корень\n5)Найдем его по формуле "
                            f"x = (-b + 0) / (2 * a) = ({-b} + √0) / (2 * {a}) = {x:.3f}\n6)Следователно корень "
                            f"уравнения x = {x:.6f}\n7)Теперь построим ось Ox и расположим на ней этот корень"
                            f"\n8)Этот корень разбивает ось Ox на два интервала со знаками (-;-)\n9)Так как "
                            f"у нас знак '{var}', то нам нужны интервалы где знак '-' и в ответ также берём сам "
                            f"корень\n10)Выбираем соответсующие интервалы и получается, что x ∈ ℝ")
            else:
                if a > 0:
                    if var == ">" or var == ">=":
                        result = "Ответ: x ∈ ℝ"
                        result_2 = (f"Ответ: x ∈ ℝ\n \nПояснение:\n1)Сначала найдем дискриминант уравнения"
                                    f"({a})x^2 + {b}x + {c}\n2)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n3)Так как дискриминант "
                                    f"меньше нуля, то данное уравнение не имеет действительных корней\n4)Следовательно график этого "
                                    f"уравнения располложен выше\nоси Ox, а так как у нас знак '{var}', то x ∈ ℝ")
                    else:
                        result = "Ответ: нет решений"
                        result_2 = (f"Ответ: нет решений\n \nПояснение:\n1)Сначала найдем дискриминант уравнения"
                                    f"({a})x^2 + {b}x + {c}\n2)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n3)Так как дискриминант "
                                    f"меньше нуля, то данное уравнение не имеет действительных корней\n4)Следовательно график этого "
                                    f"уравнения располложен выше\nоси Ox(коэффицент a > 0), а так как у нас знак '{var}', то нет решений")
                else:
                    if var == "<" or var == "<=":
                        result = "Ответ: x ∈ ℝ"
                        result_2 = (f"Ответ: x ∈ ℝ\n \nПояснение:\n1)Сначала найдем дискриминант уравнения"
                                    f"({a})x^2 + {b}x + {c}\n2)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n3)Так как дискриминант "
                                    f"меньше нуля, то данное уравнение не имеет действительных корней\n4)Следовательно график этого "
                                    f"уравнения располложен ниже\nоси Ox(коэффицент a < 0), а так как у нас знак '{var}', то x ∈ ℝ")
                    else:
                        result = "Ответ: нет решений"
                        result_2 = (f"Ответ: нет решений\n \nПояснение:\n1)Сначала найдем дискриминант уравнения"
                                    f"({a})x^2 + {b}x + {c}\n2)D = b^2 - 4 * a * c = ({b})^2 - 4 * {a} * {c} = {D}\n3)Так как дискриминант "
                                    f"меньше нуля, то данное уравнение не имеет действительных корней\n4)Следовательно график этого "
                                    f"уравнения располложен ниже\nоси Ox(коэффицент a < 0), а так как у нас знак '{var}', то нет решений")
    except ValueError:
        result = "Введите все числовые значения"
    error(frame_answer)
    result = result.replace(".000", "")
    Label_answer = Label(frame_answer, text="", font=("Arial", 12), bg="white", justify='left')
    Label_answer.pack(side="left", anchor="nw")
    typewriter(Label_answer, result, delay=50)
    Button_voice = Button(frame_answer, text="Произнести голосом", bg="orange", command=lambda: voice(result))
    Button_voice.pack(side="right")

    def help(g):
        error(frame_answer)
        g = g.replace(".000", "")
        Label_answer = Label(frame_answer, text="", font=("Arial", 12), bg="white", justify='left')
        Label_answer.pack(side="left", anchor="nw")
        typewriter(Label_answer, g, delay=50)
        Button_voice = Button(frame_answer, text="Произнести голосом", bg="orange", command=lambda: voice(g))
        Button_voice.pack(side="right")
        Button_answer_not = Button(frame_answer, text="Убрать пояснение", bg="orange",
                                   command=lambda: quar_nerve_decide(a, b, c, var))
        Button_answer_not.pack(side="right")

    Button_answer = Button(frame_answer, text="Пояснение", bg="orange", command=lambda: help(result_2))
    Button_answer.pack(side="right")
    Button_ark = Button(frame_answer, text="Более точные значения x", bg="orange",
                        command=lambda: quar_nerve_decide_2(a, b, c, var))
    Button_ark.pack(side="right")


# Отвечает за построение линейной функции

def lin_function_decide(a, b):
    try:
        a, b = float(a), float(b)
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        # Данные для графика
        x = np.linspace(-10, 10, 1000)
        y = a * x + b

        # Строим график
        ax.plot(x, y, label=f'y = {a}x + {b}')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.legend()
        ax.grid(True)
        ax.set_ylim(-10, 10)
        ax.axhline(y=0, color='black', linewidth=1.5)
        ax.axvline(x=0, color='black', linewidth=1.5)
        error(frame_answer)

        canvas = FigureCanvasTkAgg(fig, master=frame_answer)
        canvas.draw()
        from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
        toolbar = NavigationToolbar2Tk(canvas, frame_answer)
        toolbar.update()

        # Упаковываем сначала toolbar, потом canvas
        toolbar.pack(side="top", fill="x")
        widget = canvas.get_tk_widget()
        widget.pack(fill="both", expand=True, padx=10, pady=10)
    except ValueError:
        error(frame_answer)
        Label_answer = Label(frame_answer, text="Ошибка: введите числовые значения", font=("Arial", 12), bg="white",
                             justify='left')
        Label_answer.pack(side="left", anchor="nw")



# Отвечает за построение графика квадратичной функции
def quar_function_decide(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        # Данные для графика
        x = np.linspace(-10, 10, 1000)
        y = a * x ** 2 + b * x + c

        # Строим график
        ax.plot(x, y, label=f'y = {a}x^2 + {b}x + {c}')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.legend()
        ax.grid(True)
        ax.set_ylim(-10, 10)
        ax.axhline(y=0, color='black', linewidth=1.5)
        ax.axvline(x=0, color='black', linewidth=1.5)
        error(frame_answer)

        canvas = FigureCanvasTkAgg(fig, master=frame_answer)
        canvas.draw()
        from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
        toolbar = NavigationToolbar2Tk(canvas, frame_answer)
        toolbar.update()

        # Упаковываем сначала toolbar, потом canvas
        toolbar.pack(side="top", fill="x")
        widget = canvas.get_tk_widget()
        widget.pack(fill="both", expand=True, padx=10, pady=10)
    except ValueError:
        error(frame_answer)
        Label_answer = Label(frame_answer, text="Ошибка: введите числовые значения", font=("Arial", 12), bg="white",
                             justify='left')
        Label_answer.pack(side="left", anchor="nw")


# Отвечает за интерфейс при выборе линеного уравнения
def lin_ur():
    error(frame_filling)
    error(frame_answer)
    Label_frame_filling_main_lin_ur = Label(frame_filling, text="Решение линейного уравнения",
                                            font=("Arial", 14, "bold"), bg="white")
    Label_frame_filling_main_lin_ur.pack(pady=10)
    Label_frame_filling_lin_ur = Label(frame_filling, text="Введите коэффиценты уравнения вида ax + b = 0:",
                                       font=("Arial", 10), bg="white")
    Label_frame_filling_lin_ur.pack(pady=5)
    frame_filling_1 = Frame(frame_filling, bg="white")
    frame_filling_1.pack(pady=20)
    Label_a = Label(frame_filling_1, text="a:", bg="white")
    Label_a.pack(side="left", padx=(15, 0))
    Entry_a = Entry(frame_filling_1, width=6, relief="sunken")
    Entry_a.pack(side="left", padx=(0, 0))
    Label_b = Label(frame_filling_1, text="b:", bg="white")
    Label_b.pack(side="left", padx=(40, 0))
    Entry_b = Entry(frame_filling_1, width=6, relief="sunken")
    Entry_b.pack(side="left", padx=(0, 20))
    frame_filling_2 = Frame(frame_filling, bg="white")
    frame_filling_2.pack(pady=20)
    Button_decide = Button(frame_filling_2, text="Решить", bg="green", width=15, fg="white", font=("Arial", 11),
                           command=lambda: lin_ur_decide(Entry_a.get(), Entry_b.get()))
    Button_decide.pack(side="left", pady=(0, 0), padx=(0, 0))


# Отвечает за интерфейс при выборе квадратного уравнения
def quar_ur():
    error(frame_filling)
    error(frame_answer)
    Label_frame_filling_main_quar_ur = Label(frame_filling, text="Решение квадратного уравнения",
                                             font=("Arial", 14, "bold"), bg="white")
    Label_frame_filling_main_quar_ur.pack(pady=10)
    Label_frame_filling_quar_ur = Label(frame_filling, text="Введите коэффиценты уравнения вида ax^2 + bx + c = 0:",
                                        font=("Arial", 10), bg="white")
    Label_frame_filling_quar_ur.pack(pady=5)
    frame_filling_1 = Frame(frame_filling, bg="white")
    frame_filling_1.pack(pady=20)
    Label_a = Label(frame_filling_1, text="a:", bg="white")
    Label_a.pack(side="left", padx=(0, 0))
    Entry_a = Entry(frame_filling_1, width=6, relief="sunken")
    Entry_a.pack(side="left", padx=(0, 0))
    Label_b = Label(frame_filling_1, text="b:", bg="white")
    Label_b.pack(side="left", padx=(30, 0))
    Entry_b = Entry(frame_filling_1, width=6, relief="sunken")
    Entry_b.pack(side="left", padx=(0, 30))
    Label_c = Label(frame_filling_1, text="c:", bg="white")
    Label_c.pack(side="left", padx=(0, 0))
    Entry_c = Entry(frame_filling_1, width=6, relief="sunken")
    Entry_c.pack(side="left", padx=(0, 0))
    frame_filling_2 = Frame(frame_filling, bg="white")
    frame_filling_2.pack(pady=20)
    Button_decide = Button(frame_filling_2, text="Решить", bg="green", width=15, fg="white", font=("Arial", 11),
                           command=lambda: quar_ur_decide(Entry_a.get(), Entry_b.get(), Entry_c.get()))
    Button_decide.pack(side="left", pady=(0, 0), padx=(0, 0))


# Отвечает за интерфейс при выборе линейного неравентсва
def lin_nerve():
    error(frame_filling)
    error(frame_answer)
    Label_frame_filling_main_lin_ur = Label(frame_filling, text="Решение линейного неравенства ",
                                            font=("Arial", 14, "bold"), bg="white")
    Label_frame_filling_main_lin_ur.pack(pady=10)
    Label_frame_filling_lin_ur = Label(frame_filling, text="Введите коэффиценты неравенства вида ax + b ? 0:",
                                       font=("Arial", 10), bg="white")
    Label_frame_filling_lin_ur.pack(pady=5)
    frame_filling_1 = Frame(frame_filling, bg="white")
    frame_filling_1.pack(pady=20)
    Label_a = Label(frame_filling_1, text="a:", bg="white")
    Label_a.pack(side="left", padx=(0, 0))
    Entry_a = Entry(frame_filling_1, width=6, relief="sunken")
    Entry_a.pack(side="left", padx=(0, 0))
    Label_b = Label(frame_filling_1, text="b:", bg="white")
    Label_b.pack(side="left", padx=(20, 0))
    Entry_b = Entry(frame_filling_1, width=6, relief="sunken")
    Entry_b.pack(side="left", padx=(0, 0))
    Label_sign = Label(frame_filling_1, text="Знак:", bg="white")
    Label_sign.pack(side="left", padx=(20, 0))
    var = StringVar(value=" ")
    Radiobutton_1 = Radiobutton(frame_filling_1, text=">", variable=var, value=">", bg="white")
    Radiobutton_1.pack(side="left")
    Radiobutton_2 = Radiobutton(frame_filling_1, text=">=", variable=var, value=">=", bg="white")
    Radiobutton_2.pack(side="left")
    Radiobutton_3 = Radiobutton(frame_filling_1, text="<", variable=var, value="<", bg="white")
    Radiobutton_3.pack(side="left")
    Radiobutton_4 = Radiobutton(frame_filling_1, text="<=", variable=var, value="<=", bg="white")
    Radiobutton_4.pack(side="left")
    frame_filling_2 = Frame(frame_filling, bg="white")
    frame_filling_2.pack(pady=20)
    Button_decide = Button(frame_filling_2, text="Решить", bg="green", width=15, fg="white", font=("Arial", 11),
                           command=lambda: lin_nerve_decide(Entry_a.get(), Entry_b.get(), var.get()))
    Button_decide.pack(side="left", pady=(0, 0), padx=(0, 0))


# Отвечает за интерфейс при выборе квадратного неравенства
def quar_nerve():
    error(frame_filling)
    error(frame_answer)
    Label_frame_filling_main_quar_ur = Label(frame_filling, text="Решение квадратного неравенства",
                                             font=("Arial", 14, "bold"), bg="white")
    Label_frame_filling_main_quar_ur.pack(pady=10)
    Label_frame_filling_quar_ur = Label(frame_filling,
                                        text="Введите коэффиценты неравенства вида ax^2 + bx + c ? 0:",
                                        font=("Arial", 10), bg="white")
    Label_frame_filling_quar_ur.pack(pady=5)
    frame_filling_1 = Frame(frame_filling, bg="white")
    frame_filling_1.pack(pady=20)
    Label_a = Label(frame_filling_1, text="a:", bg="white")
    Label_a.pack(side="left", padx=(0, 0))
    Entry_a = Entry(frame_filling_1, width=6, relief="sunken")
    Entry_a.pack(side="left", padx=(0, 0))
    Label_b = Label(frame_filling_1, text="b:", bg="white")
    Label_b.pack(side="left", padx=(30, 0))
    Entry_b = Entry(frame_filling_1, width=6, relief="sunken")
    Entry_b.pack(side="left", padx=(0, 30))
    Label_c = Label(frame_filling_1, text="c:", bg="white")
    Label_c.pack(side="left", padx=(0, 0))
    Entry_c = Entry(frame_filling_1, width=6, relief="sunken")
    Entry_c.pack(side="left", padx=(0, 0))
    Label_sign = Label(frame_filling_1, text="Знак:", bg="white")
    Label_sign.pack(side="left", padx=(20, 0))
    var = StringVar(value=" ")
    Radiobutton_1 = Radiobutton(frame_filling_1, text=">", variable=var, value=">", bg="white")
    Radiobutton_1.pack(side="left")
    Radiobutton_2 = Radiobutton(frame_filling_1, text=">=", variable=var, value=">=", bg="white")
    Radiobutton_2.pack(side="left")
    Radiobutton_3 = Radiobutton(frame_filling_1, text="<", variable=var, value="<", bg="white")
    Radiobutton_3.pack(side="left")
    Radiobutton_4 = Radiobutton(frame_filling_1, text="<=", variable=var, value="<=", bg="white")
    Radiobutton_4.pack(side="left")
    frame_filling_2 = Frame(frame_filling, bg="white")
    frame_filling_2.pack(pady=20)
    Button_decide = Button(frame_filling_2, text="Решить", bg="green", width=15, fg="white", font=("Arial", 11)
                           , command=lambda: quar_nerve_decide(Entry_a.get(), Entry_b.get(), Entry_c.get(),
                                                               var.get()))
    Button_decide.pack(side="left", pady=(0, 0), padx=(0, 0))


# Отвечает за создание интерфейса при выборе линейной функция
def lin_function():
    error(frame_filling)
    error(frame_answer)
    Label_frame_filling_main_lin_ur = Label(frame_filling, text="Построение графика линейной функции",
                                            font=("Arial", 14, "bold"), bg="white")
    Label_frame_filling_main_lin_ur.pack(pady=10)
    Label_frame_filling_lin_ur = Label(frame_filling, text="Введите коэффиценты функции вида y = ax + b",
                                       font=("Arial", 10), bg="white")
    Label_frame_filling_lin_ur.pack(pady=5)
    frame_filling_1 = Frame(frame_filling, bg="white")
    frame_filling_1.pack(pady=20)
    Label_a = Label(frame_filling_1, text="a:", bg="white")
    Label_a.pack(side="left", padx=(0, 0))
    Entry_a = Entry(frame_filling_1, width=6, relief="sunken")
    Entry_a.pack(side="left", padx=(0, 0))
    Label_b = Label(frame_filling_1, text="b:", bg="white")
    Label_b.pack(side="left", padx=(60, 0))
    Entry_b = Entry(frame_filling_1, width=6, relief="sunken")
    Entry_b.pack(side="left", padx=(0, 0))
    frame_filling_2 = Frame(frame_filling, bg="white")
    frame_filling_2.pack(pady=20)
    Button_decide = Button(frame_filling_2, text="Построить график", bg="orange", width=20, fg="white",
                           font=("Arial", 11), command=lambda: lin_function_decide(Entry_a.get(), Entry_b.get()))
    Button_decide.pack(side="left", pady=(0, 0), padx=(0, 0))


# Отвечает за создание интерфеса при выборе квадратичной функция
def quar_function():
    error(frame_filling)
    error(frame_answer)
    Label_frame_filling_main_quar_ur = Label(frame_filling, text="Построение графика квадратичной функции",
                                             font=("Arial", 14, "bold"), bg="white")
    Label_frame_filling_main_quar_ur.pack(pady=10)
    Label_frame_filling_quar_ur = Label(frame_filling, text="Введите коэффиценты функции вида y = ax^2 + bx + c",
                                        font=("Arial", 10), bg="white")
    Label_frame_filling_quar_ur.pack(pady=5)
    frame_filling_1 = Frame(frame_filling, bg="white")
    frame_filling_1.pack(pady=20)
    Label_a = Label(frame_filling_1, text="a:", bg="white")
    Label_a.pack(side="left", padx=(0, 0))
    Entry_a = Entry(frame_filling_1, width=6, relief="sunken")
    Entry_a.pack(side="left", padx=(0, 0))
    Label_b = Label(frame_filling_1, text="b:", bg="white")
    Label_b.pack(side="left", padx=(30, 0))
    Entry_b = Entry(frame_filling_1, width=6, relief="sunken")
    Entry_b.pack(side="left", padx=(0, 30))
    Label_c = Label(frame_filling_1, text="c:", bg="white")
    Label_c.pack(side="left", padx=(0, 0))
    Entry_c = Entry(frame_filling_1, width=6, relief="sunken")
    Entry_c.pack(side="left", padx=(0, 0))
    frame_filling_2 = Frame(frame_filling, bg="white")
    frame_filling_2.pack(pady=20)
    Button_decide = Button(frame_filling_2, text="Построить график", bg="orange", width=20, fg="white",
                           font=("Arial", 11),
                           command=lambda: quar_function_decide(Entry_a.get(), Entry_b.get(), Entry_c.get()))
    Button_decide.pack(side="left", pady=(0, 0), padx=(0, 0))


# Отвечает за создание начального интерфейса, который видит пользователь
frame_main = Frame(root, bg="#E6E6FA")
frame_main.pack(fill="both", expand=True)

Label_main = Label(frame_main, text="Алгебраист", font=("Arial", 18, "bold italic"), bg="#E6E6FA")
Label_main.pack(pady=10)

frame_choice = Frame(frame_main, borderwidth=0, relief="solid", bg="#E6E6FA", height=100)
frame_choice.pack(pady=(5, 10), padx=(10, 5), side="left", fill="y")
Label_frame_choice = Label(frame_choice, text="Выберите задачу:", font=("Arial", 13, "bold"), bg="#E6E6FA")
Label_frame_choice.pack(pady=(10, 0))
Label_frame_choice_ur = Label(frame_choice, text="Уравнения:", font=("Arial", 11, "bold"), bg="#E6E6FA")
Label_frame_choice_ur.pack(pady=(20, 0))
Button_frame_choice_lin_ur = Button(frame_choice, text="Линейное уравнение", font=("Arial", 10), bg="white",
                                    padx=17, pady=10, relief="flat", command=lin_ur)
Button_frame_choice_lin_ur.pack(pady=(15, 8))
Button_frame_choice_quad_ur = Button(frame_choice, text="Квадратное уравнение", font=("Arial", 10), bg="white",
                                     padx=11, pady=10, relief="flat", command=quar_ur)
Button_frame_choice_quad_ur.pack(pady=3)
Label_frame_choice_nerve = Label(frame_choice, text="Неравенства:", font=("Arial", 11, "bold"), bg="#E6E6FA")
Label_frame_choice_nerve.pack(pady=15)
Button_frame_choice_lin_nerve = Button(frame_choice, text="Линейное неравенство", font=("Arial", 10), bg="white",
                                       padx=11, pady=10, relief="flat", command=lin_nerve)
Button_frame_choice_lin_nerve.pack(pady=(0, 8))
Button_frame_choice_quad_nerve = Button(frame_choice, text="Квадратное неравенство", font=("Arial", 10), bg="white",
                                        padx=5, pady=10, relief="flat", command=quar_nerve)
Button_frame_choice_quad_nerve.pack(pady=3)
Label_frame_choice_nerve = Label(frame_choice, text="Функции:", font=("Arial", 11, "bold"), bg="#E6E6FA")
Label_frame_choice_nerve.pack(pady=15)
Button_frame_choice_lin_nerve = Button(frame_choice, text="Линейная функция", font=("Arial", 10), bg="white",
                                       padx=23, pady=10, relief="flat", command=lin_function)
Button_frame_choice_lin_nerve.pack(pady=(0, 8))
Button_frame_choice_quad_nerve = Button(frame_choice, text="Квадратичная функция", font=("Arial", 10), bg="white",
                                        padx=10, pady=10, relief="flat", command=quar_function)
Button_frame_choice_quad_nerve.pack(pady=3)

frame_filling = Frame(frame_main, borderwidth=0, relief="solid", bg="white", height=220)
frame_filling.pack(pady=(5, 10), padx=(5, 10), side="top", fill="both", expand=True)
frame_filling.pack_propagate(False)
frame_filling.grid_propagate(False)

frame_answer = Frame(frame_main, borderwidth=0, relief="solid", bg="white", width=1000, height=450)
frame_answer.pack(pady=(0, 10), padx=(5, 10), side="bottom", fill="both", expand=True)
frame_answer.pack_propagate(False)
frame_answer.grid_propagate(False)

# Запускаем программу
root.mainloop()
