from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key='my super secret key'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/process', methods=['post'])
def process():
    errors = 0
    if len(request.form['name']) < 1:
        # the field was not filled in
        flash('Name field is required!')
        errors += 1

    if errors is not 0:
        return redirect('/')
    else:
        session['count'] += 1
        print(request.form)
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']
        return redirect('/success')
        # return render_template('success.html', name = name, location = location, language = language, comment = comment)

app.run(debug=True)