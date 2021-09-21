import json
from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
app = Flask(__name__)

# Apesar de já possuir um módulo com a definição da classe paciente, precisei criar uma
# versão para ser usado nesse módulo pois estava enfrentando problemas de importação
class Patient:
  #Construtor
  def __init__(self):
    self.first_name = first_name
    self.last_name = last_name
    self.oxigenacao = oxigenacao
    self.name = name
    self.gravidade = False
    self.name = ''.join((self.first_name," ",self.last_name))

patients = [] # array que vai armazenar os pacientes e seus dados

# Apenas retorna uma mensagem quando o endpoint padrão é acessado, útil para testar
# pode ser removido se quiser
@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message' : 'Olá!'})

# Retorna a lista de todos os pacientes já registrados quando o endpoint <url_do_app>/pacientes
# for acessado 
@app.route('/pacientes', methods = ['GET'])
def returnAll():
  array_resultante = jsonify(patients)  # Formata em JSON
  return render_template('index.html', array_resultante = array_resultante.json) #envia para o template index.html os dados em formato JSON

# Recebe uma requisição POST e exibe no endpoint <url_do_app>/pacientes registrando um paciente 
@app.route('/pacientes', methods=['POST'])
def addOne():
    new_patient = request.get_json() # armazena a requisição em formato JSON
    new_patient_data = json.loads(new_patient) # recebe os dados da requisição e converte para tipo string
    patients.append(new_patient_data) # adiciona ao final da array patients instanciada na linha 20
    print("POST patients", patients) # Apenas para debugar
    
    array_resultante = jsonify(patients) # Cria uma nova variável para enviar ao front-end (cliente do médico)
    return render_template('index.html', array_resultante = array_resultante.json) # envia para o template index.html

# Recebe uma requisição PUT e exibe no endpoint <url_do_app>/pacientes registrando um paciente 
@app.route('/pacientes', methods=['PUT'])
def editAll():
    
    new_patient = request.get_json()
    new_patient_data = json.loads(new_patient)
    
    #esse buffer temporario serve para comparar informações dos novos POST request com os que já foram armazenados
    tmp_buffer = []
    tmp_buffer.append(new_patient_data['nome'])
    tmp_buffer.append(new_patient_data['oxigenacao'])
    tmp_buffer.append(new_patient_data['gravidade'])
    print(tmp_buffer) # Apenas para controle, pode retirar se desejar
    for patient in patients:
      # se o nome do paciente já estiver registrado atualiza seu valor de oxigenação e gravidade
      if(patient['nome'] == tmp_buffer[0]):
        patient['oxigenacao'] = tmp_buffer[1]
        patient['gravidade'] = tmp_buffer[2]
      print ("dentro do put req mas fora do if") # controle (pode retirar se quiser)
      print(patient)                              # controle
      print("put patients", patients)              # controle
    array_resultante = jsonify(patients)
    return render_template('index.html', array_resultante = array_resultante.json) 

if __name__ == '__main__':
    app.run(debug=True, port=3000)
