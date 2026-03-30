# Sliding Window Median

## Problem Statement
The Sliding Window Median problem involves finding the median of all numbers in a given array within a sliding window of size `k`. The array is defined as `nums`, and the size of the sliding window is `k`. The task is to calculate the median for each position of the sliding window and return a vector of these medians. The input array `nums` contains `n` integers, and the size of the sliding window `k` is less than or equal to `n`. For example, given `nums = [1, 3, -1, -3, 5, 3, 6, 7]` and `k = 3`, the output should be `[1, -1, -1, 3, 5, 6]`.

## Approach
To solve this problem, we use two heaps: a max heap to store the smaller half of the numbers and a min heap to store the larger half. The max heap stores the `k/2` smallest numbers, and the min heap stores the `k/2` largest numbers. We maintain the balance between the two heaps to ensure the median can be calculated efficiently.

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
- Utilize two heaps to maintain the smaller and larger halves of the numbers within the sliding window.
- Balance the heaps to ensure efficient calculation of the median.
- Remove numbers that are out of the window by checking which heap they belong to and rebalancing the heaps as necessary.