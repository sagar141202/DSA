# Top K Frequent Elements

## Problem Statement
Given an integer array `nums` and an integer `k`, return the top `k` frequent elements in the array. The output should be sorted in descending order of frequency, and if two elements have the same frequency, they should be sorted in ascending order. For example, given `nums = [1,1,1,2,2,3]` and `k = 2`, the output should be `[1,2]`. The array `nums` has a length of at most `10^5` and `k` is at most `10^4`.

## Approach
We can use a priority queue to solve this problem, where the priority queue stores pairs of elements and their frequencies. The priority queue will automatically sort the elements based on their frequencies and values. We can then pop the top `k` elements from the priority queue to get the top `k` frequent elements.

## Complexity
- Time: O(N log k)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Create a hashmap to store the frequency of each element
        unordered_map<int, int> frequency;
        for (int num : nums) {
            frequency[num]++;
        }

        // Create a priority queue to store the top k frequent elements
        priority_queue<pair<int, int>> pq;
        for (auto& it : frequency) {
            pq.push({it.second, it.first});
        }

        // Get the top k frequent elements
        vector<int> result;
        for (int i = 0; i < k; i++) {
            result.push_back(pq.top().second);
            pq.pop();
        }

        return result;
    }
};
```

## Test Cases
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Input: nums = [1], k = 1
Output: [1]
```

## Key Takeaways
- Use a priority queue to store the top k frequent elements
- Use a hashmap to store the frequency of each element
- The time complexity is O(N log k) due to the use of the priority queue