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
Write a function, in C, that checks if a singly linked list has a cycle in it.
    - ***Prototype***: `int check_cycle(listint_t *list)`
    - ***Return***: `0 if there is no cycle, 1 if there is a cycle`
  
## Palindrome integer
Write, in C, a function that checks whether or not a given unsigned integer is a palindrome.
    - ***Prototype***: `int is_palindrome(unsigned long n)`
    - ***Return***: `1 if n is a palindrome, and 0 otherwise`
    - You are not allowed to allocate memory dynamically (malloc, calloc, …)

## UTF-8 Validation
Write a method that determines if a given data set represents a valid UTF-8 encoding.
    - ***Prototype***: `def validUTF8(data)`
    - ***Return***: `True if data is a valid UTF-8 encoding, else return False`
  
## Menger sponge
Write a C function that draws a 2D Menger Sponge
    - ***Prototype***: `void menger(int level)`
    - Where `level` is the level of the Menger Sponge to draw
    - If `level` is lower than `0`, your function must do nothing
  
## Linear search in skip list
Write a function that searches for a value in a sorted skip list of integers, in C.
- ***Prototype***: `skiplist_t *linear_skip(skiplist_t *list, int value)`
- Where `list` is a pointer to the head of the skip list to search in
- ***Return***: `a pointer on the first node where value is located`

## Star Wars API
Write a JS script that prints all characters of a Star Wars movie:
- The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
- Display one character name per line in the same order as the “characters” list in the /films/ endpoint

## Rain
Given a list of non-negative integers representing the heights of walls with unit width 1, as if viewing the cross-section of a relief map, calculate in Python how many square units of water will be retained after it rains.
- ***Prototype***: `def rain(walls)`
- ***Return***: `Integer indicating total amount of rainwater retained`

## Heap sort
Write a function that sorts an array of integers in ascending order using the heap sort algorithm.
- ***Prototype***: `void heap_sort(int *array, size_t size)`
- You must implement the sift-down heap sort algorithm
- You’re expected to print the array after each time you swap two elements

## Advanced binary search
Write a function that searches for a value in a sorted array of integers.
- ***Prototype***: `int advanced_binary(int *array, size_t size, int value)`
- ***Return***: `The index where value is located, or -1`

## Count it!
Write a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords.
- ***Prototype***: `def count_words(subreddit, word_list)`
- ***Return***: `Results printed in descending order, by the count`

## Heap Extract
Write a C function that extracts the root node of a Max Binary Heap:
- ***Prototype***: `int heap_extract(heap_t **root)`
- ***Return***: `int value stored in the root node, or O for fail`

