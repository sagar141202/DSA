# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. The input will be an array of integers, and the output should be a vector of vectors, where each inner vector is a unique permutation of the input array. For example, given the input [1, 1, 2], the output should be [[1, 1, 2], [1, 2, 1], [2, 1, 1]]. The input array can contain up to 10^5 elements, and each element can be in the range [0, 10^5].

## Approach
To solve this problem, we can use backtracking to generate all permutations of the input array. We will sort the array first and then use a recursive function to generate all permutations. We will skip the duplicate elements to avoid duplicate permutations.

## Complexity
- Time: O(N! / (k1! * k2! * ... * km!)) where N is the length of the input array, and k1, k2, ..., km are the frequencies of each element in the array.
- Space: O(N) for the recursive call stack.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, vector<bool>& visited, vector<int>& path, vector<vector<int>>& result) {
    if (path.size() == nums.size()) {
        result.push_back(path);
        return;
    }
    for (int i = 0; i < nums.size(); i++) {
        if (visited[i] || (i > 0 && nums[i] == nums[i - 1] && !visited[i - 1])) {
            continue;
        }
        visited[i] = true;
        path.push_back(nums[i]);
        backtrack(nums, visited, path, result);
        path.pop_back();
        visited[i] = false;
    }
}

vector<vector<int>> permuteUnique(vector<int>& nums) {
    vector<vector<int>> result;
    vector<bool> visited(nums.size(), false);
    vector<int> path;
    sort(nums.begin(), nums.end());
    backtrack(nums, visited, path, result);
    return result;
}

int main() {
    vector<int> nums = {1, 1, 2};
    vector<vector<int>> result = permuteUnique(nums);
    for (auto& permutation : result) {
        for (auto& num : permutation) {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: [1, 1, 2]
Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
Input: [2, 1, 1]
Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
```

## Key Takeaways
- Sorting the input array helps to avoid duplicate permutations.
- Using a recursive function with backtracking can efficiently generate all permutations of the input array.
- Skipping duplicate elements ensures that the output permutations are unique.