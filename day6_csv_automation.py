import os
import csv
import datetime

# Tell Python where to look for files — ALWAYS FIRST
os.chdir(r"C:\Users\Lenovo\Desktop\AI+Automation\Py_files")

# --- SECTION 3: KPI Analyzer ---
pending_count = 0
completed_count = 0
high_risk_count = 0
pending_suppliers = []
high_risk_suppliers = []

with open("suppliers.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        status = row["status"]
        name = row["name"]
        if status == "Pending":
            pending_count += 1
            pending_suppliers.append(name)
        elif status == "Completed":
            completed_count += 1
        elif status == "High-Risk":
            high_risk_count += 1
            high_risk_suppliers.append(name)

print("=== SUPPLIER KPI SUMMARY ===")
print(f"Completed  : {completed_count}")
print(f"Pending    : {pending_count} → {pending_suppliers}")
print(f"High-Risk  : {high_risk_count} → {high_risk_suppliers}")

# --- SECTION 4: Report Generator ---
today = datetime.date.today()

with open("suppliers.csv", "r") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

total = len(rows)

with open("summary_report.txt", "w", encoding="utf-8") as report:
    report.write("SUPPLIER SUMMARY REPORT\n")
    report.write("========================\n")
    report.write(f"Engineer        : Your Name\n")
    report.write(f"Date            : {today}\n")
    report.write(f"Total Suppliers : {total}\n")
    report.write(f"Completed       : {completed_count}\n")
    report.write(f"Pending         : {pending_count} → {pending_suppliers}\n")
    report.write(f"High-Risk       : {high_risk_count} → {high_risk_suppliers}\n")
    report.write("------------------------\n")
    report.write("FULL SUPPLIER LIST:\n")
    for row in rows:
        report.write(f"  {row['name']} | {row['status']} | {row['project']}\n")

print("✅ summary_report.txt generated successfully")

    