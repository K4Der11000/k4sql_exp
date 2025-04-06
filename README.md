# SQLi Scanner WebApp by kader11000

A professional SQL Injection vulnerability scanner using `sqlmap` integrated into a modern web interface.

## Features

- Supports multiple URL scanning.
- Supports POST, PUT, HEAD, and OPTIONS methods.
- Advanced SQLMap options support.
- Live scan progress with percent indication.
- Colored and structured scan results.
- Auto-generation of HTML reports.
- Login-protected interface with password.
- Logout and session lockout on brute-force.
- Downloads sqlmap only once on first run.

## Default Login

- **Password**: `kader11000`

---

## How to Run

1. **Install Python 3** (if not already installed)

2. **Save the script** to a file named:
   ```bash
   app.py
   ```

3. **Run the script**:
   ```bash
   python app.py
   ```

   On first run, it will automatically:
   - Install Flask and Requests.
   - Clone sqlmap from GitHub.

4. **Open your browser** and go to:
   ```
   http://127.0.0.1:5000
   ```

5. **Login** using the password: `kader11000`

6. **Use the scanner**:
   - Paste multiple URLs (each on a new line).
   - Optionally provide advanced sqlmap options like: `--risk=3 --level=5`.
   - View colored scan results and download HTML reports.

---

## Notes

- Reports are saved under `outputs/` with auto-organized folders.
- To change the password, modify this line in the script:
  ```python
  if request.form["password"] == "kader11000":
  ```
