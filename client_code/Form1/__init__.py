from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
from anvil import media

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call("klasifikasi",self.file_loader_1.file)
    text=anvil.server.call("hasil")
    
    if text == "Anggrek Bulan":
      deskripsi= "Anggrek bulan (Phalaenopsis amabilis) adalah salah satu bunga nasional Indonesia yang dikenal karena keindahan dan keanggunannya. Bunga ini memiliki kelopak berwarna putih dengan corak kuning dan ungu di bagian tengah, menyerupai bentuk kupu-kupu. Anggrek bulan tumbuh di daerah beriklim tropis dan biasanya ditemukan di hutan-hutan lembap di Indonesia. Tanaman ini termasuk epifit, yang berarti hidup menumpang pada pohon lain tanpa merugikannya. Karena peson"
    elif text == "Anggrek Hitam":
      deskripsi= "Anggrek hitam (Coelogyne pandurata) adalah salah satu anggrek langka dan eksotis yang berasal dari Indonesia, khususnya dari Kalimantan dan Papua. Ciri khas bunga ini adalah lidah bunga (labellum) berwarna hitam pekat dengan garis-garis hijau, yang membuatnya tampak unik dan berbeda dari anggrek lainnya.Tanaman ini biasanya tumbuh di hutan hujan tropis pada ketinggian rendah dan sering hidup sebagai epifit di batang atau cabang pohon besar. Anggrek hitam mekar pada musim tertentu, dan bunganya mengeluarkan aroma harum yang khas. Karena keindahan dan kelangkaannya, anggrek hitam menjadi salah satu tanaman yang dilindungi di Indonesia dan simbol kekayaan hayati nusantara."
    elif text == "Bunga Bangkai Raksasa":
      deskripsi = "Bunga Bangkai Raksasa (Amorphophallus titanum) adalah salah satu bunga terbesar di dunia yang berasal dari hutan hujan tropis Sumatra, Indonesia. Tanaman ini dikenal karena ukuran bunganya yang bisa mencapai tinggi lebih dari 3 meter dan aromanya yang sangat menyengat, mirip bau bangkai, yang berfungsi menarik serangga penyerbuk seperti lalat dan kumbang. Bunga bangkai hanya mekar sekali setiap beberapa tahun dan mekar penuh hanya selama 1–2 hari. Struktur bunganya terdiri dari tongkol besar (spadix) yang dikelilingi oleh selubung berwarna ungu gelap (spathe). Meskipun sering disamakan dengan Rafflesia arnoldii, bunga bangkai berbeda karena berasal dari keluarga yang berbeda dan memiliki struktur bunga yang kompleks. Tanaman ini menjadi simbol keanekaragaman hayati Indonesia dan termasuk tumbuhan langka yang dilindungi karena habitat aslinya yang semakin terancam."
    elif text == "Bunga Padma Raksasa":
      deskripsi = "Bunga Padma Raksasa (Rafflesia arnoldii) adalah bunga terbesar di dunia yang berasal dari hutan tropis Sumatra, Indonesia. Bunga ini dapat mencapai diameter hingga 1 meter dan berat sekitar 11 kilogram. Keunikan utamanya terletak pada ukurannya yang luar biasa besar dan baunya yang busuk seperti daging membusuk, sehingga menarik serangga seperti lalat untuk membantu proses penyerbukan. Berbeda dengan bunga biasa, Rafflesia arnoldii tidak memiliki batang, daun, atau akar sejati. Ia hidup sebagai parasit di dalam jaringan tanaman inang, terutama jenis tumbuhan dari genus Tetrastigma. Bunga ini sangat langka dan hanya mekar selama beberapa hari sebelum layu. Bunga padma raksasa menjadi simbol keanekaragaman hayati Indonesia dan termasuk tumbuhan yang dilindungi karena populasinya yang terancam akibat kerusakan habitat."
    elif text == "Edelweiss Jawa":
      deskripsi = "Edelweiss Jawa (Anaphalis javanica) adalah tumbuhan khas pegunungan di Indonesia yang dikenal sebagai bunga abadi karena bunganya dapat bertahan lama bahkan setelah dipetik. Tanaman ini tumbuh di ketinggian di atas 2.000 meter di atas permukaan laut, terutama di gunung-gunung seperti Semeru, Gede, dan Rinjani. Edelweiss Jawa memiliki bentuk semak dengan daun hijau keperakan dan bunga kecil berwarna putih kekuningan yang tumbuh bergerombol. Tanaman ini melambangkan keabadian dan cinta sejati, dan sering menjadi simbol romantis bagi para pendaki gunung. Sayangnya, karena sering dipetik secara liar dan habitatnya yang terancam, edelweiss Jawa kini termasuk tumbuhan yang **dilindungi** oleh hukum Indonesia. Upaya konservasi dan larangan memetiknya di kawasan taman nasional dilakukan untuk menjaga kelestariannya."
    else:
      deskripsi = ""
    
    self.label_4.text=text+": "+deskripsi
    pass
