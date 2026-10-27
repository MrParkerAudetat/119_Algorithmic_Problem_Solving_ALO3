"""Demonstrate ticket lookup, updates, filtering, queue repair, and cancellation."""

from ticket_data import TICKETS
from main import (
    build_registry,
    list_scan,
    indexed_lookup,
    update_priority,
    filter_by_category,
    repair_queue,
    cancel_ticket,
)


def main():
    registry = build_registry(TICKETS)

    print("HELP DESK TICKETS")
    print()

    # Lookup examples
    print("List scan lookup for T301:")
    print(list_scan(TICKETS, "T301"))
    print()

    print("Indexed lookup for T301:")
    print(indexed_lookup(registry, "T301"))
    print()

    print("Missing lookup:")
    print(indexed_lookup(registry, "T999"))
    print()

    # Priority update
    print("Updating T301 priority to high:")
    update_priority(registry, "T301", "high")
    print(registry["T301"])
    print()

    print("Original record is unchanged:")
    print(TICKETS[0])
    print()

    # Category filtering
    print("Account tickets:")
    account_tickets = filter_by_category(registry, "account")
    print(account_tickets)
    print()

    print("Classroom tickets:")
    print(filter_by_category(registry, "classroom"))
    print()

    print("Parking tickets:")
    print(filter_by_category(registry, "parking"))
    print()

    # Tuesday queue repair
    pending = ["T301", "T999", "T302", "T998"]

    repaired, removed = repair_queue(registry, pending)

    print("Original queue:")
    print(pending)

    print("Repaired queue:")
    print(repaired)

    print("Removed IDs:")
    print(removed)
    print()

    # Install repaired queue into state
    state = {
        "registry": registry,
        "pending": pending,
    }

    repaired, removed = repair_queue(
        state["registry"],
        state["pending"]
    )

    state["pending"] = repaired

    print("Live pending queue:")
    print(state["pending"])
    print()

    # Cancellation
    history = []

    print("Cancel pending ticket T301:")
    cancel_ticket(
        registry,
        state["pending"],
        history,
        "T301"
    )

    print("Pending:")
    print(state["pending"])
    print("History:")
    print(history)
    print()

    print("Cancel open ticket not in pending (T304):")
    cancel_ticket(
        registry,
        state["pending"],
        history,
        "T304"
    )

    print("History:")
    print(history)
    print()

    print("Attempt to cancel completed ticket T306:")
    success = cancel_ticket(
        registry,
        state["pending"],
        history,
        "T306"
    )

    print(success)
    print()

    # Historical copy demonstration
    fresh_registry = build_registry(TICKETS)

    saved_report = filter_by_category(
        fresh_registry,
        "account"
    )

    update_priority(
        fresh_registry,
        "T301",
        "high"
    )

    cancel_ticket(
        fresh_registry,
        [],
        [],
        "T304"
    )

    print("Saved report:")
    print(saved_report)
    print()

    print("Live registry:")
    print(fresh_registry["T301"])
    print(fresh_registry["T304"])


if __name__ == "__main__":
    main()
