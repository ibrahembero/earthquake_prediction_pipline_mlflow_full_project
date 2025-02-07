# 1. Set the path to your virtual environment and script
$venv_path = "C:\bero\shAI\Qafza_Training\Content_Of_Course\week 7\pipeline_earthquake\venv\Scripts\Activate.ps1"
$script_path = "C:\bero\shAI\Qafza_Training\Content_Of_Course\week 7\pipeline_earthquake\pipeline_earth.py"

# 2. Activate the virtual environment
Write-Host "Activating virtual environment..."
. $venv_path  # This activates the virtual environment in PowerShell

# 3. Run the Python script
Write-Host "Running the Python script..."
python $script_path

Write-Host "Pipeline execution complete!"
