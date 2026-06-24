# Smallest Range Covering Elements from K Lists

## Problem Statement
Given K sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as [min, max], where min and max are the minimum and maximum values in the range, respectively. The size of the range is max - min. If there are multiple ranges with the same size, return the one with the smallest min value. For example, given the lists [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]], the smallest range covering elements from all lists is [20, 24] with a size of 4.

## Approach
We can use a priority queue to keep track of the smallest elements from each list. We initialize the queue with the first element from each list, along with the list index and element index. Then, we repeatedly extract the smallest element from the queue, update the range if necessary, and insert the next element from the same list into the queue.

## Complexity
- Time: O(N log K)
- Space: O(K)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int val, listIdx, elemIdx;
    Node(int val, int listIdx, int elemIdx) : val(val), listIdx(listIdx), elemIdx(elemIdx) {}
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
    int minRange = INT_MAX, minVal = INT_MAX;
    while (!pq.empty()) {
        Node node = pq.top();
        pq.pop();
        if (maxVal - node.val < minRange) {
            minRange = maxVal - node.val;
            minVal = node.val;
        }
        if (node.elemIdx + 1 < nums[node.listIdx].size()) {
            maxVal = max(maxVal, nums[node.listIdx][node.elemIdx + 1]);
            pq.push(Node(nums[node.listIdx][node.elemIdx + 1], node.listIdx, node.elemIdx + 1));
        } else {
            break;
        }
    }
    return {minVal, minVal + minRange};
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
- We keep track of the maximum value seen so far to update the range.
- The time complexity is O(N log K) due to the use of the priority queue, where N is the total number of elements and K is the number of lists.