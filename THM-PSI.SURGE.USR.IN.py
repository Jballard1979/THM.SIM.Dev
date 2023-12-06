#--
#-- ************************************************************************************************************:
#-- *********************************************** THM PSI SURGE **********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2019.3.07                                                                                         :
#-- Script:   THM-PSI.SURGE.USR.IN.py                                                                           :
#-- Purpose:  A python script to calc PSI Surges in a liquid Pipeline using inputs from user.                   :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ****************************************************:
#-- DEFINE PARAMES, CONFIGS, IMPORT MODULES & CLASSES   :
#-- ****************************************************:
import math
#--
def calculate_pressure_surges(p1, p2, v, c, l, t):
    """
    Calculates pressure surges in a liquid pipeline using the method of characteristics.
    p1: initial pressure (psi)
    p2: final pressure (psi)
    v: fluid velocity (ft/s)
    c: sonic velocity (ft/s)
    l: pipeline length (ft)
    t: pipeline transit time (s)
    """
    dp = p2 - p1
    d1 = (dp + math.sqrt(dp**2 + 4*c**2*(v**2))) / (2*c**2)
    d2 = (dp - math.sqrt(dp**2 + 4*c**2*(v**2))) / (2*c**2)
    a = l / (t*v)
    b = c**2 / (v**2)
    #--
    if d1 > t:
        p_max = p1 + v*c*(d1-t) - a*b*dp*math.exp(-b*(d1-t))
    else:
        p_max = p1 + v*c*(t-d2) + a*b*dp*math.exp(-b*(t-d2))
    return p_max
#--
#-- RETRIEVE INPUTS FROM USER:
p1 = float(input("Enter the initial pressure (psi): "))
p2 = float(input("Enter the final pressure (psi): "))
v = float(input("Enter the fluid velocity (ft/s): "))
c = float(input("Enter the sonic velocity (ft/s): "))
l = float(input("Enter the pipeline length (ft): "))
t = float(input("Enter the pipeline transit time (s): "))
#--
#-- CALL FUNCTION TO CALC PSI SURGES:
p_max = calculate_pressure_surges(p1, p2, v, c, l, t)
#--
#-- PRINT RESULTS:
print("THE MAXIMUM PSI SURGE IS", round(p_max, 2), "PSI:")
#--
#-- ****************************************************:
#-- END OF PYTHON SCRIPT                                :
#-- ****************************************************: