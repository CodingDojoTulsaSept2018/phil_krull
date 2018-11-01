from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'my super secret key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['post'])
def process():
    print(request.form['name'])
    print(request.form['location'])
    session['name'] = request.form['name']
    return redirect('/')

@app.route('/user/<name>')
def userName(name):
    return 'the name given is: ' + name

app.run(debug = True)

# what imports are needed for the given server file?
# what lines of code are missing, if any?
# what url would you use to display the index.html page?
# what would the html form look like to make the process method work
# what code would you add in the index html to display the data saved in session
# what url would you use the userName method, what would you expect the response to be