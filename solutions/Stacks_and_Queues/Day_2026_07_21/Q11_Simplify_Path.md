# Simplify Path

## Problem Statement
Given an absolute path, simplify it by resolving '..' and '.' in the path. The path is made of directories separated by '/'. '.' represents the current directory, and '..' represents the parent directory. For example, "/home/" and "/../" are equivalent to "/". Also, "/home//foo/" is equivalent to "/home/foo/". The path is guaranteed to start with '/' and only contains letters, '.', and '/'. There will be no '.' or '..' at the beginning of the path.

## Approach
The approach is to use a stack to store the directories in the path. When we encounter '..', we pop the last directory from the stack if it's not empty. When we encounter '.', we skip it. Otherwise, we push the directory to the stack.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string simplifyPath(string path) {
        stack<string> st;
        string res = "";
        for (int i = 0; i < path.length(); i++) {
            if (path[i] == '/') {
                if (res == "..") {
                    if (!st.empty()) st.pop();
                } else if (res != "" && res != ".") {
                    st.push(res);
                }
                res = "";
            } else {
                res += path[i];
            }
        }
        if (res == "..") {
            if (!st.empty()) st.pop();
        } else if (res != "" && res != ".") {
            st.push(res);
        }
        string ans = "";
        while (!st.empty()) {
            ans = "/" + st.top() + ans;
            st.pop();
        }
        if (ans == "") return "/";
        return ans;
    }
};
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
- Use a stack to store the directories in the path.
- Handle '..' and '.' separately to simplify the path.
- The time complexity is O(n) where n is the length of the path, and the space complexity is also O(n) for storing the directories in the stack.