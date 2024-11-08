
<!DOCTYPE html>
<html lang="en">
  <body>
  <h1>Radix Sort</h1>
  <div class="panel-body text-justify">
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
<li>Unless specified otherwise, you are not allowed to use the standard library. Any use of functions like <em>printf, puts, &hellip;</em> is totally forbidden.</li>
<li>In the following examples, the <code>main.c</code> files are shown as examples. You can use them to test your functions, but you don&rsquo;t have to push them to your repo (if you do we won&rsquo;t take them into account). We will use our own <code>main.c</code> files at compilation. Our <code>main.c</code> files might be different from the one shown in the examples</li>
<li>The prototypes of all your functions should be included in your header file called <code>sort.h</code></li>
<li>Don&rsquo;t forget to push your header file</li>
<li>All your header files should be include guarded</li>
<li>A list/array does not need to be sorted if its size is less than 2.</li>
</ul>

<h2>More Info</h2>

<p>For this project you are given the following <code>print_array</code> function:</p>

<pre><code>alexa@ubuntu-xenial:radix_sort$ cat `print_array.c`
#include &lt;stdlib.h&gt;
#include &lt;stdio.h&gt;

/**
 * print_array - Prints an array of integers
 *
 * @array: The array to be printed
 * @size: Number of elements in @array
 */
void print_array(const int *array, size_t size)
{
    size_t i;

    i = 0;
    while (array &amp;&amp; i &lt; size)
    {
        if (i &gt; 0)
            printf(&quot;, &quot;);
        printf(&quot;%d&quot;, array[i]);
        ++i;
    }
    printf(&quot;\n&quot;);
}
alexa@ubuntu-xenial:radix_sort$
</code></pre>

<ul>
<li>Our file <code>print_array.c</code> will be compiled with your function during the correction.</li>
<li>Please declare the prototype of the function <code>print_array</code> in your <code>sort.h</code> header file</li>
</ul>

  </div>
</div>
        </div>
      </div>
    </div>

<h2 id="task-container" class="gap">Tasks</h2>
  
  <div class="col-sm-12 col-md-12 col-lg-8 xol-xl-9">
      <div data-role="task21120" data-position="38" id="task-num-0">
        <div class="panel panel-default task-card " id="task-21120">

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Radix sort
    </h3>

  </div>

  <div class="panel-body">

<!-- Progress vs Score -->

<!-- Task Body -->
<p>Write a function that sorts an array of integers in ascending order using the <a href="https://en.wikipedia.org/wiki/Radix_sort" title="Radix sort" target="_blank">Radix sort</a> algorithm</p>

<ul>
<li>Prototype: <code>void radix_sort(int *array, size_t size);</code></li>
<li>You must implement the <code>LSD</code> radix sort algorithm</li>
<li>You can assume that <code>array</code> will contain only numbers <code>&gt;= 0</code></li>
<li>You are allowed to use <code>malloc</code> and <code>free</code> for this task</li>
<li>You&rsquo;re expected to print the <code>array</code> each time you increase your <code>significant digit</code> (See example below)</li>
</ul>

<pre><code>alexa@ubuntu-xenial:radix_sort$ cat 0-main.c
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &quot;sort.h&quot;

/**
 * main - Entry point
 *
 * Return: Always 0
 */
int main(void)
{
    int array[] = {19, 48, 99, 71, 13, 52, 96, 73, 86, 7};
    size_t n = sizeof(array) / sizeof(array[0]);

    print_array(array, n);
    printf(&quot;\n&quot;);
    radix_sort(array, n);
    printf(&quot;\n&quot;);
    print_array(array, n);
    return (0);
}
alexa@ubuntu-xenial:radix_sort$ gcc -Wall -Wextra -Werror -pedantic 0-main.c 0-radix_sort.c print_array.c -o radix
alexa@ubuntu-xenial:radix_sort$ ./radix
19, 48, 99, 71, 13, 52, 96, 73, 86, 7

71, 52, 13, 73, 96, 86, 7, 48, 19, 99
7, 13, 19, 48, 52, 71, 73, 86, 96, 99

7, 13, 19, 48, 52, 71, 73, 86, 96, 99
alexa@ubuntu-xenial:radix_sort$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-interview</code></li>
    <li>Directory: <code>radix_sort</code></li>
    <li>File: <code>0-radix_sort.c</code></li>
</ul>
</div>

<!-- Self-paced manual review -->
  </div>

      
</body>
</html>
