# Importa
from flask import Flask, render_template, request

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

# Il modulo
@app.route('/form')
def form():
    return render_template('form.html')

#I risultati del modulo
@app.route('/submit', methods=['POST'])
def submit_form():
    # Dichiarare le variabili per la raccolta dei dati
    name = request.form['name']
    email = request.form['email']
    date = request.form['date'] 
    address = request.form['address']

    # Salvare i dati nel file form.txt
    with open('form.txt', 'a') as f:
        f.write(f"Name: {name}\n")
        f.write(f"Email: {email}\n")
        f.write(f"Date: {date}\n")
        f.write(f"Address: {address}\n")
        f.write("\n")

    # È possibile salvare i dati o inviarli via e-mail
    return render_template('form_result.html', 
                           # Inserire le variabili qui
                           name=name,
                           email=email,
                           date=date,
                           address=address
                           )

if __name__ == "__main__":
    app.run(debug=True)