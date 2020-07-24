from flask import Flask, render_template
from markupsafe import Markup
from chart_1 import Chart_1
from chart_2 import Chart_2
from chinaMap import ChinaMap
from chart_3 import Chart_3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('my_test.html')
    #return Markup(Chart_1().render_embed())

@app.route('/world/')
def world():
    return render_template('my_test_2.html')
    #return Markup(Chart_2().render_embed())

@app.route('/predict/')
def predict():
    return render_template('my_test_3.html')
    #return Markup(Chart_3().render_embed())

if __name__ == '__main__':
    app.run(debug=True)

