from flask import Flask, render_template, redirect, request, session
from random import randint
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/')
def index():
    if 'total_gold' not in session:
        session['total_gold'] = 0
        session['activites'] = []

    return render_template('index.html')

@app.route('/process_money', methods=['post'])
def process():
    print(request.form)
    
    print('the current date is: ', datetime.now())
    date = datetime.now()
    changedDate = date.strftime("%Y/%m/%d %I:%M:%S %p")
    print('8'*90)
    if request.form['building'] == 'farm':
        randNum = randint(10, 20)
    elif request.form['building'] == 'cave':
        randNum = randint(5, 10)
    elif request.form['building'] == 'house':
        randNum = randint(2, 5)
    elif request.form['building'] == 'casino':
        randNum = randint(-50, 50)

    session['total_gold'] += randNum

    if randNum > 0:
        activitiy = 'You entered a ' + request.form['building'] + ' and earned ' + str(randNum) + ' golds! @ ' + changedDate
        result = 'green'
    else:
        activitiy = 'Entered a ' + request.form['building'] + ' and lost ' + str(abs(randNum)) + ' golds! .... Ouch!!! @ ' + changedDate
        result = 'red'

    session['activites'].insert(0, {'class': result, 'message': activitiy})

    print('total gold', session['total_gold'])
    print('You entered a ' + request.form['building'] + ' and earned ' + str(randNum) + ' golds!')

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)