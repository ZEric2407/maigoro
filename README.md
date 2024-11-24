# maigoro

# Project Setup Guide

This project consists of a Python/Flask backend and a SvelteKit frontend. Follow the instructions below to set up both environments.

---

## Prerequisites

- **Python 3.8+** (for backend)
- **Node.js and npm** (for frontend)
- **Tesseract OCR** (install separately for OCR functionality in the backend)

---

## Backend Setup

1. **Navigate to the backend directory**:
   ```bash
   cd backend
   ```
2. **Install the required libraries**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Initialize the database**:
   ```
   py model.py
   ```
---

## Frontend Setup

1. **Navigate to the frontend directory**:
   ```bash
   cd ../frontend
   ```

2. **Install the required packages**:
   ```bash
   npm install
   ```

---

## Running the Project

After completing the installation steps, you can run both the backend and frontend servers. Typically, you would:

1. **Run the Flask server** (in the backend directory):
   ```bash
   flask run
   ```

2. **Run the SvelteKit frontend server** (in the frontend directory):
   ```bash
   npm run dev
   ```

---

## Additional Notes

- **Tesseract Installation**: Make sure to install Tesseract OCR on your system, as it is required for OCR functionality in the backend.
- **To Do: Google Lens API reverse search, elasticsearch vector searching, tesseract for text extraction
---
