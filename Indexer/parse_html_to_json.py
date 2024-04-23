import pandas as pd
from pathlib import Path
from bs4 import BeautifulSoup

class HTMLParser:
    def __init__(self):
        self.data = []
        self.output_filename = "/Users/rahulmansharamani/Desktop/Files/Spring 2024/CS429/Project/information-retrieval-system/Indexer/output.json"  # Specify the output JSON file path here

    def parse_html_files(self, html_dir):
        for file_path in Path(html_dir).iterdir():
            if file_path.suffix == ".html":
                with open(file_path, "r", encoding="utf-8") as f:
                    contents = f.read()
                    soup = BeautifulSoup(contents, 'html.parser')
                    title = soup.find("h1", id="firstHeading").get_text()
                    paragraphs = [p.get_text() for p in soup.select("div.mw-content-ltr p")]
                    content = " ".join(paragraphs).replace("\n", " ")
                    self.data.append({"title": title, "content": content})

    def save_as_json(self):
        json_data = pd.DataFrame(self.data)
        json_data.to_json(self.output_filename, orient='records')

def main():
    html_directory = "/Users/rahulmansharamani/Desktop/Files/Spring 2024/CS429/Project/information-retrieval-system/Crawler/webscraper/new_files"  # Specify the directory containing HTML files

    parser = HTMLParser()
    parser.parse_html_files(html_directory)
    parser.save_as_json()