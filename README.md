# AL03 - Find, Update, and Select

## Purpose

This project manages campus help desk tickets using lists, dictionaries, and sets.

## Functions

- build_registry()
- list_scan()
- indexed_lookup()
- update_priority()
- filter_by_category()
- repair_queue()
- cancel_ticket()

## Data Structures

### List
Stores ticket records and pending ticket IDs.

### Dictionary
Stores tickets by ID for quick lookup and updates.

### Set
Stores supported ticket categories.

## Comparison

### Lookup
A dictionary registry is best because tickets can be found directly by ID.

### Update
A dictionary registry is best because a ticket can be found and updated by ID.

### Filter
Filtering requires checking tickets to find matching categories.

## Tuesday Features

### Queue Repair

The program repairs a pending queue by removing ticket IDs that do not exist in the registry.

Example:

```text
Original:
[T301, T999, T302, T998]

Repaired:
[T301, T302]

Removed:
[T999, T998]
```

### Ticket Cancellation

The program can:

- Cancel an open pending ticket
- Cancel an open ticket that is not pending
- Reject cancellation of missing tickets
- Reject cancellation of completed tickets

Pending ticket order is preserved.

## Testing

The tests verify:

- Found lookup
- Missing lookup
- Empty input
- Duplicate IDs
- Priority updates
- Category filtering
- Queue repair
- Ticket cancellation
- Independent copies

Run:

```bash
python test_demo.py
```

Expected output:

```text
Checks passed.
```

## Learning Notes

This activity helped me understand how dictionaries support quick lookups, how lists can be repaired without changing the original data, and how copied records can be used to preserve historical reports even when live records change.

## AI Usage

Microsoft Copilot was used to explain concepts, review code, and assist with documentation. All submitted work was reviewed and tested before submission.
