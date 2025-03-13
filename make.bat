@echo off

set ADDON_DIR=C:\tmp
set VERSION=1.5.0

call env.bat

if "%1"=="" (
    exit
)

if "%1"=="build" (
    rd /s /q "%ADDON_DIR%\puppeteer" >NUL 2>&1
    xcopy /q /i /s .\source "%ADDON_DIR%\puppeteer" >NUL 2>&1
    xcopy /q .\*.md "%ADDON_DIR%\puppeteer" >NUL 2>&1
    exit
)

if "%1"=="package" (
    rd /s /q .\out >NUL 2>&1
    mkdir .\out >NUL 2>&1
    xcopy /q /i /s .\source .\out\puppeteer >NUL 2>&1
    xcopy /q .\*.md .\out\puppeteer >NUL 2>&1
    cd .\out
    tar -acf puppeteer_%VERSION%.zip puppeteer
    cd ..
    exit
)
