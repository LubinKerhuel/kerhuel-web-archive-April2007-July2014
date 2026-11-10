@echo off
rem ============================================================
rem  Regenere le site statique kerhuel.eu (wiki + forum) depuis :
rem    - le dump SQL  www.kerhuel.eu\SQL\mysql168.kerhuelforum.2019-03-25-09h30.gz  (lecture seule)
rem    - l'arbre du site www.kerhuel.eu\
rem  Etape 1 : tools\build_archive.py  -> content\ et static\ + reports\
rem  Etape 2 : Hugo                    -> public\ (nettoye, sans fichiers perimes)
rem ============================================================
setlocal
cd /d "%~dp0"

set "HUGO=D:\M91449\MCHP_Blockset\Projects\hugo\hugo.exe"

where python >nul 2>&1
if errorlevel 1 (
    echo ERREUR : python introuvable dans le PATH.
    exit /b 1
)
if not exist "%HUGO%" (
    echo ERREUR : hugo introuvable : %HUGO%
    exit /b 1
)

echo [1/2] Generation du contenu depuis le dump SQL et le site...
python tools\build_archive.py
if errorlevel 1 (
    echo ECHEC : generation du contenu ^(tools\build_archive.py^).
    exit /b 1
)

echo [2/2] Build Hugo...
"%HUGO%" --minify --cleanDestinationDir --ignoreCache
if errorlevel 1 (
    echo ECHEC : build Hugo.
    exit /b 1
)

echo.
echo OK. Site : %~dp0public\
echo Rapport  : %~dp0reports\build-report.md
endlocal
exit /b 0
