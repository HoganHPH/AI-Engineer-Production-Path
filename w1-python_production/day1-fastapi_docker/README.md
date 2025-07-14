# AI Engineer Production Path - Daily Report 🚀

## 📌 Day 1: FastAPI & Docker
**Date:** 14/07/2025  
**Objective:** Build API endpoints, Docker images and integrate a basic ML model with Pydantic data model


### 🛠 Techstack
- FastAPI
- Scikit-learn
- Pydantic
- Docker


### 📝 Contents
1. **API Development**
    - Create endpoint `/predict` with Pydantic validation
    - Details at `src/routers/ml_page.py` file

2. **Train and test a ML model**
    - Dataset: IRIS (4 features, 150 samples)
    - Train a Logistic Regression model (details in `train_ml/train.py` script file)
    - Create Pydantic model for IRIS data samples

3. **Build Docker image**
    - Create `Dockerfile`, build Docker image
    - Check docker image size
    - Test working API with Postman app


### ⚙️ How to run?
1. **Clone repo**
```
git clone https://github.com/yourusername/AI-Engineer-Production-Path.git
```

2. **Create .env file**

Define `HOST` and `PORT` in `.env` file. See `.env.example` file

3. **Run with Docker**
```
docker build -t <docker_image_name>
docker run -p 8000:8000 <docker_image_name>
```


### 📊 Results
1. Docker runs API perfectly and stablly (tested by Postman app)
2. ML model predict new data samples correctly (accuracy score is 100%)
3. Docker image size is 1.2GB (not yet optimized)