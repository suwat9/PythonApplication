from flask import Flask, render_template
app = Flask(__name__)
@app.route('/index')
def index():    
 return render_template('index.html')

@app.route('/user')
def user():
 return render_template('user.html', name="Suwat",lastname="Tacha",email="Suwat.tac@mail.pbru.ac.th")

if __name__ == '__main__':
    app.run()
