# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times, determine the minimum number of rooms required to accommodate all meetings. Each meeting interval is represented as a pair of integers, where the first integer is the start time and the second integer is the end time. The start time is inclusive, and the end time is exclusive. For example, if we have two meetings, one from 0 to 30 and another from 5 to 10, we need two rooms because the two meetings overlap. The input array of meeting intervals is not guaranteed to be sorted.

## Approach
We can solve this problem by using a priority queue to keep track of the end times of the meetings. We first sort the meeting intervals based on their start times. Then, we iterate over the sorted intervals and use the priority queue to find the earliest end time that is not earlier than the current start time. If we find such an end time, we remove it from the queue and add the current end time. If we don't find such an end time, we add the current end time to the queue. The size of the queue at any point represents the minimum number of rooms required so far.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        // If there are no meetings, we don't need any rooms.
        if (intervals.empty()) {
            return 0;
        }

        // Sort the meetings by their start time.
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        // Initialize a priority queue to store the end times of the meetings.
        priority_queue<int, vector<int>, greater<int>> endTimes;

        // Initialize the minimum number of rooms required.
        int minRooms = 0;

        // Iterate over the meetings.
        for (const auto& interval : intervals) {
            // If the meeting starts after the earliest end time, update the earliest end time.
            if (!endTimes.empty() && interval[0] >= endTimes.top()) {
                endTimes.pop();
            }

            // Add the current meeting's end time to the priority queue.
            endTimes.push(interval[1]);

            // Update the minimum number of rooms required.
            minRooms = max(minRooms, (int)endTimes.size());
        }

        // Return the minimum number of rooms required.
        return minRooms;
    }
};
```

## Test Cases
```
Input: [[0,30],[5,10],[15,20]]
Output: 2
Input: [[7,10],[2,4]]
Output: 1
```

## Key Takeaways
- We can use a priority queue to efficiently find the earliest end time that is not earlier than the current start time.
- Sorting the meeting intervals by their start times allows us to process them in a way that minimizes the number of rooms required.
- The size of the priority queue at any point represents the minimum number of rooms required so far.