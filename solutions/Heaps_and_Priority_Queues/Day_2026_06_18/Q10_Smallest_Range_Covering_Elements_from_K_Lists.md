# Smallest Range Covering Elements from K Lists

## Problem Statement
Given `k` sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as `[min_val, max_val]`, where `min_val` and `max_val` are the minimum and maximum values in the range, respectively. The size of the range is defined as `max_val - min_val`. If there are multiple ranges with the same size, return the one with the smallest `min_val`. The input lists are non-empty, and each list contains at least one element. The total number of elements across all lists is `n`.

## Approach
The problem can be solved using a priority queue to keep track of the smallest element from each list. We initialize the priority queue with the first element from each list, along with the list index and element index. We then repeatedly extract the smallest element from the priority queue, update the range if necessary, and insert the next element from the same list into the priority queue.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int val, list_idx, elem_idx;
    Node(int val, int list_idx, int elem_idx) : val(val), list_idx(list_idx), elem_idx(elem_idx) {}
};

struct Compare {
    bool operator()(const Node& a, const Node& b) {
        return a.val > b.val;
    }
};

vector<int> smallestRange(vector<vector<int>>& nums) {
    priority_queue<Node, vector<Node>, Compare> pq;
    int max_val = INT_MIN;
    for (int i = 0; i < nums.size(); i++) {
        pq.push(Node(nums[i][0], i, 0));
        max_val = max(max_val, nums[i][0]);
    }

    int min_range = INT_MAX, min_val = INT_MAX;
    while (!pq.empty()) {
        Node node = pq.top();
        pq.pop();
        if (max_val - node.val < min_range) {
            min_range = max_val - node.val;
            min_val = node.val;
        }
        if (node.elem_idx + 1 < nums[node.list_idx].size()) {
            int next_val = nums[node.list_idx][node.elem_idx + 1];
            max_val = max(max_val, next_val);
            pq.push(Node(next_val, node.list_idx, node.elem_idx + 1));
        } else {
            break;
        }
    }
    return {min_val, min_val + min_range};
}

int main() {
    vector<vector<int>> nums = {{4, 10, 15, 24, 26}, {0, 9, 12, 20}, {5, 18, 22, 30}};
    vector<int> result = smallestRange(nums);
    cout << "[" << result[0] << ", " << result[1] << "]" << endl;
    return 0;
}
```

## Test Cases
```
Input: nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
Output: [20, 24]
```

## Key Takeaways
- The use of a priority queue allows us to efficiently find the smallest element across all lists.
- The time complexity is O(n log k) due to the priority queue operations, where n is the total number of elements and k is the number of lists.
- The space complexity is O(k) for storing the priority queue.