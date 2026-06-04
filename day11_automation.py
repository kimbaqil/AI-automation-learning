from pathlib import Path
from datetime import date

base      = Path(r"C:\Users\Lenovo\Desktop\AI+Automation\Py_files")
out_dir   = base / "outputs"
out_dir.mkdir(exist_ok=True)

today     = date.today().strftime("%Y-%m-%d")
filename  = f"supplier_report_{today}.xlsx"
out_path  = out_dir / filename

print("Saving to:", out_path)