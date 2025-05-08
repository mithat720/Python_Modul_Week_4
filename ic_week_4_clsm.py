deger =   '{"kullanici": [{"yas": 23, "ad": "ibrahim"}, {"yas": 45, "ad": "mehmet"}]}'
import json
veri = json.loads(deger)
print(type(veri))

print(veri["kullanici"][0]["yas"])
