# Smallest Range Covering Elements from K Lists

## Problem Statement
You are given K sorted lists of integers. Find the smallest range that covers at least one element from each list. The range is defined as [min, max] where min and max are the minimum and maximum values in the range respectively. If there are multiple such ranges, return the one with the smallest length. If there are still multiple ranges with the same length, return the one with the smallest start value. For example, given the lists [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]], the smallest range covering elements from all lists is [20,24].

## Approach
We can use a priority queue to keep track of the smallest element from each list. We initialize the priority queue with the first element from each list along with its list index and element index. Then we keep removing the smallest element from the priority queue and add the next element from the same list until we find a range that covers all lists.

## Complexity
- Time: O(N log K)
- Space: O(K)

## C++ Solution
```cpp
#include <vector>
#include <queue>
using namespace std;

struct Node {
    int val, list, idx;
    Node(int v, int l, int i) : val(v), list(l), idx(i) {}
};

struct Compare {
    bool operator()(const Node& a, const Node& b) {
        return a.val > b.val;
    }
};

vector<int> smallestRange(vector<vector<int>>& nums) {
    priority_queue<Node, vector<Node>, Compare> pq;
    int maxVal = INT_MIN;
    for (int i = 0; i < nums.size(); i++) {
        maxVal = max(maxVal, nums[i][0]);
        pq.push(Node(nums[i][0], i, 0));
    }
    
    int minRange = INT_MAX, start = 0, end = 0;
    while (true) {
        Node node = pq.top();
        pq.pop();
        if (maxVal - node.val < minRange) {
            minRange = maxVal - node.val;
            start = node.val;
            end = maxVal;
        }
        
        if (node.idx + 1 == nums[node.list].size()) {
            break;
        }
        
        int nextVal = nums[node.list][node.idx + 1];
        maxVal = max(maxVal, nextVal);
        pq.push(Node(nextVal, node.list, node.idx + 1));
    }
    
    return {start, end};
}
```

## Test Cases
```
Input: [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
```

## Key Takeaways
- Use a priority queue to keep track of the smallest element from each list.
- Keep removing the smallest element from the priority queue and add the next element from the same list until we find a range that covers all lists.
- Update the maximum value and the range whenever we find a smaller range.