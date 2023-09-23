import os
import sys
import subprocess

def create_venv():
    print("Creating virtual environment 'venv'...")
    if sys.platform == "darwin":  # MacOS
        subprocess.run(["python3", "-m", "venv", "venv"])
    else:  # Windows and others
        subprocess.run(["python", "-m", "venv", "venv"])
    print("Virtual environment created successfully!")

def install_dependencies():
    print("Installing required dependencies...")
    pip_command = "pip3" if sys.platform == "darwin" else "pip"
    
    # Return the command to install Gradio
    return f"{pip_command} install gradio==3.44.4"

def main():
    # Check if venv exists
    if not os.path.exists("venv"):
        create_venv()
    else:
        print("Virtual environment 'venv' already exists.")

    # Activate venv and install dependencies
    activate_venv = ".\\venv\\Scripts\\activate" if os.name == "nt" else "source venv/bin/activate"
    os.system(f"{activate_venv} && {install_dependencies()} && python launch.py")

if __name__ == "__main__":
    main()
