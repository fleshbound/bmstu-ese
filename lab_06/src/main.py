import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Импортируем GUI, созданный в code.py (tkinter)
import code  # Предполагается, что code.py содержит код tkinter GUI

# Импортируем константы и классы из cocomo (нужно будет адаптировать)
from cocomo.constants import *
from cocomo.cocomo import *
from study.study import *


# Глобальные переменные (избегайте их, если возможно, используйте для отладки)
cocomo_instance = None # Объявляем глобальную переменную

# --- Таблицы соответствия уровней и значений атрибутов ---
attribute_values = {
    "RELY": {"Очень низкий": 0.75, "Низкий": 0.86, "Номинальный": 1.0, "Высокий": 1.15, "Очень высокий": 1.4},
    "DATA": {"Низкий": 0.94, "Номинальный": 1.0, "Высокий": 1.08, "Очень высокий": 1.16},
    "CPLX": {"Очень низкий": 0.7, "Низкий": 0.85, "Номинальный": 1.0, "Высокий": 1.15, "Очень высокий": 1.3},
    "TIME": {"Номинальный": 1.0, "Высокий": 1.11, "Очень высокий": 1.5},
    "STOR": {"Номинальный": 1.0, "Высокий": 1.06, "Очень высокий": 1.21},
    "VIRT": {"Низкий": 0.87, "Номинальный": 1.0, "Высокий": 1.15, "Очень высокий": 1.3},
    "TURN": {"Низкий": 0.87, "Номинальный": 1.0, "Высокий": 1.07, "Очень высокий": 1.15},
    "ACAP": {"Очень низкий": 1.46, "Низкий": 1.19, "Номинальный": 1.0, "Высокий": 0.86, "Очень высокий": 0.71},
    "AEXP": {"Очень низкий": 1.29, "Низкий": 1.15, "Номинальный": 1.0, "Высокий": 0.91, "Очень высокий": 0.82},
    "PCAP": {"Очень низкий": 1.42, "Низкий": 1.17, "Номинальный": 1.0, "Высокий": 0.86, "Очень высокий": 0.7},
    "VEXP": {"Очень низкий": 1.21, "Низкий": 1.1, "Номинальный": 1.0, "Высокий": 0.9},
    "LEXP": {"Очень низкий": 1.14, "Низкий": 1.07, "Номинальный": 1.0, "Высокий": 0.95},
    "MODP": {"Очень низкий": 1.24, "Низкий": 1.1, "Номинальный": 1.0, "Высокий": 0.91, "Очень высокий": 0.82},
    "TOOL": {"Очень низкий": 1.24, "Низкий": 1.1, "Номинальный": 1.0, "Высокий": 0.91, "Очень высокий": 0.82},
    "SCED": {"Очень низкий": 1.23, "Низкий": 1.08, "Номинальный": 1.0, "Высокий": 1.04, "Очень высокий": 1.1},
}

def build_chart():
    global cocomo_instance  # Используем глобальную переменную

    def addlabels(months, empls):
        for m, e in zip(months, empls):
            plt.text(m, e, e)

    employees, _, times = cocomo_instance.get_employees()

    months = []
    numbers = []
    for e, t in zip(employees, times):
        prev = len(months)
        duration = int(round(t))

        months.extend([i + prev + 1 for i in range(duration)])
        numbers.extend([e for i in range(duration)])

    # Создаем фигуру и оси Matplotlib
    fig, ax = plt.subplots()
    ax.bar(months, numbers)
    ax.set_xlabel("Месяц")
    ax.set_xticks(months)
    ax.set_ylabel("Число привлеченных сотрудников")
    addlabels(months, numbers)
    #plt.show()  # Не используем plt.show() в tkinter

    # Создаем новое окно
    chart_window = tk.Toplevel(code.root)
    chart_window.title("Диаграмма привлечения сотрудников")

    # Создаем виджет FigureCanvasTkAgg для интеграции с tkinter
    canvas = FigureCanvasTkAgg(fig, master=chart_window)
    canvas.draw()

    # Размещаем виджет FigureCanvasTkAgg в новом окне
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def update_tables():
    global cocomo_instance
    results = cocomo_instance.get_results()
    effort_base = results["effort_base"]
    time_base = results["time_base"]
    effort_total = results["effort_total"]

    # Обновление таблицы twStages
    for i, item in enumerate(code.tw_stages.get_children()):
        effort = effort_base * int(stages_data[i][1]) / 100
        time = time_base * int(stages_data[i][3]) / 100
        code.tw_stages.item(item, values=(stages_data[i][0], stages_data[i][1], "{:.2f}".format(effort), stages_data[i][3], "{:.2f}".format(time)))

    # Обновление таблицы twActivities, средняя з/п 180
    analyst = 160000
    manager = 140000
    architect = 250000
    teamlead = 220000
    developer = 165000
    qa_engineer = 150000

    price = (analyst + manager + architect + teamlead + developer + qa_engineer) / 6 / 1000

    for i, item in enumerate(code.tw_activities.get_children()):
        effort = effort_total * int(activities_data[i][1]) / 100
        price_value = effort * price
        code.tw_activities.item(item, values=(activities_data[i][0], activities_data[i][1], "{:.2f}".format(effort), "{:.2f}".format(price_value)))

def update_size():
    global cocomo_instance  # Используем глобальную переменную
    global modes

    try:
        new_size = int(code.size_value.get())
    except Exception as e:
        print(f'Ошибка получения KLOC, {str(e)}')
        return
    
    if new_size < 50:
        mode_index = CocomoModes.ORGANIC
    elif 50 <= new_size <= 500:
        mode_index = CocomoModes.SEMIDETACHED
    else:
        mode_index = CocomoModes.EMBEDDED
        
    cocomo_instance.set_size(new_size)  # Получаем значение из Spinbox
    cocomo_instance.set_mode(CocomoModes(mode_index))
    code.cb_Mode.set(modes[mode_index.value])
    update_effort_base() # Добавлено обновление трудозатрат после изменения размера
    update_time_base() # Добавлено обновление времени после изменения размера
    update_all()
    update_tables()

def update_effort_base():
    global cocomo_instance
    effort_base = cocomo_instance.get_results()["effort_base"]
    code.effort_base_value.set(str(int(effort_base)))

def update_time_base():
    global cocomo_instance
    time_base = cocomo_instance.get_results()["time_base"]
    code.time_base_value.set(str(int(time_base)))

def update_all():
    global cocomo_instance
    results = cocomo_instance.get_results()

    effort_plan = results["effort_plan"]
    effort_total = results["effort_total"]

    time_base = results["time_base"]
    time_plan = results["time_plan"]
    time_total = results["time_total"]

    code.effort_plan_value.set(str(int(effort_plan)))
    code.effort_total_value.set(str(int(effort_total)))

    code.time_base_value.set(str(int(time_base)))
    code.time_plan_value.set(str(int(time_plan)))
    code.time_total_value.set(str(int(time_total)))


def change_cocomo_coefs():
    global cocomo_instance
    
    mode_index = code.cb_Mode.current()

    cocomo_instance.set_mode(CocomoModes(mode_index))

    mode = cocomo_instance.get_results()["mode"]

    code.c1_value.set(str(mode.c1))
    code.p1_value.set(str(mode.p1))
    code.c2_value.set(str(mode.c2))
    code.p2_value.set(str(mode.p2))    
    update_effort_base() # Добавлено обновление трудозатрат после изменения размера
    update_time_base() # Добавлено обновление времени после изменения размера
    update_all()
    update_tables()


#def sync_driver_sb(combox, spinbox, driver, nominal):
 #   global cocomo_instance  # Используем глобальную переменную
  #  index = combox.current()#TODO: разобраться, как правильно брать индекс

   # cocomo_instance.set_driver(driver, Level(2 - nominal + index))
    #value = cocomo_instance.get_driver(driver)

    #spinbox.delete(0, tk.END)
    #spinbox.insert(0, value)

def update_eaf():
     global cocomo_instance  # Используем глобальную переменную
     # code.dsb_EAF.delete(0, tk.END)
     code.eaf_value.set(str(cocomo_instance.get_results()['eaf']))
     # code.dsb_EAF.insert(0, cocomo_instance.get_results()["eaf"])

def run_study():
    #StudySWCocomo(250, CocomoModes.SEMIDETACHED).run(Level.NOMINAL)
    #StudySWCocomo(250, CocomoModes.SEMIDETACHED).run(Level.HIGH)
    #StudySWCocomo(250, CocomoModes.SEMIDETACHED).run(Level.VERY_HIGH)
    StudySWCocomo(250, CocomoModes.SEMIDETACHED).run()
    plt.show()


# --- Инициализация ---
def initialize():
    global cocomo_instance  # Используем глобальную переменную

    # 1. Создаем экземпляр Cocomo с начальными значениями
    cocomo_instance = Cocomo(int(code.size_value.get()), CocomoModes.ORGANIC)  # Используем code.sb_Size

    # 2. Заполняем выпадающие списки (Comboboxes) и устанавливаем начальные значения
    attribute_names = [
        "RELY", "DATA", "CPLX", "TIME", "STOR", "VIRT", "TURN",
        "MODP", "TOOL", "SCED", "ACAP", "AEXP", "PCAP", "VEXP", "LEXP"
    ]

    driver_comboboxes = [
        code.cb_RELY,
        code.cb_DATA,
        code.cb_CPLX,
        code.cb_TIME,
        code.cb_STOR,
        code.cb_VIRT,
        code.cb_TURN,
        code.cb_MODP,
        code.cb_TOOL,
        code.cb_SCED,
        code.cb_ACAP,
        code.cb_AEXP,
        code.cb_PCAP,
        code.cb_VEXP,
        code.cb_LEXP,
    ]

    driver_spinboxes = [
        code.dsb_RELY,
        code.dsb_DATA,
        code.dsb_CPLX,
        code.dsb_TIME,
        code.dsb_STOR,
        code.dsb_VIRT,
        code.dsb_TURN,
        code.dsb_MODP,
        code.dsb_TOOL,
        code.dsb_SCED,
        code.dsb_ACAP,
        code.dsb_AEXP,
        code.dsb_PCAP,
        code.dsb_VEXP,
        code.dsb_LEXP,
    ]

    # Словарь для хранения переменных IntVar для каждого атрибута
    attribute_vars = {
        "RELY": code.rely_value,
        "DATA": code.data_value,
        "CPLX": code.cplx_value,
        "TIME": code.time_value,
        "STOR": code.stor_value,
        "VIRT": code.virt_value,
        "TURN": code.turn_value,
        "MODP": code.modp_value,
        "TOOL": code.tool_value,
        "SCED": code.sced_value,
        "ACAP": code.acap_value,
        "AEXP": code.aexp_value,
        "PCAP": code.pcap_value,
        "VEXP": code.vexp_value,
        "LEXP": code.lexp_value,
    }

    for i, (attribute_name, combox) in enumerate(zip(attribute_names, driver_comboboxes)):
        # Получаем доступные значения для текущего атрибута
        available_values = list(attribute_values[attribute_name].keys())
        combox['values'] = available_values  # Заполняем ComboBox значениями
        combox.set("Номинальный")  # Устанавливаем "Номинальный" по умолчанию

        # Устанавливаем начальное значение IntVar
        attribute_vars[attribute_name].set(attribute_values[attribute_name]["Номинальный"])


        # Создаем lambda-функцию для каждого ComboBox
        f = lambda event, idx=i: sync_driver(attribute_names[idx], i) #Убрали лишние параметры
        combox.bind("<<ComboboxSelected>>", f)  # Привязываем событие выбора к функции

    global modes 
    modes = ["Обычный", "Промежуточный", "Встроенный"]
    code.cb_Mode['values'] = modes
    code.cb_Mode.set("Промежуточный")  # Выберем "Промежуточный" по умолчанию
    code.cb_Mode.bind("<<ComboboxSelected>>", lambda event: change_cocomo_coefs())

    # 3. Устанавливаем обработчики событий для кнопок и других виджетов
    #code.sb_Size.bind("<KeyRelease>", lambda event: update_size()) #Странно работает. Надо фиксить
    code.btn_employees.config(command=build_chart)
    code.btn_Study.config(command=run_study)

    # 4. Вызываем функции для начального обновления интерфейса
    change_cocomo_coefs()
    update_effort_base()
    update_time_base()
    update_eaf()
    update_all()
    update_tables()

    code.sb_Size.bind("<KeyRelease>", lambda event: update_size())


def sync_driver(attribute_name, index): #Убрали лишние параметры
    global cocomo_instance

    # Получаем выбранное значение из Combobox
    selected_value = get_combobox_value(attribute_name)

    # Получаем числовое значение из таблицы
    numerical_value = attribute_values[attribute_name][selected_value]

    # Устанавливаем значение IntVar (это автоматически обновит Spinbox)
    set_intvar_value(attribute_name, numerical_value)
    cocomo_instance.drivers[index] = numerical_value
    update_effort_base()
    update_time_base()
    update_eaf()
    update_all()
    update_tables()

def get_combobox_value(attribute_name):
    if attribute_name == "RELY":
        return code.cb_RELY.get()
    elif attribute_name == "DATA":
        return code.cb_DATA.get()
    elif attribute_name == "CPLX":
        return code.cb_CPLX.get()
    elif attribute_name == "TIME":
        return code.cb_TIME.get()
    elif attribute_name == "STOR":
        return code.cb_STOR.get()
    elif attribute_name == "VIRT":
        return code.cb_VIRT.get()
    elif attribute_name == "TURN":
        return code.cb_TURN.get()
    elif attribute_name == "MODP":
        return code.cb_MODP.get()
    elif attribute_name == "TOOL":
        return code.cb_TOOL.get()
    elif attribute_name == "SCED":
        return code.cb_SCED.get()
    elif attribute_name == "ACAP":
        return code.cb_ACAP.get()
    elif attribute_name == "AEXP":
        return code.cb_AEXP.get()
    elif attribute_name == "PCAP":
        return code.cb_PCAP.get()
    elif attribute_name == "VEXP":
        return code.cb_VEXP.get()
    elif attribute_name == "LEXP":
        return code.cb_LEXP.get()

def set_intvar_value(attribute_name, value):
    if attribute_name == "RELY":
        code.rely_value.set(value)
    elif attribute_name == "DATA":
        code.data_value.set(value)
    elif attribute_name == "CPLX":
        code.cplx_value.set(value)
    elif attribute_name == "TIME":
        code.time_value.set(value)
    elif attribute_name == "STOR":
        code.stor_value.set(value)
    elif attribute_name == "VIRT":
        code.virt_value.set(value)
    elif attribute_name == "TURN":
        code.turn_value.set(value)
    elif attribute_name == "MODP":
        code.modp_value.set(value)
    elif attribute_name == "TOOL":
        code.tool_value.set(value)
    elif attribute_name == "SCED":
        code.sced_value.set(value)
    elif attribute_name == "ACAP":
        code.acap_value.set(value)
    elif attribute_name == "AEXP":
        code.aexp_value.set(value)
    elif attribute_name == "PCAP":
        code.pcap_value.set(value)
    elif attribute_name == "VEXP":
        code.vexp_value.set(value)
    elif attribute_name == "LEXP":
        code.lexp_value.set(value)



# Данные для таблиц, так как напрямую из UI их не получить
stages_data = [
    ("Планирование", "8", "", "36", ""),
    ("Проектирование", "18", "", "36", ""),
    ("Детальное проектирование", "25", "", "18", ""),
    ("Кодирование и тестирование", "26", "", "18", ""),
    ("Интеграция и тестирование", "31", "", "28", ""),
    ("ИТОГО (без планирования)", "100", "", "100", ""),
    ("ИТОГО", "108", "", "136", ""),
]

activities_data = [
    ("Анализ требований", "4", "", ""),
    ("Проектирование продукта", "12", "", ""),
    ("Программирование", "44", "", ""),
    ("Тестирование", "6", "", ""),
    ("Верификация", "14", "", ""),
    ("Канцелярия", "7", "", ""),
    ("Управление конфигурацией", "7", "", ""),
    ("Создание руководств", "6", "", ""),
    ("ИТОГО", "100", "", ""),
]

# --- Запуск программы ---
if __name__ == "__main__":
    initialize()  # Инициализация
    code.root.mainloop()  # Запуск основного цикла tkinter (из code.py)
