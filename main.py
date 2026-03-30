import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import tkinter as tk
from tkinter import messagebox

# 1. Load the data 
# Update the path below to where your 'youtube.csv' is saved
try:
    data = pd.read_csv('youtube.csv') 
except FileNotFoundError:
    # Fallback for demonstration if file isn't in the local folder
    messagebox.showerror("Error", "youtube.csv not found. Please check the file path.")

# 2. Preprocessing
# Handle missing values
data['description'] = data['description'].fillna('')
data['title'] = data['title'].fillna('Unknown Title')

# Create a combined 'content' column for better matching
# We use Title, Description, and Category to find similarities
data['content'] = data['title'] + ' ' + data['description'] + ' ' + data['category']

# 3. TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['content'])

# 4. Compute cosine similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# 5. Recommendation function
def get_recommendations(title):
    # Check if title exists (case-insensitive)
    if not data['title'].str.contains(title, case=False).any():
        return "Video not found"
    
    # Get index of the first video matching the title
    idx = data[data['title'].str.contains(title, case=False)].index[0]
    
    # Get similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get top 5 similar videos (skipping the first one as it's the video itself)
    sim_scores = sim_scores[1:6]
    video_indices = [i[0] for i in sim_scores]
    
    # Return specific columns from your CSV
    return data.iloc[video_indices][['link', 'title', 'category']]

# 6. GUI setup
def recommend_videos():
    user_input = title_entry.get()
    if not user_input.strip():
        messagebox.showwarning("Input Error", "Please enter a video title.")
        return

    recommendations = get_recommendations(user_input)

    if isinstance(recommendations, str):
        messagebox.showerror("Error", recommendations)
    else:
        result = f"Top recommendations for '{user_input}':\n\n"
        for _, row in recommendations.iterrows():
            # Format: Title (Category) - Link
            result += f"• {row['title']}\n  Category: {row['category']}\n  Link: {row['link']}\n\n"
        
        # Create a popup with the results
        result_window = tk.Toplevel(root)
        result_window.title("Recommendations")
        tk.Label(result_window, text=result, justify="left", padx=10, pady=10).pack()

root = tk.Tk()
root.title("YouTube Content Recommender")
root.geometry("400x200")

tk.Label(root, text="Enter a Video Title (e.g., 'Bali' or 'Scandinavia'):").pack(pady=10)

title_entry = tk.Entry(root, width=50)
title_entry.pack(pady=5)

recommend_button = tk.Button(root, text="Get Recommendations", command=recommend_videos, bg="red", fg="white")
recommend_button.pack(pady=20)

root.mainloop()