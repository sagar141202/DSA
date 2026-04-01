# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all unique permutations. The input collection is given as an array of integers, and the output should be a list of lists, where each sublist is a unique permutation of the input array. For example, if the input is `[1, 1, 2]`, the output should be `[[1,1,2], [1,2,1], [2,1,1]]`. The input array will contain at most 100 elements, and the elements will be in the range `[1, 100]`.

## Approach
To solve this problem, we will use a backtracking approach with recursion to generate all permutations of the input array. We will also use a sorting step to handle duplicates and avoid generating the same permutation multiple times.

## Complexity
- Time: O(N! / (k1! * k2! * ... * km!)) where N is the number of elements in the input array, and k1, k2, ..., km are the frequencies of each distinct element.
- Space: O(N) for the recursion stack.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, vector<bool>& used, vector<int>& path, vector<vector<int>>& result) {
    if (path.size() == nums.size()) {
        result.push_back(path);
        return;
    }
    for (int i = 0; i < nums.size(); i++) {
        if (used[i] || (i > 0 && nums[i] == nums[i - 1] && !used[i - 1])) {
            continue;
        }
        used[i] = true;
        path.push_back(nums[i]);
        backtrack(nums, used, path, result);
        path.pop_back();
        used[i] = false;
    }
}

vector<vector<int>> permuteUnique(vector<int>& nums) {
    vector<vector<int>> result;
    vector<bool> used(nums.size(), false);
    vector<int> path;
    sort(nums.begin(), nums.end());
    backtrack(nums, used, path, result);
    return result;
}
```

## Test Cases
```
Input: [1, 1, 2]
Output: [[1,1,2], [1,2,1], [2,1,1]]
Input: [2, 1, 1]
Output: [[1,1,2], [1,2,1], [2,1,1]]
```

## Key Takeaways
- Use backtracking to generate all permutations of the input array.
- Sort the input array to handle duplicates and avoid generating the same permutation multiple times.
- Use a `used` array to keep track of the elements that have been used in the current permutation.