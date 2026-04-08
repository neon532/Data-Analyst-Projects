Customer Opinion Analysis Pipeline (LLM Edition)

Project Overview

The objective of this project was to transition from traditional Machine Learning (Logistic Regression/TF-IDF) to a modern Large Language Model (LLM) approach for sentiment analysis. While my previous project achieved a solid 89.52% accuracy, it struggled with the nuance of human language, metaphors, and sarcasm.

This project solves those limitations by utilizing GPT-4o-mini via the OpenAI API to provide high-precision sentiment analysis and concise summaries, wrapped in a scalable data pipeline that exports results to business-ready formats.


Why This Project? (The Evolution)

In my previous NLP project (Movie Reviews), I used a Logistic Regression model. Even with tuned N-grams, the model was "blind" to context—it saw individual words but didn't truly "understand" the meaning.

I didn't want to take the easy way out. Instead of just running a simple script, I built a production-ready tool that:

  1. Improves Accuracy: Leverages the semantic understanding of LLMs.
  2. Scalability: Moves away from "hardcoded" strings to a file-based database system.
  3. Data Portability: Generates structured CSV/XLS data for further training or business reporting.


The Pipeline Process

  1. External Database (opinion_base.txt): To make the tool useful, I designed it to read from an external text file. This allows for batch processing of thousands of opinions without touching the Python code.
  2. Environment Isolation: Implementation of a Virtual Environment (venv) and .env security to protect API credentials.
  3. LLM Integration: Using the OpenAI chat.completions API with a system prompt forcing JSON output for structured data integrity.
  4. Data Transformation: Converting raw LLM responses into a tabular format using the Python csv module.


Comparison: Traditional ML vs. LLM Pipeline

While my previous project relied on traditional statistical methods like Logistic Regression and TF-IDF, which were limited to analyzing word frequency and often missed the deeper context of human language, this current pipeline represents a significant technological leap by utilizing the semantic understanding of GPT-4o-mini. Instead of generating simple "Positive" or "Negative" labels, this new system produces structured JSON objects that include both a sentiment score and a concise summary. Furthermore, the workflow has evolved from manual input to a scalable batch processing system that reads from .txt files and exports professional, business-ready reports in .csv or .xls format, providing much greater utility for further data analysis compared to basic console logs.


Challenges & Solutions

Problem: Security Risks & Hardcoded Keys
  - Initially, the API key was handled as a string. To follow industry best practices, I moved the sensitive data to an external file (open_ai__api_key) and used python-dotenv to load it securely.

Problem: PowerShell Execution Policies
During the setup of the venv, Windows blocked the activation script.
  - Solution: I diagnosed the issue as a restriction in PowerShell and successfully migrated the workflow to Command Prompt (CMD), ensuring the environment was properly isolated.

Problem: Handling API Rate Limits & Quotas
When testing with large batches, API limits can cause a program to crash.
  - Solution: I implemented a try-except block within the analysis function. This ensures that even if one request fails (e.g., due to quota limits), the rest of the pipeline remains stable.

Problem: CSV Formatting for Excel
Standard CSV files often fail to open correctly in Excel due to encoding or delimiters.
  - Solution: I used utf-8-sig encoding to support special characters and changed the delimiter to a semicolon (;), ensuring the file opens perfectly in Microsoft Excel for business users.


Project Structure
  - main.py: The core engine of the pipeline.
  - opinion_base.txt: The input file where each line represents a new customer opinion.
  - open_ai__api_key: (Excluded from Git) Contains the secure API key.
  - analysis_results.csv: The final generated report.
  - venv/: Isolated environment for project dependencies(on Git in 2 parts zip files to marge via extract).


Key Takeaways
This project demonstrates that while traditional ML models are efficient baselines, LLM-based pipelines provide a level of intelligence and flexibility that is essential for modern data tasks. I have successfully built a bridge between raw text data and structured analytical reports.


How to run:
  1. Place your opinions in opinion_base.txt (one per line).
  2. Ensure your API key is in the config file.
  3. Run python main.py.
  4. Open analysis_results.csv to see your results.
