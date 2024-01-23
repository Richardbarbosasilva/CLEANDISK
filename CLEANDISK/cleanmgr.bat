@echo off

if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit

::create some variables to tell the batch file where to find the powershell script.

set "caminhodownloads=%USERPROFILE%\Downloads\cleangmr.ps1"
set "caminhoareadetrabalho=%USERPROFILE%\Desktop\cleanmgr.ps1"
set "caminhodocumentos=%USERPROFILE%\Documents\cleanmgr.ps1"
set "caminhoappdata=%USERPROFILE%\AppData\Local\Programs\Python\Python312\cleanmgr.ps1"
set "caminhopastaatual=%~dp0cleanmgr.ps1"

:: Verify if the file does exists

if exist "%caminhodownloads%" (
    echo Python interpreter found. Starting python.
    :: Bypasses python's policy execution.
    powershell.exe -WindowStyle Hidden -NoProfile -ExecutionPolicy Bypass -File "%~dp0cleanmgr.ps1" -Verb RunAs
) else if exist "%caminhoareadetrabalho%" (
    echo Python interpreter found. Starting python.
     :: Bypasses python's policy execution.
  powershell.exe -WindowStyle Hidden -NoProfile -ExecutionPolicy Bypass -File "%~dp0cleanmgr.ps1" -Verb RunAs
) else if exist "%caminhodocumentos%" (
     echo Python interpreter found. Starting python.
    :: Bypasses python's policy execution.
    powershell.exe -WindowStyle Hidden -NoProfile -ExecutionPolicy Bypass -File "%~dp0cleanmgr.ps1" -Verb RunAs
) else if exist "%caminhoappdata%" (
    echo Python interpreter found. Starting python.
    :: Bypasses python's policy execution.
   powershell.exe -WindowStyle Hidden -NoProfile -ExecutionPolicy Bypass -File "%~dp0cleanmgr.ps1" -Verb RunAs
) else if exist "%caminhopastaatual%" (    
    echo Python interpreter found. Starting python.
    :: Bypasses python's policy execution.
    powershell.exe -WindowStyle Hidden -NoProfile -ExecutionPolicy Bypass -File "%~dp0cleanmgr.ps1" -Verb RunAs
) else (
    goto :Filenotfound
)

:Filenotfound

echo Powershell script not found, verify it's path and try once again.

:: exit or pause

exit
 
