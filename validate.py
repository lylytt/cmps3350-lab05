import json
import sys

REQUIRED_FIELDS = {"name", "github"}

try:
    with open("lab_student_names.json") as f:
        data = json.load(f)
except Exception:
    print("ERROR: Invalid JSON format.")
    sys.exit(1)

if "students" not in data or not isinstance(data["students"], list):
    print("ERROR: Missing or invalid 'students' list.")
    sys.exit(1)

for i, entry in enumerate(data["students"], start=1):
    if not isinstance(entry, dict):
        print(f"ERROR in Entry {i}: Entry must be an object.")
        sys.exit(1)

    entry_fields = set(entry.keys())

    missing_fields = REQUIRED_FIELDS - entry_fields
    if missing_fields:
        print(f"ERROR in Entry {i}: Missing field(s): {', '.join(sorted(missing_fields))}")
        sys.exit(1)

    unexpected_fields = entry_fields - REQUIRED_FIELDS
    if unexpected_fields:
        print(f"ERROR in Entry {i}: Unexpected field(s): {', '.join(sorted(unexpected_fields))}")
        sys.exit(1)

    for field in REQUIRED_FIELDS:
        if not isinstance(entry[field], str) or entry[field].strip() == "":
            print(f"ERROR in Entry {i}: Field '{field}' must be a non-empty string.")
            sys.exit(1)

print("Validation successful.")
