# Beautiful Arrangement

## Problem Statement
Suppose you have n integers from 1 to n, and you want to arrange them in a way that for every i, the value at position i is either i times a factor of the value, or the value is a factor of i. Given an integer n, return the number of possible arrangements. For example, if n = 2, the possible arrangements are [1, 2] and [2, 1]. If n = 3, there are no possible arrangements.

## Approach
The problem can be solved using backtracking and recursion. We can start by trying to place each number from 1 to n at the current position, and then recursively try to fill the remaining positions. If we find a valid arrangement, we increment the count.

## Complexity
- Time: O(k), where k is the number of possible arrangements
- Space: O(n), for the recursive call stack and the current arrangement

## C++ Solution
```cpp
class Solution {
public:
    int countArrangement(int n) {
        vector<bool> visited(n + 1, false);
        int count = 0;
        backtrack(1, n, visited, count);
        return count;
    }

    void backtrack(int pos, int n, vector<bool>& visited, int& count) {
        if (pos > n) {
            count++;
            return;
        }

        for (int i = 1; i <= n; i++) {
            if (!visited[i] && (i % pos == 0 || pos % i == 0)) {
                visited[i] = true;
                backtrack(pos + 1, n, visited, count);
                visited[i] = false;
            }
        }
    }
};
```

## Test Cases
```
Input: n = 2
Output: 2
Input: n = 3
Output: 3
```

## Key Takeaways
- The problem requires using backtracking and recursion to try all possible arrangements.
- We use a visited array to keep track of the numbers that have been used in the current arrangement.
- The time complexity is O(k), where k is the number of possible arrangements, because we only count each arrangement once.