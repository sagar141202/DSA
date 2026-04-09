# Activity Selection

## Problem Statement
Given a set of activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. The activities are given as pairs of start and finish times, and the goal is to find the maximum number of activities that do not conflict with each other. For example, if we have the following activities: (1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14), the maximum number of non-conflicting activities is 4: (1, 4), (5, 7), (8, 11), (12, 14). The activities are selected based on their finish times, and the activity with the earliest finish time is selected first.

## Approach
The algorithm sorts the activities based on their finish times and then iterates over the sorted activities, selecting the activities that do not conflict with the previously selected activities. The activity with the earliest finish time is selected first, and the next activity is selected only if its start time is greater than or equal to the finish time of the previously selected activity. This approach ensures that the maximum number of non-conflicting activities is selected.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a structure to represent an activity
struct Activity {
    int start;
    int finish;
};

// Compare function to sort activities based on finish times
bool compareActivities(const Activity &a, const Activity &b) {
    return a.finish < b.finish;
}

// Function to select the maximum number of non-conflicting activities
int selectActivities(Activity activities[], int n) {
    // Sort the activities based on their finish times
    sort(activities, activities + n, compareActivities);

    // Initialize the count of selected activities
    int count = 1;

    // Initialize the finish time of the last selected activity
    int lastFinish = activities[0].finish;

    // Iterate over the sorted activities
    for (int i = 1; i < n; i++) {
        // Check if the current activity does not conflict with the last selected activity
        if (activities[i].start >= lastFinish) {
            // Increment the count of selected activities
            count++;

            // Update the finish time of the last selected activity
            lastFinish = activities[i].finish;
        }
    }

    // Return the count of selected activities
    return count;
}

int main() {
    // Example usage
    Activity activities[] = {{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9}, {6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}};
    int n = sizeof(activities) / sizeof(activities[0]);

    // Select the maximum number of non-conflicting activities
    int count = selectActivities(activities, n);

    // Print the count of selected activities
    cout << "Maximum number of non-conflicting activities: " << count << endl;

    return 0;
}
```

## Test Cases
```
Input: activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
Output: Maximum number of non-conflicting activities: 4
```

## Key Takeaways
- The activity selection problem can be solved using a greedy approach by sorting the activities based on their finish times.
- The activity with the earliest finish time is selected first, and the next activity is selected only if its start time is greater than or equal to the finish time of the previously selected activity.
- The time complexity of the algorithm is O(n log n) due to the sorting step, and the space complexity is O(1) as no extra space is used.