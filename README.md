# 🤖 UCL AI Search – LLM Fine-Tuning with RefinedWeb & Synthetic Dataset

This project is an **end-to-end evaluation and enhancement pipeline** for domain-specific LLMs. It focuses on boosting performance on **fashion retail**-related prompts using both real and synthetic data sources.

---

## 🔄 Project Overview

We adopt a **four-phase approach**:

1. **Baseline Analysis**  
   Compare model responses from Olmo2 using domain-relevant prompts.
   
2. **Synthetic Dataset Generation**  
   Create augmented data using GPT models (e.g., GPT-3.5, GPT-4) to expand prompt coverage.
   
3. **Fine-Tuning**  
   Fine-tune LLMs using hybrid datasets (RefinedWeb + Synthetic) with different parameter configurations.

4. **Evaluation**  
   Evaluate pre- and post-trained model outputs for improvement in alignment and insightfulness.

---

## 📚 What is RefinedWeb?

RefinedWeb is a cleaned, deduplicated, and filtered web crawl dataset optimized for training and evaluating large-scale language models. It includes high-quality, domain-specific text content suitable for commercial applications such as:

- Brand intelligence  
- Product sentiment analysis  
- Customer service automation  

---

## 🎯 Project Objectives

The main objective is to improve brand ranking both trend and scale that relevance of AI-powered response and insight tools by fine-tuning models on focused web content. This analysis of the pretrained RefinedWeb dataset supports:

- 📈 Improved brand visibility  
- 🤖 Enhanced internal tools (e.g., search assistants, chatbots)  
- 💡 Actionable business insights in:
  - Brand perception  
  - Competitive intelligence  
  - SEO performance  
  - Campaign strategy optimization  

---

## ⚙️ Environment Versions

This project was tested using the following environment setup:

```python
Python: 3.12.8 [conda-forge, GCC 13.3.0]  
NumPy: 1.26.4  
Pandas: 2.2.3  
PySpark: 4.0.0

---

Ensure your local or cloud environment matches or is compatible with these versions to avoid compatibility issues, especially with PySpark.

## 🗂️ Project Structure
```bash
ucl-ai-search/
├── 1_baseline_analysis/
│   └── pretrained_dataset_exploration/
│       └── 1_baseline_llm_response_olmo2_7b.ipynb
│       └── 2_refinedweb_analysis_keyword_extraction_only_pos.ipynb
│       └── 2_refinedweb_analysis_keyword_extraction_pos_and_neu.ipynb
│
├── 2_synthetic_dataset_generation/
│   └── 3_synthetic_data_generation_and_augmentation.ipynb
│
├── 3_finetuning/
│   └── notebook/
│       └── 4_fine_tuning_synthetic_instruct_full.ipynb
│
├── 4_evaluation/
│   └── notebook/
│       └── 5_post_training_llm_response_olmo2_instruction.ipynb
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
---

### 🗃️ Data Folders

These directories are part of the project structure, but their contents (e.g., `.csv`, `.parquet`) are excluded from version control via `.gitignore`. You will find `.gitkeep` files to preserve their presence in the repository:
```bash
data/
├── csv_data/ # Stores intermediate CSVs
├── filtered_data/ # Output from Spark/DuckDB filtering
├── parquet_data/ # Raw files downloaded from HuggingFace
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
