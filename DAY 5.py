suppliers = [
    {"name": "Bosch", "status": "Completed"},
    {"name": "Valeo", "status": "Pending"}
]

file = open("supplier_report.txt", "w")

file.write("SUPPLIER REPORT\n")
file.write("-------------------\n")

for supplier in suppliers:
    line = supplier["name"] + " - " + supplier["status"] + "\n"
    file.write(line)

file.close()

print("Report generated successfully")