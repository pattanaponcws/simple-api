FROM python:3.7-alpine

# Set working directory
WORKDIR /app

# Environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Install Gunicorn
RUN pip install gunicorn

# Expose the port Gunicorn will run on
EXPOSE 5000

# Copy project files
COPY . .

# Run the application with Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]