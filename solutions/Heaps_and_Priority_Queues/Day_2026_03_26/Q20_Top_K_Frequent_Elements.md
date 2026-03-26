# Top K Frequent Elements

## Problem Statement
Given an integer array `nums` and an integer `k`, return the top `k` frequent elements in the array. The output should be in any order. The input array will contain at least `k` elements. The frequency of an element is the number of times it appears in the array. For example, given `nums = [1,1,1,2,2,3]` and `k = 2`, the output should be `[1,2]` because `1` appears three times and `2` appears two times.

## Approach
We will use a hash map to count the frequency of each element, then use a priority queue to find the top `k` frequent elements. The priority queue will store pairs of elements and their frequencies, and will be ordered by frequency in descending order.

## Complexity
- Time: O(n log k)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Count the frequency of each element
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }

        // Use a priority queue to find the top k frequent elements
        priority_queue<pair<int, int>> maxHeap;
        for (auto& pair : count) {
            maxHeap.push({pair.second, pair.first});
        }

        // Extract the top k elements from the priority queue
        vector<int> result;
        for (int i = 0; i < k; i++) {
            result.push_back(maxHeap.top().second);
            maxHeap.pop();
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
- Use a hash map to count the frequency of each element in O(n) time.
- Use a priority queue to find the top k frequent elements in O(n log k) time.
- The space complexity is O(n) because in the worst case, we need to store all elements in the hash map and priority queue.