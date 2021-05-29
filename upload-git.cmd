@echo off
git add .
git commit -m "%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%-%DATE:~6,4%%DATE:~3,2%%DATE:~0,2%"
git push
pause