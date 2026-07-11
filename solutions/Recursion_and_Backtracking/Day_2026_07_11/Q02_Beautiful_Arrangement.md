# Beautiful Arrangement

## Problem Statement
Suppose you have N integers from 1 to N, and you want to arrange them in a beautiful way. A beautiful arrangement is one in which, for every i, either the number at position i is a multiple of i or i is a multiple of the number at position i. Given an integer N, return the number of possible beautiful arrangements. Note that the input N will be in the range [1, 15].

## Approach
We can solve this problem using recursion and backtracking by trying all possible positions for each number and checking if the arrangement is beautiful. The key idea is to use a recursive function to try all permutations of numbers and check the beautiful arrangement condition for each permutation.

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
    
    void backtrack(int pos, int N, vector<bool>& visited, int& count) {
        if (pos > N) {
            count++;
            return;
        }
        
        for (int i = 1; i <= N; i++) {
            if (!visited[i] && (i % pos == 0 || pos % i == 0)) {
                visited[i] = true;
                backtrack(pos + 1, N, visited, count);
                visited[i] = false;
            }
        }
    }
};

int main() {
    Solution solution;
    int N = 3;
    cout << solution.countArrangement(N) << endl;
    return 0;
}
```

## Test Cases
```
Input: N = 3
Output: 3
Input: N = 4
Output: 4
```

## Key Takeaways
- Recursion and backtracking can be used to try all possible permutations of numbers.
- A beautiful arrangement can be checked by verifying the condition for each position.
- The time complexity of this solution is O(N!) due to the recursive nature of the solution.