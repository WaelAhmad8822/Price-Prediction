@echo off
cd /d "f:\graduation Project"

REM Configure git user
git config --global user.name "Graduation Project"
git config --global user.email "project@example.com"

REM Initialize git repository
git init

REM Add all files
git add .

REM Create initial commit
git commit -m "Initial commit: House Price Prediction Model - Ready for PythonAnywhere deployment"

REM Display repository status
echo.
echo ===== Git Repository Initialized =====
echo.
git log --oneline
echo.
echo Files in repository:
git ls-files
echo.
echo ===== Next Steps =====
echo 1. Create a new repository on GitHub
echo 2. Run these commands to add the remote:
echo.
echo    git remote add origin https://github.com/yourusername/house-price-model.git
echo    git branch -M main
echo    git push -u origin main
echo.
pause
