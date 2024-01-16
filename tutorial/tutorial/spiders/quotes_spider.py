from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    #name: identifica il ragno. 
    # Deve essere Unico all'interno di un progetto, cioè, 
    # non è possibile impostare lo stesso nome per diversi I ragni.

    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # start-requests(): 
    # deve restituire un iterabile di Richieste 
    # (è possibile restituire un elenco di richieste o scrivere una funzione di generatore) 
    # da cui la Spider inizierà a strisciare. 
    # Le richieste successive verranno generate successivamente da queste richieste iniziali. 
            
    # parse(): 
    # un metodo che verrà chiamato a gestire la risposta scaricata 
    # per ciascuna delle richieste effettuate. 
    # Il parametro di risposta è un'istanza di TextResponse che contiene 
    # il contenuto della pagina e ha ulteriori metodi utili per gestirlo. 

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
# aa
