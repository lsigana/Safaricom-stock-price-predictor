"""
WSGI config for stock_predictor project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import sys
import os  # Missing import
from pathlib import Path
from django.core.wsgi import get_wsgi_application

project_path = '/home/lsigana/Safaricom-stock-price-predictor'

if project_path not in sys.path:
    sys.path.append(project_path)

# Set Django settings module BEFORE calling get_wsgi_application()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_predictor.settings')

application = get_wsgi_application()

