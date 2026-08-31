import os


# -------------------------------
# Clear Console Screen
# -------------------------------

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# -------------------------------
# Pause Program
# -------------------------------

def pause():
    input("\nPress Enter to continue...")


# -------------------------------
# Print Heading
# -------------------------------

def print_heading(title):
    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)


# -------------------------------
# Generate Next ID
# -------------------------------

def generate_id(records, prefix):

    if not records:
        return f"{prefix}001"

    numbers = []

    for record in records:

        id_key = None

        for key in record:
            if key.endswith("_id"):
                id_key = key
                break

        if id_key is None:
            continue

        current_id = record.get(id_key, "").strip()

        if not current_id:
            continue

        if not current_id.startswith(prefix):
            continue

        number_part = current_id[len(prefix):]

        if not number_part.isdigit():
            continue

        numbers.append(int(number_part))

    if not numbers:
        return f"{prefix}001"

    next_number = max(numbers) + 1

    return f"{prefix}{next_number:03d}"


# -------------------------------
# Find Record By ID
# -------------------------------

def find_record(records, key, value):

    for record in records:
        if record[key] == value:
            return record

    return None


# -------------------------------
# Delete Record By ID
# -------------------------------

def delete_record(records, key, value):

    for record in records:

        if record[key] == value:

            records.remove(record)

            return True

    return False


# -------------------------------
# Display Records
# -------------------------------

def display_records(records):

    if not records:

        print("\nNo Records Found.")

        return

    for i, record in enumerate(records, start=1):

        print(f"\nRecord {i}")
        print("-" * 40)

        for key, value in record.items():

            print(f"{key:<20}: {value}")

        print("-" * 40)