import unittest
from processing import exec_crawler

class CrawlerTest(unittest.TestCase):
    def test_processar_crawler(self):
        input = """<?xml version="1.0" encoding="UTF-8" ?><rss version="2.0" xmlns:dc="http://purl.org/dc/elements/1.1/">
        <channel><item>    
         <title>Chevrolet Equinox 2020</title>
         <link>https://revistaautoesporte.globo.com/Noticias/noticia/2019/12/chevrolet-equinox-2020-versoes-de-entrada-perdem-potencia-e-cambio-de-9-velocidades-para-reduzir-o-preco.html</link>
         <description>Chevrolet Equinox 2020: versoes de entrada perdem potencia e cambio de 9 marchas para reduzir o preco</description>   
         </item></channel></rss>"""
        expected="""{"feed": [{"item": {"title": "Chevrolet Equinox 2020", "link": "https://revistaautoesporte.globo.com/Noticias/noticia/2019/12/chevrolet-equinox-2020-versoes-de-entrada-perdem-potencia-e-cambio-de-9-velocidades-para-reduzir-o-preco.html", "content": [[], [], {"type": "text", "content": ""}]}}]}"""
        self.assertEqual(expected, exec_crawler(input))
