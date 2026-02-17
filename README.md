# Project Structure

```text
regression_assignment/
├── .git/                        <-- Tool: Version Control (Hidden folder)
├── .github/
│   └── workflows/
│       └── ci.yml               <-- Tool: CI/CD Pipeline (GitHub Actions robot)
├── app/
│   ├── __init__.py
│   └── store.py                 <-- The Application Code (Modules A and B)
└── tests/                       <-- Process: TDD & Test Pyramid
    ├── __init__.py
    ├── test_unit.py             
    └── test_integration.py      
