# Number Partition Problem

This repository contains an implementation of the Number Partition Problem using the Quadratic Unconstrained Binary Optimization (QUBO) model and Simulated Annealing algorithm. The Number Partition Problem is a classic NP-hard problem in computer science and combinatorial optimization.

## Table of Contents

- [Number Partition Problem](#number-partition-problem)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Example](#example)
  - [Acknowledgements](#acknowledgements)
  - [License](#license)

## Introduction

The Number Partition Problem involves dividing a set of numbers into two subsets such that the difference between the sums of the subsets is minimized. This problem can be modeled using a QUBO formulation and solved using various optimization algorithms, including Simulated Annealing.

This project provides:

- A QUBO model for the Number Partition Problem.
- An implementation of the Simulated Annealing algorithm to solve the QUBO model.
- Scripts to run the algorithm and visualize the results.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Sebastian-0912/Number-partition-problem.git
    cd Number-partition-problem
    ```

2. Set up a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Prepare your dataset: Create a text file containing the numbers to be partitioned, one per line.

2. Run the Simulated Annealing algorithm:

    ```bash
    python simulated_annealing.py <path_to_your_dataset>
    ```

3. The results, including the partitions and the objective value, will be displayed in the console.

## Example

1. Create a file `numbers.txt` with the following content:

    ```plaintext
    10
    20
    15
    5
    25
    ```

2. Run the algorithm:

    ```bash
    python simulated_annealing.py numbers.txt
    ```

3. Sample output:

    ```plaintext
    Partition 1: [10, 25]
    Partition 2: [20, 15, 5]
    Difference: 5
    ```

## Acknowledgements

This project is inspired by the need to solve combinatorial optimization problems using advanced algorithms. Special thanks to the developers and researchers who have contributed to the field of optimization and quantum computing.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
