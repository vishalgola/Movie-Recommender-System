# 🎬 Movie Recommender System

A content-based Movie Recommender System built using **Bag of Words** and **Cosine Similarity**, designed with a focus on choosing the *right approach for the data* rather than blindly following complex models.

---

## 🚀 Live Demo

👉 **Try the App:** https://movie-recommender-system-11.streamlit.app/

---

## 📸 Demo Preview

<img width="941" height="438" alt="image" src="https://github.com/user-attachments/assets/5ed65f78-b448-479a-9923-b1a9fc10711a" />


---



Most recommender systems use **TF-IDF** or **SBERT** without considering whether the dataset supports such techniques.

This project takes a different approach:

* Analyzes dataset limitations first
* Chooses a method accordingly
* Focuses on **practical performance over complexity**

---

## ⚙️ Tech Stack

* **Python**
* **Streamlit** (Deployment & UI)
* **Pandas / NumPy**
* **Scikit-learn**
* **TMDB API** (for movie posters)
* **Google Drive** (for storing data and model pickle files) 

---

## 🔍 Approach

### 1. Feature Engineering

* Used **Bag of Words (BoW)** to convert textual metadata into vectors
* Suitable for datasets with limited semantic richness

### 2. Similarity Computation

* Applied **Cosine Similarity** to measure closeness between movies

### 3. Recommendation Logic

* Finds top similar movies based on vector similarity
* Returns top 5 recommendations

---

## ✨ Features

* 🎯 Content-based movie recommendations
* 🖼️ Movie posters fetched dynamically using TMDB API
* ⚡ Fast and interactive UI with Streamlit
* ☁️ Handles large model files via external hosting (Google Drive)

---

## 📂 Project Structure

```
Movie-Recommender-System/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── model/
│   ├── movie_list.pkl
│   ├── similarity.pkl
```

---


```

## 📌 Key Learnings

* Choosing the right model > using the most advanced model
* Simpler approaches can outperform complex ones on the right data
* Deployment introduces real-world challenges (file handling, APIs, caching)

---

## 🚧 Limitations

* Uses static similarity matrix (not dynamic learning)
* No user personalization
* Dependent on external model hosting

---

## 🔮 Future Improvements

* Add user-based recommendations
* Optimize similarity matrix size
* Improve UI (Netflix-style layout)
* Add filtering (genre, rating, year)



## 📬 Contact

For feedback or collaboration:

* LinkedIn:=https://www.linkedin.com/in/vishal-prajapati93/

---

💡 *Built with the mindset: Understand data first, then choose the model.*
