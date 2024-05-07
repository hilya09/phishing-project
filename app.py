# =[Modules dan Packages]========================

from flask import Flask,render_template,request,jsonify
import numpy as np
from joblib import load
from fungsi import *

# =[Variabel Global]=============================

app = Flask(__name__, static_url_path='/static')
model = None

# =[Routing]=====================================

# [Routing untuk Halaman Utama atau Home]
@app.route("/")
def beranda():
    return render_template('index.html')

# Routing for API phishing
@app.route("/api/deteksi", methods=['POST'])
def apiDeteksi():
   
    # Nilai default untuk string input ("URL")
    text_input = ""

    if request.method == 'POST':
        # Set nilai string input dari pengguna
        text_input = request.form.get("data")  # Ambil data dari form input
        
        # Memeriksa keutuhan link menggunakan fungsi parsing URL
        parsed_url = urlparse(text_input)
    
        if not parsed_url.netloc:
            # Jika netloc tidak ditemukan, kembalikan respons bahwa bukan link
            return jsonify({"data": "Bukan sebuah URL", "note": "<br>Masukkan URL dengan struktur yang utuh"})
        else:
            # Lakukan deteksi phishing jika input merupakan link yang valid
            features_test = main(text_input)
            features_test = np.array(features_test).reshape((1, -1))
            hasil = model.predict(features_test) 
            hasil_prediksi = None  # Menginisialisasi hasil_prediksi

            if (hasil == 1):
                hasil_prediksi = "phishing"
                note = "<br>Jangan mengklik atau mengunjungi link tersebut. Sebaiknya Anda hapus email atau pesan yang berisi link tersebut atau abaikan link tersebut jika terdapat di dalam pesan atau situs web lain."
            elif (hasil == 0):
                hasil_prediksi = "non-phishing"
                note = "<br>Tetaplah waspada dan hati-hati. Pastikan bahwa Anda hanya mengklik link dari sumber yang terpercaya. "
        
        # Return hasil prediksi dengan format JSON
        if hasil_prediksi is not None:
            return jsonify({"data": hasil_prediksi, "note": note})
        else:
            return jsonify({"error": "Tidak ada hasil prediksi yang tersedia."})


# =[Main]========================================
if __name__ == '__main__':

    # Load model phishing yang telah ditraining
    model = load('model_phishing_lr.model')

    # Run Flask di localhost
    app.run(host="localhost", port=5000, debug=True)
