from pix2text import Pix2Text
from pix2text import PageJsonEncoder
import orjson
import json
import jsonpickle
from flask import jsonify

img_fp = "./screenshotfrom2024-06-1412-06-51.png"
p2t = Pix2Text.from_config()
doc = p2t.recognize_page(img_fp, page_numbers=[0])
t = json.dumps(doc, cls=PageJsonEncoder, indent=4)
print(t)
# doc.to_markdown('output-md')  # The exported Markdown information is saved in the output-md directory
#j = jsonpickle.encode(doc, unpicklable=False)
#print(j)

