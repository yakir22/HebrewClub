@echo off
:loop
yarn start
ping -n 6 127.0.0.1 > nul
goto loop
