# Trees
<!-- Short summary or background information -->

### Challenge
<!-- Description of the challenge -->
Branch Name: trees

Challenge Type: New Implementation

Features
<ul>
<li>
<li style="color:yellow">Node</li>

Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
<li style="color:green">Binary Tree
<ul>
Create a Binary Tree class
Define a method for each of the depth first traversals:
  which returns an array of the values, ordered appropriately.
  <li>pre-order</li>
  <li>in order</li>
  <li>post order</li>
</ul>
</li>

<li style="color:lightgreen">Binary Search Tree
<ul>
<li>Create a Binary Search Tree class</li>
  This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
<li>Add</li>
  Arguments: value
Return: nothing
  Adds a new node with that value in the correct location in the binary search tree.
<li>Contains</li>
  Argument: value
  Returns: boolean indicating whether or not the value is in the tree at least once.
</ul>
</li>
</ul>

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The big O is O(n) because we dont know how many nodes are in the tree. The space and time is reflective of the number of nodes
## API
<!-- Description of each method publicly available in each of your trees -->
Binary Tree
  - pre_order
    - returns a list ROOT--->LEFT--->RIGHT
  - in_order
    - returns a list LEFT--->ROOT--->RIGHT
  - post_order
    - returns a list LEFT--->RIGHT--->ROOT

BST
   - Add
     - adds a new node left for smaller, right for larger
   - Contains
     - Checks if a value is present in the Tree, If smaller, check left, if larger check right, return False if does not exist
