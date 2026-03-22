# Wiki Lusophone Project

Outreachy Round 32 contribution by **Itoro James**

This repository contains the microtask submissions for the project **"Addressing the Lusophone Technological Wishlist"** a Wikimedia Brasil initiative to improve tools and platforms for the Portuguese-speaking Wikimedia community.

---

## Task 1 — JavaScript: JSON Manipulation (`Task1-Intern.html`)

Reads a JSON object containing Wikipedia article data and displays each entry in a human-readable format inside an HTML page.

**Output format:**
```
Article "ARTICLE TITLE" (Page ID PAGEID) was created at MONTH DAY, YEAR.
```

**How to run:**
Simply open `Task1-Intern.html` in any web browser.

---

## Task 2 — Python: URL Status Checker (`Task2-Intern.py`)

Reads a list of URLs from a `.csv` file and prints the HTTP status code of each one.

**Output format:**
```
(STATUS CODE) URL
```

**How to run:**
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install requests
python3 Task2-Intern.py
```

---

## About the Project

The Lusophone technological wishlist is a survey that identifies the most important technological needs of editors, readers and researchers of Wikimedia projects in Portuguese. This project aims to implement two of those community wishes:

- **Wish #3**: implement a duplicate reference checker in the Visual Editor
- **Wish #8**: add Wikidata support to wikiscore, allowing edit-a-thons and contests to count Wikidata contributions

**Mentors:** Ederporto, Arcstur