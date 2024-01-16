from pathlib import Path

import scrapy



class ExampleSpider(scrapy.Spider):
    name = "wptheme"
    allowed_domains = ["wordpress.org"]
    start_urls = ["https://wordpress.org/themes/"]

    def parse(self, response):
        filename = f"wp-themes.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")

# per lanciarlo: scrapy crawl wptheme
# quindi non conta il nome del file, ma il nome dello spider
