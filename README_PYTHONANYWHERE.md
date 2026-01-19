# House Price Prediction Model - PythonAnywhere Ready

This project is ready for deployment on PythonAnywhere!

## Quick Deploy Checklist

- [ ] Upload files to PythonAnywhere
- [ ] Create virtual environment
- [ ] Configure WSGI file
- [ ] Set web app settings
- [ ] Reload and test

## Files Included

| File | Purpose |
|------|---------|
| `app.py` | Flask application |
| `requirements.txt` | Python dependencies |
| `config.py` | Configuration settings |
| `pythonanywhere_wsgi.py` | WSGI entry point |
| `setup_pythonanywhere.sh` | Automated setup script |
| `PYTHONANYWHERE_DEPLOYMENT.md` | Detailed deployment guide |
| `best_model_pipeline_*.pkl` | Trained ML model |

## Quick Start (3 Steps)

### Step 1: Upload Files
1. Go to PythonAnywhere Files
2. Create folder: `house-price-model`
3. Upload all files above

### Step 2: Setup Virtual Environment
In PythonAnywhere Bash console:
```bash
cd ~/house-price-model
chmod +x setup_pythonanywhere.sh
bash setup_pythonanywhere.sh
```

Or manually:
```bash
cd ~/house-price-model
mkvirtualenv --python=/usr/bin/python3.10 myenv
pip install -r requirements.txt
```

### Step 3: Configure Web App
1. **Web tab** → Add new web app
2. Select **Python 3.10 (Manual configuration)**
3. Set:
   - **Virtualenv:** `/home/yourusername/.virtualenvs/myenv`
   - **Source code:** `/home/yourusername/house-price-model`
   - **WSGI file:** Copy content from `pythonanywhere_wsgi.py`
4. Click **Reload**

## API Endpoints

### Health Check
```bash
GET https://yourusername.pythonanywhere.com/health
```

### Get Model Info
```bash
GET https://yourusername.pythonanywhere.com/model-info
```

### Make Prediction
```bash
POST https://yourusername.pythonanywhere.com/predict
Content-Type: application/json

{
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
}
```

## Troubleshooting

### Issue: ImportError with Flask
**Solution:** Check virtualenv path in Web settings matches your setup

### Issue: Model file not found
**Solution:** Verify model file is in `/home/yourusername/house-price-model/`

### Issue: 502 Bad Gateway
**Solution:** Check error log in Web tab → Error log

### Issue: Slow predictions
**Solution:** Upgrade to PythonAnywhere paid account for better CPU

## Updating Model

To deploy a new trained model:
1. Upload new `.pkl` file via Files
2. Go to Web tab → Reload
3. Test with prediction endpoint

## Need Help?

- **PythonAnywhere Docs:** https://help.pythonanywhere.com/
- **Flask Docs:** https://flask.palletsprojects.com/
- **Full Guide:** See `PYTHONANYWHERE_DEPLOYMENT.md`

---

**Deployed Model Location:** Your app URL will be `https://yourusername.pythonanywhere.com`
