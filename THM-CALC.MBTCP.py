#--
#-- ************************************************************************************************************:
#-- *********************************************** CALCULATE THM **********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2019.1.13                                                                                         :
#-- Script:   THM-CALC.MBTCP.py                                                                                 :
#-- Purpose:  A python script to calc the Transient Hydraulic Model by reading values from the SIM PLC Server.  :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ****************************************************:
#-- DEFINE PARAMES, CONFIGS, IMPORT MODULES & CLASSES   :
#-- ****************************************************:
from pymodbus.client.sync import ModbusTcpClient
import struct
import numpy as np
import matplotlib.pyplot as plt
#--
#-- DEFINE MBTCP CONNECTION PARAMETERS:
SERVER_HOST = '10.165.3.40'
SERVER_PORT = 10367
#--
#-- DEFINE  MBTCP REGISTER ADDRESSES:
DIAMETER_ADDR = 1000
LENGTH_ADDR = 1001
DENSITY_ADDR = 1002
VISCOSITY_ADDR = 1003
ROUGHNESS_ADDR = 1004
HEAT_CAPACITY_ADDR = 1005
THERMAL_CONDUCTIVITY_ADDR = 1006
FLOW_RATE_ADDR = 2000
INLET_TEMP_ADDR = 2001
OUTLET_TEMP_ADDR = 2002
INLET_PRESSURE_ADDR = 2003
OUTLET_PRESSURE_ADDR = 2004
#--
#-- INITIALIZE MBTCP CLIENT:
client = ModbusTcpClient(SERVER_HOST, SERVER_PORT)
#--
#-- CONNECT TO MBTCP SERVER:
client.connect()
#--
#-- READ VALUES FROM MBTCP REGISTERS:
diameter = struct.unpack('!f', client.read_holding_registers(DIAMETER_ADDR, 2).registers)[0]
length = struct.unpack('!f', client.read_holding_registers(LENGTH_ADDR, 2).registers)[0]
rho = struct.unpack('!f', client.read_holding_registers(DENSITY_ADDR, 2),registers)[0]
viscosity = struct.unpack('!f', client.read_holding_registers(VISCOSITY_ADDR, 2).registers)[0]
roughness = struct.unpack('!f', client.read_holding_registers(ROUGHNESS_ADDR, 2).registers)[0]
Cp = struct.unpack('!f', client.read_holding_registers(HEAT_CAPACITY_ADDR, 2).registers)[0]
k = struct.unpack('!f', client.read_holding_registers(THERMAL_CONDUCTIVITY_ADDR, 2).registers)[0]
V = struct.unpack('!f', client.read_holding_registers(FLOW_RATE_ADDR, 2).registers)[0]
T_in = struct.unpack('!f', client.read_holding_registers(INLET_TEMP_ADDR, 2).registers)[0]
T_out = struct.unpack('!f', client.read_holding_registers(OUTLET_TEMP_ADDR, 2).registers)[0]
P_in = struct.unpack('!f', client.read_holding_registers(INLET_PRESSURE_ADDR, 2).registers)[0]
P_out = struct.unpack('!f', client.read_holding_registers(OUTLET_PRESSURE_ADDR, 2).registers)[0]
#--
#-- DISSCONNECT FROM MBTCP SERVER:
client.close()
#--
#-- DEFINE ADDITIONAL PARAMETERS:
A = np.pi * diameter**2 / 4
t_step = 1
t_final = 100
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
f = 0.25 /
#--
#-- ****************************************************:
#-- END OF PYTHON SCRIPT                                :
#-- ****************************************************: