# Simplify Path

## Problem Statement
Given an absolute path, simplify it by resolving '..' and '.' in the path. The function should take a string path as input and return a string representing the simplified path. For example, "/home/" should be simplified to "/home", "/../" should be simplified to "/", and "/home//foo/" should be simplified to "/home/foo". The path will not contain any files or directories with '.' or '..' in their names.

## Approach
We will use a stack to store the directories in the path. When we encounter '..', we pop the last directory from the stack if it is not empty. When we encounter '.', we skip it. Otherwise, we push the directory into the stack.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

string simplifyPath(string path) {
    // Split the path into directories
    stringstream ss(path);
    string dir;
    vector<string> dirs;
    while (getline(ss, dir, '/')) {
        if (dir != "" && dir != ".") {
            dirs.push_back(dir);
        }
    }

    // Use a stack to store the directories
    stack<string> st;
    for (const auto& dir : dirs) {
        if (dir == "..") {
            if (!st.empty()) {
                st.pop();
            }
        } else {
            st.push(dir);
        }
    }

    // Build the simplified path
    string simplifiedPath;
    while (!st.empty()) {
        simplifiedPath = "/" + st.top() + simplifiedPath;
        st.pop();
    }

    // If the path is empty, return "/"
    if (simplifiedPath == "") {
        return "/";
    } else {
        return simplifiedPath;
    }
}
```

## Test Cases
```
Input: "/home/"
Output: "/home"
Input: "/../"
Output: "/"
Input: "/home//foo/"
Output: "/home/foo"
```

## Key Takeaways
- Use a stack to store the directories in the path
- Resolve '..' and '.' in the path by popping or skipping them
- Build the simplified path by concatenating the directories in the stack