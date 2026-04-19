#  Review Summarizer using LLM

##  Overview
This project is a Python-based application that scrapes product reviews from an e-commerce webpage, preprocesses the extracted text, and leverages a Large Language Model (LLM) via an OpenAI-compatible API to generate concise sentiment analysis and summaries.

The system is designed to be robust, modular, and adaptable to different websites.

---

##  Features

-  **Web Scraping** using BeautifulSoup  
-  **Text Preprocessing** (cleaning, formatting, handling noise)  
-  **LLM Integration** using OpenRouter (OpenAI-compatible API)  
-  **Sentiment Analysis + Summary Generation**  
-  **Structured Output** stored in CSV format  
-  **Error Handling** for API failures and scraping issues  
-  **Fallback Mechanism** for unavailable data  

---

## 📁 Project Structure

<pre>
review-summarizer/
│
├── main.py              # Entry point of the application
├── scraper.py           # Scrapes reviews from product URL
├── preprocess.py        # Cleans and preprocesses review text
├── llm.py               # Handles LLM API interaction (OpenRouter)
│
├── reviews_output.csv   # Generated output file
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
│
├── .env                 # API key (not committed)
├── .gitignore           # Ignore sensitive/system files
│
├── __pycache__/         # Python cache (auto-generated)
└── venv/                # Virtual environment (not committed)
</pre>

---

## LLM Integration

This project uses **OpenRouter** as an OpenAI-compatible API to access open-source LLMs such as:

- LLaMA 3 (meta-llama/llama-3-8b-instruct)

This avoids dependency on paid APIs while maintaining full compatibility with OpenAI-style endpoints.

---

## ▶️ How to Run

<pre>
1. Clone the Repository
   git clone https://github.com/YOUR_USERNAME/review-summarizer-llm.git
   cd review-summarizer-llm

2. Create Virtual Environment
   python -m venv venv

3. Activate Environment

   Windows (PowerShell):
   venv\Scripts\activate

   Mac/Linux:
   source venv/bin/activate

4. Install Dependencies
   pip install -r requirements.txt

5. Create .env file and add API key
   OPENROUTER_API_KEY=your_api_key_here

6. Run the Application
   python main.py

7. Enter Product URL (example)
   https://webscraper.io/test-sites/e-commerce/static/product/518

8. Output will be saved in
   reviews_output.csv
</pre>

##  Tested URL
Example product page used for testing: http://books.toscrape.com/catalogue/category/books/travel_2/index.html

##  Design Choices

- Used OpenRouter instead of OpenAI to avoid paid API dependency  
- Implemented fallback reviews to handle scraping failures  
- Used modular structure for scalability and readability  
- Limited tokens to reduce API usage and latency
  
  ## ⚠️ Limitations

<pre>
- Some websites (e.g., Amazon, Flipkart) may block scraping
- HTML structure varies across websites
- Free LLM APIs may have rate limits
</pre>

---

## 🛠️ Tech Stack

<pre>
- Python
- BeautifulSoup
- Requests
- Pandas
- OpenRouter API
</pre>

---

## 🎯 Future Improvements

<pre>
- Support multi-page scraping
- Add a web UI (Streamlit)
- Improve scraper robustness
- Store data in a database
</pre>

---

## 📌 Notes

<pre>
- API keys are securely managed using environment variables
- .env file is excluded from version control
</pre>

## Project Demo Video Link: 
https://drive.google.com/file/d/1gvBjboatpCoz4MRSInTiFaKVZjm1vCzM/view?usp=drive_link

