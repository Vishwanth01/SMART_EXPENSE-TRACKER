# 💰 Expense Tracker (Python CLI App)

A simple command-line based Expense Tracker built using Python.
This application helps you record, view, and analyze your daily expenses efficiently.

---

## 🚀 Features

* ➕ Add expenses with date, category, amount, and description
* 📄 View all saved expenses
* 📊 Monthly expense summary
* 🥧 Category-wise breakdown with pie chart visualization
* ⚠️ Spending insights and warnings
* 🗑️ Clear all saved data (with confirmation)

---

## 🛠️ Technologies Used

* Python
* JSON (for data storage)
* Matplotlib (for charts)

---

## 📁 Project Structure

```
expense_tracker/
│
├── expenses.json       # Stores all expense data
├── main.py             # Main application file
└── README.md           # Project documentation
```

---

## ▶️ How to Run

1. Install Python (if not installed)

2. Install required library:

```bash
pip install matplotlib
```

3. Run the program:

```bash
python main.py
```

---

## 📌 How It Works

* Data is stored in a JSON file (`expenses.json`)
* Each expense contains:

  * Date (YYYY-MM-DD)
  * Category (Food, Travel, Shopping, Bills, Rent, Others)
  * Amount
  * Description

---

## 📊 Example Menu

```
--- Expense Tracker ---
1. Add Expense
2. View Expenses
3. Monthly Summary
4. Show Chart
5. Insights
6. Clear All Data
7. Exit
```

---

## ⚠️ Important Notes

* Clearing data will permanently delete all stored expenses
* Ensure correct date format: `YYYY-MM-DD`
* Amount must be greater than 0

---

## 🔮 Future Improvements

* ✏️ Edit existing expenses
* ❌ Delete individual expense
* 📅 Filter by date range
* 📤 Export to Excel/CSV
* 🔐 User authentication.
* 
