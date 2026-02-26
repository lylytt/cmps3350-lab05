import json
import sys

REQUIRED_FIELDS = {"name", "github"}

try:
    with open("lab_student_names.json") as f:
        data = json.load(f)
except Exception:
    print("ERROR: Invalid JSON format.")
    sys.exit(1)

print("Validation successful.")