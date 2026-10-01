from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave-super-secreta'

@app.route("/")
def index():
    if 'lista' not in session:
      session['lista'] = []
    return render_template('tarefas.html', lista=session['lista'])
    


if __name__ == '__main__':
    app.run(debug=True)