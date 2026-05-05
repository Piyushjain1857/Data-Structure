# DSA Viva Questions with Solutions

**1. What is data?**  
Data is raw facts or values, such as numbers, characters, or observations, that by themselves may not have meaning.

**2. What is information?**  
Information is processed and organized data that becomes meaningful and useful.

**3. Difference between data and information?**  
Data is raw input, while information is the meaningful output obtained after processing data.

**4. What are types of data?**  
Common types include numeric, character, string, boolean, and more complex forms like records or objects.

**5. What is metadata?**  
Metadata is data about data, such as file size, creation date, or data type.

**6. What is a data structure?**  
A data structure is a way of organizing and storing data so it can be accessed and modified efficiently.

**7. Why do we need data structures?**  
They help manage data efficiently, improve performance, and make operations like searching, insertion, and deletion easier.

**8. Types of data structures?**  
Main types are linear data structures and non-linear data structures.

**9. Linear vs Non-linear data structures?**  
In linear structures, elements are arranged sequentially, such as arrays and linked lists. In non-linear structures, elements form hierarchical or network relationships, such as trees and graphs. 

**10. Static vs Dynamic data structures?**  
Static structures have fixed size, while dynamic structures can grow or shrink during execution.

**11. What is an Abstract Data Type (ADT)?**  
An ADT is a logical model that defines data and operations without specifying implementation details.

**12. Difference between ADT and data structure?**  
ADT defines what operations are performed, while a data structure defines how the data is actually stored and implemented.

**13. Examples of ADT?**  
Stack, queue, list, map, and set are common examples.

**14. Why ADT is important?**  
It separates interface from implementation, which improves modularity and flexibility.

**15. What is an algorithm?**  
An algorithm is a finite sequence of well-defined steps to solve a problem.

**16. Characteristics of an algorithm?**  
It should be finite, definite, have input and output, and be effective.

**17. What is pseudocode?**  
Pseudocode is an informal, language-independent way of describing algorithm steps.

**18. What is flowchart?**  
A flowchart is a diagrammatic representation of an algorithm or process using symbols and arrows.

**19. Difference between algorithm and program?**  
An algorithm is the logic or plan, while a program is the actual coded implementation.

**20. What is time complexity?**  
Time complexity measures how running time grows with input size.

**21. What is space complexity?**  
Space complexity measures how much memory an algorithm needs as input size grows.

**22. Best, worst, average case?**  
Best case is the minimum time, worst case is the maximum time, and average case is the expected time for typical inputs.

**23. What is asymptotic notation?**  
It is a mathematical way to describe algorithm growth for large input sizes.

**24. Big-O notation?**  
Big-O gives the upper bound of time or space complexity.

**25. Omega notation?**  
Omega gives the lower bound of complexity.

**26. Theta notation?**  
Theta gives the tight bound, meaning both upper and lower bounds match.

**27. Difference between O(n) and O(log n)?**  
O(n) grows linearly with input size, while O(log n) grows much more slowly and is generally more efficient.

**28. What is constant time complexity?**  
Constant time, O(1), means the execution time does not depend on input size.

**29. What is exponential complexity?**  
Exponential complexity, such as O(2^n), grows very rapidly as input increases.

**30. What is polynomial complexity?**  
Polynomial complexity has the form O(n^k), where k is a constant.

**31. What is amortized complexity?**  
It is the average cost of an operation over a sequence of operations.

**32. What is recursion complexity?**  
It is the time and space cost of recursive calls, including call stack usage.

**33. What is auxiliary space?**  
Auxiliary space is the extra memory used by an algorithm apart from the input data.

**34. What is in-place algorithm?**  
An in-place algorithm uses only a small, constant amount of extra memory.

**35. What is trade-off between time and space?**  
It means reducing time may require more memory, or saving memory may increase running time.

**36. What is complexity of nested loops?**  
It usually depends on how many times the loops run together; for two full loops of size n, it is often O(n^2).

**37. How to analyze recursive functions?**  
Write a recurrence relation for the function and solve it using substitution, recursion tree, or master theorem.

**38. What is master theorem?**  
It is a method to solve recurrences of the form T(n) = aT(n/b) + f(n).

**39. What is logarithmic complexity?**  
Logarithmic complexity, O(log n), means work grows slowly as input size increases, often by repeatedly halving the problem.

**40. Why complexity analysis is important?**  
It helps compare algorithms and choose the most efficient one for large inputs.

**41. What is an array?**  
An array is a collection of elements of the same type stored in contiguous memory locations.

**42. Advantages of array?**  
Arrays allow fast indexed access, simple traversal, and efficient memory usage.

**43. Disadvantages of array?**  
They have fixed size in static form, insertion and deletion can be costly, and they require contiguous memory.

**44. Static vs dynamic array?**  
A static array has fixed size, while a dynamic array can resize during execution.

**45. How memory is allocated in array?**  
Memory is allocated in contiguous blocks, so each element can be accessed by index arithmetic.

**46. What is indexing?**  
Indexing is accessing an element by its position number in the array.

**47. What is contiguous memory?**  
Contiguous memory means elements are stored in adjacent memory locations.

**48. Insertion in array?**  
To insert, elements may need to be shifted right to create space at the target position.

**49. Deletion in array?**  
To delete, elements after the deleted item may need to be shifted left.

**50. Traversal of array?**  
Traversal means visiting each element one by one.

**51. Searching in array?**  
Searching means finding whether an element exists and locating its position.

**52. Updating elements?**  
Updating means changing the value stored at a given index.

**53. Time complexity of insertion?**  
Worst-case insertion in an array is O(n) because elements may need to be shifted.

**54. Time complexity of deletion?**  
Worst-case deletion in an array is O(n) because shifting may be required.

**55. 1D vs 2D array?**  
A 1D array is a linear list, while a 2D array stores elements in rows and columns like a matrix.

**56. What is multidimensional array?**  
It is an array with more than one index, such as 2D or 3D arrays.

**57. Row-major vs column-major order?**  
Row-major stores rows consecutively, while column-major stores columns consecutively.

**58. How to create matrix?**  
A matrix can be created using a 2D array with rows and columns.

**59. Matrix traversal?**  
Matrix traversal means visiting all elements row by row, column by column, or in another pattern.

**60. Row-wise traversal?**  
It visits all columns of one row before moving to the next row.

**61. Column-wise traversal?**  
It visits all rows of one column before moving to the next column.

**62. What is transpose of matrix?**  
Transpose converts rows into columns and columns into rows.

**63. Algorithm for transpose?**  
Swap element at position (i, j) with element at (j, i) for a square matrix.

**64. What is matrix rotation?**  
It is the process of rotating matrix elements by 90°, 180°, or 270°.

**65. Rotate matrix by 90°?**  
One common method is transpose the matrix and then reverse each row for clockwise rotation.

**66. Rotate matrix by 180°?**  
Reverse the order of rows and then reverse each row, or rotate twice by 90°.

**67. What is diagonal traversal?**  
It visits matrix elements along diagonal paths instead of row or column order.

**68. What is sparse matrix?**  
A sparse matrix has mostly zero values and very few non-zero elements.

**69. Representation of sparse matrix?**  
It can be represented using triplet form, linked lists, or compressed row/column storage.

**70. What is identity matrix?**  
An identity matrix is a square matrix with 1s on the main diagonal and 0s elsewhere.

**71. What is symmetric matrix?**  
A symmetric matrix is equal to its transpose.

**72. What is upper triangular matrix?**  
It is a square matrix in which all elements below the main diagonal are zero.

**73. What is lower triangular matrix?**  
It is a square matrix in which all elements above the main diagonal are zero.

**74. Applications of arrays?**  
Arrays are used in matrices, lookup tables, strings, heaps, and implementing other data structures.

**75. What is dynamic resizing?**  
It is the process of increasing or decreasing array capacity when needed.

**76. What is array overflow?**  
Overflow happens when insertion is attempted in a full fixed-size array.

**77. What is array underflow?**  
Underflow happens when deletion is attempted from an empty array or structure.

**78. Difference between array and linked list?**  
Arrays use contiguous memory and fast indexing, while linked lists use nodes and pointers with dynamic size.

**79. What is sliding window technique?**  
It is an optimization technique that processes a subset of consecutive elements by moving a window across data.

**80. What is prefix sum array?**  
A prefix sum array stores cumulative sums so range-sum queries can be answered quickly.

**81. What is linked list?**  
A linked list is a linear data structure made of nodes, where each node stores data and a link to the next node.

**82. Types of linked list?**  
Singly linked list, doubly linked list, and circular linked list.

**83. Node structure?**  
A node usually contains a data field and one or more pointer fields.

**84. Difference between array and linked list?**  
Arrays support direct indexing, while linked lists support easier insertions and deletions at known positions.

**85. Insertion at beginning?**  
Create a new node, point it to the current head, and update head to the new node.

**86. Insertion at end?**  
Traverse to the last node and link the new node after it, or use a tail pointer.

**87. Insertion at position?**  
Traverse to the target position, then adjust pointers to insert the new node.

**88. Deletion at beginning?**  
Move head to the next node and free the old first node.

**89. Deletion at end?**  
Traverse to the second-last node, remove the last node, and set next to null.

**90. Deletion at position?**  
Traverse to the node before the target, change links, and remove the target node.

**91. Traversal?**  
Traversal in a linked list means visiting nodes from head until null.

**92. Searching?**  
Searching means checking nodes one by one until the desired value is found.

**93. What is doubly linked list?**  
A doubly linked list has nodes with pointers to both next and previous nodes.

**94. Advantages over singly linked list?**  
It supports backward traversal and easier deletion of a known node.

**95. Insertion in DLL?**  
Adjust both next and previous pointers of neighboring nodes and the new node.

**96. Deletion in DLL?**  
Relink the previous and next nodes around the target node, then remove it.

**97. What is circular linked list?**  
It is a linked list in which the last node points back to the first node.

**98. Detect loop in linked list?**  
Use Floyd’s cycle detection method with slow and fast pointers.

**99. Reverse a linked list?**  
Iteratively change each node’s next pointer to point to the previous node.

**100. Find middle element?**  
Use slow and fast pointers; when fast reaches the end, slow is at the middle.

**101. Length of linked list?**  
Traverse the list and count the nodes.

**102. Merge two linked lists?**  
Join them by linking the last node of one list to the head of the other, or merge sorted lists by comparing nodes.

**103. What is tail pointer?**  
A tail pointer stores the address of the last node to allow faster insertion at the end.

**104. What is sentinel node?**  
A sentinel node is a dummy node used to simplify boundary cases.

**105. Applications of linked list?**  
They are used in dynamic memory management, stacks, queues, graph adjacency lists, and undo features.

**106. Memory allocation in linked list?**  
Nodes are allocated dynamically and need not be contiguous in memory.

**107. Time complexity of operations?**  
Access by position is O(n); insertion or deletion at the head is O(1); searching is O(n).

**108. What is dynamic memory?**  
Dynamic memory is memory allocated at runtime as needed.

**109. What is pointer?**  
A pointer is a variable that stores the memory address of another variable.

**110. Why linked list is preferred over array?**  
It is preferred when size changes frequently and insertions or deletions are common.

**111. What is stack?**  
A stack is a linear structure that follows the Last In, First Out principle.

**112. LIFO principle?**  
LIFO means the most recently inserted element is removed first.

**113. Push operation?**  
Push adds an element to the top of the stack.

**114. Pop operation?**  
Pop removes and returns the top element of the stack.

**115. Peek operation?**  
Peek returns the top element without removing it.

**116. Stack overflow?**  
It occurs when trying to push into a full stack.

**117. Stack underflow?**  
It occurs when trying to pop from an empty stack.

**118. Implementation using array?**  
Use an array and a top index to track the current top element.

**119. Implementation using linked list?**  
Use the head node as the top so insertion and deletion happen at the front.

**120. Applications of stack?**  
Stacks are used in function calls, recursion, expression evaluation, syntax parsing, and undo operations.

**121. What is queue?**  
A queue is a linear data structure that follows the First In, First Out principle.

**122. FIFO principle?**  
FIFO means the earliest inserted element is removed first.

**123. Enqueue operation?**  
Enqueue inserts an element at the rear of the queue.

**124. Dequeue operation?**  
Dequeue removes an element from the front of the queue.

**125. Types of queue?**  
Simple queue, circular queue, priority queue,Deque (Double Ended Queue)

**126. Circular queue?**  
A circular queue connects the rear to the front so space can be reused efficiently.

**127. Priority queue?**  
A priority queue removes elements based on priority rather than insertion order.

**128. Deque (Double Ended Queue)?**  
A deque is a double-ended queue that allows insertion and deletion at both ends.

**129. Applications of queue?**  
Queues are used in scheduling, buffering, BFS, printers, and customer service systems.

**130. Difference between stack and queue?**  
A stack is LIFO, while a queue is FIFO.

**131. What is double-ended queue?**  
It is another name for deque, where operations are allowed at both front and rear.

**132. What is blocking queue?**  
A blocking queue waits when the queue is empty during removal or full during insertion, often in concurrent programming.

**133. What is queue overflow?**  
Queue overflow occurs when insertion is attempted in a full queue.

**134. Time complexity of operations?**  
Basic queue operations are generally O(1) in efficient implementations.

**135. Real-life examples?**  
Examples include ticket lines, printer jobs, CPU scheduling, and call centers.

**136. What is sorting?**  
Sorting is the process of arranging data in ascending or descending order.

**137. Types of sorting?**  
Common types include bubble sort, selection sort, insertion sort, merge sort, quick sort, heap sort, and counting sort.

**138. Explain selection sort?**  
Selection sort repeatedly finds the minimum element from the unsorted part and places it in the correct position.

**139. Time complexity?**  
Selection sort has O(n^2) time complexity in best, average, and worst cases.

**140. Is it stable?**  
Basic selection sort is not stable.

**141. Explain bubble sort?**  
Bubble sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.

**142. Best case complexity?**  
With optimization, the best case for bubble sort is O(n).

**143. Optimized bubble sort?**  
It stops early if no swaps occur in a pass.

**144. Explain insertion sort?**  
Insertion sort builds the sorted part one element at a time by inserting each item into its correct position.

**145. Best case complexity?**  
Insertion sort has best-case time complexity O(n) when the array is already sorted.

**146. Explain merge sort?**  
Merge sort divides the array into halves, sorts each half recursively, and then merges the sorted halves.

**147. Divide and conquer?**  
It is a strategy of dividing a problem into smaller subproblems, solving them, and combining their results.

**148. Time complexity?**  
Merge sort runs in O(n log n) time.

**149. Space complexity?**  
Merge sort typically uses O(n) extra space.

**150. Explain quick sort?**  
Quick sort chooses a pivot, partitions elements around it, and recursively sorts the subarrays.

**151. Pivot selection?**  
A pivot may be chosen as the first, last, random, or median-like element.

**152. Worst case?**  
Quick sort worst-case time complexity is O(n^2), usually when partitions are highly unbalanced.

**153. What is searching?**  
Searching is the process of finding the location of a target element in a data set.

**154. Linear search?**  
Linear search checks elements one by one until the target is found or the list ends.

**155. Time complexity?**  
Linear search has O(n) worst-case time complexity.

**156. Binary search?**  
Binary search repeatedly divides a sorted array into halves to locate the target.

**157. Preconditions of binary search?**  
The data must be sorted, and random access is preferred.

**158. Iterative vs recursive binary search?**  
Iterative binary search uses a loop, while recursive binary search uses function calls.

**159. Time complexity of binary search?**  
Binary search runs in O(log n) time.

**160. Applications of searching?**  
Searching is used in databases, dictionaries, file systems, and lookup operations.

**161. Interpolation search?**  
Interpolation search estimates the likely position of the target in uniformly distributed sorted data.

**162. Jump search?**  
Jump search skips blocks of elements and then performs linear search in the identified block.

**163. What is hashing?**  
Hashing maps keys to indexes using a hash function for fast access.

**164. What is collision?**  
A collision occurs when two different keys map to the same hash index.

**165. Load factor in hashing?**  
Load factor is the ratio of stored elements to total table size.

**166. What is tree?**  
A tree is a hierarchical data structure made of nodes connected by edges.

**167. Root node?**  
The root is the topmost node of a tree.

**168. Leaf node?**  
A leaf node is a node with no children.

**169. Height of tree?**  
The height is the number of edges on the longest path from root to a leaf.

**170. Depth of tree?**  
Depth usually means the number of edges from the root to a specific node; the depth of the root is 0.

**171. Degree of node?**  
The degree of a node is the number of children it has.

**172. What is subtree?**  
A subtree is a tree formed by a node and all of its descendants.

**173. What is binary tree?**  
A binary tree is a tree in which each node has at most two children.

**174. Types of binary tree?**  
Common types are full, complete, perfect, balanced, and skewed binary trees.

**175. Full vs complete binary tree?**  
In a full binary tree, each node has either 0 or 2 children. In a complete binary tree, all levels are filled except possibly the last, which is filled from left to right.

**176. Inorder traversal?**  
Visit left subtree, root, then right subtree.

**177. Preorder traversal?**  
Visit root, then left subtree, then right subtree.

**178. Postorder traversal?**  
Visit left subtree, right subtree, then root.

**179. Level order traversal?**  
Visit nodes level by level from top to bottom, usually using a queue.

**180. What is Binary Search Tree?**  
A BST is a binary tree where left subtree values are smaller and right subtree values are larger than the root.

**181. Properties of BST?**  
For every node, keys in the left subtree are smaller, keys in the right subtree are larger, and both subtrees are also BSTs.

**182. Insertion in BST?**  
Compare the new value with current nodes and place it in the correct left or right null position.

**183. Deletion in BST?**  
Delete a node by handling one of three cases: leaf node, one child, or two children using inorder successor or predecessor.

**184. Searching in BST?**  
Compare the target with the current node and move left or right accordingly.

**185. What is heap?**  
A heap is a complete binary tree that satisfies the heap property.

**186. Max heap vs Min heap?**  
In a max heap, the parent is greater than or equal to children. In a min heap, the parent is smaller than or equal to children.

**187. Heap property?**  
The parent node must follow the ordering rule relative to its children.

**188. Heapify?**  
Heapify is the process of restoring heap property in a tree or array representation.

**189. Applications of heap?**  
Heaps are used in priority queues, heap sort, scheduling, and graph algorithms like Dijkstra’s algorithm.

**190. What is graph?**  
A graph is a set of vertices and edges representing relationships between entities.

**191. Types of graph?**  
Graphs can be directed, undirected, weighted, unweighted, cyclic, acyclic, connected, or disconnected.

**192. Directed vs undirected graph?**  
Directed graphs have edges with direction, while undirected graphs have edges without direction.

**193. Weighted graph?**  
A weighted graph assigns values or costs to edges.

**194. What is adjacency matrix?**  
It is a 2D matrix where each cell indicates whether an edge exists between two vertices.

**195. What is adjacency list?**  
It is a representation where each vertex stores a list of its neighboring vertices.

**196. What is BFS?**  
Breadth-First Search visits nodes level by level using a queue.

**197. What is DFS?**  
Depth-First Search explores as far as possible along one path before backtracking.

**198. Difference between BFS and DFS?**  
BFS uses a queue and explores by levels, while DFS uses a stack or recursion and explores depth first.

**199. Applications of graph?**  
Graphs are used in social networks, maps, routing, recommendation systems, dependency analysis, and communication networks.

**200. What is cycle in graph?**  
A cycle is a path that starts and ends at the same vertex without repeating edges unnecessarily.
