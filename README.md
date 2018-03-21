# F\&F Scraper

* Scraps [The Guardian](https://www.theguardian.com/international), [The Independent](https://www.independent.co.uk/), [Metro](http://metro.co.uk/) and [BBC](http://www.bbc.com/) to collect headlines along with their links. 
* Lemmatizes the scraped headlines using `Spacy` and performs cosine similarity to show relevant and non-repetative headlines.

### Usage
Run `python 'F&F.py'`

### ToDo
- [ ] Include league specific requests.
- [ ] Store user preferences and display only relevant data.

*Making multiple requests in a short amount of time is not adviseable.*

---
### Tested On

Python 3.5.2

requests 2.18.4

bs4 4.6.0

Spacy 2.0.9

`en_core_web_sm` model from Spacy
