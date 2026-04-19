from scraper import scrape_reviews
from preprocess import clean_text
from llm import analyze_review
import pandas as pd
import time

def main():
    url = input("Enter product URL: ")

    print("\n Scraping reviews...")
    reviews = scrape_reviews(url)

    final_data = []

    print(" Processing with LLM...\n")

    for i, r in enumerate(reviews):
        cleaned = clean_text(r["text"])
        summary = analyze_review(cleaned)

        final_data.append({
            "original_review": r["text"],
            "rating": r["rating"],
            "summary": summary
        })

        print(f"Processed {i+1}/{len(reviews)}")
        time.sleep(1)  # avoid rate limits

    df = pd.DataFrame(final_data)
    df.to_csv("reviews_output.csv", index=False)

    print("\n Done! Saved to reviews_output.csv")

if __name__ == "__main__":
    main()