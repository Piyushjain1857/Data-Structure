# Data Structure -- Exam Notes

## 1. Basics of Data Structure

### Meaning

A Data Structure is a way of organizing, storing, and managing data in a
computer so that it can be used efficiently.

### Definition

A Data Structure is a method of organizing data in computer memory so
that it can be accessed and modified efficiently.

### Need of Data Structures

-   Handle large data efficiently
-   Reduce time and memory usage
-   Improve program performance

### Types of Data Structures

**Primitive Data Structures** - Integer - Float - Character - Boolean

**Non‑Primitive Data Structures**

Linear - Array - Linked List - Stack - Queue

Non‑Linear - Tree - Graph

------------------------------------------------------------------------

## 2. Basics of ADT (Abstract Data Type)

### Meaning

An Abstract Data Type (ADT) is a logical description of a data structure
that specifies what operations can be performed without describing how
they are implemented.

### Definition

An ADT is a mathematical model that defines the data and the operations
that can be performed on that data.

### Example: Stack ADT

Operations: - Push - Pop - Peek - IsEmpty

### ADT vs Data Structure

  ADT             Data Structure
  --------------- -------------------------
  Logical model   Physical implementation

------------------------------------------------------------------------

## 3. Big-O (Time and Space Complexity)

Big-O notation measures the efficiency of algorithms.

### Time Complexity

Measures how long an algorithm takes to run.

Example: Linear search worst case → **O(n)**

### Space Complexity

Measures how much memory an algorithm uses.

### Common Big-O Complexities

-   **O(1)** -- Constant time
-   **O(log n)** -- Logarithmic
-   **O(n)** -- Linear
-   **O(n log n)** -- Efficient sorting
-   **O(n²)** -- Quadratic

### Operation vs Time Complexity

  Operation / Algorithm               Time Complexity   Example Usage
  ----------------------------------- ----------------- -------------------------------
  Access element in array             O(1)              arr\[i\] direct access
  Stack Push / Pop                    O(1)              Insert/remove from top
  Queue Enqueue / Dequeue             O(1)              Insert/remove in queue
  Binary Search                       O(log n)          Searching in sorted array
  Array Traversal                     O(n)              Visiting every element
  Linked List Traversal               O(n)              Moving from head to last node
  Linear Search                       O(n)              Sequential search
  Merge Sort / Quick Sort (average)   O(n log n)        Efficient sorting
  Bubble Sort / Selection Sort        O(n²)             Comparing elements
  Generating all subsets              O(2ⁿ)             Recursion problems

------------------------------------------------------------------------

## 4. Array and Matrix

### Array Definition

An array is a collection of elements of the same data type stored in
contiguous memory locations.

Example

    A = [10, 20, 30, 40]

### Characteristics

-   Fixed size
-   Same data type
-   Indexed access
-   Continuous memory storage

### Matrix

A matrix is a two-dimensional array.

Example

    [
     [1,2,3],
     [4,5,6]
    ]

### Applications

-   Graph representation
-   Image processing
-   Scientific computing

------------------------------------------------------------------------

## 5. Linked List ADT

### Definition

A linked list is a linear data structure where elements are stored in
nodes and connected using pointers.

Each node contains: - Data - Address of next node

Example

    10 → 20 → 30 → 40

### Types

-   Singly Linked List
-   Doubly Linked List
-   Circular Linked List

### Advantages

-   Dynamic size
-   Easy insertion and deletion

### Disadvantages

-   Extra memory for pointers
-   Sequential access only

------------------------------------------------------------------------

## 6. Stack ADT

### Definition

A stack is a linear data structure that follows **LIFO (Last In First
Out)**.

### Operations

-   Push -- insert element
-   Pop -- remove element
-   Peek -- view top element
-   IsEmpty -- check if stack is empty

### Applications

-   Function calls
-   Expression evaluation
-   Undo operations

------------------------------------------------------------------------

## 7. Queue ADT

### Definition

A queue is a linear data structure that follows **FIFO (First In First
Out)**.

### Operations

-   Enqueue -- insert element
-   Dequeue -- remove element
-   Front -- first element
-   Rear -- last element

### Applications

-   CPU scheduling
-   Printer queue
-   Network buffering

------------------------------------------------------------------------

## 8. Difference Between Stack, Queue, Linked List

  -----------------------------------------------------------------------
  Feature           Stack             Queue             Linked List
  ----------------- ----------------- ----------------- -----------------
  Definition        Insert/remove     Insert rear       Nodes connected
                    from same end     remove front      with pointers

  Principle         LIFO              FIFO              No fixed
                                                        principle

  Main Operations   Push, Pop, Peek   Enqueue, Dequeue  Insertion,
                                                        Deletion

  Access Method     Only top          Front to rear     Traversal from
                    accessible                          head

  Memory Structure  Array or linked   Array or linked   Nodes with
                    list              list              pointers

  Insertion         Top               Rear              Anywhere

  Deletion          Top               Front             Anywhere

  Applications      Undo, recursion   Scheduling,       Dynamic
                                      queues            structures
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 9. Basics of List, Tuple, Dictionary (Python)

### List

Ordered collection of elements.

Example

``` python
A = [10, 20, 30]
```

-   Mutable
-   Allows duplicates

### Tuple

Immutable collection.

``` python
T = (10, 20, 30)
```

### Dictionary

Key‑value pair storage.

``` python
student = {
 "name": "Piyush",
 "age": 18
}
```

-   Keys are unique
-   Fast lookup
