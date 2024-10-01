"""
    Módulo de funções para cálculo de áreas de polígonos.
"""
import math


def area_circulo(raio):
    """
        Função que calcula a área do círculo a partir do raio.
        Args:
            raio (float): Raio do círculo.
        Returns:
            float: Área calculada.
    """
    area = math.pi * raio * raio
    return area


def area_quadrado(lado):
    """
        Função que calcula a área do quadro a partir do lado.
        Args:
            lado (float): Lado do quadrado.
        Returns:
            float: Área calculada.
    """
    area = lado * lado
    return area


def area_retangulo(base, altura):
    """
        Função que calcula a área do retângulo a partir da base e da altura.
        Args:
            base (float): Base do retângulo.
            altura (float): Altura do retângulo.
        Returns:
            float: Área calculada.
    """
    area = base * altura
    return area


def area_triangulo(base, altura):
    """
        Função que calcula a área do triângulo a partir da base e da altura.
        Args:
            base (float): Base do triângulo.
            altura (float): Altura do triângulo.
        Returns:
            float: Área calculada.
    """
    area = base * altura
    return area