@echo off
cd /d "E:\rsakhare\OneDrive - purdue.edu\_curricular\RS\research"
echo Running build_pages.py to regenerate all pages...
python build_pages.py
echo.
echo Checking Git status...
git status
echo.
set "COMMIT_MSG=%*"
if not defined COMMIT_MSG set "COMMIT_MSG=Update site content and regenerate pages"

echo Staging and committing changes...
git add .
git commit -m "%COMMIT_MSG%"
echo.
echo Pushing to GitHub...
git push origin main
echo.
echo ==============================================
echo Site build and deployment successfully completed!
echo ==============================================
pause
