# Use Jupyter Docker Stack with PySpark pre-installed
FROM jupyter/pyspark-notebook:latest

# Switch to root to install system-level packages or Python libraries
USER root

# Set working directory
WORKDIR /app

# Copy all project files into container
COPY . .

# Copy Python requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# (Optional) Download SpaCy model if used in notebooks
RUN python3 -m spacy download en_core_web_sm

# Expose Jupyter notebook port
EXPOSE 8888

# Start notebook on container run
CMD ["jupyter", "notebook", "notebooks/1_refinedweb-analysis-1.ipynb", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--NotebookApp.token=''"]
