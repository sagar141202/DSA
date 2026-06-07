# Beautiful Arrangement

## Problem Statement
Suppose you have n integers from 1 to n, and you want to arrange them in such a way that for every i (1 <= i <= n), the number at position i is either a multiple of i or i is a multiple of the number at position i. Given an integer n, find the number of beautiful arrangements that can be constructed.

## Approach
We will use backtracking to generate all possible permutations of numbers from 1 to n and check if each permutation satisfies the given condition. The algorithm will recursively try to place each number in the current position and backtrack if the condition is not met.

## Complexity
- Time: O(n!)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countArrangement(int n) {
        vector<int> visited(n + 1, 0);
        int count = 0;
        backtrack(1, n, visited, count);
        return count;
    }
    
    void backtrack(int pos, int n, vector<int>& visited, int& count) {
        if (pos > n) {
            count++;
            return;
        }
        
        for (int i = 1; i <= n; i++) {
            if (!visited[i] && (i % pos == 0 || pos % i == 0)) {
                visited[i] = 1;
                backtrack(pos + 1, n, visited, count);
                visited[i] = 0;
            }
        }
    }
};

int main() {
    Solution solution;
    int n = 3;
    cout << solution.countArrangement(n) << endl;
    return 0;
}
```

## Test Cases
```
Input: n = 3
Output: 3
```

## Key Takeaways
- Use backtracking to generate all possible permutations of numbers.
- Check if each permutation satisfies the given condition before exploring further.
- Use a visited array to keep track of the numbers that have been used in the current permutation.