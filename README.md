# spotify-music-installer
install your playlist music

# Setup and Run Python Script

## 1. Install Python

Download and install Python from the [official Python website](https://www.python.org/downloads/). Ensure that you check the box to "Add Python to PATH" during the installation process.

## 2. Create a Virtual Environment

Open PowerShell or Command Prompt and navigate to your project directory:

```powershell
cd E:\spotifymusicinstaller
```
# Create a virtual environment:

```
python -m venv venv
```
# Open PowerShell in Administrator Mode

Search for PowerShell in the Start menu.

Right-click on Windows PowerShell and select "Run as administrator."

# Activate the PowerShell Script

In the Administrator PowerShell, set the execution policy to allow running scripts:
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
# Activate the virtual environment:

```
.\venv\Scripts\Activate.ps1
```
# Configure Spotify Client

Make sure to provide your Spotify client_id and client_secret in the main.py file where indicated in main.py.

```
# Replace these with your actual Spotify credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'
```

# Run the main.py File
Run your Python script with:

```
python E:\spotifymusicinstaller\main.py
```




