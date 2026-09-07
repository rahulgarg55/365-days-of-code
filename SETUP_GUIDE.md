# 🛠️ 365 Days of Code: Complete Setup & Deployment Guide

This guide walks you through setting up your automated daily project repository in under 5 minutes.

---

## 🔑 Step 1: Get Your Free Google Gemini API Key

1. Go to **[Google AI Studio](https://aistudio.google.com/app/apikey)**.
2. Sign in with your Google account.
3. Click **"Create API Key"** (or select an existing Google Cloud project).
4. Copy the generated API key (it starts with `AIza...`).

> 💡 **Cost Note**: Google AI Studio provides a generous **free tier** for Gemini 2.0 Flash / 1.5 Flash that is more than sufficient for running 1 project generation per day at $0 cost.

---

## 📁 Step 2: Create a New GitHub Repository

1. Go to **[GitHub -> New Repository](https://github.com/new)**.
2. Repository name: e.g. `365-days-of-code` or `daily-engineering-projects`.
3. Choose **Public** (recommended so it showcases on your GitHub profile) or **Private**.
4. Do **not** initialize with README or .gitignore (we already built them).
5. Click **"Create repository"**.

---

## 💻 Step 3: Push This Setup to Your New Repository

Open PowerShell or terminal in this folder (`daily-projects-engine`):

```powershell
# Move into the engine directory
cd "c:\Users\Xiaomi\Downloads\Projects\reportiq\daily-projects-engine"

# Initialize git repository
git init -b main

# Add all files
git add .
git commit -m "🎉 Initial commit: 365 Days of Code Automation Engine"

# Connect to your new GitHub repository (replace YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/365-days-of-code.git

# Push to GitHub
git push -u origin main
```

*(Alternatively, you can copy the contents of `daily-projects-engine` into any folder you prefer on your computer, initialize git, and push).*

---

## 🔐 Step 4: Add the Gemini API Key to GitHub Repository Secrets

1. In your GitHub repository, click on the **Settings** tab.
2. In the left sidebar, expand **Secrets and variables** and click **Actions**.
3. Click the green button: **"New repository secret"**.
4. Fill in the fields:
   - **Name**: `GEMINI_API_KEY`
   - **Secret**: Paste your Google Gemini API key from Step 1 (`AIza...`)
5. Click **"Add secret"**.

---

## ⚙️ Step 5: Grant GitHub Actions Write Permissions

By default, GitHub Actions workflows have read-only access. You need to enable write access so the bot can commit and push the newly generated daily projects:

1. In your repository, go to **Settings** -> **Actions** -> **General**.
2. Scroll down to the **"Workflow permissions"** section.
3. Select **"Read and write permissions"**.
4. Check the box: **"Allow GitHub Actions to create and approve pull requests"**.
5. Click **Save**.

---

## 🚀 Step 6: Test Your First Run (Manual Trigger)

You don't need to wait until midnight UTC to see it work! You can trigger the first project immediately:

1. In your repository, click on the **Actions** tab.
2. In the left sidebar, click **"Daily Project Automation Engine"**.
3. Click the **"Run workflow"** dropdown on the right side.
4. (Optional) Check *Dry Run* if you want to test without consuming any API quota, or leave it unchecked to let Gemini craft Day 1 right away!
5. Click **"Run workflow"**.

In ~60 seconds:
- Gemini will architect, code, and document a unique project.
- It will commit the project files into `projects/day-001-...`.
- It will update `projects_history.json` and the dashboard table in `README.md`.
- Your GitHub profile will show green activity!

---

## 🕒 Daily Schedule Details

The workflow is configured in `.github/workflows/daily-project.yml` with the schedule:
```yaml
schedule:
  - cron: '0 0 * * *'  # Runs automatically at 00:00 UTC every day
```
You never need to leave your computer running—GitHub's cloud servers handle everything automatically!
