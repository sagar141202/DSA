# Smallest Range Covering Elements from K Lists

## Problem Statement
Given K sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as [min, max], where min and max are the minimum and maximum values in the range, respectively. The goal is to minimize the length of the range, i.e., max - min. If there are multiple such ranges, return the one with the smallest maximum value. The input lists are non-empty and contain distinct integers. For example, given the lists [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]], the smallest range covering elements from all lists is [20, 24].

## Approach
The approach involves using a priority queue to keep track of the smallest element from each list. We initialize the queue with the first element from each list, along with its list index and element index. Then, we repeatedly extract the smallest element from the queue and add the next element from the same list to the queue, until we find a range that covers all lists.

## Complexity
- Time: O(N log K)
- Space: O(K)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Element {
    int val, listIdx, elemIdx;
    bool operator<(const Element& other) const {
        return val > other.val;
    }
};

vector<int> smallestRange(vector<vector<int>>& nums) {
    priority_queue<Element> pq;
    int maxVal = INT_MIN;
    for (int i = 0; i < nums.size(); i++) {
        maxVal = max(maxVal, nums[i][0]);
        pq.push({nums[i][0], i, 0});
    }
    int range = INT_MAX, start = 0, end = maxVal;
    while (true) {
        Element e = pq.top();
        pq.pop();
        if (maxVal - e.val < range) {
            range = maxVal - e.val;
            start = e.val;
            end = maxVal;
        }
        if (e.elemIdx + 1 == nums[e.listIdx].size()) {
            break;
        }
        maxVal = max(maxVal, nums[e.listIdx][e.elemIdx + 1]);
        pq.push({nums[e.listIdx][e.elemIdx + 1], e.listIdx, e.elemIdx + 1});
    }
    return {start, end};
}

int main() {
    vector<vector<int>> nums = {{4,10,15,24,26},{0,9,12,20},{5,18,22,30}};
    vector<int> result = smallestRange(nums);
    cout << "[" << result[0] << ", " << result[1] << "]" << endl;
    return 0;
}
```

## Test Cases
```
Input: [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20, 24]
```

## Key Takeaways
- We use a priority queue to efficiently find the smallest element from each list.
- The maximum value in the range is updated whenever we add a new element to the queue.
- The range is updated whenever we find a smaller range that covers all lists.