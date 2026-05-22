# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times, determine the minimum number of conference rooms required. Each interval is of the form [start, end] and represents the start and end times of a meeting. For example, if we have [[0, 30], [5, 10], [15, 20]], we need two conference rooms because the meeting from 5 to 10 overlaps with the meeting from 0 to 30, but the meeting from 15 to 20 can reuse the same room as the meeting from 5 to 10 after it ends.

## Approach
We will use a priority queue to keep track of the end times of the meetings. The algorithm sorts the meeting times by their start time and iterates over them, adding each meeting to the priority queue. If the earliest end time in the queue is earlier than or equal to the current meeting's start time, we remove it from the queue.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a comparator for the priority queue
struct Comparator {
    bool operator()(const int& a, const int& b) {
        return a > b;
    }
};

int minMeetingRooms(vector<vector<int>>& intervals) {
    if (intervals.empty()) return 0;

    // Sort the meeting intervals by their start time
    sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });

    // Initialize a priority queue to store the end times of the meetings
    priority_queue<int, vector<int>, Comparator> endTimes;

    // Initialize the minimum number of rooms required
    int minRooms = 0;

    // Iterate over the meeting intervals
    for (const auto& interval : intervals) {
        // If the earliest end time is earlier than or equal to the current meeting's start time, remove it from the queue
        if (!endTimes.empty() && endTimes.top() <= interval[0]) {
            endTimes.pop();
        }

        // Add the current meeting's end time to the queue
        endTimes.push(interval[1]);

        // Update the minimum number of rooms required
        minRooms = max(minRooms, (int)endTimes.size());
    }

    return minRooms;
}
```

## Test Cases
```
Input: [[0, 30], [5, 10], [15, 20]]
Output: 2
Input: [[7, 10], [2, 4]]
Output: 1
```

## Key Takeaways
- Use a priority queue to efficiently track the end times of the meetings.
- Sort the meeting intervals by their start time to ensure that we process them in the correct order.
- Update the minimum number of rooms required whenever we add a new meeting to the queue or remove an existing one.