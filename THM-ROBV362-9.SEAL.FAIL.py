#--
#-- ************************************************************************************************************:
#-- ****************************************** SET ROBV SEAL FAILURE *******************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2023.3.23                                                                                         :
#-- Script:   THM-ROBV362-9.SEAL.FAIL.py                                                                        :
#-- Purpose:  A python script sets a Seal Failure Alarm for ROBV E_04_362-9_SF.                                 :
#-- Info:     E_04_362-9_SF; 10372; 40001; Normal = 34; Alarm = 35.                                             :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#--python -m pip install PyModbus
#--
#-- ****************************************************:
#-- DEFINE PARAMES, CONFIGS, IMPORT MODULES & CLASSES   :
#-- ****************************************************:
from pymodbus.client.sync import ModbusTcpClient
#--
#-- CONNECT TO MBTCP CLIENT:
client = ModbusTcpClient('10.165.3.40', port=10372)
#--
#-- SET BYTE VALUE TO BE WRITTEN:
register_value = 35
#--
#-- WRITE BYTE VALUE TO MBTCP REGISTER:
register_address = 0
result = client.write_register(register_address, register_value)
#--
#-- VERIFY SUCCESSFUL WRITE:
if result.isError():
    print("WRITE ERROR - FAILED TO UPDATE MBTCP REGISTER:", result)
else:
    print("WRITE SUCCESSFUL:")
#--
#-- DISSCONNECT FROM MBTCP SERVER:
client.close()
#--
#-- ****************************************************:
#-- END OF PYTHON SCRIPT                                :
#-- ****************************************************: