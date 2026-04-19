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

##  Project Structure
review-summarizer/
│── main.py # Entry point
│── scraper.py # Scrapes reviews from URL
│── preprocess.py # Cleans and prepares text
│── llm.py # Handles LLM API calls
│── reviews_output.csv # Final output
│── .env # API key (not committed)
│── requirements.txt
│── README.md

---

## LLM Integration

This project uses **OpenRouter** as an OpenAI-compatible API to access open-source LLMs such as:

- LLaMA 3 (meta-llama/llama-3-8b-instruct)

This avoids dependency on paid APIs while maintaining full compatibility with OpenAI-style endpoints.

---

##  How to Run

1. Clone the repository
git clone <your-repo-link>
cd review-summarizer

2. Install dependencies
pip install -r requirements.txt

3. Add your API key

Create a .env file:

OPENROUTER_API_KEY=your_api_key_here
4. Run the application
python main.py
5. Provide a product URL when prompted

##  Tested URL
Example product page used for testing: http://books.toscrape.com/catalogue/category/books/travel_2/index.html

##  Design Choices

- Used OpenRouter instead of OpenAI to avoid paid API dependency  
- Implemented fallback reviews to handle scraping failures  
- Used modular structure for scalability and readability  
- Limited tokens to reduce API usage and latency  