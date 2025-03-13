@echo off

set ADDON_DIR=C:\tmp
set VERSION=1.5.0

call env.bat

if "%1"=="" (
    exit
)

if "%1"=="build" (
    rd /s /q "%ADDON_DIR%\geppetto" >NUL 2>&1
    xcopy /q /i /s .\source "%ADDON_DIR%\geppetto" >NUL 2>&1
    xcopy /q .\*.md "%ADDON_DIR%\geppetto" >NUL 2>&1
    exit
)

if "%1"=="package" (
    rd /s /q .\out >NUL 2>&1
    mkdir .\out >NUL 2>&1
    xcopy /q /i /s .\source .\out\geppetto >NUL 2>&1
    xcopy /q .\*.md .\out\geppetto >NUL 2>&1
    cd .\out
    tar -acf geppetto_%VERSION%.zip geppetto
    cd ..
    exit
)
