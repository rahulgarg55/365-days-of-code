# 🚀 365 Days of Code: Daily Engineering Showcase

![Progress](https://img.shields.io/badge/Progress-2%20%2F%20365%20Days-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Daily%20Automation-Active-blue?style=for-the-badge)
![AI Powered](https://img.shields.io/badge/Engine-Google%20Gemini-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)

Welcome to the **365 Days of Code Showcase**! 

Every single day at **00:00 UTC**, an automated GitHub Action workflow executes, prompting **Google Gemini** to engineer, structure, document, and push a brand-new, production-grade micro-project.

### 🌟 Project Philosophy
- **Zero Meaningless Commits**: No "Hello World" or copy-paste CRUDs. Every day tackles a distinct, real-world utility (rate limiters, webhook signers, inverted search indexes, async workers, cryptographic vaults).
- **Diverse Tech Rotation**: Rotates through **Modern PHP (8.2+ OOP)**, **MERN / Full-Stack JS/TS**, **Python FastAPI / Async**, **Go Concurrency**, and **TypeScript Tooling**.
- **Self-Documenting**: Each mini-project includes architectural diagrams, complete executable code, tests, and setup instructions.
- **Zero Duplicates**: State is maintained in `projects_history.json` to guarantee completely unique projects across all 365 days.

---

## 📊 Progress Dashboard
- **Completed**: `2 / 365` mini-projects (0.5%)
- **Last Updated**: `2026-09-07 06:33 UTC`

| Day | Project Title | Tech Stack | Concepts / Tags | Code Link |
| :--- | :--- | :--- | :--- | :--- |
| **Day 002** | [Token Bucket Rate Limiter (PHP)](./projects/day-002-php-rate-limiter) | `PHP Modern (OOP & Micro-Service)` | `rate-limiting` `security` `algorithms` | [View Code](./projects/day-002-php-rate-limiter) |
| **Day 001** | [Token Bucket Rate Limiter (MERN)](./projects/day-001-mern-rate-limiter) | `MERN / Node.js & React Full-Stack` | `rate-limiting` `security` `algorithms` | [View Code](./projects/day-001-mern-rate-limiter) |

---

## ⚙️ How It Works Under The Hood
1. **GitHub Actions Cron**: A scheduled workflow triggers daily (`.github/workflows/daily-project.yml`).
2. **History & Rotation Inspection**: `generator/generate.py` checks `projects_history.json` to determine the day number and next tech stack.
3. **Structured Generation**: Google Gemini constructs a complete project with strict Pydantic JSON validation.
4. **File Synthesis & Validation**: Files are safely created under `projects/day-XXX-<slug>/`.
5. **Auto-Commit**: GitHub Actions commits and pushes with automated release notes.

---

## 📜 License
MIT License. Feel free to explore, clone, and learn from any of the mini-projects in this repository!
