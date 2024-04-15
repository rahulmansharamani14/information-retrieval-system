# Information Retrieval Project

This repository contains the codebase for an Information Retrieval project. The project includes three components: a web crawler, an indexer, and a query processor. Each component serves a specific purpose in the overall information retrieval pipeline.

## Project Structure

- `crawler/`: Contains the Scrapy-based crawler for downloading web documents in HTML format.
- `indexer/`: Contains the Scikit-Learn-based indexer for constructing an inverted index and handling TF-IDF representation.
- `processor/`: Contains the Flask-based processor for handling free text queries and returning top-K ranked results.

## Project Codebase

### Crawler

- The Scrapy-based crawler downloads web documents in HTML format from a seed URL, following specific depth and page count limits.
- Data is stored in a JSON file containing the title, content, and URL of each crawled document.

### Indexer

- The indexer constructs an inverted index using TF-IDF representation and cosine similarity.
- Documents are transformed into TF-IDF vectors and stored for future retrieval.
- The indexer also saves the vectorizer and URLs for use in query processing.

### Processor

- The Flask-based processor handles free text queries submitted via HTTP POST requests.
- Queries are transformed into TF-IDF vectors and compared against the document vectors to calculate similarity scores.
- The processor returns top-K ranked URLs as a JSON response based on query similarity.

## How to Set Up the Project

### 1. Clone the Repository:

```bash
git clone <repository_url>
