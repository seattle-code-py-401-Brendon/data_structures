# Challenge Summary
<!-- Description of the challenge -->

## Links and Resources
<!-- Embedded whiteboard image -->
![WhiteBoard](#)

### Link To Code
<!-- Link to code solution file -->
[Solution](./hashtable.py)

### Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Im not sure about efficiency, I think they are not even O(n), the get method might be O(1)

### Solution
<!-- Show how to run your code, and examples of it in action -->

I used while loops to iterate through the list of linked list nodes to find the keys. I thnk my get method needs so me rework as it only is looking at the head and I need to make it so it is checking for the key exactly and not just at the index location

### Tests
<!-- test names and what they test for -->
1. def test_keys_apple():
    - tests for all the keys
2. def test_xfail_keys():
    - expected failure
3. def test_edge_case():
    - tests for if integers are being used
4. def test_contains_apple():
    - tests for if it contains apple. 
