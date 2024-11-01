
<!DOCTYPE html>
<html lang="en">
  <body>
  <h1>Double Circular Linked List</h1>
  <div class="panel-body text-justify">
    <h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be compiled on Ubuntu 14.04 LTS</li>
<li>Your programs and functions will be compiled with <code>gcc 4.8.4</code> using the flags <code>-Wall</code> <code>-Werror</code> <code>-Wextra</code> and <code>-pedantic</code></li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project is mandatory</li>
<li>Your code should use the <code>Betty</code> style. It will be checked using <a href="https://github.com/hs-hq/Betty/blob/master/betty-style.pl" title="betty-style.pl" target="_blank">betty-style.pl</a> and <a href="https://github.com/hs-hq/Betty/blob/master/betty-doc.pl" title="betty-doc.pl" target="_blank">betty-doc.pl</a></li>
<li>You are not allowed to use global variables</li>
<li>No more than 5 functions per file</li>
<li>The only C standard library functions allowed are <code>malloc</code>, <code>free</code>, and <code>strdup</code>. Any use of functions like <code>printf</code>, <code>puts</code>, <code>calloc</code>, <code>realloc</code> etc… is forbidden</li>
<li>In the following examples, the <code>main.c</code> files are shown as examples. You can use them to test your functions, but you don&rsquo;t have to push them to your repo (if you do we won&rsquo;t take them into account). We will use our own <code>main.c</code> files at compilation. Our <code>main.c</code> files might be different from the one shown in the examples</li>
<li>The prototypes of all your functions should be included in your header file called <code>list.h</code></li>
<li>Don&rsquo;t forget to push your header file</li>
<li>All your header files should be include guarded</li>
</ul>

<h2>More Info</h2>

<p>Please use this data structure for this project:</p>

<pre><code>/**
 * struct List - doubly linked list
 * @str: string - (malloc&#39;ed string)
 * @prev: points to the previous node
 * @next: points to the next node
 *
 * Description: doubly linked list node structure
 * for Holberton project
 */
typedef struct List
{
  char *str;
  struct List *prev;
  struct List *next;
} List;
</code></pre>

  </div>
</div>
        </div>
      </div>
    </div>

<h2 id="task-container" class="gap">Tasks</h2>
  
  <div class="col-sm-12 col-md-12 col-lg-8 xol-xl-9">
      <div data-role="task21119" data-position="5" id="task-num-0">
        <div class="panel panel-default task-card " id="task-21119">

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Add Nodes
    </h3>

  </div>

  <div class="panel-body">

<!-- Progress vs Score -->

<!-- Task Body -->
<p>Create the source file <code>0-add_node.c</code> that contains the following functions:</p>

<ul>
<li>Add a new node  to <strong>the end</strong> of a double circular linked list:

<ul>
<li>Prototype: <code>List *add_node_end(List **list, char *str);</code></li>
<li><code>List</code>: the list to modify

<ul>
<li><code>str</code>: the string to copy into the new node</li>
<li>Returns: Address of the new node, or <code>NULL</code> on failure</li>
</ul></li>
</ul></li>
<li>Add a new node to <strong>the beginning</strong> of a double circular linked list:

<ul>
<li>Prototype: <code>List *add_node_begin(List **list, char *str);</code></li>
<li><code>List</code>: the list to modify

<ul>
<li><code>str</code>: the string to copy into the new node</li>
<li>Returns: Address of the new node, or <code>NULL</code> on failure</li>
</ul></li>
</ul></li>
</ul>

<pre><code>alexa@ubuntu:double_circular_linked_list$ cat 0-main.c 
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &quot;list.h&quot;

/**
 * print_list - Print informations about each element of a list
 *
 * @list: A pointer to the head of the linkd list
 *
 * Return: void
 */
void print_list(List *list)
{
    List *tmp;

    tmp = list;
    while (tmp)
    {
        printf(&quot;%s\n&quot;, tmp-&gt;str);
        printf(&quot;\t-&gt;prev: %s\n&quot;, tmp-&gt;prev ? tmp-&gt;prev-&gt;str : &quot;NULL&quot;);
        printf(&quot;\t-&gt;next: %s\n&quot;, tmp-&gt;next ? tmp-&gt;next-&gt;str : &quot;NULL&quot;);
        tmp = tmp-&gt;next;
        if (tmp == list)
            break;
    }
}

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    List *list;

    list = NULL;
    add_node_end(&amp;list, &quot;Holberton&quot;);
    add_node_end(&amp;list, &quot;School&quot;);
    add_node_end(&amp;list, &quot;Full&quot;);
    add_node_end(&amp;list, &quot;Stack&quot;);
    add_node_end(&amp;list, &quot;Engineer&quot;);

    printf(&quot;Added to the end:\n&quot;);
    print_list(list);
    list = NULL;
    add_node_begin(&amp;list, &quot;Holberton&quot;);
    add_node_begin(&amp;list, &quot;School&quot;);
    add_node_begin(&amp;list, &quot;Full&quot;);
    add_node_begin(&amp;list, &quot;Stack&quot;);
    add_node_begin(&amp;list, &quot;Engineer&quot;);

    printf(&quot;Added to the beginning:\n&quot;);
    print_list(list);
    return (0);
}
alexa@ubuntu:double_circular_linked_list$ gcc -Wall -Wextra -Werror -pedantic 0-main.c 0-add_node.c
alexa@ubuntu:double_circular_linked_list$ ./a.out 
Holberton
        -&gt;prev: Engineer
        -&gt;next: School
School
        -&gt;prev: Holberton
        -&gt;next: Full
Full
        -&gt;prev: School
        -&gt;next: Stack
Stack
        -&gt;prev: Full
        -&gt;next: Engineer
Engineer
        -&gt;prev: Stack
        -&gt;next: Holberton
Added to the beginning:
Engineer
        -&gt;prev: Holberton
        -&gt;next: Stack
Stack
        -&gt;prev: Engineer
        -&gt;next: Full
Full
        -&gt;prev: Stack
        -&gt;next: School
School
        -&gt;prev: Full
        -&gt;next: Holberton
Holberton
        -&gt;prev: School
        -&gt;next: Engineer
alexa@ubuntu:double_circular_linked_list$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
        <li>GitHub repository: <code>holbertonschool-interview</code></li>
        <li>Directory: <code>double_circular_linked_list</code></li>
        <li>File: <code>0-add_node.c</code></li>
</ul>
</div>

<!-- Self-paced manual review -->
  </div>

</body>
</html>
