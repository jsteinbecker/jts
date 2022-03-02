import urllib
from bs4 import BeautifulSoup
import urllib3
import requests

url = 'https://en.wikipedia.org/wiki/List_of_Pixar_films'

from bs4 import BeautifulSoup
from urllib import urlopen

html = requests.get(url)
html.text
soup = BeautifulSoup(html.text,'html.parser')
tables = soup.find_all('tbody')
soup.find_all('li')


print (tables)
x = tables.find_all('tbody')
x = """<ul><li><span class="nowrap"><i><a href="/wiki/Toy_Story" title="Toy Story">Toy Story</a></i> (1995)</span></li>
<li><span class="nowrap"><i><a href="/wiki/A_Bug%27s_Life" title="A Bug's Life">A Bug's Life</a></i> (1998)</span></li>
<li><span class="nowrap"><i><a href="/wiki/Toy_Story_2" title="Toy Story 2">Toy Story 2</a></i> (1999)</span></li>
<li><span class="nowrap"><i><a href="/wiki/Monsters,_Inc." title="Monsters, Inc.">Monsters, Inc.</a></i> (2001)</span></li>
<li><span class="nowrap"><i><a href="/wiki/Finding_Nemo" title="Finding Nemo">Finding Nemo</a></i> (2003)</span></li>
<li><span class="nowrap"><i><a href="/wiki/The_Incredibles" title="The Incredibles">The Incredibles</a></i> (2004)</span></li>
<li><span class="nowrap"><i><a href="/wiki/Cars_(film)" title="Cars (film)">Cars</a></i> (2006)</span></li>
<li><span class="nowrap"><i><a href="/wiki/Ratatouille_(film)" title="Ratatouille (film)">Ratatouille</a></i> (2007)</span></li>
<li><span class="nowrap"><i><a href="/wiki/WALL-E" title="WALL-E">WALL-E</a></i> (2008)</span></li>
<li><span class="nowrap"><i><a href="/wiki/Up_(2009_film)" title="Up (2009 film)">Up</a></i> (2009)</span></li>
<li><span class="nowrap"><i><a href="/wiki/Toy_Story_3" title="Toy Story 3">Toy Story 3</a></i> (2010)</span></li>
<li><span class="nowrap"><i><a href="/wiki/Cars_2" title="Cars 2">Cars 2</a></i> (2011)</span></li>
<li><span class="nowrap"><i><a href="/wiki/Brave_(2012_film)" title="Brave (2012 film)">Brave</a></i> (2012)</span></li>
<li><span class="nowrap"><i><a href="/wiki/Monsters_University" title="Monsters University">Monsters University</a></i> (2013)</span></li>
<li><span class="nowrap"><i><a href="/wiki/Inside_Out_(2015_film)" title="Inside Out (2015 film)">Inside Out</a></i> (2015)</span></li>
<li><span class="nowrap"><i><a href="/wiki/The_Good_Dinosaur" title="The Good Dinosaur">The Good Dinosaur</a></i> (2015)</span></li>
<li><span class="nowrap"><i><a href="/wiki/Finding_Dory" title="Finding Dory">Finding Dory</a></i> (2016)</span></li>
<li><span class="nowrap"><i><a href="/wiki/Cars_3" title="Cars 3">Cars 3</a></i> (2017)</span></li>
<li><span class="nowrap"><i><a href="/wiki/Coco_(2017_film)" title="Coco (2017 film)">Coco</a></i> (2017)</span></li>
<li><span class="nowrap"><i><a href="/wiki/Incredibles_2" title="Incredibles 2">Incredibles 2</a></i> (2018)</span></li>
<li><span class="nowrap"><i><a href="/wiki/Toy_Story_4" title="Toy Story 4">Toy Story 4</a></i> (2019)</span></li>
<li><span class="nowrap"><i><a href="/wiki/Onward_(film)" title="Onward (film)">Onward</a></i> (2020)</span></li>
<li><span class="nowrap"><i><a href="/wiki/Soul_(2020_film)" title="Soul (2020 film)">Soul</a></i> (2020; international release)</span></li>
<li><span class="nowrap"><i><a href="/wiki/Luca_(2021_film)" title="Luca (2021 film)">Luca</a></i> (2021; international release)</span></li></ul>"""
x = BeautifulSoup(x.text(),'html.parser')
x.get_text()