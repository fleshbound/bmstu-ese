
import matplotlib.pyplot as plt
from cocomo.cocomo import *
from cocomo.constants import *
import numpy as np  # Добавлено для усреднения данных и тепловых карт
from enum import Enum, auto
from dataclasses import dataclass


class StudySWCocomo:
    def __init__(self, size, mode: CocomoModes):
        self.size = size
        self.mode = mode
        self.cocomo = Cocomo(size, mode)

        self.levels = [
            "Очень низкий",
            "Низкий",
            "Номинальный",
            "Высокий",
            "Очень высокий"
        ]

        self.drivers_to_study = [
            Driver.TOOL,
            Driver.MODP,
            Driver.ACAP,
            Driver.PCAP,
        ]

        # Зафиксированные драйверы (кроме тех, что исследуем)
        self.fixed_drivers = {
            Driver.RELY: Level.NOMINAL,
            Driver.DATA: Level.NOMINAL,
            Driver.CPLX: Level.NOMINAL,
            Driver.TIME: Level.NOMINAL,
            Driver.STOR: Level.NOMINAL,
            Driver.VIRT: Level.NOMINAL,
            Driver.TURN: Level.NOMINAL,
            Driver.MODP: Level.NOMINAL,  # Важно! TOOL и MODP будем исследовать
            Driver.TOOL: Level.NOMINAL,  # Важно! TOOL и MODP будем исследовать
            Driver.SCED: Level.NOMINAL,
            Driver.ACAP: Level.NOMINAL,  # Важно! PCAP и ACAP будем исследовать
            Driver.AEXP: Level.NOMINAL,
            Driver.PCAP: Level.NOMINAL,  # Важно! PCAP и ACAP будем исследовать
            Driver.VEXP: Level.NOMINAL,
            Driver.LEXP: Level.NOMINAL,
        }

    def study_driver(self, driver: Driver, levels: list[Level]):
        """
        Изучает влияние заданного драйвера на трудоемкость и время разработки.

        Args:
            driver: Драйвер затрат для исследования (например, Driver.TOOL).
            levels: Список уровней для драйвера (например, [Level.VERY_LOW, Level.LOW, ...]).

        Returns:
            Кортеж из двух списков: (efforts, times).
            efforts: Список значений трудоемкости для каждого уровня драйвера.
            times: Список значений времени разработки для каждого уровня драйвера.
        """
        efforts = []
        times = []

        # Сохраняем исходные значения драйверов, чтобы восстановить их после исследования.
        original_driver_values = {}
        for fixed_driver, level in self.fixed_drivers.items():
            original_driver_values[fixed_driver] = self.cocomo.drivers[fixed_driver]  # Сохраняем числовые значения

        # Устанавливаем фиксированные значения для всех драйверов.
        for fixed_driver, level in self.fixed_drivers.items():
            self.cocomo.set_driver(fixed_driver, level)

        # Исследуем заданный драйвер
        for level in levels:
            self.cocomo.set_driver(driver, level)
            result = self.cocomo.get_results()
            efforts.append(result["effort_base"])
            times.append(result["time_base"])

        # Восстанавливаем значения драйверов после исследования.
        for fixed_driver, original_value in original_driver_values.items():
            self.cocomo.drivers[fixed_driver] = original_value  # Восстанавливаем числовые значения

        return efforts, times

    def run(self):
        """
        Запускает исследование влияния драйверов на трудоемкость и время разработки.
        """

        # Определяем уровни для исследования (от очень низкого до очень высокого)
        levels = [Level(i) for i in range(5)]

        # Исследуем каждый драйвер
        effort_results = {}
        times_results = {}
        for driver in self.drivers_to_study:
            efforts, times = self.study_driver(driver, levels)
            effort_results[driver] = efforts
            times_results[driver] = times

        # Рисуем графики
        self.graph(effort_results, times_results)

        # Проводим анализ "персонал vs среда"
        self.personnel_vs_environment()

        # Анализ RELY vs TIME (при высокой автоматизации)
        self.rely_vs_time()

    def graph(self, effort_results, times_results):
        """
        Строит графики зависимости трудоемкости и времени разработки от уровней драйверов.

        Args:
            effort_results: Словарь, содержащий результаты по трудоемкости (ключ - драйвер, значение - список трудоемкостей).
            times_results: Словарь, содержащий результаты по времени разработки (ключ - драйвер, значение - список времен разработки).
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))  # Создаем два подграфика в одной строке

        # Стили точек и линий для графиков
        styles = [
            {'marker': 'o', 'linestyle': '-'},  # TOOL
            {'marker': 's', 'linestyle': '--'}, # MODP
            {'marker': '^', 'linestyle': ':'},  # ACAP
            {'marker': 'x', 'linestyle': '-.'}  # PCAP
        ]

        # График для трудозатрат
        for i, driver in enumerate(self.drivers_to_study):
            driver_name = str(driver).split('.')[1]  # Получаем имя драйвера из Enum
            ax1.plot(self.levels, effort_results[driver], label=driver_name, **styles[i])

        ax1.set_xlabel("Уровень")
        ax1.set_ylabel("Трудозатраты")
        ax1.set_title("Влияние драйверов на трудозатраты")
        ax1.grid(True)
        ax1.legend()

        # График для времени разработки
        for i, driver in enumerate(self.drivers_to_study):
            driver_name = str(driver).split('.')[1]  # Получаем имя драйвера из Enum
            ax2.plot(self.levels, times_results[driver], label=driver_name, **styles[i])

        ax2.set_xlabel("Уровень")
        ax2.set_ylabel("Время разработки")
        ax2.set_title("Влияние драйверов на время разработки")
        ax2.grid(True)
        ax2.legend()

        plt.tight_layout()
        #plt.show()

    def personnel_vs_environment(self):
        """
        Анализирует, что больше влияет на сокращение срока: способности персонала или параметры среды.
        """

        # 1. Baseline (все драйверы на номинальном уровне)
        baseline_drivers = self.fixed_drivers.copy()  # Копия!
        baseline_drivers[Driver.ACAP] = Level.NOMINAL
        baseline_drivers[Driver.PCAP] = Level.NOMINAL
        baseline_drivers[Driver.MODP] = Level.NOMINAL
        baseline_drivers[Driver.TOOL] = Level.NOMINAL

        # Устанавливаем значения драйверов для базового сценария
        for driver, level in baseline_drivers.items():
            self.cocomo.set_driver(driver, level)
        baseline_results = self.cocomo.get_results()
        baseline_tm = baseline_results["time_base"]

        # 2. Улучшение способностей персонала (ACAP и PCAP до HIGH)
        personnel_drivers = self.fixed_drivers.copy()  # Копия!
        personnel_drivers[Driver.ACAP] = Level.HIGH
        personnel_drivers[Driver.PCAP] = Level.HIGH
        personnel_drivers[Driver.MODP] = Level.NOMINAL
        personnel_drivers[Driver.TOOL] = Level.NOMINAL

        # Устанавливаем значения драйверов для сценария "персонал"
        for driver, level in personnel_drivers.items():
            self.cocomo.set_driver(driver, level)
        personnel_results = self.cocomo.get_results()
        personnel_tm = personnel_results["time_base"]

        # 3. Улучшение среды (MODP и TOOL до HIGH)
        environment_drivers = self.fixed_drivers.copy()  # Копия!
        environment_drivers[Driver.ACAP] = Level.NOMINAL
        environment_drivers[Driver.PCAP] = Level.NOMINAL
        environment_drivers[Driver.MODP] = Level.HIGH
        environment_drivers[Driver.TOOL] = Level.HIGH

        # Устанавливаем значения драйверов для сценария "среда"
        for driver, level in environment_drivers.items():
            self.cocomo.set_driver(driver, level)
        environment_results = self.cocomo.get_results()
        environment_tm = environment_results["time_base"]

        print("\nАнализ влияния: персонал vs. среда (для сокращения срока):")
        print(f"Baseline TM: {baseline_tm:.2f} месяцев")
        print(f"TM при улучшении персонала: {personnel_tm:.2f} месяцев (снижение на {(baseline_tm - personnel_tm) / baseline_tm * 100:.2f}%)")
        print(f"TM при улучшении среды: {environment_tm:.2f} месяцев (снижение на {(baseline_tm - environment_tm) / baseline_tm * 100:.2f}%)")

        if personnel_tm < environment_tm:
            print("Улучшение способностей персонала эффективнее для сокращения срока.")
        else:
            print("Улучшение среды разработки эффективнее для сокращения срока.")

    def rely_vs_time(self):
        """
        Анализирует, что оказывает большее влияние на трудоемкость и время выполнения при высокой автоматизации:
        высокая надежность (RELY) или требование реального времени (TIME).
        """

        # 1. Высокая автоматизация (MODP и TOOL на HIGH)
        high_automation_drivers = self.fixed_drivers.copy()  # Копия!
        high_automation_drivers[Driver.MODP] = Level.HIGH
        high_automation_drivers[Driver.TOOL] = Level.HIGH
        high_automation_drivers[Driver.RELY] = Level.NOMINAL  # Добавляем RELY
        high_automation_drivers[Driver.TIME] = Level.NOMINAL  # Добавляем TIME

        # Устанавливаем значения драйверов для сценария "высокая автоматизация"
        for driver, level in high_automation_drivers.items():
            self.cocomo.set_driver(driver, level)
        high_automation_results = self.cocomo.get_results()
        high_automation_pm = high_automation_results["effort_base"]
        high_automation_tm = high_automation_results["time_base"]

        # 2. Высокая надежность (RELY на HIGH, при высокой автоматизации)
        rely_high_drivers = self.fixed_drivers.copy()  # Копия!
        rely_high_drivers[Driver.MODP] = Level.HIGH
        rely_high_drivers[Driver.TOOL] = Level.HIGH
        rely_high_drivers[Driver.RELY] = Level.HIGH  # RELY на HIGH
        rely_high_drivers[Driver.TIME] = Level.NOMINAL

        # Устанавливаем значения драйверов для сценария "высокая надежность"
        for driver, level in rely_high_drivers.items():
            self.cocomo.set_driver(driver, level)
        rely_high_results = self.cocomo.get_results()
        rely_high_pm = rely_high_results["effort_base"]
        rely_high_tm = rely_high_results["time_base"]

        # 3. Требование реального времени (TIME на HIGH, при высокой автоматизации)
        time_high_drivers = self.fixed_drivers.copy()  # Копия!
        time_high_drivers[Driver.MODP] = Level.HIGH
        time_high_drivers[Driver.TOOL] = Level.HIGH
        time_high_drivers[Driver.RELY] = Level.NOMINAL
        time_high_drivers[Driver.TIME] = Level.HIGH  # TIME на HIGH

        # Устанавливаем значения драйверов для сценария "требование реального времени"
        for driver, level in time_high_drivers.items():
            self.cocomo.set_driver(driver, level)
        time_high_results = self.cocomo.get_results()
        time_high_pm = time_high_results["effort_base"]
        time_high_tm = time_high_results["time_base"]

        print("\nВлияние RELY vs. TIME (высокая автоматизация):")
        print(f"Baseline PM (высокая автоматизация): {high_automation_pm:.2f} человеко-месяцев")
        print(f"Baseline TM (высокая автоматизация): {high_automation_tm:.2f} месяцев")
        print(f"PM при RELY = HIGH: {rely_high_pm:.2f} человеко-месяцев (изменение на {(rely_high_pm - high_automation_pm) / high_automation_pm * 100:.2f}%)")
        print(f"TM при RELY = HIGH: {rely_high_tm:.2f} месяцев (изменение на {(rely_high_tm - high_automation_tm) / high_automation_tm * 100:.2f}%)")
        print(f"PM при TIME = HIGH: {time_high_pm:.2f} человеко-месяцев (изменение на {(time_high_pm - high_automation_pm) / high_automation_pm * 100:.2f}%)")
        print(f"TM при TIME = HIGH: {time_high_tm:.2f} месяцев (изменение на {(time_high_tm - high_automation_tm) / high_automation_tm * 100:.2f}%)")

        if rely_high_pm > time_high_pm:
            print("RELY оказывает большее влияние на трудоемкость (при высокой автоматизации).")
        else:
            print("TIME оказывает большее влияние на трудоемкость (при высокой автоматизации).")

        if rely_high_tm > time_high_tm:
            print("RELY оказывает большее влияние на время разработки (при высокой автоматизации).")
        else:
            print("TIME оказывает большее влияние на время разработки (при высокой автоматизации).")


# Пример использования
if __name__ == "__main__":
    size = 100  # Размер программного кода в тысячах строк (KLOC)
    mode = CocomoModes.SEMIDETACHED  # Промежуточный тип проекта  !!!

    study = StudySWCocomo(size, mode)
    study.run()
