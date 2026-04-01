Movie Review Sentiment Analysis (NLP)


Project Overview

The goal of this project was to build a machine learning model capable of classifying movie reviews as positive or negative based on their text content. This project demonstrates the full Data Science lifecycle: from raw CSV data processing to deep model error analysis.


Dataset

The model was trained using the IMDb Dataset, which contains 50,000 highly polar movie reviews labeled as positive or negative.


Step-by-Step Process

1. Text Preprocessing
Raw text was cleaned to remove informational "noise":
  - Lowercasing: Standardizing all text to lowercase.
  - HTML Cleaning: Removing <br /> tags common in web-scraped data.
  - Punctuation Removal: Eliminating special characters.
  - Stopwords Removal: Using the nltk library to filter out frequent but meaningless English words (e.g., the, a, in, is).

2. Feature Engineering (TF-IDF)
Text data was converted into numerical format using TfidfVectorizer.
  - N-grams: I implemented an ngram_range of (1, 3), allowing the model to "see" single words, pairs, and triplets (e.g., "not good" vs. "good"). This is crucial for capturing context.

3. Modeling
I used a Logistic Regression algorithm wrapped in a Pipeline. This ensures that the same transformation steps are applied consistently to both training and testing data.


Model Evolution & Results
The model underwent several iterations of hyperparameter tuning:

|...Version.......|Changes (Parameters).|Test Accuracy|..Conclusion..........................|
|v1 (Basic).......|TF-IDF (5k features),|..88.99%.....|..Solid start, but....................|
|                 | Default LogReg      |             |  struggles with metaphors.           |
|v2 (Overfitted)..|N-grams (1,2),.......|..90.02%.....|..Highest score, but too..............|
|                 | C=10.0              |             |  "rigid" for creative language.      |
|v3 (Final).......|N-grams (1,3),.......|..89.52%.....|..The Sweet Spot. Better..............|
|                 |C=0.5                |             |  generalization on complex reviews.  |


Challenges & Solutions

- Problem: ModuleNotFoundError for NLTK/Pandas
  - Cause: The Jupyter Notebook kernel was not synchronized with the system's Python environment.
  - Solution: Installed packages directly within the notebook using !pip install and restarted the kernel to ensure the path was updated.

- Problem: Misclassification of Literary Reviews
  - Cause: The model initially failed on reviews like "Instead of paper cutouts, we have flesh-and-blood characters." It saw words like "paper" and "cutouts" as negative indicators.
  - Solution: I expanded the N-grams to triplets and lowered the regularization parameter C to 0.5. This prevented the model from over-relying on specific "negative" words and forced it to look at the broader context.


Final Analysis (Confusion Matrix)
Analysis of the 10,000-review test set revealed:
- True Positives/Negatives: Over 8,900 correct classifications.
- False Negatives (451): The model still occasionally misidentifies highly descriptive, intelligent praise as negative if it contains "sad-sounding" vocabulary (e.g., melancholic, drowsiness).


Key Takeaways

This project proved that Accuracy is not the only metric. While Version 2 had a higher score, Version 3 was more robust when faced with real-world, nuanced human language. While advanced deep learning models (like BERT) are better at sarcasm, a well-tuned Logistic Regression + TF-IDF remains a highly efficient and powerful baseline for sentiment analysis.
