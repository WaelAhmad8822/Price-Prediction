# PythonAnywhere Deployment Guide

## Prerequisites
- PythonAnywhere account (free or paid)
- Your model file: `best_model_pipeline_*.pkl`

## Step-by-Step Deployment

### 1. Upload Files to PythonAnywhere

1. Go to [www.pythonanywhere.com](https://www.pythonanywhere.com)
2. Login to your account
3. Click on "Files" in the top menu
4. Navigate to your home directory `/home/yourusername/`
5. Create a new folder: `house-price-model`
6. Upload the following files:
   - `app.py`
   - `requirements.txt`
   - `best_model_pipeline_*.pkl`
   - `config.py`

### 2. Create Virtual Environment

1. Open "Bash console" from the Consoles section
2. Run these commands:

```bash
cd ~/house-price-model
mkvirtualenv --python=/usr/bin/python3.10 myenv
pip install -r requirements.txt
```

### 3. Create WSGI Configuration

1. Go to "Web" tab
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Select "Python 3.10"
5. Edit the WSGI file (usually at `/var/www/yourusername_pythonanywhere_com_wsgi.py`):

Replace the content with:
```python
import sys
import os

# Add project directory to path
path = os.path.expanduser('~/house-price-model')
if path not in sys.path:
    sys.path.insert(0, path)

# Load environment variables from config
os.environ['WERKZEUG_RUN_MAIN'] = 'true'

# Import and run the Flask app
from app import app as application
```

### 4. Configure Web App Settings

1. **Virtualenv path:** `/home/yourusername/.virtualenvs/myenv`
2. **WSGI configuration file:** `/var/www/yourusername_pythonanywhere_com_wsgi.py`
3. **Source code:** `/home/yourusername/house-price-model`

### 5. Set Working Directory

In the WSGI file, add before importing app:
```python
import os
os.chdir(os.path.expanduser('~/house-price-model'))
```

### 6. Reload Web App

1. Go to "Web" tab
2. Click the green "Reload" button
3. Your app is now live at: `https://yourusername.pythonanywhere.com`

## Testing Your API

### Test Health Endpoint
```bash
curl https://yourusername.pythonanywhere.com/health
```

### Test Prediction
```bash
curl -X POST https://yourusername.pythonanywhere.com/predict \
  -H "Content-Type: application/json" \
  -d '{
    "bedrooms": 3,
    "bathrooms": 2,
    "sqft_living": 2000,
    "sqft_lot": 5000,
    "floors": 1,
    "condition": 3,
    "grade": 8,
    "sqft_above": 2000,
    "sqft_basement": 0,
    "yr_built": 2000,
    "zipcode": 98101,
    "lat": 47.6,
    "long": -122.3,
    "sqft_living15": 1900,
    "sqft_lot15": 5000
  }'
```

## Important Notes

- **Model File Size:** Ensure your model file is not too large (PythonAnywhere has file upload limits)
- **Free Account Limitations:**
  - Limited disk space
  - Slower execution
  - Limited traffic
  - Auto-reload after 100 days of inactivity
- **Paid Account Benefits:**
  - More disk space
  - Better performance
  - 24/7 uptime
  - Custom domain support

## Troubleshooting

### Import Error in Web App
1. Check Virtualenv path is correct
2. Verify all packages installed: `/home/yourusername/.virtualenvs/myenv/bin/pip list`
3. Check error log: Go to "Web" → "Error log"

### Model File Not Found
1. Verify model file is in `/home/yourusername/house-price-model/`
2. Check file name matches in app.py
3. Use absolute path in app.py if needed:
```python
model_path = os.path.join(os.path.dirname(__file__), 'best_model_pipeline_*.pkl')
```

### 502 Bad Gateway
1. Check error logs
2. Reload the web app
3. Verify WSGI configuration
4. Increase timeout if model is large

## Environment-Specific Configuration

Create `config.py`:
```python
import os

class Config:
    DEBUG = False
    TESTING = False
    JSON_SORT_KEYS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
```

## Monitoring & Logs

Access logs from:
- **Web tab** → "Error log"
- **Web tab** → "Server log"
- Use tail command in Bash console:
```bash
tail -f /var/log/yourusername.pythonanywhere.com.error.log
```

## Updating Your Model

1. Upload new model file via Files
2. Reload web app from Web tab
3. Test with curl command above

## Support
- PythonAnywhere Help: https://help.pythonanywhere.com/
- Flask Documentation: https://flask.palletsprojects.com/
