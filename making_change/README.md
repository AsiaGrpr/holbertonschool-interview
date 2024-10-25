
<!DOCTYPE html>
<html lang="en">
  <body>
  <h1>Making Change</h1>
  <div class="panel-body text-justify">
    <h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using <code>python3</code> (version 3.4.3)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>PEP 8</code> style (version 1.7.x)</li>
<li>All your files must be executable</li>
</ul>

  </div>
</div>
        </div>
      </div>
    </div>

<h2 id="task-container" class="gap">Tasks</h2>
  
  <div class="col-sm-12 col-md-12 col-lg-8 xol-xl-9">
      <div data-role="task21180" data-position="1" id="task-num-0">
        <div class="panel panel-default task-card " id="task-21180">

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Change comes from within
    </h3>

  </div>

  <div class="panel-body">

<!-- Progress vs Score -->

<!-- Task Body -->
<p>Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount <code>total</code>.</p>

<ul>
<li>Prototype: <code>def makeChange(coins, total)</code></li>
<li>Return: fewest number of coins needed to meet <code>total</code>

<ul>
<li>If <code>total</code> is <code>0</code> or less, return <code>0</code></li>
<li>If <code>total</code> cannot be met by any number of coins you have, return <code>-1</code></li>
</ul></li>
<li><code>coins</code> is a list of the values of the coins in your possession</li>
<li>The value of a coin will always be an integer greater than <code>0</code></li>
<li>You can assume you have an infinite number of each denomination of coin in the list</li>
<li>Your solution&rsquo;s runtime will be evaluated in this task</li>
</ul>

<pre><code>carrie@ubuntu:~/making_change$ cat 0-main.py
#!/usr/bin/python3
&quot;&quot;&quot;
Main file for testing
&quot;&quot;&quot;

makeChange = __import__(&#39;0-making_change&#39;).makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

carrie@ubuntu:~/making_change$
</code></pre>

<pre><code>carrie@ubuntu:~/making_change$ ./0-main.py
7
-1
carrie@ubuntu:~/making_change$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-interview</code></li>
    <li>Directory: <code>making_change</code></li>
    <li>File: <code>0-making_change.py</code></li>
</ul>
</div>

<!-- Self-paced manual review -->
  </div>

</body>
</html>
