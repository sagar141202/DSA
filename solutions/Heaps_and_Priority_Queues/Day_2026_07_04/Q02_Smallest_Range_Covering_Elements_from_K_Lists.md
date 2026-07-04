# Smallest Range Covering Elements from K Lists

## Problem Statement
Given K sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as [min, max] where min and max are the minimum and maximum values in the range. The problem can be formalized as follows: Given K lists of integers, nums[i] where i = 0, 1, ..., K-1, find the smallest range that covers at least one element from each list. The range [min, max] should be such that min is the minimum possible and max is the maximum possible in the range.

## Approach
The problem can be solved using a priority queue to keep track of the smallest range. We start by pushing the first element of each list into the priority queue along with its list index and element index. Then, we keep removing the smallest element from the queue and adding the next element from the same list until we find the smallest range that covers all lists.

## Complexity
- Time: O(N log K) where N is the total number of elements across all lists and K is the number of lists.
- Space: O(K) for storing the elements in the priority queue.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int val, listIndex, elementIndex;
    Node(int val, int listIndex, int elementIndex) : val(val), listIndex(listIndex), elementIndex(elementIndex) {}
};

struct compare {
    bool operator()(const Node& a, const Node& b) {
        return a.val > b.val;
    }
};

vector<int> smallestRange(vector<vector<int>>& nums) {
    priority_queue<Node, vector<Node>, compare> pq;
    int maxValue = INT_MIN;
    for (int i = 0; i < nums.size(); i++) {
        pq.push(Node(nums[i][0], i, 0));
        maxValue = max(maxValue, nums[i][0]);
    }
    
    int minRange = INT_MAX, start = 0, end = 0;
    while (true) {
        Node node = pq.top();
        pq.pop();
        int minValue = node.val;
        if (maxValue - minValue < minRange) {
            minRange = maxValue - minValue;
            start = minValue;
            end = maxValue;
        }
        
        if (node.elementIndex + 1 == nums[node.listIndex].size()) {
            break;
        }
        
        pq.push(Node(nums[node.listIndex][node.elementIndex + 1], node.listIndex, node.elementIndex + 1));
        maxValue = max(maxValue, nums[node.listIndex][node.elementIndex + 1]);
    }
    
    return {start, end};
}

int main() {
    vector<vector<int>> nums = {{4,10,15,24,26}, {0,9,12,20}, {5,18,22,30}};
    vector<int> result = smallestRange(nums);
    cout << "[" << result[0] << ", " << result[1] << "]" << endl;
    return 0;
}
```

## Test Cases
```
Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20, 24]
```

## Key Takeaways
- Use a priority queue to keep track of the smallest range.
- Push the first element of each list into the priority queue along with its list index and element index.
- Remove the smallest element from the queue and add the next element from the same list until we find the smallest range that covers all lists.