# Top K Frequent Elements

## Problem Statement
Given an integer array `nums` and an integer `k`, return the top `k` frequent elements in the array. The output should be in any order. The input array will have at least `k` elements. For example, if `nums = [1,1,1,2,2,3]` and `k = 2`, the output should be `[1,2]` because `1` and `2` are the two most frequent elements in the array.

## Approach
We can use a priority queue to solve this problem. First, count the frequency of each element, then push the elements into a priority queue based on their frequencies. The priority queue will automatically sort the elements based on their frequencies.

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
        // Count the frequency of each element
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }
        
        // Create a priority queue to store the elements and their frequencies
        priority_queue<pair<int, int>> pq;
        for (auto& it : count) {
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
- Use a priority queue to sort elements based on their frequencies.
- Use an unordered map to count the frequency of each element.
- The time complexity is O(N log k) because we are using a priority queue to get the top k elements.