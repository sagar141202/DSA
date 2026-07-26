# Sliding Window Median

## Problem Statement
The Sliding Window Median problem involves finding the median of all numbers in a sliding window of size k in an array of integers. The array is given as `nums`, and the size of the sliding window is given as `k`. The goal is to calculate the median for each position of the sliding window and return a list of these medians. For example, given `nums = [1, 3, -1, -3, 5, 3, 6, 7]` and `k = 3`, the output should be `[1, -1, -1, 3, 5, 6]`.

## Approach
We will use two priority queues (heaps) to solve this problem: a max-heap for the smaller half of the numbers and a min-heap for the larger half. This allows us to efficiently maintain the median as we slide the window.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MedianFinder {
public:
    priority_queue<int> maxHeap; // max-heap for the smaller half
    priority_queue<int, vector<int>, greater<int>> minHeap; // min-heap for the larger half

    void addNum(int num) {
        // Add num to the correct heap
        if (maxHeap.empty() || num <= maxHeap.top()) {
            maxHeap.push(num);
        } else {
            minHeap.push(num);
        }

        // Balance the heaps
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }

    double findMedian() {
        // Calculate the median
        if (maxHeap.size() == minHeap.size()) {
            return (maxHeap.top() + minHeap.top()) / 2.0;
        } else {
            return (double)maxHeap.top();
        }
    }
};

vector<double> medianSlidingWindow(vector<int>& nums, int k) {
    MedianFinder mf;
    vector<double> medians;
    for (int i = 0; i < nums.size(); i++) {
        mf.addNum(nums[i]);
        if (i >= k) {
            // Remove the oldest number from the window
            if (nums[i - k] <= mf.maxHeap.top()) {
                // Remove from max-heap
                priority_queue<int> temp;
                while (mf.maxHeap.top() != nums[i - k]) {
                    temp.push(mf.maxHeap.top());
                    mf.maxHeap.pop();
                }
                mf.maxHeap.pop();
                while (!temp.empty()) {
                    mf.maxHeap.push(temp.top());
                    temp.pop();
                }
            } else {
                // Remove from min-heap
                priority_queue<int, vector<int>, greater<int>> temp;
                while (mf.minHeap.top() != nums[i - k]) {
                    temp.push(mf.minHeap.top());
                    mf.minHeap.pop();
                }
                mf.minHeap.pop();
                while (!temp.empty()) {
                    mf.minHeap.push(temp.top());
                    temp.pop();
                }
            }
        }
        if (i >= k - 1) {
            medians.push_back(mf.findMedian());
        }
    }
    return medians;
}

int main() {
    vector<int> nums = {1, 3, -1, -3, 5, 3, 6, 7};
    int k = 3;
    vector<double> medians = medianSlidingWindow(nums, k);
    for (double median : medians) {
        cout << median << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [1, -1, -1, 3, 5, 6]
```

## Key Takeaways
- Use two priority queues (heaps) to maintain the median in a sliding window.
- Balance the heaps to ensure the max-heap size is at most one more than the min-heap size.
- Remove the oldest number from the window by checking which heap it belongs to and rebalancing the heaps as necessary.