<!DOCTYPE html>
<html lang="en">
<body>
<div class="project row">
  <div class="col-xs-12 col-md-10 col-lg-8 contains-images">
<h1>Advanced binary search</h1>
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
<li>You are only allowed to use the <code>printf</code> function of the standard library. Any call to another function like <code>strdup</code>, <code>malloc</code>, &hellip; is forbidden.</li>
<li>In the following examples, the <code>main.c</code> files are shown as examples. You can use them to test your functions, but you don&rsquo;t have to push them to your repo (if you do we won&rsquo;t take them into account). We will use our own <code>main.c</code> files at compilation. Our <code>main.c</code> files might be different from the one shown in the examples</li>
<li>The prototypes of all your functions should be included in your header file called <code>search_algos.h</code></li>
<li>Don&rsquo;t forget to push your header file</li>
<li>Your header file should be include guarded</li>
</ul>

  </div>
</div>


      

      

        
<h2 class="gap">Tasks</h2>

<div>
<div>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Advanced Binary Search
    </h3>

  </div>

  <div class="panel-body">
<!-- Task Body -->
<p>You may have noticed that basic binary search does not necessarily return the index of the <em>first</em> value in the array (if this value appears more than once in the array).
In this exercise, you&rsquo;ll have to solve this problem.</p>

<p>Write a function that searches for a value in a sorted array of integers.</p>

<ul>
<li>Prototype : <code>int advanced_binary(int *array, size_t size, int value);</code></li>
<li><code>array</code> is a pointer to the first element of the array to search in</li>
<li><code>size</code> is the number of elements in <code>array</code></li>
<li><code>value</code> is the value to search for</li>
<li>Your function must return the index where <code>value</code> is located</li>
<li>You can assume that <code>array</code> will be sorted in ascending order</li>
<li>If <code>value</code> is not present in <code>array</code> or if <code>array</code> is <code>NULL</code>, your function must return <code>-1</code></li>
<li>Every time you split the array, you have to print the new array (or subarray) you&rsquo;re searching in (See example)</li>
<li>You have to use recursion. You may only use one loop (<code>while</code>, <code>for</code>, <code>do while</code>, etc.) in order to print the array</li>
</ul>

<pre><code>wilfried@0x1D-search_algorithms$ cat 0-main.c 
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &quot;search_algos.h&quot;

/**
 * main - Entry point
 *
 * Return: Always EXIT_SUCCESS
 */
int main(void)
{
    int array[] = {
        0, 1, 2, 5, 5, 6, 6, 7, 8, 9
    };
    size_t size = sizeof(array) / sizeof(array[0]);

    printf(&quot;Found %d at index: %d\n\n&quot;, 8, advanced_binary(array, size, 8));
    printf(&quot;Found %d at index: %d\n\n&quot;, 5, advanced_binary(array, size, 5));
    printf(&quot;Found %d at index: %d\n&quot;, 999, advanced_binary(array, size, 999));
    return (EXIT_SUCCESS);
}
wilfried@0x1D-search_algorithms$ gcc -Wall -Wextra -Werror -pedantic 0-main.c 0-advanced_binary.c -o 0-advanced_binary
wilfried@0x1D-search_algorithms$ ./0-advanced_binary
Searching in array: 0, 1, 2, 5, 5, 6, 6, 7, 8, 9
Searching in array: 6, 6, 7, 8, 9
Searching in array: 8, 9
Found 8 at index: 8

Searching in array: 0, 1, 2, 5, 5, 6, 6, 7, 8, 9
Searching in array: 0, 1, 2, 5, 5
Searching in array: 5, 5
Found 5 at index: 3

Searching in array: 0, 1, 2, 5, 5, 6, 6, 7, 8, 9
Searching in array: 6, 6, 7, 8, 9
Searching in array: 8, 9
Searching in array: 9
Found 999 at index: -1
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-interview</code></li>
    <li>Directory: <code>advanced_binary_search</code></li>
    <li>File: <code>0-advanced_binary.c</code></li>
</ul>
</div>

<!-- Self-paced manual review -->
  </div>

</body>
</html>
