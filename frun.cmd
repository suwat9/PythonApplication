py -3 -m venv .venv
.venv\scripts\activate

python -m pip install --upgrade pip
python -m pip install flask
python -m flask --app main.py run -p 80
