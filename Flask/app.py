from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return "Hello, world!"

@app.route('/about')
def about():
    return "About page"

@app.route('/<name>')
def print_name(name):
    return "Its a {} page".format(name)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)