
# DevOps Internship Project
CI/CD, Docker, Kubernetes, Monitoring with Datadog.
=======
# DevOps Internship Assignment 🚀

This repository contains the solution to my DevOps internship assignment. The project demonstrates setting up CI pipelines using GitHub Actions and CircleCI, Dockerizing a FastAPI application, and monitoring using Datadog.


## ✅ Key Highlights

- **CI with GitHub Actions and CircleCI**
- **Dockerized FastAPI app**
- **Monitored using Datadog Agent on Kubernetes**
- **Used DockerHub for container image storage**

---

## 🚀 How to Run

 1. Build Docker Image


docker build -t myfastapiapp .

2. Run Docker Container


docker run -d -p 8000:8000 myfastapiapp


🔁 Continuous Integration
GitHub Actions
Automatically triggers on push to main branch.

Installs dependencies and checks build.

CircleCI
Builds Docker image

Pushes to DockerHub (using stored secrets)

📈 Monitoring
Datadog Agent deployed as a DaemonSet in Kubernetes.

API Key stored securely as a Kubernetes Secret.

Configured to collect logs and metrics.

👩‍💻 Author
Hema CJ

Aspiring DevOps Engineer 💻☁️


GitHub: hemajairam

📄 License
This project is for learning and internship demonstration purposes.


---

Let me know if you want a shorter version or want to include screenshots, badges, or links to pipelin
