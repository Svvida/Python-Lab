# -*- coding: utf-8 -*-
"""Klasa Product -- zadanie do samodzielnego wykonania."""


class Product:
    """Reprezentuje produkt w sklepie internetowym."""

    def __init__(self, name: str, price: float, quantity: int):
        # Pamietaj o walidacji: price >= 0, quantity >= 0
        if(price < 0):
            raise ValueError("Cena nie moze byc ujemna.")
        if(quantity < 0):
            raise ValueError("Ilosc nie moze byc ujemna.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount: int):
        """Dodaje okreslona ilosc produktow do magazynu.

        Raises:
            ValueError: jesli amount jest ujemne
        """
        if(amount < 0):
            raise ValueError("Ilosc do dodania nie moze byc ujemna.")
        self.quantity += amount

    def remove_stock(self, amount: int):
        """Usuwa okreslona ilosc produktow z magazynu.

        Raises:
            ValueError: jesli amount jest ujemne lub wieksze niz dostepna ilosc
        """
        if(amount < 0):
            raise ValueError("Ilosc do usuniecia nie moze byc ujemna.")
        if(amount > self.quantity):
            raise ValueError("Ilosc do usuniecia jest wieksza niz dostepna ilosc.")
        self.quantity -= amount

    def is_available(self) -> bool:
        """Zwraca True jesli produkt jest dostepny (quantity > 0)."""
        return self.quantity > 0

    def total_value(self) -> float:
        """Zwraca calkowita wartosc produktow w magazynie (price * quantity)."""
        return self.price * self.quantity

    def apply_discount(self, percent: float):
        """Obniza cene o podany procent (0-100)."""
        if (percent < 0 or percent > 100):
            raise ValueError("Procent rabatu musi byc w zakresie 0-100.")

        discount_amount = self.price * (percent / 100)
        self.price -= discount_amount
