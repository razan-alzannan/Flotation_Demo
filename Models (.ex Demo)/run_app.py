import sys
import subprocess
from pathlib import Path

# Absolute path to your Streamlit app
app_path = Path(
    r"C:\Users\USER\Desktop\Projects\CPM\GUI\Models (.ex Demo)\main.py"
)

subprocess.run([
    sys.executable,
    "-m",
    "streamlit",
    "run",
    str(app_path)
])