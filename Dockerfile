# Base Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose ports
EXPOSE 8501
EXPOSE 8000

# Run both frontend and backend
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.headless=true"]


