@echo off
cd /d "E:\rsakhare\OneDrive - purdue.edu\_curricular\RS\research"
echo Running build_pages.py to regenerate all pages...
python build_pages.py
echo.
echo Checking Git status...
git status
echo.
set "COMMIT_MSG=%~1"
if "%COMMIT_MSG%"=="" set "COMMIT_MSG=Update phrasing to capital project prioritization and remove comma before and"

echo Staging and committing changes with message: "%COMMIT_MSG%"...
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
