#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:46:46 2026

@author: sab
"""

# Simulation of a falling body on Earth
ACCELERATION_G =  9.8 # m/s^2
TIME = 5.0 # seconds

def calculate_displacement(g, t):
    return 0.5 * g * (t ** 2)


print(f"Displacement after {TIME}s: {calculate_displacement(ACCELERATION_G, TIME)} meters")