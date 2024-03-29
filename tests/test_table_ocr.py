# coding: utf-8
import pytest
import os

from pix2text.utils import read_img
from pix2text.ocr_engine import prepare_ocr_engine
from pix2text.table_ocr import TableOCR, visualize_cells


def test_recognize():
    image_path = 'docs/examples/table3.jpg'
    os.environ['HF_ENDPOINT'] = os.getenv('HF_ENDPOINT', 'https://hf-mirror.com')
    languages = ('en', 'ch_sim')
    text_ocr = prepare_ocr_engine(languages, {})
    ocr = TableOCR(text_ocr=text_ocr)
    result = ocr.recognize(image_path, out_csv=True, out_cells=True, out_objects=False, out_html=True, out_markdown=True)

    visualize_cells(read_img(image_path, 'Image'), result['cells'][0], 'out-table-rec.png')
    print(result)
