# Task3-Elevate-Labs-
Task 3 Web Scraper for News Headlines Application
# 📰 News Headlines Web Scraper (Python)

A simple and efficient Python-based web scraper that extracts top news headlines from any public news website.  
This script uses **Requests** to fetch webpage content and **BeautifulSoup** to parse and extract headlines from `<h2>` tags.  
All extracted headlines are saved neatly into a `headlines.txt` file.

---

## 🚀 Features

- Scrapes headlines from any news website URL you provide  
- Defaults to **BBC News** if no URL is entered  
- Automatically extracts text from `<h2>` tags  
- Cleans results to remove empty or invalid entries  
- Saves output in a structured `.txt` file  
- Simple, lightweight, and beginner-friendly  

---

## 📂 Project Structure

```
📁 Project Folder
│── scraper.py
│── headlines.txt (generated after running)
│── README.md

```
---

## 🧰 Technologies Used

- **Python 3**
- **requests** — for fetching web pages  
- **BeautifulSoup (bs4)** — for parsing HTML  

Install dependencies:
```bash
pip install requests beautifulsoup4
```

## 🧠 How It Works (Simple Explanation)

-  The script asks the user for a news website URL
-  If nothing is entered → it uses BBC News
-  It fetches the page content using requests.get()
-  BeautifulSoup parses all h2 tags
-  Headlines are cleaned and saved to headlines.txt
- The program displays how many headlines were collected
This makes it perfect for internships, beginner projects, and data collection practice.

## 🖥️ Usage

Run the script from your terminal:
```
python scraper.py
```

You will see:
```
Enter the URL of the news website to scrape headlines from (default: BBC News):
```
- Press Enter to use BBC News Or type any website URL (ex: https://www.cnn.com):
- After completion:
```
Scraping completed! 28 headlines saved to headlines.txt
```
## 📝 Sample Output (headlines.txt)
```
----------------------------------
US election: Latest updates
----------------------------------
Tech giants reveal new innovations
----------------------------------
Global markets open higher today
----------------------------------
```

Every headline is separated for easy reading.

## 🛠️ Code Overview
Core scraping logic:
- Fetch HTML with requests
- Parse with BeautifulSoup
- Extract h2 text
Write output to file

## Error Handling:
- Invalid URL
- Website unreachable
- No headline tags found

Your script remains stable even if the website structure changes.

## 🤝 Contributing

Suggestions, improvements, or bug fixes are welcome.
Feel free to fork the repo and submit pull requests.
