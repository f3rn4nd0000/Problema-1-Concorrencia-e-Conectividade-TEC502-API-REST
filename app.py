import json
from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
# from livereload import Server    
app = Flask(__name__)

class Patient:
  #Construtor
  def __init__(self):
    self.first_name = first_name
    self.last_name = last_name
    self.oxigenacao = oxigenacao
    self.name = name
    self.gravidade = False
    # self.name.append(self.first_name)
    # self.name.append(self.last_name)
    self.name = ''.join((self.first_name," ",self.last_name))

patients = [] # array que vai armazenar os pacientes e seus dados

# @app.route('/', methods=['GET'])
# def hello_world():
#     return jsonify({'message' : 'Olá!'})

# We're using the new route that allows us to read a date from the URL
@app.route('/pacientes', methods = ['GET'])
def returnAll():
  # data = request.get_data().decode()
    # array_resultante = json.loads({patients})
  # array_resultante = jsonify({'patients' : patients})
  # return render_template('index.html', array_resultante = array_resultante) 
  # return jsonify({'patients' : patients})
  # array_resultante = json.loads(patients)
  # array_resultante = jsonify({patients})
  array_resultante = jsonify(patients)
  return render_template('index.html', array_resultante = array_resultante.json) 
  # return request.headers.get('your-header-name')

@app.route('/pacientes', methods=['POST'])
def addOne():
    new_patient = request.get_json()
    new_patient_data = json.loads(new_patient)
    patients.append(new_patient_data)
    print("POST patients", patients)
    # patients.insert(new_patient)
    array_resultante = jsonify(patients)
    # array_resultante = jsonify({patients})
    return render_template('index.html', array_resultante = array_resultante.json) 
    # return jsonify({'patients': patients})

@app.route('/pacientes', methods=['PUT'])
def editAll():
    # patient_stored = Patient() # aqui serao carregados os dados contidos no array já armazenado no server até agora
    
    new_patient = request.get_json()
    new_patient_data = json.loads(new_patient)
    #esse buffer temporario serve para comparar informações dos novos POST request com os que já foram armazenados
    tmp_buffer = []
    tmp_buffer.append(new_patient_data['nome'])
    tmp_buffer.append(new_patient_data['oxigenacao'])
    tmp_buffer.append(new_patient_data['gravidade'])
    # print("asidoasidoa")
    print(tmp_buffer)
    # patient_stored.first_name = new_patient_data
    for patient in patients:
      # se o nome do paciente já estiver registrado atualiza seu valor de oxigenação e gravidade
      if(patient['nome'] == tmp_buffer[0]):
        patient['oxigenacao'] = tmp_buffer[1]
        patient['gravidade'] = tmp_buffer[2]
      print ("dentro do put req mas fora do if")
      print(patient)
      print("put patients", patients)
    array_resultante = jsonify(patients)
    return render_template('index.html', array_resultante = array_resultante.json) 
    # array_resultante = patients
    # return jsonify({'patients' : patients})
    #   if (patie)
    # for patient in patients
    #   if patient
    #     patients[i] = new_patient    
    # ps = request.get_json()
    # array_resultante = jsonify({'patients': patients})
    # array_resultante = patients
    # print(array_resultante)
    # return render_template('index.html', array_resultante = array_resultante) 
    # array_resultante = json.loads(patients)
    # return render_template('index.html', array_resultante = array_resultante)     
    # array_resultante=array_resultante

if __name__ == '__main__':
    app.run(debug=True, port=3000)
    # pyautogui.hotkey('f5')
    # server = Server(app.wsgi_app)
    # server.serve(port=3000)
