# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times, determine the minimum number of rooms required to accommodate all meetings. The intervals are in the format [start, end] where start and end are integers representing the start and end times of a meeting. For example, given the intervals [[0, 30], [5, 10], [15, 20]], the minimum number of rooms required would be 2 because the meeting from 5 to 10 overlaps with the meeting from 0 to 30, and the meeting from 15 to 20 also overlaps with the meeting from 0 to 30.

## Approach
We can solve this problem using a priority queue to keep track of the end times of the meetings. The algorithm sorts the meeting intervals by start time and then iterates over them, updating the priority queue with the end times. The size of the priority queue at any point represents the minimum number of rooms required so far.

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

        // Sort the meetings by start time.
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        // Initialize a priority queue to store the end times of the meetings.
        priority_queue<int, vector<int>, greater<int>> endTimes;

        // Add the end time of the first meeting to the priority queue.
        endTimes.push(intervals[0][1]);

        // Iterate over the rest of the meetings.
        for (int i = 1; i < intervals.size(); i++) {
            // If the current meeting starts after the earliest end time, update the earliest end time.
            if (intervals[i][0] >= endTimes.top()) {
                endTimes.pop();
            }

            // Add the end time of the current meeting to the priority queue.
            endTimes.push(intervals[i][1]);
        }

        // The size of the priority queue represents the minimum number of rooms required.
        return endTimes.size();
    }
};
```

## Test Cases
```
Input: [[0, 30], [5, 10], [15, 20]]
Output: 2
Input: [[7, 10], [2, 4]]
Output: 1
```

## Key Takeaways
- The priority queue helps to efficiently keep track of the end times of the meetings.
- The size of the priority queue at any point represents the minimum number of rooms required so far.
- Sorting the meeting intervals by start time ensures that we process the meetings in the correct order.