#-- ************************************************************************************************************:
#-- ********************************************** SEAL FAIL ALARM *********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBallard (JEB)                                                                                    :
#-- Date:     2023.3.24                                                                                         :
#-- Script:   THM-ROBV39-5.SFA.ps1                                                                              :
#-- Purpose:  A PowerShell script that writes a value to a MBTCP register:                                      :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ****************************************************:
#-- DEFINE PARAMES, CONFIGS, IMPORT MODULES & CLASSES   :
#-- ****************************************************:
ADD-TYPE -PATH "C:\0_SVN\6_PS.RUN.Dir\NModbus.dll"
$ipAddress = "10.165.3.40"
$port = 10367
$unitId = 1
#--
#-- WRITE TO MBTCP REGISTER:
$registerAddress = 0
#--
#-- VALUE WRITING TO REGISTER:
$valueToWrite = 35
#--
#-- CREATE NEW MBTCP CLIENT OBJECT:
$client = NEW-OBJECT NModbus.ModbusIpTcpClient($ipAddress, $port)
#--
#-- OPEN MBTCP CONNECTION:
$client.Connect()
#--
#-- WRITE VALUE TO MBTCP REGISTER:
$client.WriteSingleRegister($unitId, $registerAddress, $valueToWrite)
#--
#-- CLOSE MBTCP CONNECTION:
$client.Disconnect()
#--
#-- ********************************************************:
#-- END OF POWERSHELL SCRIPT                                :
#-- ********************************************************: