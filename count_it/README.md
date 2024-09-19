
<!DOCTYPE html>
<html lang="en">
<body>
<div class="panel panel-default" id="project-description">
  <div class="panel-body">
  <h1>Count it!</h1>
    <h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://www.reddit.com/dev/api/" title="Reddit API Documentation" target="_blank">Reddit API Documentation</a> </li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using <code>python3</code> (version 3.4.3)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>Libraries imported in your Python files must be organized in alphabetical order</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>PEP 8</code> style</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>You must use the Requests module for sending HTTP requests to the Reddit API</li>
</ul>

  </div>
</div>


      

      

        
<h2 class="gap">Tasks</h2>

<div>
    <div>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Count it!
    </h3>

  </div>

  <div class="panel-body">

<!-- Progress vs Score -->

<!-- Task Body -->
<p>Write a <em>recursive function</em> that queries the <a href="/rltoken/R6e5bdJ19xlCk7qxyngEGQ" title="Reddit API" target="_blank">Reddit API</a>, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. <code>Javascript</code> should count as <code>javascript</code>, but <code>java</code> should not).</p>

<p>Requirements:</p>

<ul>
<li>Prototype: <code>def count_words(subreddit, word_list)</code></li>
<li>Note: You may change the prototype, but it must be able to be called with just a subreddit supplied and a list of keywords. AKA you can add a counter or anything else, but the function must work without supplying a starting value in the main.</li>
<li>If <code>word_list</code> contains the same word (case-insensitive), the final count should be the sum of each duplicate (example below with <code>java</code>)</li>
<li>Results should be printed in descending order, by the count, and if the count is the same for separate keywords, they should then be sorted alphabetically (ascending, from A to Z). Words with no matches should be skipped and not printed. Words must be printed in lowercase.</li>
<li>Results are based on the number of times a keyword appears, not titles it appears in. <code>java java java</code> counts as 3 separate occurrences of <code>java</code>.</li>
<li>To make life easier, <code>java.</code> or <code>java!</code> or <code>java_</code> should not count as <code>java</code></li>
<li>If no posts match or the subreddit is invalid, print nothing.</li>
<li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are NOT following redirects.</li>
</ul>

<p>Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop but the point is to use a recursive function. :)</p>

<p><strong>Disclaimer</strong>: number presented in this example <em>cannot be accurate now</em> - Reddit is hot articles are always changing.</p>

<pre><code>bob@dylan $ cat 0-main.py 
#!/usr/bin/python3
&quot;&quot;&quot;
0-main
&quot;&quot;&quot;
import sys

if __name__ == &#39;__main__&#39;:
    count_words = __import__(&#39;0-count&#39;).count_words
    if len(sys.argv) &lt; 3:
        print(&quot;Usage: {} &lt;subreddit&gt; &lt;list of keywords&gt;&quot;.format(sys.argv[0]))
        print(&quot;Ex: {} programming &#39;python java javascript&#39;&quot;.format(sys.argv[0]))
    else:
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])
bob@dylan $             
bob@dylan $ python3 0-main.py programming &#39;react python java javascript scala no_results_for_this_one&#39;
java: 27
javascript: 20
python: 17
react: 17
scala: 4
bob@dylan $ python3 0-main.py programming &#39;JavA java&#39;
java: 54
bob@dylan $ python3 0-main.py not_a_valid_subreddit &#39;python java javascript scala no_results_for_this_one&#39;
bob@dylan $ python3 0-main.py not_a_valid_subreddit &#39;python java&#39;
bob@dylan $ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-interview</code></li>
    <li>Directory: <code>count_it</code></li>
    <li>File: <code>0-count.py</code></li>
</ul>
</div>

<!-- Self-paced manual review -->
  </div>

      
</body>
</html>
