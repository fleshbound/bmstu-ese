
import tkinter as tk
from tkinter import ttk

# --- Основные настройки окна ---
root = tk.Tk()
root.title("Авдейкина Валерия ИУ7-83Б Л/Р №6 COCOMO")
# Размеры из PyQt ui-файла.  В tkinter это просто начальный размер.
root.geometry("2496x1021")
#root.configure(bg="#FFB6C1")  # Пастельно-розовый фон - Убрали розовый

# --- Создание и размещение виджетов ---

# --- GroupBox "Настройки модели COCOMO" (gbDrivers) ---
gb_drivers = ttk.LabelFrame(root, text="Настройки модели COCOMO", padding=10, labelanchor='nw')
gb_drivers.grid(row=0, column=0, rowspan=5, sticky="nsew", padx=5, pady=5)

# --- GroupBox "Атрибуты проекта" (gbProject) ---
gb_project = ttk.LabelFrame(gb_drivers, text="Атрибуты проекта", padding=5, labelanchor='nw')
gb_project.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

lbl_MODP = tk.Label(gb_project, text="MODP")
lbl_MODP.grid(row=0, column=0, padx=2, pady=2, sticky="w")
cb_MODP = ttk.Combobox(gb_project, state="readonly") #state="readonly"
cb_MODP.grid(row=0, column=1, padx=2, pady=2, sticky="ew")
modp_value = tk.IntVar()
dsb_MODP = tk.Spinbox(gb_project, from_=0.0, to=2.0, increment=0.05, textvariable=modp_value, state="readonly", width=5)
dsb_MODP.grid(row=0, column=2, padx=2, pady=2, sticky="e")

lbl_TOOL = tk.Label(gb_project, text="TOOL")
lbl_TOOL.grid(row=1, column=0, padx=2, pady=2, sticky="w")
cb_TOOL = ttk.Combobox(gb_project, state="readonly") #state="readonly"
cb_TOOL.grid(row=1, column=1, padx=2, pady=2, sticky="ew")
tool_value = tk.IntVar()
dsb_TOOL = tk.Spinbox(gb_project, from_=0.0, to=2.0, increment=0.05, textvariable=tool_value, state="readonly", width=5)
dsb_TOOL.grid(row=1, column=2, padx=2, pady=2, sticky="e")

lbl_SCED = tk.Label(gb_project, text="SCED")
lbl_SCED.grid(row=2, column=0, padx=2, pady=2, sticky="w")
cb_SCED = ttk.Combobox(gb_project, state="readonly") #state="readonly"
cb_SCED.grid(row=2, column=1, padx=2, pady=2, sticky="ew")
sced_value = tk.IntVar()
dsb_SCED = tk.Spinbox(gb_project, from_=0.0, to=2.0, increment=0.05, textvariable=sced_value, state="readonly", width=5)
dsb_SCED.grid(row=2, column=2, padx=2, pady=2, sticky="e")

# --- GroupBox "Атрибуты персонала" (gbStaff) ---
gb_staff = ttk.LabelFrame(gb_drivers, text="Атрибуты персонала", padding=5, labelanchor='nw')
gb_staff.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

lbl_ACAP = tk.Label(gb_staff, text="ACAP")
lbl_ACAP.grid(row=0, column=0, padx=2, pady=2, sticky="w")
cb_ACAP = ttk.Combobox(gb_staff, state="readonly") #state="readonly"
cb_ACAP.grid(row=0, column=1, padx=2, pady=2, sticky="ew")
acap_value = tk.IntVar()
dsb_ACAP = tk.Spinbox(gb_staff, from_=0.0, to=2.0, increment=0.05, textvariable=acap_value, state="readonly", width=5)
dsb_ACAP.grid(row=0, column=2, padx=2, pady=2, sticky="e")

lbl_AEXP = tk.Label(gb_staff, text="AEXP")
lbl_AEXP.grid(row=1, column=0, padx=2, pady=2, sticky="w")
cb_AEXP = ttk.Combobox(gb_staff, state="readonly") #state="readonly"
cb_AEXP.grid(row=1, column=1, padx=2, pady=2, sticky="ew")
aexp_value = tk.IntVar()
dsb_AEXP = tk.Spinbox(gb_staff, from_=0.0, to=2.0, increment=0.05, textvariable=aexp_value, state="readonly", width=5)
dsb_AEXP.grid(row=1, column=2, padx=2, pady=2, sticky="e")

lbl_PCAP = tk.Label(gb_staff, text="PCAP")
lbl_PCAP.grid(row=2, column=0, padx=2, pady=2, sticky="w")
cb_PCAP = ttk.Combobox(gb_staff, state="readonly") #state="readonly"
cb_PCAP.grid(row=2, column=1, padx=2, pady=2, sticky="ew")
pcap_value = tk.IntVar()
dsb_PCAP = tk.Spinbox(gb_staff, from_=0.0, to=2.0, increment=0.05, textvariable=pcap_value, state="readonly", width=5)
dsb_PCAP.grid(row=2, column=2, padx=2, pady=2, sticky="e")

lbl_VEXP = tk.Label(gb_staff, text="VEXP")
lbl_VEXP.grid(row=3, column=0, padx=2, pady=2, sticky="w")
cb_VEXP = ttk.Combobox(gb_staff, state="readonly") #state="readonly"
cb_VEXP.grid(row=3, column=1, padx=2, pady=2, sticky="ew")
vexp_value = tk.IntVar()
dsb_VEXP = tk.Spinbox(gb_staff, from_=0.0, to=2.0, increment=0.05, textvariable=vexp_value, state="readonly", width=5)
dsb_VEXP.grid(row=3, column=2, padx=2, pady=2, sticky="e")

lbl_LEXP = tk.Label(gb_staff, text="LEXP")
lbl_LEXP.grid(row=5, column=0, padx=2, pady=2, sticky="w")
cb_LEXP = ttk.Combobox(gb_staff, state="readonly") #state="readonly"
cb_LEXP.grid(row=5, column=1, padx=2, pady=2, sticky="ew")
lexp_value = tk.IntVar()
dsb_LEXP = tk.Spinbox(gb_staff, from_=0.0, to=2.0, increment=0.05, textvariable=lexp_value, state="readonly", width=5)
dsb_LEXP.grid(row=5, column=2, padx=2, pady=2, sticky="e")

# --- GroupBox "Атрибуты компьютера" (gbComputer) ---
gb_computer = ttk.LabelFrame(gb_drivers, text="Атрибуты компьютера", padding=5, labelanchor='nw')
gb_computer.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

lbl_TIME = tk.Label(gb_computer, text="TIME")
lbl_TIME.grid(row=0, column=0, padx=2, pady=2, sticky="w")
cb_TIME = ttk.Combobox(gb_computer, state="readonly") #state="readonly"
cb_TIME.grid(row=0, column=1, padx=2, pady=2, sticky="ew")
time_value = tk.IntVar()
dsb_TIME = tk.Spinbox(gb_computer, from_=0.0, to=2.0, increment=0.05, textvariable=time_value, state="readonly", width=5)
dsb_TIME.grid(row=0, column=2, padx=2, pady=2, sticky="e")

lbl_STOR = tk.Label(gb_computer, text="STOR")
lbl_STOR.grid(row=1, column=0, padx=2, pady=2, sticky="w")
cb_STOR = ttk.Combobox(gb_computer, state="readonly") #state="readonly"
cb_STOR.grid(row=1, column=1, padx=2, pady=2, sticky="ew")
stor_value = tk.IntVar()
dsb_STOR = tk.Spinbox(gb_computer, from_=0.0, to=2.0, increment=0.05, textvariable=stor_value, state="readonly", width=5)
dsb_STOR.grid(row=1, column=2, padx=2, pady=2, sticky="e")

lbl_VIRT = tk.Label(gb_computer, text="VIRT")
lbl_VIRT.grid(row=2, column=0, padx=2, pady=2, sticky="w")
cb_VIRT = ttk.Combobox(gb_computer, state="readonly") #state="readonly"
cb_VIRT.grid(row=2, column=1, padx=2, pady=2, sticky="ew")
virt_value = tk.IntVar()
dsb_VIRT = tk.Spinbox(gb_computer, from_=0.0, to=2.0, increment=0.05, textvariable=virt_value, state="readonly", width=5)
dsb_VIRT.grid(row=2, column=2, padx=2, pady=2, sticky="e")

lbl_TURN = tk.Label(gb_computer, text="TURN")
lbl_TURN.grid(row=3, column=0, padx=2, pady=2, sticky="w")
cb_TURN = ttk.Combobox(gb_computer, state="readonly") #state="readonly"
cb_TURN.grid(row=3, column=1, padx=2, pady=2, sticky="ew")
turn_value = tk.IntVar()
dsb_TURN = tk.Spinbox(gb_computer, from_=0.0, to=2.0, increment=0.05, textvariable=turn_value, state="readonly", width=5)
dsb_TURN.grid(row=3, column=2, padx=2, pady=2, sticky="e")

# --- GroupBox "Атрибуты программного продукта" (gbSW) ---
gb_sw = ttk.LabelFrame(gb_drivers, text="Атрибуты программного продукта", padding=5, labelanchor='nw')
gb_sw.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

lbl_RELY = tk.Label(gb_sw, text="RELY")
lbl_RELY.grid(row=0, column=0, padx=2, pady=2, sticky="w")
cb_RELY = ttk.Combobox(gb_sw, state="readonly") #state="readonly"
cb_RELY.grid(row=0, column=1, padx=2, pady=2, sticky="ew")
rely_value = tk.IntVar()
dsb_RELY = tk.Spinbox(gb_sw, from_=0.0, to=2.0, increment=0.05, textvariable=rely_value, state="readonly", width=5)
dsb_RELY.grid(row=0, column=2, padx=2, pady=2, sticky="e")

lbl_DATA = tk.Label(gb_sw, text="DATA")
lbl_DATA.grid(row=1, column=0, padx=2, pady=2, sticky="w")
cb_DATA = ttk.Combobox(gb_sw, state="readonly") #state="readonly"
cb_DATA.grid(row=1, column=1, padx=2, pady=2, sticky="ew")
data_value = tk.IntVar()
dsb_DATA = tk.Spinbox(gb_sw, from_=0.0, to=2.0, increment=0.05, textvariable=data_value, state="readonly", width=5)
dsb_DATA.grid(row=1, column=2, padx=2, pady=2, sticky="e")

lbl_CPLX = tk.Label(gb_sw, text="CPLX")
lbl_CPLX.grid(row=2, column=0, padx=2, pady=2, sticky="w")
cb_CPLX = ttk.Combobox(gb_sw, state="readonly") #state="readonly"
cb_CPLX.grid(row=2, column=1, padx=2, pady=2, sticky="ew")
cplx_value = tk.IntVar()
dsb_CPLX = tk.Spinbox(gb_sw, from_=0.0, to=2.0, increment=0.05, textvariable=cplx_value, state="readonly", width=5)
dsb_CPLX.grid(row=2, column=2, padx=2, pady=2, sticky="e")

# --- GroupBox "Режим модели COCOMO" (gbMode) ---
gb_mode = ttk.LabelFrame(gb_drivers, text="Режим модели COCOMO", padding=5, labelanchor='nw')
gb_mode.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

lbl_Mode = tk.Label(gb_mode, text="Режим")
lbl_Mode.grid(row=0, column=0, padx=2, pady=2, sticky="w")
cb_Mode = ttk.Combobox(gb_mode, state="readonly") #state="readonly"
cb_Mode.grid(row=0, column=1, padx=2, pady=2, sticky="ew")

# --- GroupBox "Уточняющий фактор" (gbEAF) ---
gb_eaf = ttk.LabelFrame(gb_drivers, text="Уточняющий фактор", padding=5, labelanchor='nw')
gb_eaf.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

lbl_EAF = tk.Label(gb_eaf, text="EAF")
lbl_EAF.grid(row=0, column=0, padx=2, pady=2, sticky="w")
eaf_value = tk.StringVar()
dsb_EAF = tk.Spinbox(gb_eaf, from_=0.0, to=1000.0, increment=0.05, state="disabled", width=5, textvariable=eaf_value) #disabled
dsb_EAF.grid(row=0, column=1, padx=2, pady=2, sticky="e")

# --- GroupBox "Влияние драйверов" (gbTask1) ---
gb_task1 = ttk.LabelFrame(gb_drivers, text="Влияние драйверов", padding=5, labelanchor='nw')
gb_task1.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)

btn_Study = tk.Button(gb_task1, text="Исследовать")
btn_Study.pack(padx=5, pady=5)

# --- GroupBox "Размер" (gbSize) ---
gb_size = ttk.LabelFrame(gb_drivers, text="Размер", padding=5, labelanchor='nw')
gb_size.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)

lbl_Size = tk.Label(gb_size, text="Размер")
lbl_Size.grid(row=0, column=0, padx=2, pady=2, sticky="w")
size_value = tk.IntVar()
size_value.set(400)
sb_Size = tk.Spinbox(gb_size, from_=0, to=1000, width=5, textvariable=size_value)
sb_Size.grid(row=0, column=1, padx=2, pady=2, sticky="ew")
lbl_KLOC = tk.Label(gb_size, text="KLOC")
lbl_KLOC.grid(row=0, column=2, padx=2, pady=2, sticky="w")


# --- Кнопка "Диаграмма привлечения сотрудников" (btnEmployees) ---
btn_employees = tk.Button(root, text="Диаграмма привлечения сотрудников")
btn_employees.grid(row=5, column=0, sticky="ew", padx=5, pady=5)

# --- GroupBox "Расчеты" (gbResultsGeneral) ---
gb_results_general = ttk.LabelFrame(root, text="Расчеты", padding=10, labelanchor='nw')
gb_results_general.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

# --- GroupBox "Трудозатраты" (gbEffort) ---
gb_effort = ttk.LabelFrame(gb_results_general, text="Трудозатраты", padding=5, labelanchor='nw')
gb_effort.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

lbl_C1 = tk.Label(gb_effort, text="C1")
lbl_C1.grid(row=0, column=0, padx=2, pady=2, sticky="w")
c1_value = tk.StringVar()
dsb_C1 = tk.Spinbox(gb_effort, from_=0.0, to=1000.0, increment=0.05, state="readonly", width=5, textvariable=c1_value) #disabled
dsb_C1.grid(row=0, column=1, padx=2, pady=2, sticky="e")

lbl_P1 = tk.Label(gb_effort, text="P1")
lbl_P1.grid(row=1, column=0, padx=2, pady=2, sticky="w")
p1_value = tk.StringVar()
dsb_P1 = tk.Spinbox(gb_effort, from_=0.0, to=1000.0, increment=0.05, state="readonly", width=5, textvariable=p1_value) #disabled
dsb_P1.grid(row=1, column=1, padx=2, pady=2, sticky="e")

lbl_EffortBase = tk.Label(gb_effort, text="Трудозатраты")
lbl_EffortBase.grid(row=0, column=3, padx=2, pady=2, sticky="w")
effort_base_value = tk.StringVar()
dsb_EffortBase = tk.Spinbox(gb_effort, from_=0.0, to=1000000.0, increment=0.05, state="readonly", width=10, textvariable=effort_base_value) #disabled
dsb_EffortBase.grid(row=1, column=3, padx=2, pady=2, sticky="e")

lbl_EffortPlan = tk.Label(gb_effort, text="+8%")
lbl_EffortPlan.grid(row=0, column=5, padx=2, pady=2, sticky="w")
effort_plan_value = tk.StringVar()
dsb_EffortPlan = tk.Spinbox(gb_effort, from_=0.0, to=1000000.0, increment=0.05, state="readonly", width=10, textvariable=effort_plan_value) #disabled
dsb_EffortPlan.grid(row=1, column=5, padx=2, pady=2, sticky="e")

lbl_EffortTotal = tk.Label(gb_effort, text="Всего")
lbl_EffortTotal.grid(row=0, column=6, padx=2, pady=2, sticky="w")
effort_total_value = tk.StringVar()
dsb_EffortTotal = tk.Spinbox(gb_effort, from_=0.0, to=1000000.0, increment=0.05, state="readonly", width=10, textvariable=effort_total_value) #disabled
dsb_EffortTotal.grid(row=1, column=6, padx=2, pady=2, sticky="e")

# --- GroupBox "Время" (gbTime) ---
gb_time = ttk.LabelFrame(gb_results_general, text="Время", padding=5, labelanchor='nw')
gb_time.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

lbl_C2 = tk.Label(gb_time, text="C2")
lbl_C2.grid(row=0, column=0, padx=2, pady=2, sticky="w")
c2_value = tk.StringVar()
dsb_C2 = tk.Spinbox(gb_time, from_=0.0, to=1000.0, increment=0.05, state="readonly", width=5, textvariable=c2_value) #disabled
dsb_C2.grid(row=0, column=1, padx=2, pady=2, sticky="e")

lbl_P2 = tk.Label(gb_time, text="P2")
lbl_P2.grid(row=1, column=0, padx=2, pady=2, sticky="w")
p2_value = tk.StringVar()
dsb_P2 = tk.Spinbox(gb_time, from_=0.0, to=1000.0, increment=0.05, state="readonly", width=5, textvariable=p2_value) #disabled
dsb_P2.grid(row=1, column=1, padx=2, pady=2, sticky="e")

lbl_TimeBase = tk.Label(gb_time, text="Время")
lbl_TimeBase.grid(row=0, column=3, padx=2, pady=2, sticky="w")
time_base_value = tk.StringVar()
dsb_TimeBase = tk.Spinbox(gb_time, from_=0.0, to=1000.0, increment=0.05, state="readonly", width=10, textvariable=time_base_value) #disabled
dsb_TimeBase.grid(row=1, column=3, padx=2, pady=2, sticky="e")

lbl_TimePlan = tk.Label(gb_time, text="+36%")
lbl_TimePlan.grid(row=0, column=4, padx=2, pady=2, sticky="w")
time_plan_value = tk.StringVar()
dsb_TimePlan = tk.Spinbox(gb_time, from_=0.0, to=1000.0, increment=0.05, state="readonly", width=10, textvariable=time_plan_value) #disabled
dsb_TimePlan.grid(row=1, column=4, padx=2, pady=2, sticky="e")

lbl_TimeTotal = tk.Label(gb_time, text="Всего")
lbl_TimeTotal.grid(row=0, column=5, padx=2, pady=2, sticky="w")
time_total_value = tk.StringVar()
dsb_TimeTotal = tk.Spinbox(gb_time, from_=0.0, to=1000.0, increment=0.05, state="readonly", width=10, textvariable=time_total_value) #disabled
dsb_TimeTotal.grid(row=1, column=5, padx=2, pady=2, sticky="e")

# --- GroupBox "Распределение работ" (gbDistribution) ---
gb_distribution = ttk.LabelFrame(root, text="Распределение работ", padding=10, labelanchor='nw')
gb_distribution.grid(row=1, column=1, rowspan=5, sticky="nsew", padx=5, pady=5)

# --- GroupBox "По стадиям жизненного цикла" (gbStages) ---
gb_stages = ttk.LabelFrame(gb_distribution, text="По стадиям жизненного цикла", padding=5, labelanchor='nw')
gb_stages.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

# Создание таблицы twStages
tw_stages = ttk.Treeview(gb_stages, columns=("test", "col1", "col2", "col3", "col4"), show='headings') #"test",
tw_stages.heading("test", text="")
tw_stages.heading("col1", text="Трудозатраты (%)")
tw_stages.heading("col2", text="Трудозатраты")
tw_stages.heading("col3", text="Время (%)")
tw_stages.heading("col4", text="Время")
tw_stages.insert("", tk.END, values=("Test", "8", "", "36", "")) #"Test",
tw_stages.insert("", tk.END, values=("Test", "18", "", "36", "")) #"Test",
tw_stages.insert("", tk.END, values=("Test", "25", "", "18", "")) #"Test",
tw_stages.insert("", tk.END, values=("Test", "26", "", "18", "")) #"Test",
tw_stages.insert("", tk.END, values=("Test", "31", "", "28", "")) #"Test",
tw_stages.insert("", tk.END, values=("Test", "100", "", "100", "")) #"Test",
tw_stages.insert("", tk.END, values=("Test", "108", "", "136", "")) #"Test",
tw_stages.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

# --- GroupBox "По видам деятельности" (gbActivities) ---
gb_activities = ttk.LabelFrame(gb_distribution, text="По видам деятельности", padding=5, labelanchor='nw')
gb_activities.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

# Создание таблицы twActivities
tw_activities = ttk.Treeview(gb_activities, columns=("test", "col1", "col2", "col3"), show='headings') #"test",
tw_activities.heading("test", text="")
tw_activities.heading("col1", text="Бюджет (%)")
tw_activities.heading("col2", text="Чел.-месяцы")
tw_activities.heading("col3", text="Затраты (тыс. руб)")
tw_activities.insert("", tk.END, values=("Test", "421231", "", "")) #"Test",
tw_activities.insert("", tk.END, values=("Test", "12", "", "")) #"Test",
tw_activities.insert("", tk.END, values=("Test", "44", "", "")) #"Test",
tw_activities.insert("", tk.END, values=("Test", "6", "", "")) #"Test",
tw_activities.insert("", tk.END, values=("Test", "14", "", "")) #"Test",
tw_activities.insert("", tk.END, values=("Test", "7", "", "")) #"Test",
tw_activities.insert("", tk.END, values=("Test", "7", "", "")) #"Test",
tw_activities.insert("", tk.END, values=("Test", "6", "", "")) #"Test",
tw_activities.insert("", tk.END, values=("Test", "100", "", "")) #"Test",

tw_activities.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

# --- Конфигурация строк и столбцов для адаптивности ---
# Чтобы виджеты растягивались вместе с окном
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)  # Больше места для "Распределения работ"

for i in range(6):
    root.rowconfigure(i, weight=1)

gb_drivers.columnconfigure(0, weight=1)
gb_drivers.columnconfigure(1, weight=1)
for i in range(4):
    gb_drivers.rowconfigure(i, weight=1)

gb_results_general.columnconfigure(0, weight=1)
gb_results_general.columnconfigure(1, weight=1)
gb_results_general.rowconfigure(0, weight=1)

gb_distribution.columnconfigure(0, weight=1)
gb_distribution.rowconfigure(0, weight=1)
gb_distribution.rowconfigure(1, weight=1)


# --- Главный цикл окна ---
#root.mainloop() #Перенесли в main.py
