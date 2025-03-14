@echo off
echo Đang thiet lap moi truong ao...
python -m venv venv
call venv\Scripts\activate

echo Dang cai cac goi phu thuoc...
pip install --upgrade pip
pip install flask flask-login flask-wtf werkzeug

echo Cai dat hoan tat!!!
echo Run ung dung Flask...
python app.py
