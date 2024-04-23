



# Information Retrieval Project : Soccer Edition

## Introduction
The Soccer Info Retrieval System is designed to crawl, index, and retrieve soccer-related content from the web. It utilizes a Scrapy-based crawler to download web documents in HTML format, a Scikit-Learn-based indexer to construct an inverted index, and a Flask-based processor to handle and respond to free text queries. This project is aimed at providing an efficient way to search and retrieve soccer information from various sources dynamically.

## Features
- **Web Crawling**: Customizable Scrapy crawler to fetch HTML pages up to a specified depth (Max Depth) and count (Max Pages).
- **Indexing**: Constructs an inverted index using TF-IDF scoring, allowing for efficient retrieval of documents based on cosine similarity.
- **Query Processing**: Flask-based web server that handles text queries and returns top-K relevant documents.

## Requirements
- Python 3.10+
- Scrapy 2.11+
- Scikit-Learn 1.2+
- Flask 2.2+

## Installation
Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/rahulmansharamani14/information-retrieval-system
cd soccer-info-retrieval
```
Setup a Python virtual environment and activate it (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Starting the Crawler

Navigate to the crawler directory and run the Scrapy crawler:

```bash
cd crawler
scrapy crawl soccer
```

Running the Indexer 
From the project root, execute:

```BASH
python indexer/index.py
```
Query Processor

Start the Flask server:

```bash
cd processor
python main.py
```

scrapy>=2.11
flask>=2.2
scikit-learn>=1.2.0
pandas>=1.4.0


<!-- # Information Retrieval Project

# This repository contains the codebase for an Information Retrieval project. The project includes three components: a web crawler, an indexer, and a query processor. Each component serves a specific purpose in the overall information retrieval pipeline.

# ## Project Structure

# - `crawler/`: Contains the Scrapy-based crawler for downloading web documents in HTML format.
# - `indexer/`: Contains the Scikit-Learn-based indexer for constructing an inverted index and handling TF-IDF representation.
# - `processor/`: Contains the Flask-based processor for handling free text queries and returning top-K ranked results.

# ## Project Codebase

# ### Crawler

# - The Scrapy-based crawler downloads web documents in HTML format from a seed URL, following specific depth and page count limits.
# - Data is stored in a JSON file containing the title, content, and URL of each crawled document.

# ### Indexer

# - The indexer constructs an inverted index using TF-IDF representation and cosine similarity.
# - Documents are transformed into TF-IDF vectors and stored for future retrieval.
# - The indexer also saves the vectorizer and URLs for use in query processing.

# ### Processor

# - The Flask-based processor handles free text queries submitted via HTTP POST requests.
# - Queries are transformed into TF-IDF vectors and compared against the document vectors to calculate similarity scores.
# - The processor returns top-K ranked URLs as a JSON response based on query similarity.

# ## How to Set Up the Project

# ### 1. Clone the Repository:
 -->
