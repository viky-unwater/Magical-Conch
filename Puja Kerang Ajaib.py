from flask import Flask, jsonify, request
import random
import os

app = Flask(__name__)

responses = [ # respon yang akan diberikan
        "hiiii :3",
        "you should dance!",
        "you should sing!",
        "eat a borgar!",
        "pet the first kitty you're going to saw today!",
        "exercise more!",
        "stay hidrated!",
        "have a cookie!",
        "eat more veggies!",
        "GO NUKE POLAND NOW!!!"
    ]

@app.route('/Puja-Kerang-Ajaib/', methods=['GET']) # pada rute laman tanpa parameter nama
def conch_responses_to_the_mortal():
    response = random.choice(responses) # mengambil salah satu respon secara acak
    return jsonify({"Respon": response}) # me-return respon dalam bentuk json 

@app.route('/Puja-Kerang-Ajaib/<name>', methods=['GET', 'POST']) # pada rute laman dengan parameter nama
def personalized_conch_responses_to_the_mortal(name):
    if request.method == 'POST': # jika mendapat request POST
        return jsonify({"Pesan" : f"Selamat datang, {name}, anda berhasil masuk ke Puja Kerang Ajaib."})  # me-return ucapan dalam bentuk json 

    if request.method == 'GET': # jika mendapat request GET
        response = random.choice(responses) # mengambil salah satu respon secara acak
        return jsonify({"Respon": f"{name}, {response}"}) # me-return respon dalam bentuk json 
    
if __name__ == '__main__':
    host = os.environ.get('FLASK_HOST','0.0.0.0')
    port = os.environ.get('FLASK_HOST','80')
    