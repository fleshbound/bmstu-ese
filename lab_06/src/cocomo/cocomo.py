import math

from cocomo.constants import *

class Cocomo:
    def __init__(self, kloc, mode):
        self.drivers = {
            Driver.RELY : DriversCoeffs.get_coef(Driver.RELY),
            Driver.DATA : DriversCoeffs.get_coef(Driver.DATA),
            Driver.CPLX : DriversCoeffs.get_coef(Driver.CPLX),

            Driver.TIME : DriversCoeffs.get_coef(Driver.TIME),
            Driver.STOR : DriversCoeffs.get_coef(Driver.STOR),
            Driver.VIRT : DriversCoeffs.get_coef(Driver.VIRT),
            Driver.TURN : DriversCoeffs.get_coef(Driver.TURN),

            Driver.MODP : DriversCoeffs.get_coef(Driver.MODP),
            Driver.TOOL : DriversCoeffs.get_coef(Driver.TOOL),
            Driver.SCED : DriversCoeffs.get_coef(Driver.SCED),

            Driver.ACAP : DriversCoeffs.get_coef(Driver.ACAP),
            Driver.AEXP : DriversCoeffs.get_coef(Driver.AEXP),
            Driver.PCAP : DriversCoeffs.get_coef(Driver.PCAP),
            Driver.VEXP : DriversCoeffs.get_coef(Driver.VEXP),
            Driver.LEXP : DriversCoeffs.get_coef(Driver.LEXP)
        }

        self.size = kloc
        self.mode = MODES[mode]

    @property
    def eaf(self):
        return math.prod(self.drivers.values())

    @property
    def effort_base(self):
        return self.mode.c1 * self.eaf * self.size ** self.mode.p1

    @property
    def time_base(self):
        return self.mode.c2 * self.effort_base ** self.mode.p2

    @property
    def effort_plan(self):
        return 0.08 * self.effort_base

    @property
    def time_plan(self):
        return 0.36 * self.time_base

    @property
    def effort_total(self):
        return self.effort_base + self.effort_plan

    @property
    def time_total(self):
        return self.time_base + self.time_plan
    
    def set_mode(self, mode):
        self.mode = MODES[mode]

    def get_results(self):
        return {
                "eaf" : self.eaf,
                "mode" : self.mode,
                "effort_base" : self.effort_base,
                "time_base" : self.time_base,
                "effort_plan" : self.effort_plan,
                "time_plan" : self.time_plan,
                "effort_total" : self.effort_total,
                "time_total" : self.time_total,
                }

    def set_drivers(self, drivers: dict):
        for key, values in drivers.items():
            self.drivers[key] = value

    def set_driver(self, driver, level):
        self.drivers[driver] = DriversCoeffs.get_coef(driver, level)

    def get_driver(self, driver):
        return self.drivers[driver]

    def set_size(self, size):
        self.size = size

    def get_employees(self):
        if self.time_base == 0:
            return [], [], []

        effort = self.effort_base
        time = self.time_base

        times = [
            0.36 * time,
            0.36 * time,
            0.18 * time,
            0.18 * time,
            0.28 * time
        ]

        efforts = [
            0.08 * effort,
            0.18 * effort,
            0.25 * effort,
            0.26 * effort,
            0.31 * effort
        ]

        employees = [int(e / t) + 1 for t, e in zip(times, efforts)]

        return employees, efforts, times

