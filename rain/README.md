<!DOCTYPE html>
<html lang="en">

<h1>Rain</h1>
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
      <h2>0. Rain</h2>

<!-- Task Body -->
<p>Given a list of non-negative integers representing the heights of walls with unit width 1, as if viewing the cross-section of a relief map, calculate how many square units of water will be retained after it rains.</p>

<ul>
<li>Prototype: <code>def rain(walls)</code></li>
<li><code>walls</code> is a list of non-negative integers.</li>
<li>Return: Integer indicating total amount of rainwater retained.</li>
<li>Assume that the ends of the list (before index 0 and after index walls[-1]) are <strong>not</strong> walls, meaning they will not retain water.</li>
<li>If the list is empty return <code>0</code>.</li>
</ul>

<pre><code>jesse@ubuntu:~/$ cat 0_main.py
#!/usr/bin/python3
&quot;&quot;&quot;
0_main
&quot;&quot;&quot;
rain = __import__(&#39;0-rain&#39;).rain

if __name__ == &quot;__main__&quot;:
    walls = [0, 1, 0, 2, 0, 3, 0, 4]
    print(rain(walls))
    walls = [2, 0, 0, 4, 0, 0, 1, 0]
    print(rain(walls))

jesse@ubuntu:~/$ 
jesse@ubuntu:~/$ ./0_main.py
6
6
jesse@ubuntu:~/$ 
</code></pre>

<p>Visual representation of the walls <code>[0, 1, 0, 2, 0, 3, 0, 4]</code></p>

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2021/4/85ef782020ac6efdc7004b62ea86724a552285b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240827%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240827T162558Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a944ad9d5e60615e52ba709504955d26b21202b496c3776d0aab6adeaf7b325d" alt="" loading='lazy' style="width: 400px" /></p>

<p>Visual representation of the walls <code>[2, 0, 0, 4, 0, 0, 1, 0]</code></p>

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2021/4/9a27c3e4e214e55b3c0b8b1439fdc99b4a184ff5.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240827%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240827T162558Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4f185cd22dd306b1e704c040a66f6aa65d5a14152455c290378ab5073d56fa8b" alt="" loading='lazy' style="width: 400px" /></p>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-interview</code></li>
    <li>Directory: <code>rain</code></li>
    <li>File: <code>0-rain.py</code></li>
</ul>
</div>

</body>
</html>
