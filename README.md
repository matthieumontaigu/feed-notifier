# Feed notifier

## Overview

This project provides a Python-based tool for retrieving and processing content from RSS feeds and HTML pages. It supports a variety of sources and can filter, format, and send relevant items via email or SMS. The tool is designed for flexibility, making it easy to integrate new sources and parsing logic.

## Features
- Fetch content from multiple RSS and HTML sources.
- Relevance filtering based on user-defined rules.
- Automatic deduplication of already processed items.
- Periodic updates to ensure new content is fetched regularly.
- Configurable AWS based email and SMS notifications for sending updates.
- Modular structure for easy customization and extension.

## Requirements
- Python 3.9 or higher

## Installation
### 1. Clone the Repository:
```bash
git clone https://github.com/matthieumontaigu/feed-notifier.git
cd feed-notifier
```

### 2. Create a Virtual Environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies:
```bash
pip install -r requirements.txt
```
### 4. Configure the application:  

Create a `config.json` file containing all the parameters. Below is an example.
```json
{
    "feeds": [
        {
            "feed_type": "rss",
            "feed_url": "https://rss.com",
            "items_type": "letters",
            "update_interval": 300,
            "filters": [
                "[a-z]+"
            ]
        },
        {
            "feed_type": "html",
            "feed_url": "https://html.com",
            "items_type": "numbers",
            "update_interval": 21600,
            "filters": [
                "\\d+"
            ]
        },
    ],
    "message_sender": {
        "message_type": "email",
        "aws_credentials": {
            "region_name": "",
            "aws_access_key_id": "",
            "aws_secret_access_key": ""
        },
        "sources": {
            "letters": "Letters <letters.email@example.com>",
            "numbers": "Numbers <numbers.email@example.com>",
        },
        "destination": "your.email@example.com"
    },
    "memory_manager": {
        "path": "feed_cache.csv",
        "save_interval": 300
    },
    "execution_interval" : 60
}
```


## Usage

To start the feed reader, run:
```bash
python launch.py --config-path <PATH>
```

### Example:
```bash
python launch.py --config-path "/path/to/config.json"
```

The application will periodically fetch content, filter it based on relevance, and send updates via the configured notification methods.


## Directory Structure

```plaintext
movie_poster_tool/
├── launch.py                   # Entry point for the application
├── services/                   # Main services that compose the application
│   ├── notifier_service.py
│   ├── items_fetcher.py
│   ├── memory_manager.py
│   └── message_sender.py
├── web_scraper/                # Module that handles scraping and parsing web pages into list of items
│   ├── parser/
│   │   ├── parser/
│   │   │── base_parser.py
│   │   │── parser_factory.py
│   │   └── ...
│   ├── base_web_scraper.py
│   ├── html_web_scraper.py
│   ├── rss_web_scraper.py
│   └── web_scraper_factory.py
├── aws/                        # Functions to send notifications through aws
│   ├── base_sender.py
│   ├── email_sender.py
│   ├── sms_sender.py
│   └── sender_factory.py
└── schema/                     # Schema of the objects used in the repository
│   └── item.py
├── utils/                      # Functions to send notifications through aws
│   ├── config_utils.py
│   ├── date_utils.py
│   └── url_utils.py
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── .gitignore                  # Git ignored files
```

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (git checkout -b feature/new-feature).
3. Commit your changes (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature/new-feature).
5. Open a pull request.

## Acknowledgments
- BeautifulSoup for HTML parsing.
- Requests for HTTP requests.
- Feedparsers to parse RSS feeds.