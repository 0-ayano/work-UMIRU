@echo off
setlocal

pushd "%~dp0"
cd api
uvicorn app:app --reload
popd

pause