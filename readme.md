# Algorithms and Data Structures I - Course Projects

## Description
This repository contains the projects developed for the **Algorithms and Data Structures I** course. The assignments cover algorithm efficiency analysis, data structures such as stacks, and tree-based calculations. The projects are implemented in **Python** and **Java**.

## Assignments and Implementations

### 1. **Operation Counting Analysis (Python) - `trab1.py`**
- Implements different algorithms and measures their performance using **operation counting**.
- Determines whether algorithms follow polynomial or exponential growth.
- Uses Python's `matplotlib` to generate **graphs** of algorithm complexity.
- **Key Algorithms:**
  - Fibonacci sequence with recursion.
  - Multiple nested loops with varying complexities.
  - Exponential and polynomial function detection.

### 2. **Complex Number Stack-Based Calculator (Python) - `main.py`, `pilha.py`**
- Implements a **stack-based calculator** for complex numbers.
- Supports basic arithmetic operations: `+`, `-`, `*`, `/`.
- Additional operations: **inverse (`inv`), absolute value (`abs`), swap (`swap`), and duplicate (`dup`)**.
- Reads input from a file and executes the operations.

### 3. **Tree Structure Analysis (Java) - `Tree.java`, `TTest.java`**
- Implements a **tree-based model** for evaluating the stability of structures.
- Nodes represent parts of a **monument**, and calculations determine whether it remains **balanced**.
- Includes operations:
  - **Insert nodes (`ins`)**
  - **Calculate height (`alt`)**
  - **Evaluate stability (`kak`)**
  - **Recursive operations (`tudo`)**
- Reads input and dynamically constructs the tree representation.

## Files in This Repository
| File | Description |
|------|-------------|
| `trab1.py` | Implements performance analysis via operation counting. |
| `Relatório.pdf` | Report on algorithm performance and complexity classification. |
| `main.py` | Stack-based calculator for complex numbers. |
| `pilha.py` | Implementation of the stack structure used in `main.py`. |
| `Tree.java` | Java implementation of a tree-based structure evaluation. |
| `TTest.java` | Test program to interact with the tree structure. |
| `t2.pdf` | Assignment description for the complex number calculator. |
| `t3.pdf` | Assignment description for the tree-based monument stability calculation. |

## How to Run
### Running Performance Analysis (Python)
```sh
python trab1.py
```
### Running the Complex Number Calculator (Python)
```sh
python main.py < input.txt
```
### Running the Tree Structure Evaluation (Java)
```sh
javac Tree.java TTest.java
java TTest
```

## Technologies Used
- **Python** for algorithmic analysis and stack-based computation.
- **Java** for tree-based structure modeling.
- **Matplotlib** for visualization of algorithm performance.

## License
This project is for educational purposes.

## Author
Developed for the **Algorithms and Data Structures I** course.


