import anvil.server

anvil.server.connect("server_5MHOUPDD3H6RMUVNPB3KRTIP-VILDRTZ3CALGFRHJ")

from anvil import server, media
import os
import cv2
import numpy as np
from keras.models import load_model

# Inisialisasi label dan model (hanya sekali saat server start)
LabelKelas = ["Bunga Bangkai Raksasa", "Edelweiss Jawa", "Anggrek Hitam", "Anggrek Bulan", "Bunga Padma Raksasa"]
ModelCNN = load_model("/content/ModelBungaIndonesia.h5")

# Variabel global untuk menyimpan hasil klasifikasi
global_hasil_klasifikasi = None

@server.callable
def klasifikasi(img_media):
    global global_hasil_klasifikasi

    with media.TempFile(img_media) as file_path:
        img = cv2.imread(file_path, 1)
        img = cv2.resize(img, (128, 128))
        img = np.asarray(img) / 255.0
        img = img.astype('float32')
        X = np.array([img])

        # Prediksi
        pred = ModelCNN.predict(X)
        hasil_kelas = "~"
        if pred[0].max() > 0.5:
            idx = np.argmax(pred[0])
            hasil_kelas = LabelKelas[idx]

        # Simpan ke variabel global
        global_hasil_klasifikasi = hasil_kelas
        return hasil_kelas

@server.callable
def hasil():
    # Ambil hasil terakhir
    return global_hasil_klasifikasi if global_hasil_klasifikasi is not None else "Belum ada hasil."
