# Binary Search Implementation

## Context
Binary search is a fundamental algorithm used in computer science for efficiently finding elements in sorted arrays. It's commonly used in database indexing, search engines, and optimization problems where logarithmic time complexity is crucial for performance.

## Problem Statement
Implement a comprehensive binary search system that demonstrates different variations and applications:
1. Classic binary search for finding exact matches in sorted arrays
2. Search for insertion position (leftmost/rightmost insertion points)
3. Search in rotated sorted arrays
4. Find first/last occurrence of duplicated elements
5. Search in 2D sorted matrix

## Requirements
- Implement iterative and recursive versions of binary search
- Handle edge cases (empty arrays, single elements, not found)
- Provide clear time and space complexity analysis
- Support different data types (integers, strings, custom objects)
- Include comprehensive test cases with performance validation
- Implement proper error handling for invalid inputs
- Use type hints and follow Python best practices

## Assumptions
- Input arrays are properly sorted (except for rotated array variation)
- Array elements are comparable using standard comparison operators
- Memory constraints allow for reasonable array sizes (up to 10^6 elements)
- No external libraries required beyond standard Python
- Focus on algorithmic correctness and efficiency

## For Examiner

### Difficulty Level
Intermediate

### Expected Time
45-60 minutes

### Key Concepts Being Tested
- Algorithm design and implementation
- Time and space complexity analysis
- Edge case handling and input validation
- Code organization and modularity
- Testing and performance validation
- Understanding of binary search variations

### Hints (if needed)
- Remember that binary search requires sorted input
- Consider off-by-one errors in index calculations
- Think about how to handle the search space reduction
- Consider both iterative and recursive approaches
- Test with various array sizes and edge cases

### Solution Approach Plan
1. Implement classic binary search (iterative and recursive)
2. Add insertion position search functionality
3. Implement rotated array search variation
4. Add first/last occurrence search for duplicates
5. Implement 2D matrix search
6. Create comprehensive test suite with performance validation
7. Add proper documentation and complexity analysis

## Example Input/Output
```
Input: arr = [1, 3, 5, 7, 9, 11, 13], target = 7
Output: 3 (index of target element)

Input: arr = [1, 3, 5, 7, 9, 11, 13], target = 6
Output: -1 (element not found)

Input: arr = [1, 2, 2, 2, 3, 4, 5], target = 2, find_first = True
Output: 1 (first occurrence of target)
```
