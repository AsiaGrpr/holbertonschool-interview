<div align="center">

# HolbertonSchool Interview 

![image](./asset/img/algorythms.jpeg)

</div>

---

In this folder, there will be added the algorithm projects carried out during the second year of our Fullstack specialization at holberton school. Theses are algorithm projects in order to be prepared for technicals interview.

---

## Lockboxes:
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened. (python)

## Insert_in_sorted_linked_list:
Write a function in C that inserts a number into a sorted singly linked list.

    - **Prototype**: `listint_t *insert_node(listint_t **head, int number)`;  
    - **Return**:  `the address of the new node, or NULL if it failed`
  
## Heap Insert:
Write a function in C that creates a binary tree node:

    - **Prototype**: `binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)`;  
    - **Return**:  `a pointer to the new node, or NULL if it failed`;

Write a function in C that inserts a value into a Max Binary Heap:

    - **Prototype**: `heap_t *heap_insert(heap_t **root, int value)`;  
    - **Return**:  `the address of the inserted node, or NULL if it failed`;

## Minimum operations:
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file. Be smart about how you utilize the memory! (python)

## Sandpiles
Write a function in C that computes the sum of two sandpiles

    - **Prototype**: `void sandpiles_sum(int grid1[3][3], int grid2[3][3])`;
    - Each element of the grid represents the number of sand grains in that cell. Adding the sandpiles must be done according to specific rules, and the final result should be a stable sandpile.

## Linked list palindrome
Write a function in C that checks if a singly linked list is a palindrome.

    - **Prototype**: `int is_palindrome(listint_t **head)`;
    - **Return**: `0 if it is not a palindrome, 1 if it is a palindrome`
    - An empty list is considered a palindrome

## Log parsing
Write a Python script that reads stdin line by line and computes metrics.

    - Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (if the format is not this one, the line must be skipped)
    - After every 10 lines and/or a keyboard interruption (`CTRL + C`), print these statistics from the beginning: 
      - Total file size: `File size: <total size>`.
      - Number of lines by status code in ascending order.

## 2048 (single line)
The goal of this task is to reproduce the 2048 game(NSFW !!) mechanics on a single horizontal line.

Write a function that slides and merges an array of integers.
    - **Prototype**: `int slide_line(int *line, size_t size, int direction)`
    - **Return**: `1 if the operation was successful, 0 if it failed`
    - `direction` is either `SLIDE_LEFT` or `SLIDE_RIGHT`

## Nqueen
The N queens puzzle is the python challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

## Array to AVL
Write, in C, a function that builds an AVL tree from an array
    - **Prototype**: `avl_t *sorted_array_to_avl(int *array, size_t size)`
    - **Return**: `a pointer to the root node of the created AVL tree, or NULL on failure`
    - `array` is a pointer to the first element of the array to be converted

## Linked list cycle
Write a function in C that checks if a singly linked list has a cycle in it.
    - ***Prototype***: `int check_cycle(listint_t *list)`
    - ***Return***: `0 if there is no cycle, 1 if there is a cycle`
  
