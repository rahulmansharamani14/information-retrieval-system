



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
cd Indexer
python indexer/inverted_index.py
```
Query Processor

Start the Flask server:

```bash
cd Processor
python main.py
```


Web Search Endpoint
```code
POST /search

Body: 

- query: string
- top_k: number

```

### Example Test Query

```json
{
    "query": "serie league", 
    "top_k": 6
}
```

### Example Test Query Response

```json
[
    {
        "Id": "56",
        "score": 0.11516222795273667,
        "title": "United States soccer league system"
    },
    {
        "Id": "16",
        "score": 0.07186884314724615,
        "title": "Major League Soccer"
    },
    {
        "Id": "75",
        "score": 0.051735155684219915,
        "title": "FA Cup"
    },
    {
        "Id": "3",
        "score": 0.05133822130268852,
        "title": "United States Soccer Federation"
    },
    {
        "Id": "24",
        "score": 0.04886188751537362,
        "title": "Rugby football"
    },
    {
        "Id": "40",
        "score": 0.037023597815022444,
        "title": "National Basketball Association"
    }
]
```

### Architecture

![img a](./Screenshot%202024-04-22%20at%2011.58.23 PM.png)