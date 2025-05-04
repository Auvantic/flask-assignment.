from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit-get')
def submit_get():
    name = request.args.get('username')
    return f"Hello from GET, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
