# 🔐 Password Generator

A command-line password generator built in Python. Supports custom settings or quick default generation.

## Features

- Generate passwords with custom length
- Toggle letters, digits, and punctuation
- Generate multiple passwords at once
- Default mode (8 characters, letters + digits)

## Usage

Run the script:

```bash
python password_generator.py
```

You'll see a menu with two options:

```
=====Password Generator=====
1. Modify password generator
2. Generate password default settings
3. Exit
```

### Option 1 — Custom Generator

Lets you configure before generating:

| Setting | Default |
|---|---|
| Password length | 8 |
| Letters (a-zA-Z) | On |
| Digits (0-9) | On |
| Punctuation (!@#...) | Off |
| Amount to generate | 1 |

### Option 2 — Default Generator

Instantly generates one 8-character password using letters and digits.

## Example Output

```
Your generated password: aB3kRt9Z
Your generated password: Xm2pQv7N
```

## Requirements

- Python 3.x
- No external libraries needed (uses built-in `random` and `string`)
