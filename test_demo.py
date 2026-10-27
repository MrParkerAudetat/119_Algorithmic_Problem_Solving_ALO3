"""Regression checks for the ticket application."""

from main import (
    build_registry,
    list_scan,
    indexed_lookup,
    update_priority,
    filter_by_category,
    repair_queue,
    cancel_ticket,
)
from ticket_data import TICKETS


def self_check():
    registry = build_registry(TICKETS)

    # Lookup tests
    assert list_scan(TICKETS, "T301") == TICKETS[0]
    assert indexed_lookup(registry, "T301") == registry["T301"]

    assert list_scan(TICKETS, "T999") is None
    assert indexed_lookup(registry, "T999") is None

    # Empty registry
    assert build_registry([]) == {}

    # Independent copies
    registry["T301"]["priority"] = "high"
    assert TICKETS[0]["priority"] == "normal"

    # Priority update
    updated = update_priority(registry, "T304", "high")
    assert updated["priority"] == "high"

    # Missing update
    assert update_priority(registry, "T999", "high") is None

    # Category filtering
    account = filter_by_category(registry, "account")
    assert len(account) == 2

    classroom = filter_by_category(registry, "classroom")
    assert classroom == []

    assert filter_by_category(registry, "parking") is None

    # Queue repair
    repaired, removed = repair_queue(
        registry,
        ["T301", "T999", "T302", "T998"]
    )

    assert repaired == ["T301", "T302"]
    assert removed == ["T999", "T998"]

    # Cancel ticket
    pending = ["T301", "T302"]
    history = []

    assert cancel_ticket(
        registry,
        pending,
        history,
        "T301"
    )

    assert pending == ["T302"]

    # Reject completed ticket
    assert not cancel_ticket(
        registry,
        pending,
        history,
        "T306"
    )

    # Duplicate IDs rejected
    duplicate_tickets = TICKETS.copy()
    duplicate_tickets.append(TICKETS[0].copy())

    try:
        build_registry(duplicate_tickets)
    except ValueError:
        pass
    else:
        raise AssertionError("Duplicate IDs must be rejected")


if __name__ == "__main__":
    self_check()
    print("Checks passed.")
