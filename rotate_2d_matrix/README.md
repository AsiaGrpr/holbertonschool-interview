
<!DOCTYPE html>
<html lang="en">
  <body>
  <h1>Rotate 2D Matrix</h1>
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
<li>You are not allowed to import any module</li>
<li>All modules and functions must be documented</li>
<li>All your files must be executable</li>
</ul>

  </div>
</div>
        </div>
      </div>
    </div>

<h2 id="task-container" class="gap">Tasks</h2>
  
  <div>
      <div>
        <div>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Rotate 2D Matrix
    </h3>

  </div>

  <div class="panel-body">

<!-- Progress vs Score -->

<!-- Task Body -->
<p>Given an <code>n</code> x <code>n</code> 2D matrix, rotate it 90 degrees clockwise.</p>

<ul>
<li>Prototype: <code>def rotate_2d_matrix(matrix):</code></li>
<li>Do not return anything. The matrix must be edited <strong>in-place</strong>.</li>
<li>You can assume the matrix will have 2 dimensions and will not be empty.</li>
</ul>

<pre><code>jessevhedden$ cat main_0.py
#!/usr/bin/python3
&quot;&quot;&quot;
Test  - Rotate 2D Matrix
&quot;&quot;&quot;
rotate_2d_matrix = __import__(&#39;0-rotate_2d_matrix&#39;).rotate_2d_matrix

if __name__ == &quot;__main__&quot;:
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

jessevhedden$
jessevhedden$ ./main_0.py
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]
jessevhedden$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
   <p><strong>Repo:</strong></p>
   <ul>
      <li>GitHub repository: <code>holbertonschool-interview</code></li>
      <li>Directory: <code>rotate_2d_matrix</code></li>
      <li>File: <code>0-rotate_2d_matrix.py</code></li>
   </ul>
</div>

<!-- Self-paced manual review -->
  </div>

</body>
</html>
