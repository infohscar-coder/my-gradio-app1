---
title: Quick Image Studio
emoji: 🖼️
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: 4.0.0
app_file: app.py
pinned: false
---

# Quick Image Studio

Quick Image Studio is a Gradio web application for uploading images, converting
them to grayscale, and rotating them by 0, 90, 180, or 270 degrees.

The repository is configured for CI/CD deployment to a Hugging Face Space.
Pushes to the `main` branch, or manually dispatched workflow runs, use GitHub
Actions to synchronize the application with the Space using the `HF_TOKEN`
repository secret.
