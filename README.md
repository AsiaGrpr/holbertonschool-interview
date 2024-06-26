<div align="center">

# HolbertonSchool Interview 

![image](./asset/img/algorythms.jpeg)

</div>

---

In this folder, there will be added the algorithm projects carried out during the second year of our Fullstack specialization at holberton school. Theses are algorithm projects in order to be prepared for technicals interview.

---

## 1 - Lockboxes:
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened. (python)

## 2- Insert_in_sorted_linked_list:
Write a function in C that inserts a number into a sorted singly linked list.

    - **Prototype**: `listint_t *insert_node(listint_t **head, int number)`;  
    - **Return**:  `the address of the new node, or NULL if it failed`
  
## 3- Heap Insert:
Write a function in C that creates a binary tree node:

    - **Prototype**: `binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)`;  
    - **Return**:  `a pointer to the new node, or NULL if it failed`;

Write a function in C that inserts a value into a Max Binary Heap:

    - **Prototype**: `heap_t *heap_insert(heap_t **root, int value)`;  
    - **Return**:  `the address of the inserted node, or NULL if it failed`;

## 4- Minimum operations:
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file. Be smart about how you utilize the memory! (python)

## 5- Sandpiles
Write a function in C that computes the sum of two sandpiles

    - **Prototype**: `void sandpiles_sum(int grid1[3][3], int grid2[3][3])`;
    - Each element of the grid represents the number of sand grains in that cell. Adding the sandpiles must be done according to specific rules, and the final result should be a stable sandpile.

## 6- Linked list cycle
Write a function in C that checks if a singly linked list is a palindrome.

    - **Prototype**: `int is_palindrome(listint_t **head)`;
    - **Return**: `0 if it is not a palindrome, 1 if it is a palindrome`
    - An empty list is considered a palindrome

## 7- Log parsing
Write a Python script that reads stdin line by line and computes metrics.

    - Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (if the format is not this one, the line must be skipped)
    - After every 10 lines and/or a keyboard interruption (`CTRL + C`), print these statistics from the beginning: 
      - Total file size: `File size: <total size>`.
      - Number of lines by status code in ascending order.
