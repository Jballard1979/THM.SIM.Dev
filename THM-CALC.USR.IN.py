#--
#-- ************************************************************************************************************:
#-- *********************************************** CALCULATE THM **********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2019.1.13                                                                                         :
#-- Script:   THM-CALC.USR.IN.py                                                                                :
#-- Purpose:  A python script Calculates the Transient Hydraulic Model using user inputs.                       :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#-- USER IMPUTS:
#-- pipe diameter, length, fluid density, viscosity, pipe roughness, heat capacity, thermal conductivity, 
#-- flow rate, inlet temperature, outlet temperature, inlet pressure, outlet pressure, time step, and final
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ****************************************************:
#-- DEFINE PARAMES, CONFIGS, IMPORT MODULES & CLASSES   :
#-- ****************************************************:
import numpy as np
import matplotlib.pyplot as plt
#--
#-- DEFINE PARAMETERS:
diameter = float(input("PLEASE PROVIDE THE PIPE DIAMETER IN METERS: "))
length = float(input("PLEASE PROVIDE THE PIPE LENGTH IN METERS: "))
rho = float(input("PLEASE PROVIDE FLUID DENSITY IN kg/m^3: "))
viscosity = float(input("PLEASE PROVIDE FLUID VISCOSITY IN Pa.s: "))
roughness = float(input("PLEASE PROVIDE THE PIPE ROUGHNESS IN METERS: "))
Cp = float(input("PLEASE PROVIDE HEAT CAPACITY OF THE FLUID IN J/kg.K: "))
k = float(input("PLEASE PROVIDE THE THERMAL CONDUCTIVITY OF THE FLUID IN W/m.K: "))
A = np.pi * diameter**2 / 4
V = float(input("PLEASE PROVIDE THE CURRENT FLOW RATE IN m^3/s: "))
T_in = float(input("PLEASE PROVIDE THE INLET TEMP IN CELSIUS:"))
T_out = float(input("PLEASE PROVIDE THE OUTLET TEMP IN CELSIUS: "))
P_in = float(input("PLEASE PROVIDE THE INLET PRESSURE IN Pa: "))
P_out = float(input("PLEASE PROVIDE THE OUTLET PRESSURE IN Pa: "))
t_step = float(input("PLEASE PROVIDE THE TIME STEP IN SECONDS: "))
t_final = float(input("PLEASE PROVIDE THE FINAL TIME IN SECONDS: "))
#--
#-- CONVERT TEMP FROM CELSIUS TO KELVIN:
T_in = T_in + 273.15
T_out = T_out + 273.15
#--
#-- INITIALIZE VARIABLES:
t = 0
Q = V / A
u = Q / (np.pi * diameter)
Re = rho * u * diameter / viscosity
f = 0.25 / np.log10((roughness / diameter / 3.7)**1.11 + 6.9 / Re)**2
P = P_in
T = T_in
dTdt = (Q * Cp * (T_out - T_in) - k * np.pi * diameter * (T - T_in) / length) / (rho * Cp * V)
#--
#-- CREATE ARRAYS TO STORE RESULTS:
time = [t]
pressure = [P]
temperature = [T]
#--
#-- CALCULATE MODEL:
while t < t_final:
    t += t_step
    Q = V / A
    u = Q / (np.pi * diameter)
    Re = rho * u * diameter / viscosity
    f = 0.25 / np.log10((roughness / diameter / 3.7)**1.11 + 6.9 / Re)**2
    dPdx = -f * rho * u**2 / 2
    P += dPdx * length
    dTdt = (Q * Cp * (T_out - T) - k * np.pi * diameter * (T - T_in) / length) / (rho * Cp * V)
    T += dTdt * t_step
    time.append(t)
    pressure.append(P)
    temperature.append(T)
#--
#-- PLOT RESULTS:
plt.subplot(2, 1, 1)
plt.plot(time, pressure)
plt.xlabel('Time (s)')
plt.ylabel('Pressure (Pa)')
plt.title('Transient Liquid Hydraulic Model')
#--
plt.subplot(2, 1, 2)
plt.plot(time, temperature)
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
#--
plt.show()
#--
#-- ****************************************************:
#-- END OF PYTHON SCRIPT                                :
#-- ****************************************************: