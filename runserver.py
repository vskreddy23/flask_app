from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', title="Home")

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', title="Dashboard")

@app.route('/reports')
def reports():
    return render_template('reports.html', title="Reports")

if __name__ == '__main__':
    app.run(debug=True)