
<!DOCTYPE html>
<html lang="en">
  <body>
  <h1>AVL Trees</h1>
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

<h4>AVL Tree</h4>

<pre><code>typedef struct binary_tree_s avl_t;
</code></pre>

<h3>Print function</h3>

<p>To match the examples in the tasks, you are given <a href="https://github.com/hs-hq/0x1C.c" title="this function" target="_blank">this function</a>.</p>

<p>This function is used only for visualization purposes. You don&rsquo;t have to push it to your repo. It may not be used during the correction.</p>

  </div>
</div>
        </div>
      </div>
    </div>

<h2 id="task-container" class="gap">Tasks</h2>
  
  <div class="col-sm-12 col-md-12 col-lg-8 xol-xl-9">
      <div data-role="task21132" data-position="31" id="task-num-0">
        <div class="panel panel-default task-card " id="task-21132">

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Is AVL
    </h3>

  </div>

  <div class="panel-body">

<!-- Progress vs Score -->

<!-- Task Body -->
<p>Write a function that checks if a binary tree is a valid <a href="/rltoken/702dClPKf4JcLP0unKbwgw" title="AVL Tree" target="_blank">AVL Tree</a></p>

<ul>
<li>Prototype: <code>int binary_tree_is_avl(const binary_tree_t *tree);</code></li>
<li>Where <code>tree</code> is a pointer to the root node of the tree to check</li>
<li>Your function must return <code>1</code> if <code>tree</code> is a valid AVL Tree, and <code>0</code> otherwise</li>
<li>If <code>tree</code> is <code>NULL</code>, return <code>0</code></li>
</ul>

<p>Properties of an AVL Tree:</p>

<ul>
<li>An AVL Tree is a BST</li>
<li>The difference between heights of left and right subtrees cannot be more than one</li>
<li>The left and right subtree each must also be a binary search tree</li>
</ul>

<p>Note: In order for the main file to compile, you are provided with <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/interviews/484/libavl.a" title="this static library" target="_blank">this static library</a>. This library won’t be used during correction, its only purpose is for testing.</p>

<pre><code>alex@/tmp/binary_trees$ cat 0-main.c
#include &lt;stdlib.h&gt;
#include &lt;stdio.h&gt;
#include &quot;binary_trees.h&quot;

/**
 * basic_tree - Build a basic binary tree
 *
 * Return: A pointer to the created tree
 */
binary_tree_t *basic_tree(void)
{
    binary_tree_t *root;

    root = binary_tree_node(NULL, 98);
    root-&gt;left = binary_tree_node(root, 12);
    root-&gt;right = binary_tree_node(root, 128);
    root-&gt;left-&gt;right = binary_tree_node(root-&gt;left, 54);
    root-&gt;right-&gt;right = binary_tree_node(root, 402);
    root-&gt;left-&gt;left = binary_tree_node(root-&gt;left, 10);
    return (root);
}

/**
 * main - Entry point
 *
 * Return: Always 0 (Success)
 */
int main(void)
{
    binary_tree_t *root;
    int avl;

    root = basic_tree();

    binary_tree_print(root);
    avl = binary_tree_is_avl(root);
    printf(&quot;Is %d avl: %d\n&quot;, root-&gt;n, avl);
    avl = binary_tree_is_avl(root-&gt;left);
    printf(&quot;Is %d avl: %d\n&quot;, root-&gt;left-&gt;n, avl);

    root-&gt;right-&gt;left = binary_tree_node(root-&gt;right, 97);
    binary_tree_print(root);
    avl = binary_tree_is_avl(root);
    printf(&quot;Is %d avl: %d\n&quot;, root-&gt;n, avl);

    root = basic_tree();
    root-&gt;right-&gt;right-&gt;right = binary_tree_node(root-&gt;right-&gt;right, 430);
    binary_tree_print(root);
    avl = binary_tree_is_avl(root);
    printf(&quot;Is %d avl: %d\n&quot;, root-&gt;n, avl);

    root-&gt;right-&gt;right-&gt;right-&gt;left = binary_tree_node(root-&gt;right-&gt;right-&gt;right, 420);
    binary_tree_print(root);
    avl = binary_tree_is_avl(root);
    printf(&quot;Is %d avl: %d\n&quot;, root-&gt;n, avl);
    return (0);
}
alex@/tmp/binary_trees$ gcc -Wall -Wextra -Werror -pedantic binary_tree_print.c 0-main.c 0-binary_tree_is_avl.c -L. -lavl -o 0-is_avl
alex@/tmp/binary_trees$ ./0-is_avl
       .-------(098)--.
  .--(012)--.       (128)--.
(010)     (054)          (402)
Is 98 avl: 1
Is 12 avl: 1
       .-------(098)-------.
  .--(012)--.         .--(128)--.
(010)     (054)     (097)     (402)
Is 98 avl: 0
       .-------(098)--.
  .--(012)--.       (128)--.
(010)     (054)          (402)--.
                              (430)
Is 98 avl: 0
       .-------(098)--.
  .--(012)--.       (128)--.
(010)     (054)          (402)-------.
                                .--(430)
                              (420)
Is 98 avl: 0
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
    <li>Directory: <code>avl_trees</code></li>
    <li>File: <code>0-binary_tree_is_avl.c</code></li>
</ul>
</div>

<!-- Self-paced manual review -->
  </div>

</body>
</html>
