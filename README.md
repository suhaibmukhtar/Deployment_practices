1. Create a Simple Project with Dockerfile
Let's say project is a simple Python Flask app.

Project Structure

my_project/
│── app.py
│── requirements.txt
│── Dockerfile
app.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

requirements.txt
flask

2. Create a Dockerfile
Inside your project folder (my_project), create a Dockerfile:
dockerfile

# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]

3. Build the Docker Image
Navigate to the project directory and run

docker build -t my_flask_app .
This builds the Docker image and tags it as my_flask_app.

4. Run the Docker Container
After building the image, run the container:

docker run -p 5000:5000 my_flask_app
Now, your Flask app should be running at http://localhost:5000.

5. Push the Docker Image to Docker Hub
(a) Login to Docker Hub

docker login
Enter your Docker Hub credentials.

(b) Tag Your Image
You need to tag the image with your Docker Hub username and repository name.

docker tag my_flask_app YOUR_DOCKERHUB_USERNAME/my_flask_app
(c) Push the Image

docker push YOUR_DOCKERHUB_USERNAME/my_flask_app
Now, the image is available on Docker Hub.

6. Pull the Docker Image from Another Machine
If you want to run this image on another system, you can pull it from Docker Hub:

docker pull YOUR_DOCKERHUB_USERNAME/my_flask_app
7. Run the Pulled Image

docker run -p 5000:5000 YOUR_DOCKERHUB_USERNAME/my_flask_app
Now, the container should be running on another machine.

🎯 Summary of Commands
sh
Copy
Edit
# Build the Docker image
docker build -t my_flask_app .

# Run the container
docker run -p 5000:5000 my_flask_app

# Login to Docker Hub
docker login

# Tag the image
docker tag my_flask_app YOUR_DOCKERHUB_USERNAME/my_flask_app

# Push the image to Docker Hub
docker push YOUR_DOCKERHUB_USERNAME/my_flask_app

# Pull the image from Docker Hub
docker pull YOUR_DOCKERHUB_USERNAME/my_flask_app

# Run the pulled image
docker run -p 5000:5000 YOUR_DOCKERHUB_USERNAME/my_flask_app