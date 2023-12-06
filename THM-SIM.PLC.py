#--
#-- ************************************************************************************************************:
#-- ********************************************* THM PLC SIMULATOR ********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2020.1.17                                                                                         :
#-- Script:   THM-SIM.PLC.py                                                                                    :
#-- Purpose:  A python script Simulates a running PLC.                                                          :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ****************************************************:
#-- DEFINE PARAMES, CONFIGS, IMPORT MODULES & CLASSES   :
#-- ****************************************************:
#-- DEFINE OUTPUT & INPUT SIGNALS:
input1 = False
input2 = False
input3 = False
output1 = False
output2 = False
#--
#-- DEFINE PLC LOGIC:
def plc_logic():
    global input1, input2, input3, output1, output2
    if input1 and input2:
        output1 = True
    else:
        output1 = False
    if input3:
        output2 = True
    else:
        output2 = False
#--
#-- DEFINE LOOP TO SIMULATE PLC:
while True:
    #--
    #-- READ INPUT SIGNALS:
    input1 = bool(int(input("ENTER INPUT 1 (0 or 1): ")))
    input2 = bool(int(input("ENTER INPUT 2 (0 or 1): ")))
    input3 = bool(int(input("ENTER INPUT 3 (0 or 1): ")))
    #--
    #-- EXECUTE PLC LOGIC:
    plc_logic()
    #--
    #-- PRINT OUTPUT SIGNALS:
    print("OUTPUT 1: ", int(output1))
    print("OUTPUT 2: ", int(output2))
#--
#-- ****************************************************:
#-- END OF PYTHON SCRIPT                                :
#-- ****************************************************: