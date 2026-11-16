# Lab 8: Implementing Applications using Platform as a Service (PaaS) on Render

## Aim
To become familiar with the **Platform as a Service (PaaS)** cloud computing model and implement, deploy, monitor, and manage a Python web application using **Render** (as a zero-billing alternative to Google App Engine).

---

## Overview of Tasks
| Task | Objective | Expected Deliverable / Evidence |
| :--- | :--- | :--- |
| **Task 1** | Understand PaaS and configure a Render account & project environment | Render dashboard setup and deployment region configuration |
| **Task 2** | Develop and test a simple Python Flask web application locally | Working web application running at `http://127.0.0.1:8080` |
| **Task 3** | Push code to GitHub and deploy the application on Render | Live HTTPS application accessible via `https://<your-app>.onrender.com` |
| **Task 4** | Manage versions, monitor logs, redeploy updates, and inspect metrics | Live logs, multiple deployment versions (V1 & V2), and resource metrics |

---

## Task 1: Introduction to PaaS and Render Setup

### 1.1 What is Platform as a Service (PaaS)?
Platform as a Service (PaaS) is a cloud computing model in which a third-party provider delivers hardware and software tools over the internet so developers can build, deploy, and manage applications without maintaining underlying infrastructure.

* **Managed by the PaaS Provider (Render):** Physical servers, networking, operating system, Python runtime environment, SSL certificates, and automatic builds/deployments.
* **Managed by the Developer:** Application source code (`main.py`) and dependency definitions (`requirements.txt`).

### 1.2 Account and Environment Preparation
1. Create a free account on [GitHub](https://github.com) (if you do not already have one).
2. Navigate to [Render](https://render.com) and sign up using **GitHub Authentication** (no credit card or billing details required).
3. Familiarize yourself with the Render Dashboard, where you can create **Web Services**, inspect **Logs**, manage **Deploys/Versions**, and monitor **Metrics**.

---

## Task 2: Develop and Test the Web Application Locally

### Step 1: Create the Project Directory
Open your terminal or command prompt and create a dedicated directory for the lab:

```bash
mkdir cloud-lab8
cd cloud-lab8
```

### Step 2: Create the Application File (`main.py`)
Create a file named `main.py` inside `cloud-lab8` and add the following Flask application code:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Cloud Computing Lab 8</h1>
    <p>Application successfully implemented using Render (PaaS).</p>
    <p>This application demonstrates Platform as a Service (PaaS).</p>
    """

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
```

**Code Explanation:**
* `Flask(__name__)` initializes the Flask web application instance (`app`).
* `@app.route("/")` maps the root URL path (`/`) to the `home()` function.
* `home()` returns the HTML response displayed in the browser.
* `app.run(...)` starts the local development server on port `8080` for local verification.

### Step 3: Create the Dependencies File (`requirements.txt`)
Create a file named `requirements.txt` in the same directory:

```text
Flask
gunicorn
```

> **Note:** `Flask` is the web framework, while `gunicorn` is a production-grade Python WSGI HTTP server used by Render to run the application in the cloud.

### Step 4: Run and Test Locally
1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the local server:
   ```bash
   python main.py
   ```
3. Open a web browser and visit:
   ```text
   http://127.0.0.1:8080
   ```
4. **Verification:** Confirm that the page renders the **"Cloud Computing Lab 8"** heading. Press `Ctrl + C` in the terminal to stop the local server before proceeding.

---

## Task 3: Configure and Deploy the Application to Render

### Step 1: Push the Application to GitHub
Render deploys applications directly from Git repositories. Initialize Git locally and push your files to a new GitHub repository (e.g., `cloud-lab8`):

```bash
git init
git add main.py requirements.txt
git commit -m "Initial commit - Version 1"
git branch -M main
git remote add origin https://github.com/<your-username>/cloud-lab8.git
git push -u origin main
```

### Step 2: Create a Web Service on Render
1. Log in to the [Render Dashboard](https://dashboard.render.com).
2. Click **New +** in the top navigation bar and select **Web Service**.
3. Under **Build and deploy from a Git repository**, locate your `cloud-lab8` repository and click **Connect**.

### Step 3: Configure Service Settings & Region
Fill in the deployment settings as follows:
* **Name:** `cloud-lab8` (or a unique service name)
* **Region:** Select the geographic region closest to you (e.g., `Singapore` or `Oregon`) — *Note: Like Google App Engine, the region is locked upon creation.*
* **Branch:** `main`
* **Language / Runtime:** `Python 3`
* **Build Command:**
  ```bash
  pip install -r requirements.txt
  ```
* **Start Command:**
  ```bash
  gunicorn main:app
  ```
* **Instance Type:** Select **Free** (`$0/month`, 512 MB RAM, 0.1 CPU)

Click **Deploy Web Service**.

### Step 4: Verify the Deployed Application
1. Monitor the **Deploy Logs** in Render as it installs dependencies and starts Gunicorn.
2. Once the log displays `Your service is live 🎉`, copy your public Render URL at the top-left of the dashboard (e.g., `https://cloud-lab8.onrender.com`).
3. Open the URL in your browser.
4. **Verification:** Confirm that your live cloud-hosted webpage loads over HTTPS and displays the **Cloud Computing Lab 8** message.

---

## Task 4: Application Monitoring, Versions, and Management

### Task 4A: Explore Application Versions (Deploys)
1. In the Render service dashboard, click **Events** (or **Deploys**) in the left sidebar.
2. **Observe:**
   * **Commit Hash & Message:** `Initial commit - Version 1`
   * **Status:** `Live`
   * **Timestamp:** Build and deployment completion time
   * **Rollback Option:** Ability to revert to previous versions if needed.

### Task 4B: Monitor Application Logs
1. Click **Logs** in the left sidebar of your Render service.
2. Open your live `https://<your-app>.onrender.com` URL in another browser tab and refresh it 3–5 times.
3. **Observe:** The live log stream immediately records incoming HTTP traffic (e.g., `GET / HTTP/1.1` with status code `200`), demonstrating real-time cloud observability without SSH access.

### Task 4C: Modify and Redeploy the Application (Version 2)
1. Open `main.py` on your local machine and update the HTML output to indicate **Version 2**:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to Cloud Computing Lab 8</h1>
    <p>Application Version 2</p>
    <p>Successfully deployed using Render (PaaS).</p>
    """

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
```

2. Commit and push the changes to GitHub to trigger Render's continuous deployment (CD) pipeline:

```bash
git add main.py
git commit -m "Deploy Version 2"
git push origin main
```

3. **Verify:**
   * Return to the **Events** tab in Render and watch the new deployment (`Deploy Version 2`) build automatically and replace Version 1 with zero downtime.
   * Refresh your live `.onrender.com` URL in the browser and verify that **Application Version 2** is displayed.

### Task 4D: Explore PaaS Management Features
Explore the remaining sections of the Render Dashboard to observe managed cloud operations:
* **Metrics:** View real-time graphs of **CPU** and **Memory** consumption managed by the platform.
* **Environment:** Inspect or add environment variables (`KEY=VALUE`) without modifying source code.
* **Settings:** Review auto-deploy triggers, health check paths, start/build commands, and instance scaling options.

---

## Troubleshooting Note: `ModuleNotFoundError: No module named 'app'`
* **Cause:** If the **Start Command** is left at Render's default (`gunicorn app:app`), Gunicorn searches for a file named `app.py` instead of `main.py`.
* **Resolution:** Go to **Settings > Build & Deploy > Start Command**, update it to `gunicorn main:app` (where `main` refers to `main.py` and `app` refers to the `app = Flask(__name__)` object), and save changes to trigger an automatic restart.

---

## Conclusion
In this experiment, a Python Flask web application was developed locally, version-controlled via GitHub, and deployed to the cloud using **Render (PaaS)**. Through this workflow, the platform automatically provisioned the runtime environment, installed dependencies, served the application via HTTPS, provided real-time HTTP request logs and resource metrics, and automated version updates via Git pushes—demonstrating the core capabilities of Platform as a Service without manual server administration.