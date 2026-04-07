# Sliding Window Median

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the median of each `k`-sized subarray. The median is the middle value in an ordered integer list. If the size of the list is even, the median is the mean of the two middle values. For example, given `nums = [1, 3, -1, -3, 5, 3, 6, 7]` and `k = 3`, the output should be `[1, -1, -1, 3, 5, 6]`.

## Approach
We will use two heaps, a max heap to store the smaller half of the numbers and a min heap to store the larger half. This allows us to efficiently calculate the median of each subarray.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MedianFinder {
public:
    priority_queue<int> maxHeap; // max heap to store the smaller half
    priority_queue<int, vector<int>, greater<int>> minHeap; // min heap to store the larger half

    void addNum(int num) {
        // Add the number to the correct heap
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
    vector<double> result;

    for (int i = 0; i < nums.size(); i++) {
        mf.addNum(nums[i]);
        if (i >= k) {
            // Remove the number that is out of the window
            if (nums[i - k] <= mf.maxHeap.top()) {
                // Remove from max heap
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
                // Remove from min heap
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
            result.push_back(mf.findMedian());
        }
    }
    return result;
}

int main() {
    vector<int> nums = {1, 3, -1, -3, 5, 3, 6, 7};
    int k = 3;
    vector<double> result = medianSlidingWindow(nums, k);
    for (double num : result) {
        cout << num << " ";
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
- Use two heaps to store the smaller and larger halves of the numbers.
- Balance the heaps to ensure the max heap size is at most one more than the min heap size.
- Calculate the median based on the sizes of the two heaps.