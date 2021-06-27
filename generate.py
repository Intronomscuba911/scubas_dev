import requests, json, random, time, socket, platform

timestr = time.strftime("%Y-%m-%d - %H:%M:%S UTC")
nameid = "VicRoesems"
repoid = "Jar-Runtime"
yamlid = "generate-code"
f = open("./README.md", "w")
f.write(f'''



<h3 align="left">🧑🏻‍💻 Languages and Tools:</h3>
<p align="left"> <a href="https://www.w3schools.com/cpp/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg" alt="cplusplus" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://pytorch.org/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="pytorch" width="40" height="40"/> </a></p>




<table style="margin:0 0;">
<tr>
	<td>
<p>&nbsp;<img align="left"  src="https://github-readme-stats.vercel.app/api?username=scallions&show_icons=true&locale=en" alt="scallions" /></p>
	</td>
	<td>
<p><img align="right"  src="https://github-readme-stats.vercel.app/api/top-langs?username=scallions&show_icons=true&locale=en&layout=compact" alt="scallions" /></p>
	</td>
</tr>
<tr>
	<td>
<p><img align="left"  src="https://github-readme-streak-stats.herokuapp.com/?user=scallions&" alt="scallions" /></p>
	</td>
	<td>
<p><img align="right"  src="https://stats.justsong.cn/api/leetcode?username=scallions&cn=true" /></p>
	</td>
</tr>
</table>

<p align="center">

  
<p align="left"> <img src="https://komarev.com/ghpvc/?username=scallions&label=Profile%20views&color=0e75b6&style=flat" alt="scallions" /> </p>

#### This Page Create at:

```bash

{timestr}

```

#### Create By Machine:

```bash

Host Name : {socket.gethostname()}

platform  : {platform.platform()}

Ip Local  : {socket.gethostbyname(socket.gethostname())}

```
</p> 
''')
f.close()
