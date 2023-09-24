# README: Using a Python Script in Windows

This guide will walk you through the steps to use a Python script on a Windows operating system. We will cover the following:

1. **Download and Install Python:** If you don't already have Python installed, we'll start by downloading and installing it.

2. **Create a Virtual Environment:** We'll create a virtual environment to isolate your Python project and its dependencies from the system-wide Python installation.

3. **Run the Python Script:** Finally, we'll execute your Python script within the virtual environment.

## Prerequisites

Before you begin, ensure that you have:

- An internet connection to download Python.
- Basic knowledge of using the Windows command prompt (CMD).

## 1. Download and Install Python

1.1. Open your web browser and navigate to the official Python website at [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/).

1.2. Scroll down to find the latest stable version of Python for Windows. Click on the "Download" button for the installer that matches your system architecture (usually 64-bit).

1.3. Run the downloaded installer:

   - Check the box that says "Add Python x.x to PATH" during installation. This will make it easier to run Python from the command prompt.
   - Click "Install Now" to start the installation process.

1.4. Once the installation is complete, you can verify it by opening a command prompt (CMD) and running the following command:

   ```
   python --version
   ```

   You should see the installed Python version displayed.

## 2. Create a Virtual Environment

2.1. Open a command prompt (CMD) by pressing `Win + R`, typing "cmd," and pressing Enter.

2.2. Navigate to the directory where you want to create your Python project. You can use the `cd` command to change directories. For example:

   ```
   cd C:\path\to\your\project\folder
   ```

2.3. Create a virtual environment by running the following command:

   ```
   python -m venv venv
   ```

   This will create a new directory named "venv" in your project folder, containing a separate Python environment.

2.4. Activate the virtual environment by running the activation script. The script's location may vary depending on your Windows version, but it's typically located in the "Scripts" directory within your virtual environment. Run one of the following commands:

   - For Windows Command Prompt:

     ```
     venv\Scripts\activate
     ```

   - For Windows PowerShell:

     ```
     .\venv\Scripts\Activate.ps1
     ```

   - For Windows Git Bash:

     ```
     source venv/Scripts/activate
     ```

   When activated, you'll notice that your command prompt displays the virtual environment's name in parentheses, like this: `(venv)`.

### 3 Install Dependencies

3.1 Inside the virtual environment install the dependencies stored in requirements.txt

   ```
   pip install -r requirements.txt
   ```

## 4. Run the Python Script

4.1. With the virtual environment activated, you can now run your Python script using the `python` command followed by the script's filename. For example:

   ```
   python main.py
   ```


4.2. Your script will execute within the virtual environment, ensuring that it uses the Python version and dependencies specific to your project.


Congratulations! You've successfully downloaded and installed Python, created a virtual environment, and executed a Python script on a Windows system. You can now work on your Python projects with a clean and isolated environment.