import os
from typing import List, Dict, Union, Optional

from dotenv import load_dotenv
from flask import flash
import requests


load_dotenv()

PROD_URI = "http://127.0.0.1:3000/api/products/"
USER_URI = "http://127.0.0.1:3000/api/users/"


def get_products(url: str = PROD_URI) -> List[Dict]:
    """
    Получает список всех продуктов.
    """
    if not url:
        raise ValueError("PRODUCT_URI is not set in the environment variables.")
    
    response = requests.get(url)
    response.raise_for_status()  # Проверка на ошибки HTTP
    return response.json()


def buy_product(product_id, name):
    url = f"https://rozetka.com.ua/ua/igrovie-mishi/c4673278/producer=logitech/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Проверка на ошибки HTTP
    return response.text  # Если это HTML-страница, используйте .text вместо .json()

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

