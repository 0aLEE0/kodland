# Importa
from flask import Flask, render_template

app = Flask(__name__)

def result_calculate(size, lights, device):
    # Variabili per il consumo energetico dei dispositivi
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5
    eco_coef = 0.1  # Very small coefficient for eco-friendly construction
    
    if device == 'eco':
        return size * home_coef + lights * light_coef + eco_coef
    else:
        return size * home_coef + lights * light_coef + int(device) * devices_coef

# Prima pagina
@app.route('/')
def index():
    return render_template('index.html')

# Seconda pagina
@app.route('/<size>')
def lights(size):
    return render_template(
        'lights.html',
        size=size
    )

# Terza pagina
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
        'electronics.html',
        size=size,
        lights=lights
    )

# Calcolo
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    result = result_calculate(int(size), int(lights), device)
    return render_template('end.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
