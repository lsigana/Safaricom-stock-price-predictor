# Safaricom Stock Price Analyzer

## Overview
A Django-based web application that analyzes and visualizes Safaricom (SCOM) stock price data. The application provides interactive visualizations, statistical analysis, and moving average calculations to help users understand stock price trends.

## Features
- Historical stock price visualization
- Statistical analysis dashboard
- 100-day and 200-day moving averages
- Interactive dark/light mode toggle
- Responsive design for all devices
- Data visualization using Matplotlib

## Tech Stack
- **Backend:** Python, Django
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib
- **Frontend:** HTML, CSS, JavaScript
- **Data:** CSV-based storage

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/stock-predictor.git
cd stock-predictor
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django pandas numpy matplotlib
```

4. Apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run the development server:
```bash
python manage.py runserver
```

6. Visit `http://127.0.0.1:8000/` in your browser

## Project Structure
```
stock_predictor/
├── stocks/
│   ├── static/
│   │   └── stocks/
│   │       ├── style.css
│   │       └── js/
│   │           └── main.js
│   ├── templates/
│   │   └── stocks/
│   │       ├── base.html
│   │       ├── stock_data.html
│   │       ├── about.html
│   │       └── contact.html
│   ├── views.py
│   ├── urls.py
│   └── models.py
└── manage.py
```

## Usage
1. Upload your SCOM_data.csv file to the stocks/ directory
2. The CSV should contain columns: Date, Close, High, Low, Open, Volume
3. Access different visualizations through the navigation menu
4. Toggle between dark and light modes using the theme button

## Data Format
The application expects a CSV file with the following columns:
- Date: YYYY-MM-DD format
- Close: Closing price
- High: Day's highest price
- Low: Day's lowest price
- Open: Opening price
- Volume: Trading volume

## Features in Detail
1. **Statistical Analysis**
   - Mean, median, standard deviation
   - Min and max values
   - Volume analysis

2. **Technical Analysis**
   - 100-day moving average
   - 200-day moving average
   - Price trend visualization

3. **User Interface**
   - Responsive design
   - Dark/light mode
   - Interactive graphs

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
Leah Sigana

## Acknowledgments
- Data provided by Safaricom PLC
- Built as part of a data analysis project