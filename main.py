from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def comman():
    return render_template('index.html')

@app.route('/one')
def one():
    return render_template('one.html')

@app.route('/two')
def two():
    return render_template('two.html')

@app.route('/three')
def three():
    return render_template('three.html')
@app.route('/four')
def four():
    return render_template('four.html')
@app.route('/five')
def five():
    return render_template('five.html')
@app.route('/six')
def six():
    return render_template('six.html')
@app.route('/seven')
def seven():
    return render_template('seven.html')
@app.route('/eight')
def eight():
    return render_template('eight.html')

@app.route('/nine')
def nine():
    return render_template('nine.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(port=5000)
   