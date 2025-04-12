import os
from typing import List, Dict, Union, Optional

from dotenv import load_dotenv
from flask import flash
import requests


load_dotenv()

PROD_URI = os.getenv("PRODCT_URI")
USER_URI = os.getenv("USER_URI")


def get_products(url:str = PROD_URI) -> List[Dict]:
    return requests.get(url).json()


def get_product(product_id: str, url:str = PROD_URI) -> Dict:
    return requests.get(url + product_id).json()


def add_product(name: str, description: str, price: float, img_url:str, url:str = PROD_URI):
    body = dict(
        name=name,
        description=description,
        price=price,
        img_url=img_url
    )

    msg = requests.post(url, json=body)
    flash(msg, category="success")


def update_product(product_id: str, name: str, description: str, price: float, img_url:str, url:str = PROD_URI):
    body = dict(
        name=name,
        description=description,
        price=price,
        img_url=img_url
    )

    msg = requests.put(url + product_id, json=body)
    flash(msg, category="success")

def add_review(product_id: str, text: str, name: str, url: str = PROD_URI):
    body = dict(text=text, name=name)
    msg = requests.patch(url + product_id, json=body).json()
    flash(msg, category="success")


def buy_product(product_id: str, text: str, name: str, url: str = PROD_URI):
    body = dict(text = text,name=name)
    msg = requests.post(url + product_id, json=body).json()
    flash(msg, category="success")

