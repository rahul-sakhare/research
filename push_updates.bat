@echo off
cd /d "E:\rsakhare\OneDrive - purdue.edu\_curricular\RS\research"
echo Running build_pages.py to regenerate all pages with Google Analytics...
python build_pages.py
echo.
echo Checking Git status...
git status
echo.
echo Staging and committing changes...
git add .
git commit -m "Add Google Analytics 4 (G-JX6RBVBKF6) and update About page heading"
echo.
echo Pushing to GitHub...
git push origin main
echo.
echo ==============================================
echo Site build and deployment successfully completed!
echo ==============================================
pause
