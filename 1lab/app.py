from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    a = pd.DataFrame({'A': [1, 2, 3]})
    html_table = a.to_html()
    return render_template('index.html', html_table=html_table)

if __name__ == '__main__':
    app.run(debug=True)