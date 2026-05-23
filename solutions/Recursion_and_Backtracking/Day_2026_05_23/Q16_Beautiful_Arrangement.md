# Beautiful Arrangement

## Problem Statement
Suppose you have N integers from 1 to N, and you want to arrange them in a beautiful arrangement where for every i, the adjacent elements (at indices i-1 and i+1) are not equal to i. Given an integer N, return the number of possible beautiful arrangements. Note that the integers can be used only once, and the arrangement should be a permutation of the numbers from 1 to N.

## Approach
The problem can be solved using recursion and backtracking by generating all possible permutations and checking if each permutation satisfies the condition. We can use a recursive function to generate all permutations and a helper function to check if a permutation is beautiful.

## Complexity
- Time: O(N!)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countArrangement(int N) {
        vector<bool> visited(N + 1, false);
        int count = 0;
        backtrack(1, N, visited, count);
        return count;
    }
    
    void backtrack(int index, int N, vector<bool>& visited, int& count) {
        if (index > N) {
            count++;
            return;
        }
        
        for (int i = 1; i <= N; i++) {
            if (!visited[i] && (i % index == 0 || index % i == 0)) {
                visited[i] = true;
                backtrack(index + 1, N, visited, count);
                visited[i] = false;
            }
        }
    }
};

```

## Test Cases
```
Input: N = 3
Output: 3
Explanation: There are 3 possible beautiful arrangements: [1, 2, 3], [2, 1, 3], [2, 3, 1]

Input: N = 4
Output: 4
```

## Key Takeaways
- The problem requires generating all permutations of numbers from 1 to N and checking if each permutation satisfies the condition.
- Recursion and backtracking can be used to generate all permutations and check if each permutation is beautiful.
- The time complexity of the solution is O(N!) due to the generation of all permutations.