# SQLi Scanner Web App by kader11000

A professional web interface for scanning and exploiting SQLi vulnerabilities using sqlmap.

## Requirements

- Python 3.x
- Flask
- requests
- sqlmap (must be installed and available in PATH)

## Installation & Usage

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Make sure sqlmap is working:
```
sqlmap --version
```

3. Run the app:
```
python app.py
```

Or using the script:
```
chmod +x start.sh
./start.sh
```

4. Open your browser at:
```
http://localhost:5000
```

## Login Info

- Password: `kader11000`

## Features

- Multi-URL scanning
- Advanced sqlmap options
- Export HTML reports
- Start/Stop buttons
- Colorful and structured UI
- Logout button
- Brute-force protection