# YouTube Video Recommendation System 📺

A Machine Learning-based desktop application that suggests YouTube videos based on content similarity. Developed using Python, this project implements NLP techniques to find related content within a video metadata dataset.

## 📅 Project Context
* **Originally Created:** January 2025 (Final Board Practical Project)
* **GitHub Release:** March 2026
* **Status:** Complete & Functional

---

## 🚀 Overview
This project solves the "cold start" problem in recommendations by using **Content-Based Filtering**. Instead of relying on user history, the engine analyzes the metadata of a video (Title, Description, and Category) to identify patterns and suggest the top 5 most similar videos.

---

## 📊 Dataset
The dataset used in this project was sourced from **Kaggle**: [YouTube Analytics Data](https://www.kaggle.com/datasets/shaistashahid/youtube-analytics-data).
- **Format:** CSV
- **Key Features Used:** `title`, `description`, `category`, and `link`.
- **Content:** Metadata covering various niches including Travel, History, and Science.

---

## 🛠️ Technical Stack
* **Language:** Python 3.12+
* **GUI Framework:** `Tkinter`
* **Data Handling:** `Pandas`
* **Machine Learning:** `scikit-learn`
    * **TF-IDF Vectorization:** Converts text into numerical importance scores.
    * **Cosine Similarity:** Measures the angular distance between video vectors to find matches.
