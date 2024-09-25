
<!DOCTYPE html>
<html lang="en">
  <body>
<div id="project_id" style="display: none" data-project-id="2274"></div>


<h1> Heap Extract </h1>
      

      

<div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be compiled on Ubuntu 14.04 LTS</li>
<li>Your programs and functions will be compiled with <code>gcc 4.8.4</code> using the flags <code>-Wall</code> <code>-Werror</code> <code>-Wextra</code> and <code>-pedantic</code></li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>Betty</code> style. It will be checked using <a href="https://github.com/hs-hq/Betty/blob/master/betty-style.pl" title="betty-style.pl" target="_blank">betty-style.pl</a> and <a href="https://github.com/hs-hq/Betty/blob/master/betty-doc.pl" title="betty-doc.pl" target="_blank">betty-doc.pl</a></li>
<li>You are not allowed to use global variables</li>
<li>No more than 5 functions per file</li>
<li>You are allowed to use the standard library</li>
<li>In the following examples, the <code>main.c</code> files are shown as examples. You can use them to test your functions, but you don&rsquo;t have to push them to your repo (if you do we won&rsquo;t take them into account). We will use our own <code>main.c</code> files at compilation. Our <code>main.c</code> files might be different from the one shown in the examples</li>
<li>The prototypes of all your functions should be included in your header file called <code>binary_trees.h</code></li>
<li>Don&rsquo;t forget to push your header file</li>
<li>All your header files should be include guarded</li>
</ul>

<h2>More Info</h2>

<h3>Data structures</h3>

<p>Please use the following data structures and types for binary trees. Don&rsquo;t forget to include them in your header file.</p>

<h4>Basic Binary Tree</h4>

<pre><code>/**
 * struct binary_tree_s - Binary tree node
 *
 * @n: Integer stored in the node
 * @parent: Pointer to the parent node
 * @left: Pointer to the left child node
 * @right: Pointer to the right child node
 */
struct binary_tree_s
{
    int n;
    struct binary_tree_s *parent;
    struct binary_tree_s *left;
    struct binary_tree_s *right;
};

typedef struct binary_tree_s binary_tree_t;
</code></pre>

<h4>Max Binary Heap</h4>

<pre><code>typedef struct binary_tree_s heap_t;
</code></pre>

<h3>Print function</h3>

<p>To match the examples in the tasks, you are given <a href="https://github.com/hs-hq/0x1C.c" title="this function" target="_blank">this function</a></p>

<p>This function is used only for visualization purposes. You don&rsquo;t have to push it to your repo. It may not be used during the correction.</p>

  </div>
</div>


      

      

        
<h2 class="gap">Tasks</h2>

<div>
     <div>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Heap - Extract
    </h3>

  </div>

  <div class="panel-body">

<!-- Progress vs Score -->

<!-- Task Body -->
<p>Write a function that extracts the root node of a Max Binary Heap:</p>

<ul>
<li>Prototype: <code>int heap_extract(heap_t **root);</code></li>
<li><code>root</code> is a double pointer to the root node of the heap</li>
<li>Your function must return the value stored in the root node</li>
<li>The root node must be freed and replace with the last <code>level-order</code> node of the heap</li>
<li>Once replaced, the heap must be rebuilt if necessary</li>
<li>If your function fails, return <code>0</code></li>
</ul>

<p>Note: In order for the main file to compile, you are provided with <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-low_level_programming/466/libheap.a" title="this static library" target="_blank">this static library</a>. This library won&rsquo;t be used during correction, its only purpose is for testing.</p>

<pre><code>alex@/tmp/binary_trees$ cat 0-main.c
#include &lt;stdlib.h&gt;
#include &lt;stdio.h&gt;

#include &quot;binary_trees.h&quot;

/*
 * The following are helpers functions needed in this main file
 * You don&#39;t need them in your `heap_extract function`.
 */
heap_t *_array_to_heap(int *array, size_t size);
void binary_tree_print(const binary_tree_t *tree);
void _binary_tree_delete(binary_tree_t *tree);

/**
 * main - Entry point
 *
 * Return: 0 on success, error code on failure
 */
int main(void)
{
    heap_t *tree;
    int array[] = {
        79, 47, 68, 87, 84, 91, 21, 32, 34, 2,
        20, 22, 98, 1, 62, 95
    };
    size_t n = sizeof(array) / sizeof(array[0]);
    int extract;

    tree = _array_to_heap(array, n);
    if (!tree)
        return (1);
    binary_tree_print(tree);

    extract = heap_extract(&amp;tree);
    printf(&quot;Extracted: %d\n&quot;, extract);
    binary_tree_print(tree);

    extract = heap_extract(&amp;tree);
    printf(&quot;Extracted: %d\n&quot;, extract);
    binary_tree_print(tree);

    extract = heap_extract(&amp;tree);
    printf(&quot;Extracted: %d\n&quot;, extract);
    binary_tree_print(tree);
    _binary_tree_delete(tree);
    return (0);
}
alex@/tmp/binary_trees$ gcc -Wall -Wextra -Werror -pedantic -o 0-heap_extract 0-main.c 0-heap_extract.c binary_tree_print.c -L. -lheap
alex@/tmp/binary_trees$ valgrind ./0-heap_extract
==29133== Memcheck, a memory error detector
==29133== Copyright (C) 2002-2013, and GNU GPL&#39;d, by Julian Seward et al.
==29133== Using Valgrind-3.10.1 and LibVEX; rerun with -h for copyright info
==29133== Command: ./0-heap_extract
==29133== 
                      .-----------------(098)-----------------.
            .-------(095)-------.                   .-------(091)-------.
       .--(084)--.         .--(079)--.         .--(087)--.         .--(062)--.
  .--(047)     (034)     (002)     (020)     (022)     (068)     (001)     (021)
(032)
Extracted: 98
                 .-----------------(095)-----------------.
       .-------(084)-------.                   .-------(091)-------.
  .--(047)--.         .--(079)--.         .--(087)--.         .--(062)--.
(032)     (034)     (002)     (020)     (022)     (068)     (001)     (021)
Extracted: 95
                 .-----------------(091)-----------------.
       .-------(084)-------.                   .-------(087)-------.
  .--(047)--.         .--(079)--.         .--(068)--.         .--(062)
(032)     (034)     (002)     (020)     (022)     (021)     (001)
Extracted: 91
                 .-----------------(087)-----------------.
       .-------(084)-------.                   .-------(068)--.
  .--(047)--.         .--(079)--.         .--(022)--.       (062)
(032)     (034)     (002)     (020)     (001)     (021)
==29133== 
==29133== HEAP SUMMARY:
==29133==     in use at exit: 0 bytes in 0 blocks
==29133==   total heap usage: 213 allocs, 213 frees, 9,063 bytes allocated
==29133== 
==29133== All heap blocks were freed -- no leaks are possible
==29133== 
==29133== For counts of detected and suppressed errors, rerun with: -v
==29133== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
alex@/tmp/binary_trees$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-interview</code></li>
     <li>Directory: <code>heap_extract</code></li>
     <li>File: <code>0-heap_extract.c</code></li>
</ul>
</div>

<!-- Self-paced manual review -->
  </div>

</body>
</html>
