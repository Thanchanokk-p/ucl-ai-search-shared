# 🔍 RedPajama + RefinedWeb Analysis

This project explores the use of the **RedPajama** dataset — an open-source, pretraining-ready web-scale dataset — to enhance Large Language Model (LLM) performance for enterprise and retail applications. Further analysis will also include **RefinedWeb** as a comparative fine-tuning dataset for domain-specific optimization.

---

## 📚 What is RedPajama?

**RedPajama** is a massive, pretraining-quality dataset built to replicate the data mixture used to train models like LLaMA. It includes a variety of high-quality sources, mainly from Common Crawl

> Compared to RefinedWeb, RedPajama offers a broad and diverse foundation ideal for pretraining. It is rich in metadata and coverage but tends to be more raw and less filtered. RedPajama provides expansive general knowledge, while RefinedWeb delivers high-quality, domain-specific content tailored for downstream tasks in enterprise.

---

## 🎯 Project Objectives

Our goal is to explore how combining RedPajama's generalist pretraining base with RefinedWeb's domain-specific content can lead to:

- Smarter, brand-aware chatbots  
- Improved customer sentiment modeling  
- Enhanced internal search and business intelligence tools  

---

## ⚙️ Environment Versions

This project was tested using:

```python
Python: 3.12.8 [conda-forge, GCC 13.3.0]  
NumPy: 1.26.4  
Pandas: 2.2.3  
PySpark: 4.0.0
```
Ensure your local or cloud environment matches or is compatible with these versions to avoid compatibility issues, especially with PySpark.

## 🗂️ Project Structure
```bash
refinedweb-shared/
├── data/
│   ├── csv_data/          # Intermediate processed CSVs
│   ├── filtered_data/     # Cleaned data after brand filtering
│
├── notebooks/
│   ├── 1_refinedweb-analysis.ipynb       # Spark-based EDA and filtering
│   └── 2_refinedweb_analysis_nlp.ipynb   # BERT modeling and text analytics
│
├── Dockerfile
├── get-docker.sh
├── requirements.txt
├── docker-compose.yml
└── README.md

---

### 🗃️ Data Folders

These directories are part of the project structure, but their contents (e.g., `.csv`, `.parquet`) are excluded from version control via `.gitignore`. You will find `.gitkeep` files to preserve their presence in the repository:
```bash
data/
├── csv_data/ # Stores intermediate CSVs
├── filtered_data/ # Output from Spark
```

Make sure your preprocessing or download scripts populate these folders as needed.

---

## 🚀 Getting Started

### 🛠️ Install Dependencies

```bash
pip install -r requirements.txt
```
Or inside a Jupyter Notebook:
```bash
!pip install -r ../requirements.txt
```


🐳 Run via Docker
```bash
# Build the Docker image
docker build -t refinedweb-env .

# Run the container and expose Jupyter
docker run -it -p 8888:8888 refinedweb-env
```

Navigate to http://localhost:8888 to open the notebook interface.

You should see the Jupyter Notebook interface. The first notebook to open is:
notebooks/1_refinedweb-analysis.ipynb


