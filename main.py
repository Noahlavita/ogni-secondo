from flask import Flask, render_template

app = Flask(__name__)

counter_values = {
    "co2": 0,
    "plas": 0,
    "tonn": 0,
    "barili": 0,
    "persone": 0,
    "foresta": 0,
    "luce": 0 
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def counter():
    counter_values["co2"] += 1079 
    counter_values["plas"] += 24
    counter_values["tonn"] += 24000
    counter_values["barili"] += 1.2
    counter_values["persone"] += 0.4
    counter_values["foresta"] += 0.7
    counter_values["luce"] += 4.5

    return render_template('main.html', co2=counter_values["co2"], plas=counter_values["plas"], tonn=counter_values["tonn"], barili=counter_values["barili"],persone=counter_values["persone"],foresta=counter_values["foresta"],luce=counter_values["luce"])

@app.route('/reset')
def reset():
    counter_values["co2"] = 0 
    counter_values["plas"] = 0
    counter_values["tonn"] = 0
    counter_values["barili"] = 0.0
    counter_values["persone"] = 0.0
    counter_values["foresta"] = 0.0
    counter_values["luce"] = 0.0
    return render_template('reset.html')

@app.route('/fonti')
def fonti():
    return render_template('fonti.html')


app.run(debug=True)
