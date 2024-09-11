#!/bin/bash

# =======================
# Titanoboa Framework Installation Script
# =======================

echo "Installing Titanoboa Framework..."

# Check if Python3 is installed
if ! command -v python3 &>/dev/null; then
    echo "Python3 not found. Installing Python3..."
    sudo apt update
    sudo apt install python3 python3-pip -y
else
    echo "Python3 is already installed."
fi

# Install the required Python packages
echo "Installing required Python packages..."
pip3 install fastapi uvicorn cryptography sympy sqlite3 aiohttp

# Create Titanoboa directory in /usr/local if it doesn't exist
if [ ! -d "/usr/local/titanoboa" ]; then
    sudo mkdir /usr/local/titanoboa
fi

# Copy the titanoboa script to the installation directory
sudo cp main.py /usr/local/titanoboa/titanoboa.py

# Create symbolic link to titanoboa command in /usr/local/bin
sudo ln -sf /usr/local/titanoboa/titanoboa.py /usr/local/bin/titanoboa

# Set executable permissions for the titanoboa script and symlink
sudo chmod +x /usr/local/titanoboa/titanoboa.py
sudo chmod +x /usr/local/bin/titanoboa

echo "Titanoboa installation complete!"
echo "You can now run 'titanoboa init <project_name>' to initialize a new project."

