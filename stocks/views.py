import os
from pathlib import Path
from django.conf import settings
from django.shortcuts import render
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
import numpy as np
import traceback

def plot_to_base64(fig):
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0.1)
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode()
    buffer.close()
    return image_base64


def stock_data_view(request):
    try:
        # Use Path to join paths
        csv_path = settings.BASE_DIR / 'stocks' / 'SCOM_data.csv'
        print(f"Attempting to read CSV from: {csv_path}")  # Debug prin
        # Read the CSV file
        data = pd.read_csv(csv_path, index_col='Date', parse_dates=True)
        
        # Prepare the data
        data['100_MA'] = data['Close'].rolling(window=100).mean()
        data['200_MA'] = data['Close'].rolling(window=200).mean()

        # Calculate statistics
        stats = data[['High', 'Low', 'Open', 'Close', 'Volume']].agg([
            'mean', 
            'std', 
            'min', 
            lambda x: x.median(), 
            'max'
        ])
        stats.index = ['Mean', 'Std Dev', 'Min', 'Median', 'Max']

        # Create plots
        plt.switch_backend('Agg') 
        fig, axs = plt.subplots(4, 1, figsize=(10, 20))

        # 1. Statistics Table
        axs[0].axis('off')
        axs[0].table(cellText=stats.values, rowLabels=stats.index, colLabels=stats.columns, loc='center')
        axs[0].set_title('Statistics Table')

        # 2. Closing Price vs Time
        axs[1].plot(data.index, data['Close'], label='Closing Price')
        axs[1].set_title('Closing Price vs Time')
        axs[1].set_xlabel('Date')
        axs[1].set_ylabel('Price')
        axs[1].legend()

        # 3. Closing Price with 100-day Moving Average
        axs[2].plot(data.index, data['Close'], label='Closing Price')
        axs[2].plot(data.index, data['100_MA'], label='100-Day MA', color='orange')
        axs[2].set_title('Closing Price vs Time with 100-Day Moving Average')
        axs[2].set_xlabel('Date')
        axs[2].set_ylabel('Price')
        axs[2].legend()

        # 4. Closing Price with 200-day Moving Average
        axs[3].plot(data.index, data['Close'], label='Closing Price')
        axs[3].plot(data.index, data['200_MA'], label='200-Day MA', color='green')
        axs[3].set_title('Closing Price vs Time with 200-Day Moving Average')
        axs[3].set_xlabel('Date')
        axs[3].set_ylabel('Price')
        axs[3].legend()

        # Adjust layout and convert plot to base64
        plt.tight_layout()
        plots = plot_to_base64(fig)
        plt.close(fig)

        return render(request, 'stocks/stock_data.html', {'plots': plots})
    
    except FileNotFoundError:
        error_msg = f'Data file not found. Looking for file at: {csv_path}'
        return render(request, 'stocks/stock_data.html', {'error': error_msg})
    
    except Exception as e:
        print(f"Error generating plots: {e}")
        traceback.print_exc()
        error_msg = f"An error occurred: {str(e)}"
        return render(request, 'stocks/stock_data.html', {'error': error_msg})
    
def about_view(request):
    return render(request, 'stocks/about.html')

def contact_view(request):
    return render(request, 'stocks/contact.html')    