import base64
import cv2
import numpy as np

def carrega(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro no carregamento de arquivo: {e}")


def salva(
    