
<!DOCTYPE html>
<html lang="en">
  <body>
  <h1>Find the Loop</h1>
  <div class="panel-body text-justify">
    <h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be compiled on Ubuntu 14.04 LTS</li>
<li>Your programs and functions will be compiled with <code>gcc 4.8.4</code> using the flags <code>-Wall</code> <code>-Werror</code> <code>-Wextra</code> <code>and -pedantic</code></li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project is mandatory</li>
<li>Your code should use the <code>Betty</code> style. It will be checked using <a href="https://github.com/hs-hq/Betty/blob/master/betty-style.pl" title="betty-style.pl" target="_blank">betty-style.pl</a> and <a href="https://github.com/hs-hq/Betty/blob/master/betty-doc.pl" title="betty-doc.pl" target="_blank">betty-doc.pl</a></li>
<li>You are not allowed to use global variables</li>
<li>No more than 5 functions per file</li>
<li>No standard library functions allowed. Any use of functions like <code>printf</code>, <code>puts</code>, <code>calloc</code>, <code>realloc</code> etc&hellip; is forbidden</li>
<li>In the following examples, the <code>main.c</code> files are shown as examples. You can use them to test your functions, but you don&rsquo;t have to push them to your repo (if you do we won&rsquo;t take them into account). We will use our own <code>main.c</code> files at compilation. Our <code>main.c</code> files might be different from the one shown in the examples</li>
<li>The prototypes of all your functions should be included in your header file called <code>lists.h</code></li>
<li>Don&rsquo;t forget to push your header file</li>
<li>All your header files should be include guarded</li>
<li>Please use this <code>lists.h</code>: </li>
</ul>

<pre><code>#ifndef _LISTS_H_
#define _LISTS_H_

#include &lt;stddef.h&gt;


/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

listint_t *add_nodeint(listint_t **head, const int n);
size_t print_listint_safe(const listint_t *head);
size_t free_listint_safe(listint_t **h);

listint_t *find_listint_loop(listint_t *head);

#endif
</code></pre>

  </div>
</div>
        </div>
      </div>
    </div>

<h2 id="task-container" class="gap">Tasks</h2>
  
  <div class="col-sm-12 col-md-12 col-lg-8 xol-xl-9">
      <div data-role="task21070" data-position="103" id="task-num-0">
        <div class="panel panel-default task-card " id="task-21070">

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Find the loop
    </h3>

  </div>

  <div class="panel-body">

<!-- Progress vs Score -->

<!-- Task Body -->
<p>Write a function that finds the loop in a linked list.</p>

<ul>
<li>Prototype: <code>listint_t *find_listint_loop(listint_t *head);</code></li>
<li>Returns: The address of the node where the loop starts, or <code>NULL</code> if there is no loop</li>
<li>You are not allowed to use <code>malloc</code>, <code>free</code> or arrays</li>
<li>You can only declare a maximum of two variables in your function</li>
</ul>

<p>Note: In order to compile the main file, you are provided with <a href="libloop.a" title="this static library" target="_blank">this static library</a>. This library won’t be used during the correction; Its only purpose is for testing.</p>

<pre><code>alexa@ubuntu:~/find_the_loop$ cat 0-main.c 
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include &quot;lists.h&quot;

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;
    listint_t *head2;
    listint_t *node;

    head2 = NULL;
    add_nodeint(&amp;head2, 0);
    add_nodeint(&amp;head2, 1);
    add_nodeint(&amp;head2, 2);
    add_nodeint(&amp;head2, 3);
    add_nodeint(&amp;head2, 4);
    add_nodeint(&amp;head2, 98);
    add_nodeint(&amp;head2, 402);
    add_nodeint(&amp;head2, 1024);
    print_listint_safe(head2);
    node = find_listint_loop(head2);
    if (node != NULL)
    {
        printf(&quot;Loop starts at [%p] %d\n&quot;, (void *)node, node-&gt;n);
    }
    free_listint_safe(&amp;head2);
    head = NULL;
    node = add_nodeint(&amp;head, 0);
    add_nodeint(&amp;head, 1);
    add_nodeint(&amp;head, 2);
    add_nodeint(&amp;head, 3);
    add_nodeint(&amp;head, 4);
    add_nodeint(&amp;head, 5);
    add_nodeint(&amp;head, 6);
    node-&gt;next = add_nodeint(&amp;head, 7);
    add_nodeint(&amp;head, 98);
    add_nodeint(&amp;head, 402);
    add_nodeint(&amp;head, 1024);
    print_listint_safe(head);
    node = find_listint_loop(head);
    if (node != NULL)
    {
        printf(&quot;Loop starts at [%p] %d\n&quot;, (void *)node, node-&gt;n);
    }
    free_listint_safe(&amp;head);
    return (0);
}
alexa@ubuntu:~/find_the_loop$ gcc -Wall -pedantic -Werror -Wextra 0-main.c 0-find_loop.c -L. -lloop -o main
alexa@ubuntu:~/find_the_loop$ ./main
[0x13700f0] 1024
[0x13700d0] 402
[0x13700b0] 98
[0x1370090] 4
[0x1370070] 3
[0x1370050] 2
[0x1370030] 1
[0x1370010] 0
[0x1370560] 1024
[0x1370540] 402
[0x1370010] 98
[0x1370030] 7
[0x1370050] 6
[0x1370070] 5
[0x1370090] 4
[0x13700b0] 3
[0x13700d0] 2
[0x13700f0] 1
[0x1370110] 0
-&gt; [0x1370030] 7
Loop starts at [0x1370030] 7
alexa@ubuntu:~/find_the_loop$ 
</code></pre>

<p>If you want to use source file instead of the <code>libloop.a</code> library, please use this file <a href="lib.c" title="lib.c" target="_blank">lib.c</a></p>

<p>And compile it with this command: <code>$ gcc -Wall -pedantic -Werror -Wextra 0-main.c 0-find_loop.c lib.c -o main</code></p>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
  <p><strong>Repo:</strong></p>
  <ul>
    <li>GitHub repository: <code>holbertonschool-interview</code></li>
      <li>Directory: <code>find_the_loop</code></li>
      <li>File: <code>0-find_loop.c</code></li>
  </ul>
</div>

<!-- Self-paced manual review -->
  </div>

</body>
</html>
