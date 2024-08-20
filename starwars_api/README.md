<div align="center">

<h1>Star Wars API</h1>

</div>
<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 14.04 LTS using <code>node</code> (version 10.14.x)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/node</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should be <code>semistandard</code> compliant. <a href="https://standardjs.com/rules.html" title="Rules of Standard" target="_blank">Rules of Standard</a> + <a href="https://github.com/standard/semistandard" title="semicolons on top" target="_blank">semicolons on top</a>. Also as reference: <a href="https://github.com/airbnb/javascript" title="AirBnB style" target="_blank">AirBnB style</a></li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<h2>More Info</h2>

<h3>Install Node 10</h3>

<pre><code>$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
</code></pre>

<h3>Install semi-standard</h3>

<p><a href="https://github.com/standard/semistandard" title="Documentation" target="_blank">Documentation</a></p>

<pre><code>$ sudo npm install semistandard --global
</code></pre>

<h3>Install <code>request</code> module and use it</h3>

<p><a href="https://github.com/request/request" title="Documentation" target="_blank">Documentation</a></p>

<pre><code>$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
</code></pre>

  </div>
</div>

<h2 class="gap">Tasks</h2>


<div class="panel-heading panel-heading-actions">
<h3 class="panel-title">
    1. Star Wars Characters
</h3>

<!-- Task Body -->
<p>Write a script that prints all characters of a Star Wars movie:</p>

<ul>
<li>The first positional argument passed is the Movie ID - example: <code>3</code> = &ldquo;Return of the Jedi&rdquo; </li>
<li>Display one character name per line <strong>in the same order as the &ldquo;characters&rdquo; list in the <code>/films/</code> endpoint</strong></li>
<li>You must use the <a href="https://swapi-api.hbtn.io/" title="Star wars API" target="_blank">Star wars API</a></li>
<li>You must use the <code>request</code> module</li>
</ul>

<pre><code>alexa@ubuntu:~/$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
alexa@ubuntu:~/$ 
</code></pre>

  </div>


<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-interview</code></li>
    <li>Directory: <code>starwars_api</code></li>
    <li>File: <code>0-starwars_characters.js</code></li>
</ul>
</div>
