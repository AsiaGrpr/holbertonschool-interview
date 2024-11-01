
<!DOCTYPE html>
<html lang="en">
  <body>
  <h1>Infinite Multiplication</h1>
  <div class="panel-body text-justify">
    <h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be compiled on Ubuntu 14.04 LTS</li>
<li>Your programs and functions will be compiled with <code>gcc 4.8.4</code> using the flags <code>-Wall</code> <code>-Werror</code> <code>-Wextra</code> <code>and -pedantic</code> </li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project is mandatory</li>
<li>Your code should use the <code>Betty</code> style. It will be checked using <a href="https://github.com/hs-hq/Betty/blob/master/betty-style.pl" title="betty-style.pl" target="_blank">betty-style.pl</a> and <a href="https://github.com/hs-hq/Betty/blob/master/betty-doc.pl" title="betty-doc.pl" target="_blank">betty-doc.pl</a></li>
<li>You are not allowed to use global variables</li>
<li>No more than 5 functions per file</li>
<li>The only C standard library functions allowed are <code>malloc</code>, <code>free</code> and <code>exit</code>. Any use of functions like <code>printf</code>, <code>puts</code>, <code>calloc</code>, <code>realloc</code> etc&hellip; is forbidden</li>
<li>You are allowed to use <a href="https://github.com/hs-hq/_putchar.c/blob/master/_putchar.c" title="_putchar" target="_blank">_putchar</a></li>
<li>You don&rsquo;t have to push <code>_putchar.c</code>, we will use our file. If you do it won&rsquo;t be taken into account</li>
<li>In the following examples, the <code>main.c</code> files are shown as examples. You can use them to test your functions, but you don&rsquo;t have to push them to your repo (if you do we won&rsquo;t take them into account). We will use our own <code>main.c</code> files at compilation. Our <code>main.c</code> files might be different from the one shown in the examples</li>
<li>The prototypes of all your functions and the prototype of the function <code>_putchar</code> should be included in your header file called <code>holberton.h</code></li>
<li>Don&rsquo;t forget to push your header file</li>
</ul>

  </div>
</div>
        </div>
      </div>
    </div>

<h2 id="task-container" class="gap">Tasks</h2>
  
  <div class="col-sm-12 col-md-12 col-lg-8 xol-xl-9">
      <div data-role="task21050" data-position="101" id="task-num-0">
        <div class="panel panel-default task-card " id="task-21050">

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Infinite Multiplication
    </h3>

  </div>

  <div class="panel-body">

<!-- Progress vs Score -->

<!-- Task Body -->
<p>Write a program that multiplies two positive numbers:</p>

<ul>
<li>Usage: <code>mul num1 num2</code></li>
<li><code>num1</code> and <code>num2</code> will be passed in base 10</li>
<li>Print the result, followed by a new line</li>
<li>If the number of arguments is incorrect, print <code>Error</code>, followed by a new line, and exit with a status of <code>98</code></li>
<li><code>num1</code> and <code>num2</code> should only be composed of digits. If not, print <code>Error</code>, followed by a new line, and exit with a status of <code>98</code></li>
<li>You are allowed to use more than 5 functions in your file</li>
</ul>

<p>You can use <code>bc</code> (<code>man bc</code>) to check your results.</p>

<pre><code>alexa@ubuntu:~/infinite_multiplication$ gcc -Wall -pedantic -Werror -Wextra 0-mul.c _putchar.c -o mul
alexa@ubuntu:~/infinite_multiplication$ ./mul 10 98
980
alexa@ubuntu:~/infinite_multiplication$ ./mul 235234693269436436223446526546334576437634765378653875874687649698659586695898579 28658034365084365083426083109679137608216408631430814308651084650816406134060831608310853086103769013709675067130586570832760732096730978014607369739567864508634086304807450973045703428580934825098342095832409850394285098342509834209583425345267413639235755891879970464524226159074760914989935413350556875770807019893069201247121855122836389417022552166316010013074258781583143870461182707893577849408672040555089482160343085482612348145322689883025225988799452329290281169927532160590651993511788518550547570284574715925006962738262888617840435389140329668772644708
6741363923575589187997046452422615907476091498993541335055687577080701989306920124712185512283638941702255216631601001307425878158314387046118270789357784940867204055508948216034308548261234814532268988302522598879945232929028116992753216059081057377926651337612618248332113256902485974371969385156015068813868274000683912187818601667058605418678284322237297213673482412392922068159291496274311170208689056585352782844484721140846367741649962638649229509281867896067208474178402156294978940712959518351846413859141792380853313812015295333546716634344284086426775480775747808150030732119704867805688704303461042373101473485092019906795014369069932
alexa@ubuntu:~/infinite_multiplication$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
  <p><strong>Repo:</strong></p>
  <ul>
    <li>GitHub repository: <code>holbertonschool-interview</code></li>
      <li>Directory: <code>infinite_multiplication</code></li>
      <li>File: <code>0-mul.c</code></li>
  </ul>
</div>

<!-- Self-paced manual review -->
  </div>

</body>
</html>
