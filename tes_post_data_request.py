import json, urllib, base64
from urllib import request, response

url = "http://127.0.0.1:8000/api/property/create/"

header = {
    'Method':'POST',
    'Authorization': 'Basic bWlmdGFoOjEyMzQ1Ng==',
    'Content-Type': 'application/json',
    'User-Agent': 'PostmanRuntime/7.26.10',
    'Accept': '*/*',
    'Host': '127.0.0.1:8000',
}

body = {
    "property_name": "Makmur Indah Residence - Tipe 36/72",
    "address": "Tajur Halang, Bogor",
    "property_type": "RM",
    "description": "Dikembangkan oleh PT. Cahaya Makmur Bersama Properti, Makmur Indah Residence merupakan landed house di Tajurhalang, Bogor. Daya tarik perumahan di Bogor ini memiliki lokasi yang strategis dan prospektif. Makmur Indah Residence pun turut dilengkapi sejumlah fasilitas berupa:\n\u2022 Sarana Ibadah\n\u2022 Keamanan 24 Jam\n\u2022 Area Terbuka Hijau\n\u2022 Taman Bermain\nMakmur Indah Residence memiliki desain rumah modern dan minimalis sehingga cocok untuk berbagai kalangan. Hadirnya area terbuka hijau di kawasan perumahan pun memberikan lingkungan yang asri dI Bogor. Adapun sejumlah area fasilitas publik yang menunjang aktivitas para penghuni seperti:\n\u2022 1 km ke perbankan dan ATM\n\u2022 1 km ke sejumlah resotran\n\u2022 1 km ke fasilitas pendidikan\n\u2022 7 km ke RS Hermina\n\u2022 7 km ke SPBU\n\u2022 10 km ke D Mal\nMakmur Indah Residence memiliki dua tipe yang bisa dipilih yakni Tipe 36/60 dan Tipe 36/72 dengan 2 kamar tidur, 1 kamar mandi dan 1 carport.",
    "release_date": "08-2021",
    "publish_date": "-",
    "catalog_link": "-",
    "facility": "-",
    "status": "JL",
    "certificate": "-",
    "geo_location": "-",
    "name": "Tipe 36/72",
    "price": "Mulai Rp. 370.980.000",
    "LT": "Luas Bangunan: 36 m\u00b2",
    "LB": "Luas Bangunan: 36 m\u00b2",
    "images": [
      {
        "url": "https://pictures.core.ninetynine.id/r123/750x380-inside/primary_property/project/2008/1601954145_16019541455f7be1612e1c9ads_images_3928.jpg?noWatermark"
      },
      {
        "url": "https://pictures.core.ninetynine.id/r123/750x380-inside/primary_property/project/2008/1601878703_5f7abaaf65336floorplan_3928.jpeg?noWatermark"
      }
    ],
    "source": "olx",
    "agent": [{
      "name": "PT. Cahaya Makmur Bersama Properti",
      "contact": "6287891783111"
    }],
    "developer": { "name": "-", "contact": "-" }
}
credential = "miftah:123456"
credential_b64 = base64.b64encode(credential.encode("ascii")).decode("ascii")

req = request.Request(url)
data = json.dumps(body)
data_byte = data.encode('utf-8')
req.add_header('Method','POST')
req.add_header('Authorization', 'Basic '+credential_b64)
req.add_header('Content-Type', 'application/json')
req.add_header('User-Agent', 'PostmanRuntime/7.26.10')
req.add_header('Accept', '*/*')
req.add_header('Host', '127.0.0.1:8000')
req.add_header('Content-Length',len(data_byte))

try:
    res = request.urlopen(req,data_byte)
    print("Posting data", body['property_name'], "succesed")
except urllib.error.HTTPError as e:
    print("Posting data", body['property_name'], "with error:",e.read().decode('utf-8','ignore'))
