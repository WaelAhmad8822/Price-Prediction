#!/bin/bash
# Quick setup script for PythonAnywhere deployment
# Run this in PythonAnywhere Bash console

echo "=== House Price Model - PythonAnywhere Setup ==="
echo ""

# Get username
read -p "Enter your PythonAnywhere username: " USERNAME

# Create project directory
echo "Creating project directory..."
mkdir -p ~/house-price-model
cd ~/house-price-model

# Create virtual environment
echo "Creating virtual environment..."
mkvirtualenv --python=/usr/bin/python3.10 myenv

# Activate virtual environment
source ~/.virtualenvs/myenv/bin/activate

# Install requirements
echo "Installing Python packages..."
pip install -r requirements.txt

echo ""
echo "=== Setup Complete! ==="
echo ""
echo "Next steps:"
echo "1. Go to Web tab on PythonAnywhere"
echo "2. Add a new web app with Python 3.10 (Manual configuration)"
echo "3. Set virtualenv to: /home/$USERNAME/.virtualenvs/myenv"
echo "4. Copy WSGI file content to: /var/www/${USERNAME}_pythonanywhere_com_wsgi.py"
echo "5. Set source code to: /home/$USERNAME/house-price-model"
echo "6. Click 'Reload' button"
echo ""
echo "Your app will be live at: https://$USERNAME.pythonanywhere.com"
