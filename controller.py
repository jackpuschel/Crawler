from processing import processar_crawler
from constants import URL
import json


'''Função responsável pela chamada e retorno em json do processamento do crawler'''
def exec_crawler_feed():
    response = processar_crawler(URL)
    return response
