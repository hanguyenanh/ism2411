# ISM2411 — Python for Business

**Name:** Ha Nguyen Anh Nguyen

**Semester:** Fall 2026

**Instructor:** Markum Reed

## About This Repo

This repository contains my weekly lab submissions for ISM2411.
Each folder corresponds to one module.

## Modules

- `week05/` — Conditionals: tiered discount calculator
- `week06/` — Loops: sales report with sum, average, max
- `week07/` — Functions: calculate_tax, apply_discount
- `week08/` — Git: first GitHub submission

## How to Run

Each script is standalone. Open a terminal and run:
```
python week07/functions.py
```

## Reflection

**1. Git log**

```
32b29a4 add README with module listing and run instructions
536fbd1 add module 7 functions: calculate_tax, apply_discount, final_price
161a60b add .gitignore for Python and OS files
1da136c Initial commit
```

Each commit message starts with a verb and says exactly what changed, and each commit covers one change. If I were hiring someone and saw this history, it would tell me they work in small, organized steps and communicate clearly. I could understand what they did and why without opening the files.

**2. How Git changes my approach to editing**

Before this module, I would edit a working script directly and keep copies like `functions_old.py` in case I broke something. Now I can make changes knowing every working version is saved in the history, so I can experiment and roll back if needed. I'll also commit after each small working change instead of waiting until everything is finished.

**3. Something extra for my .gitignore**

I added `venv/` (my Python virtual environment) and `*.log`. A virtual environment is specific to my computer, is large, and can be recreated from a requirements file, so it doesn't belong in the repo. Log files are generated automatically and could contain private paths or information.
