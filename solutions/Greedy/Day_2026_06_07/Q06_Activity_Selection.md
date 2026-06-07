# Activity Selection

## Problem Statement
Given a set of activities and their start and end times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. The activities are given as pairs of integers, where the first integer represents the start time and the second integer represents the end time. For example, if we have two activities (1, 4) and (3, 5), we cannot select both activities because they overlap. The goal is to find the maximum number of non-overlapping activities that can be selected.

## Approach
The algorithm sorts the activities based on their end times and then iterates through the sorted list, selecting the activities that do not overlap with the previously selected activity. This approach ensures that we select the maximum number of non-overlapping activities. The key idea is to always select the activity with the earliest end time, which gives us the maximum chance of selecting more activities in the future.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a structure to represent an activity
struct Activity {
    int start;
    int end;
};

// Compare function to sort activities based on end time
bool compare(Activity a, Activity b) {
    return a.end < b.end;
}

// Function to select the maximum number of non-overlapping activities
int activitySelection(vector<Activity> activities) {
    // Sort the activities based on end time
    sort(activities.begin(), activities.end(), compare);

    // Initialize the count of selected activities
    int count = 1;

    // Initialize the end time of the last selected activity
    int lastEnd = activities[0].end;

    // Iterate through the sorted list of activities
    for (int i = 1; i < activities.size(); i++) {
        // Check if the current activity does not overlap with the last selected activity
        if (activities[i].start >= lastEnd) {
            // Increment the count of selected activities
            count++;

            // Update the end time of the last selected activity
            lastEnd = activities[i].end;
        }
    }

    // Return the maximum number of non-overlapping activities
    return count;
}

int main() {
    // Example usage
    vector<Activity> activities = {{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9}, {6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}};
    cout << "Maximum number of non-overlapping activities: " << activitySelection(activities) << endl;
    return 0;
}
```

## Test Cases
```
Input: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
Output: 4
```

## Key Takeaways
- The greedy approach is used to solve the activity selection problem by always selecting the activity with the earliest end time.
- The time complexity of the algorithm is O(n log n) due to the sorting step.
- The space complexity of the algorithm is O(n) for storing the activities.