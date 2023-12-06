#--
#-- ************************************************************************************************************:
#-- ********************************************* THM PLC SIMULATOR ********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2020.1.17                                                                                         :
#-- Script:   THM-LIQ.PL.py                                                                                     :
#-- Purpose:  A python script Simulates a running PLC.                                                          :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ****************************************************:
#-- DEFINE PARAMES, CONFIGS, IMPORT MODULES & CLASSES   :
#-- ****************************************************:
pipe_length = float(input("Please enter the length of the pipeline in meters: ")) #length of the pipeline in meters
pipe_diameter = float(input("Please enter the diameter of the pipeline in meters: ")) #diameter of the pipeline in meters
liquid_density = float(input("Please enter the density of the liquid in kg/m^3: ")) #density of the liquid in kg/m^3
#-- 
#-- Calculate the volume of the pipeline
volume = (3.14*(pipe_diameter/2)**2)*pipe_length
#-- 
#-- Calculate the liquid in the pipeline
liquid_in_pipe = volume * liquid_density
#-- 
#-- Print the results
print("The volume of liquid in the pipeline is", round(liquid_in_pipe,2), "kg")
#--
#-- ****************************************************:
#-- END OF PYTHON SCRIPT                                :
#-- ****************************************************: