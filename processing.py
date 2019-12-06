# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests, json
from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup

'''Função responsável por carregar a URL e encaminhar a requisição para o crawler e retornar o resultado'''
def processar_crawler(feed):
    url = requests.get(feed)
    status_code = url.status_code
    if status_code == 200:
        arq_xml = url.content
        response = exec_crawler(arq_xml)
    else:
        response = {'Not possible to get the content!'}
    return response


'''Função para percorrer o feed e carregar os dados formatados em json'''
def exec_crawler(feed):
    itens_feed = []
    try:
        xml = ET.fromstring(feed)
        for node in xml.iterfind('channel/item'):
            item = {}
            item['title'] = node.findtext('title')
            item['link'] = node.findtext('link')
            description = node.findtext('description')
            item['content'] = description_formatter(description)
            itens_feed.append({'item':item})
        response = {'feed': itens_feed}
    except:
        response = {'Error' : 'Failure to process the feed'}
    return json.dumps(response)


'''Função para formatar o nó descrição para o content'''
def description_formatter(description):
    content = []
    bs4 = BeautifulSoup(description, 'html.parser')
    content.append(find_img(bs4))
    content.append(find_links(bs4))
    content.append(find_paragraph(bs4))

    return content

'''Busca tag img e retorna o src em uma lista formatada'''
def find_img(bs4):
    image = []
    for tag in bs4.select('.foto img'):
        image.append({'type': 'image',
                              'content': tag['src']})
    return image


'''Busca tag link e o retorna em uma lista formatada '''
def find_links(bs4):
    link = []
    for tag in bs4.select('a'):
        link.append({'type': 'link',
                             'content': tag['href']})
    return link


'''Busca tag p e retorna o texto em uma lista formatada '''
def find_paragraph(bs4):
    paragraph = ''
    for tag in bs4.select('p'):
        text = tag.text.replace('\n', '').replace('\t', '')
        if text.strip():
            paragraph = paragraph + text

    return {'type': 'text', 'content': paragraph}