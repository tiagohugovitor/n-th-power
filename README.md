# Power Calculation Algorithms Comparison

This project implements and compares different algorithms for calculating the n-th power of a number. It includes an iterative algorithm and two recursive algorithms using the divide and conquer technique, one with two recursive calls and another with optimized single recursive call.

## Project Context

This project was part of an assignment for the Analysis of Algorithms course in the Master's program in Computer Science at the Federal University of Uberlândia (UFU). The presentation file can be found in 'n-th-power.pdf' (presentation in Portuguese). Each calculation is performed using a base of 2 (e.g. 2 raised to the power of inputSize). Additionally, the algorithm runs 10 tests for each input, and the average time taken is recorded.

## Algorithms Implemented

1. **Iterative Algorithm**
   - Calculates the n-th power using an iterative approach.

2. **Recursive Algorithm with Two Recursive Calls**
   - Uses divide and conquer with two recursive calls to compute the n-th power.

3. **Recursive Algorithm with One Recursive Call (Optimized)**
   - Optimized version using divide and conquer with a single recursive call to compute the n-th power.

## Files

- **iterative.py**: Implementation of the iterative algorithm.
- **recursiveTwoCalls.py**: Implementation of the recursive algorithm with two recursive calls.
- **recursiveSinglecall.py**: Implementation of the recursive algorithm with one optimized recursive call.
- **compareAlgorithms.py**: Script to compare the execution time of all algorithms across a range of input sizes.

## Running the Code

1. Clone the repository:
   ```bash
   git clone https://github.com/tiagohugovitor/n-th-power.git
   cd n-th-power
   ```

2. Run the comparison script:
    ```bash
    python compareAlgorithms.py
    ```

3. Results:
    - Execution time graphs saved in the results directory.
    - Dataframe with execution times saved as results/dataframe-{inputSize}.xlsx.

## Algorithms Analysis

### Time Complexity
 - **Iterative Algorithm**: O(n)
 - **Recursive Algorithm with Two Recursive Calls**: O(n)
 - **Recursive Algorithm with One Recursive Call (Optimized)**: O(log n)

### Conclusion
The iterative algorithm operates with linear time complexity. The Divide and Conquer technique can produce algorithms with both linear (Recursive Algorithm with Two Recursive Calls) and logarithmic (Recursive Algorithm with One Recursive Call) complexities. However, for small inputs, both Divide and Conquer algorithms lag in terms of execution time.

When analyzing an input size of 50, it becomes evident that the logarithmic complexity algorithm performs faster than the traditional linear one. Although both the iterative and recursive algorithms with two calls exhibit linear complexity, the recursive one takes more time until reaching an input size of 20000, after which it begins to outperform the traditional algorithm.

The logarithmic complexity algorithm quickly emerges as the superior choice. In contrast, the Divide and Conquer approach with linear complexity takes longer but eventually surpasses the traditional approach, which also operates with linear complexity.

## Dependencies
    - Python 3.x
    - matplotlib
    - pandas
 
