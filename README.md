# Personal Finance Manager

A personal finance manager built using **Streamlit**, **SQLAlchemy**, **SQLite**, and **Plotly**. The application allows users to manage their income and expenses, visualize financial trends, and keep track of the balance over time.

## Features
- **Add Income and Expenses**: Users can input and categorize their transactions, including date, amount, and details.
- **Income vs Expenses Visualization**: Graphical representation of income and expenses using pie charts.
- **Daily Trend Tracking**: Line charts to visualize daily income and expense trends.
- **Balance Calculation**: Displays the total balance (income - expenses).

## Requirements
- Python 3.7+
- Streamlit
- SQLAlchemy
- Plotly
- SQLite

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd personal-finance-manager
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```

2. The app will open in your browser. From the sidebar, you can add income or expenses by filling out the form. Each transaction requires the **name/source**, **amount**, **category** (for expenses), and **date** (which defaults to today).

3. The main page will show:
   - A table of your income and expenses.
   - A pie chart comparing income and expenses.
   - Line charts showing daily trends for income and expenses.
   - Your current balance (income minus expenses).

## Database Schema

- **Income**:
  - `id`: Auto-incremented ID (Primary Key)
  - `source`: Source of income (string)
  - `amount`: Amount earned (float)
  - `date`: Date of income (date)

- **Expense**:
  - `id`: Auto-incremented ID (Primary Key)
  - `name`: Name of expense (string)
  - `amount`: Amount spent (float)
  - `category`: Category of expense (string)
  - `date`: Date of expense (date)

## Contributing

Feel free to fork this repository, submit pull requests, or raise issues if you find bugs or have suggestions for improvements.

## License

This project is open-source and available under the [Apache License 2.0](LICENSE).
```