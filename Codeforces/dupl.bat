@echo off
title duplicate_temp
echo Akarsh

if exist tst.C goto detst
copy temp.C tst.C
copy testcase.txt zxc.txt
goto end

:detst
del tst.C
del zxc.txt

:end