import anvil.server
import os
from keras.models import load_model
import cv2
import numpy as np

anvil.server.connect("server_5MHOUPDD3H6RMUVNPB3KRTIP-VILDRTZ3CALGFRHJ")

@anvil.server.callable
def Klasifikasi(DirDataSet, DirKlasifikasi, LabelKelas, ModelCNN):
  # Menyiapkan Data input Yang akan di klasifikasikan
  X = []
  L = []
  DirKelas = DirDataSet + "//" + DirKlasifikasi
  print(DirKelas)
  files = os.listdir(DirKelas)
  n = 0
  for f in files:
    f = f.lower()
    print(f)
    if (f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')):
      L.append(f)
      fnFile = os.path.join(DirKelas, f)
      img = cv2.imread(fnFile, 1)
      img = cv2.resize(img, (128, 128))
      img = np.asarray(img)/255
      img = img.astype('float32')
      X.append(img)
      n += 1
    # --- Akhir if
    # --- Akhir for

  X = np.array(X)
  X = X.astype('float32')

  # Melakukan prediksi klasifikasi
  hs = ModelCNN.predict(X)

  LKlasifikasi = []
  LKelasCitra = []
  n = X.shape[0]

  for i in range(n):
    v = hs[i, :]
    if v.max() > 0.5:
      idx = np.max(np.where(v == v.max()))
      LKelasCitra.append(LabelKelas[idx])
    else:
      idx = -1
      LKelasCitra.append("~")
    LKlasifikasi.append(idx)
    # --- akhir for

  LKlasifikasi = np.array(LKlasifikasi)
  return hs, LKlasifikasi, LKelasCitra

# *********************************************
# * Program Utama
# *********************************************

# a. Menentukan Direktori Yang menyimpan Data set
@anvil.server.callable
def test(img):
  with anvil.media.TempFile(img) as file_path:
    image = cv2.imread(file_path)
  return image

DirektoriDataSet = test()
# Data Set disimpan dalam direktori yang sama dengan nama kelas

# b. Label Data Set
LabelKelas = ["Bunga Bangkai Raksasa", "Edelweiss Jawa", "Anggrek Hitam", "Anggrek Bulan", "Bunga Padma Raksasa"]

# c. Load Model CNN
ModelCNN = load_model("/content/ModelBungaIndonesia.h5")
hs, h, LKelasCitra = Klasifikasi(DirektoriDataSet, "Anaphalis javanica", LabelKelas, ModelCNN)

@anvil.server.callable
def hasil():
  hs, h, LKelasCitra = Klasifikasi(DirektoriDataSet, "Anaphalis javanica", LabelKelas, ModelCNN)
  return LKelasCitra

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
