# 📊 ExpenseManager – Streamlit App

A simple, interactive **Streamlit-based** web application designed to manage and visualize personal expenses in real-time with insightful charts and a responsive UI.

---

## 🔗 Live Demo

👉 [Launch ExpenseManager on Streamlit](#) *(https://app-expensemanager.streamlit.app/)*

## 📝 Description

**ExpenseManager** allows users to easily:
- Track expenses
- Add and view records
- Analyze expense data via dynamic charts and summaries

It uses **in-memory session state** (no database) for lightweight, temporary usage — perfect for demos and quick expense reviews.

---

## 🔧 Features

- ➕ Add expenses with:
  - Date
  - Category
  - Amount
  - Description
- 📋 View a dynamic table of all entered expenses
- 📈 **Real-time statistics** summary:
  - 🥧 Pie Chart – Category-wise breakdown
  - 📊 Bar Chart – Total spent per category
- 🧠 Data retained using Streamlit’s **session state**

---

## 🛠️ Tech Stack

| Layer        | Technology       |
|--------------|------------------|
| Frontend     | Streamlit        |
| Backend      | Python + Pandas  |
| Visualization| Matplotlib, Seaborn |

---

## ▶️ Getting Started

### 📌 Prerequisites

- Python 3.7+
- pip

### 📥 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ExpenseManager.git
cd ExpenseManager

# Install required packages
pip install -r requirements.txt

# Run the app
streamlit run app.py
