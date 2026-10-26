# AL03 - Find, Update, and Select

## Purpose

This program manages campus help desk tickets using lists, dictionaries, and sets.

## What the Program Does

- Builds a ticket registry from a list of tickets
- Finds tickets using a list scan
- Finds tickets using a dictionary registry
- Updates ticket priorities
- Filters tickets by category
- Rejects duplicate ticket IDs

## Data Structures

### List
Stores all ticket records.

### Dictionary
Stores tickets by ID for quick lookup and updates.

### Set
Stores the supported ticket categories.

## Comparison

### Lookup
A dictionary registry is best because tickets can be found directly by ID.

### Update
A dictionary registry is best because a ticket can be updated using its ID.

### Filter
The registry can be searched to find all tickets in a category.

## Testing

The tests check:

- Found lookup
- Missing lookup
- Empty input
- Duplicate IDs
- Priority updates
- Category filtering
- Independent copies

Run:

```bash
python test_demo.py
```

Expected output:

```text
Checks passed.
```

## AI Usage

Microsoft Copilot was used to help explain concepts, review code, and assist with documentation. All submitted work was reviewed and tested before submission.
