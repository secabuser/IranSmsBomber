# Sms Bobmer 🇮🇷

![Screenshot of Tool](tool_screenshot.png)

---

## Features
- Multi-threaded for high performance.
- Customizable rounds and delays.
- Displays detailed results including elapsed time and success rate.

---

## Requirements
- Python 3.x or later.
- Required libraries:
  - `requests`
  - `user_agent`
  - `colorama`
  - `pystyle`

Install dependencies using:
```bash
pip install -r requirements.txt
```

## How to Use

### Linux
#### Step 1: Install Prerequisites
1. Verify Python 3.x is installed:
   ```bash
   python3 --version
   ```
2. If Python isn’t installed, use the following commands to install:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```
3. Install necessary libraries:
   ```bash
   pip3 install requests user_agent colorama pystyle
   ```

#### Step 2: Run the Script
Execute the script with Python:
```bash
python3 main.py
```

#### Step 3: Follow the Prompts
The script will ask for:
1. Target phone number.
2. Number of rounds to execute.
3. Number of threads to use.
4. Delay between rounds in seconds.

#### Step 4: View Results
After execution, results including success rates and elapsed time will be displayed in a clean, formatted table.

---

### Windows
#### Step 1: Install Python
1. Download Python from [https://www.python.org/](https://www.python.org/) and install it.
2. During installation, ensure **Add Python to PATH** is selected.
3. Verify installation by opening `cmd` and typing:
   ```cmd
   python --version
   ```

#### Step 2: Install Required Libraries
1. Open Command Prompt (`cmd`).
2. Install libraries:
   ```cmd
   pip install requests user_agent colorama pystyle
   ```

#### Step 3: Run the Script
Execute the script:
```cmd
python main.py
```

#### Step 4: Follow the Prompts
Provide:
1. Target phone number.
2. Number of rounds to execute.
3. Number of threads to use.
4. Delay between rounds in seconds.

#### Step 5: View Results
The script displays results on-screen after execution.

---

### Additional Notes
1. **Customization**:
   - Add more services by updating the `SERVICES` dictionary in `api.py`.
2. **Error Handling**:
   - Logs errors and skips failed API calls to ensure continuity.
3. **Compatibility**:
   - Compatible with Linux and Windows systems.
