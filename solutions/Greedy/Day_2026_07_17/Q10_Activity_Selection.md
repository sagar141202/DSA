# Activity Selection

## Problem Statement
Given a set of activities, each with a start and finish time, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. The activities are given in the form of pairs (start, finish), where start is the start time of the activity and finish is the finish time of the activity. The goal is to maximize the number of activities that can be performed.

## Approach
The algorithm uses a greedy approach, sorting the activities by their finish times and then selecting the activities with the earliest finish times. This approach ensures that the maximum number of activities can be performed.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a structure to represent an activity
struct Activity {
    int start, finish;
};

// Compare function to sort activities by finish time
bool compare(Activity a, Activity b) {
    return a.finish < b.finish;
}

// Function to select the maximum number of activities
int activitySelection(Activity arr[], int n) {
    // Sort the activities by finish time
    sort(arr, arr + n, compare);

    // Initialize the count of selected activities
    int count = 1;

    // Initialize the finish time of the last selected activity
    int lastFinish = arr[0].finish;

    // Iterate over the activities
    for (int i = 1; i < n; i++) {
        // If the current activity starts after the last selected activity finishes, select it
        if (arr[i].start >= lastFinish) {
            count++;
            lastFinish = arr[i].finish;
        }
    }

    // Return the count of selected activities
    return count;
}

int main() {
    // Example usage
    Activity arr[] = {{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9}, {6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}};
    int n = sizeof(arr) / sizeof(arr[0]);
    cout << "Maximum number of activities: " << activitySelection(arr, n);
    return 0;
}
```

## Test Cases
```
Input: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
Output: 4
```

## Key Takeaways
- The greedy approach is used to solve the activity selection problem.
- The activities are sorted by their finish times to ensure that the maximum number of activities can be performed.
- The time complexity of the solution is O(n log n) due to the sorting step.