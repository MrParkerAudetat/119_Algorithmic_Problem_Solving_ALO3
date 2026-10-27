"""Match ticket representations to lookup, update, and membership tasks."""
from ticket_data import TICKETS, SUPPORTED_CATEGORIES

def build_registry(records):
    registry = {}

    for ticket in records:
        ticket_id = ticket["id"]

        if ticket_id in registry:
            raise ValueError(f"Duplicate ticket ID: {ticket_id}")

        registry[ticket_id] = ticket.copy()

    return registry
    
def list_scan(records, ticket_id):
    """Find one ticket record in a list and report how many records were inspected."""
    inspected = 0
    for record in records:
        inspected += 1
        if record["id"] == ticket_id:
            return record, inspected
    return None, inspected

def indexed_lookup(records, ticket_id):
    """Find one ticket record in a list using an indexed approach and report how many records were inspected."""
    inspected = 0
    for record in records:
        inspected += 1
        if record["id"] == ticket_id:
            return record, inspected
    return None, inspected        

def update_priority(registry, ticket_id, new_priority):
    """Update the priority of a ticket in the registry and the original records list."""
    if ticket_id not in registry:
        return None
    registry[ticket_id]["priority"] = new_priority;
    return registry[ticket_id];

def filter_by_category(registry, category):
    "Return a list of tickets in the registry that match the given category."
    if category not in SUPPORTED_CATEGORIES:
        return None
    matching_tickets = []
    for ticket_id, ticket in registry.items():
        if ticket.get("category") == category:
            matching_tickets.append(ticket)
    return matching_tickets

from console_style import print_color


def build_index(records):
    """Index independent flat record copies, rejecting duplicate ticket IDs."""
    index = {}
    for record in records:
        ticket_id = record["id"]
        if ticket_id in index:
            raise ValueError(f"duplicate ID: {ticket_id}")
        copied_record = record.copy()
        index[ticket_id] = copied_record
    return index


def scan_lookup(records, ticket_id):
    """Find one ticket record and report how many records were inspected."""
    inspected = 0
    for record in records:
        inspected += 1
        if record["id"] == ticket_id:
            return record, inspected
    return None, inspected


def fixture():
    """Provide a small ticket inventory with a repeated ticket type."""
    return [
        {"id": "E01", "type": "laptop", "available": True},
        {"id": "E02", "type": "tablet", "available": True},
        {"id": "E03", "type": "laptop", "available": False},
    ]


def available_ids(index):
    """Collect the IDs of ticket currently available in the index."""
    # Original compact selection, kept as an optional reading comparison:
    # [key for key, row in index.items() if row["available"]]
    # items() supplies an ID and its record together. The loop below retrieves
    # that same record explicitly, checks availability, and collects the same ID.
    available = []
    for ticket_id in index:
        record = index[ticket_id]
        if record["available"]:
            available.append(ticket_id)
    return available


def display_record(record):
    """Present an ticket result without exposing dictionary notation."""
    if record is None:
        print_color("  No ticket found for that ID.", "caution")
        return
    if record["available"]:
        status = "Ready to borrow"
    else:
        status = "On loan"
    print(f"  {record['id']} - {record['type'].title()} - {status}")


def main():
    """Compare finding ticket, tracking unique types, and filtering availability."""
    rows = fixture()
    index = build_index(rows)
    # A set keeps each ticket type once, even when several records share it.
    types = {row["type"] for row in rows}

    print_color("ticket LOAN DESK", "heading")
    print("Find ticket E03")
    found_record, inspected = scan_lookup(rows, "E03")
    print("List search:")
    display_record(found_record)
    print(f"  Records checked: {inspected}")
    print("ID index:")
    if "E03" in index:
        display_record(index["E03"])
    else:
        display_record(None)

    print_color("\nticket types we carry", "heading")
    for ticket_type in sorted(types):
        print(f"  {ticket_type.title()}")
    if "camera" in types:
        print("Camera requests: this type is in our inventory.")
    else:
        print("Camera requests: we do not carry this type.")

    index["E01"]["available"] = False
    print_color("\nAfter checking out E01 in the working index", "heading")
    print("Working record:")
    display_record(index["E01"])
    print("Original record, kept separately:")
    display_record(rows[0])
    print("  This index uses flat copies; Week 2's index shared its records.")

    print_color("\nReady to borrow now", "heading")
    ready_ids = available_ids(index)
    if not ready_ids:
        print("  No ticket is ready to borrow.")
    for ticket_id in ready_ids:
        display_record(index[ticket_id])

    duplicate_rows = rows.copy()
    duplicate_record = rows[0].copy()
    duplicate_rows.append(duplicate_record)
    try:
        build_index(duplicate_rows)
    except ValueError:
        print_color("\nNew record not added: ticket ID E01 is already in use.", "caution")


if __name__ == "__main__":
    main()
