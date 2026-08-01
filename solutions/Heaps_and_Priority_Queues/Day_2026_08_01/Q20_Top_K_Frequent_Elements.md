# Top K Frequent Elements

## Problem Statement
Given an integer array `nums` and an integer `k`, return the top `k` frequent elements in the array. The output should be in any order. If there are multiple possible answers, any of them is acceptable. For example, given `nums = [1,1,1,2,2,3]` and `k = 2`, the output could be `[1,2]` or `[2,1]`. The constraints are: `1 <= nums.length <= 10^5` and `1 <= k <= nums.length`.

## Approach
We can use a hash map to store the frequency of each element and then use a priority queue to find the top k frequent elements. The priority queue will store pairs of elements and their frequencies, and it will be ordered by the frequency in descending order.

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
        // Create a hash map to store the frequency of each element
        unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }

        // Create a priority queue to store the top k frequent elements
        priority_queue<pair<int, int>> pq;
        for (auto& it : freq) {
            pq.push({it.second, it.first});
        }

        // Get the top k frequent elements from the priority queue
        vector<int> result;
        while (k-- > 0) {
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
- We can use a hash map to efficiently store and retrieve the frequency of each element.
- A priority queue can be used to find the top k frequent elements by ordering the elements by their frequencies in descending order.
- The time complexity of the solution is O(n log k) due to the use of the priority queue, where n is the number of elements in the input array.