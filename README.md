# K‑pop Explorer 🎶

K‑pop Explorer is a beginner‑friendly **Flask web application** that allows users to explore, search, add, and manage information about K‑pop groups through an interactive website interface.  
The project demonstrates full‑stack fundamentals, including backend routing, template rendering, and frontend interactivity with JavaScript.

---

## 🌐 Website Overview

The K‑pop Explorer website is designed as a simple CRUD-style application centered around K‑pop groups.

### 🏠 Home Page
- Displays a list of all K‑pop groups stored in the system
- Acts as the main navigation hub
- Each group can be clicked to view more detailed information

### 🔍 Search Page
- Allows users to search for K‑pop groups by name or keyword
- Results are shown on a dedicated search results page
- Designed to demonstrate form handling and dynamic rendering

### 👁️ Group Detail Page
- Shows detailed information for a selected K‑pop group
- Serves as a read‑only view for existing data
- Links to edit the current group

### ➕ Add Item Page
- Provides a form for users to add a new K‑pop group
- Collects group‑related information through input fields
- On successful submission, redirects to a confirmation page

### ✏️ Edit Item Page
- Allows users to modify existing group information
- Pre‑populates the form with current data
- Updates are reflected immediately after submission

### ✅ Success Page
- Confirms successful add or edit operations
- Improves user feedback and flow clarity

---

## ✨ Key Features

- Full CRUD functionality (Create, Read, Update)
- Flask routing with Jinja2 templates
- Client‑side JavaScript for enhanced interactivity
- Clean layout with shared base template
- Beginner‑friendly project structure

---

## 🎥 Demo Video

[Watch the demo on YouTube]([https://youtu.be/EKRNJkGr39c](https://youtu.be/n_SqJQC0hTM))

---

## 🧱 Tech Stack

**Backend**
- Python
- Flask

**Frontend**
- HTML (Jinja2 templating)
- CSS
- Vanilla JavaScript

---

## 📁 Project Structure

```
K-pop-Explorer-main/
├── server.py              # Flask application and routes
├── static/
│   ├── home.js
│   ├── add_item.js
│   ├── edit_item.js
│   ├── search_results.js
│   ├── main.css
│   └── background_image.jpg
├── templates/
│   ├── layout.html        # Base layout template
│   ├── home.html
│   ├── add_item.html
│   ├── edit_item.html
│   ├── search_results.html
│   ├── view_group.html
│   └── success.html
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/K-pop-Explorer.git
cd K-pop-Explorer-main
```

### 2. (Optional) Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate    # Windows
```

### 3. Install dependencies
```bash
pip install flask
```

### 4. Run the application
```bash
python server.py
```

### 5. Open the website
Visit:
```
http://127.0.0.1:5000
```

---

## 🎯 Project Purpose

This project is intended for:
- Learning Flask fundamentals
- Practicing backend–frontend integration
- Understanding CRUD workflows in web applications
- Building confidence with small full‑stack projects

---

## 📄 License

This project is for educational purposes.  
You are free to modify, extend, or reuse it for learning and personal projects.

---

Enjoy exploring K‑pop through code! 💿✨
