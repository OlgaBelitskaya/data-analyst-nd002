
# Summary

##### This visualization shows the growth of 20 most populous cities of the world from 1990 to 2014: the ordinal number reflects the population rating of the city, size of the circles and the text during animation - the amount of population growth in percent over the period.

##### The purpose of this visualization is to show urbanization processes on the example of large cities, as well as a huge difference between them in the population growth: the cities of Japan and USA show relatively low growth, the cities of China certainly are leaders in growth rate.

##### The unprecedented scale of China’s urban explosion is obtained by a set of reasons (economic liberalisation, development of the transport system, increase in the population in general, etc.) and, of course, a very interesting subject for research.

##### If these trends continue, a possible scenario in the future: by 2030 Chinese cities will contain around a billion people — about 70% of China’s population and an eighth of humanity. ( http://www.economist.com/news/leaders/21601027-worlds-sake-and-its-own-china-needs-change-way-it-builds-and-runs-its)

# Design

##### Basic decisions of the map are made in shades of light blue, gray, dark blue and white colors. This let us not to dissipate the user's attention with bright colors, but it makes the map very clearly defined. Text and graphics solutions in a single color scheme allow the visualization to be considered as a single information space.
##### For the circles, I picked up a collection of bright colors, because the pre-decided to make them as transparent as possible.
##### For the text I use the underscore to pay attention of users to the digital indicators.
##### The use of animations significantly expanded the provided information and underlined the findings.

# Feedback 

### 1.
##### I started the projects using high level libraries. This process reflects index01.html & index02.html.  The first feedback was a discussion on the Udacity forum about types of programms which I should use. The result was the acceptable range for code libraries: intermediate-level tools. 
##### The link: https://discussions.udacity.com/t/dand-p6-can-i-use-highcharts/188504

##### I completely redid the project and tried to add information about more cities. This step reflects files index11.html & index12.html. I didn't show them to the audience because I did not like the results. 
##### On my opinion in index11.html has too many visual points and it was hard to catch any idea for expression.  In the file index12.html , I took as a basis for other statistical data which is limited to 20 cities. But I did not like the visual view of the map, it looked more like a scheme.
##### I improved the map and added the table with names of cities and areas (index13.html & index14.html).

##### In the next step I added animation for circles and their inscriptions (index15.html & index16.html). As a result, I also was dissatisfied and decided to animate the circles individually (index17.html). I liked the most the result of changing and showed the project again.

### 2.
##### The second feedback was a verbal comment of my mother that she liked the visualization, but she wanted to see an analysis of the causes of the processes together with a graphical representation. 
##### For example, she connects high growth for Asian Cities not only with birthrate, but with the economic success of these countries in recent decades.
#####  I included my point of view with analysis into the summary section.

### 3.
##### The third feedback was an email from my son. He liked the project also and wanted to see the name of countries and another colors during the animation.
##### I added country codes and changed  the color of text in animation option (index18.html) .

### 4.
##### After that I added the comments into the code lines because I received a note about this in the previous project P4 and send P6 for the submission. 

### 5.

##### The next feedback was a review on the Udacity.com (https://review.udacity.com/#!/reviews/233328). It helps me improve my visualization (index19.html). 
##### 1 ) I added a comment at the bottom of the page with an explanation of animation to improve interconnection with users: "For more information, move the cursor on the circles on the map or on the table at right".
##### 2) I corrected the code: add ";" and " " for achieving a uniform style of the program.
##### 3) I expanded the information that can be transmitted to the reader via animation tables. These tables together with the size of circles help to underline the main finding: the cities of China demonstrate the greatest rate of growth.

### 6.
##### The feedback on the forum ( https://discussions.udacity.com/t/dand-p6-feedback-on-data-visualization-d3/189115 ) was a comment about adding a link to the source and possible changing in the color scheme and text labels.
##### 1) I added a link to the source of information.
##### 2) I left the color scheme without any changes. As the author I want to see the result of the visualization in a single color gamma.
##### 3) The adding of the long city names (with areas) makes the map overloaded by text information. That's why I created the table at right and didn't use this labels on the map.

### 7.
##### The final version - index_final.html.

# Resources 

##### Useful tutorials and code collections:

http://basemaptutorial.readthedocs.io/en/latest/installation.html

http://www.bogotobogo.com/python/IPython/iPython_Jupyter_Notebook_with_Embedded_D3.php

https://www.dashingd3js.com/table-of-contents

http://datamaps.github.io/

https://www.w3.org/TR/SVG/



http://bl.ocks.org/mbostock

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects

http://code.highcharts.com/mapdata/

http://techslides.com/over-2000-d3-js-examples-and-demos

http://www.w3schools.com/colors/colors_names.asp

http://jeffpaine.github.io/geojson-topojson/

http://papaparse.com/

http://api.highcharts.com/


##### Tools and fragments:

1) From CSV to HTML table (Advanced):

https://bl.ocks.org/ndarville/7241320

2) D3 Mouse Events:

http://bl.ocks.org/WilliamQLiu/76ae20060e19bf42d774

3) Working with Transitions

https://bost.ocks.org/mike/transition/

4) Ordinal Scales:

https://github.com/d3/d3-3.x-api-reference/blob/master/Ordinal-Scales.mdhttp://

5) CSS Background:

http://www.w3schools.com/css/css_background.asp

6) Multi-Series Line Chart:

http://bl.ocks.org/mbostock/3884955

##### Data websites:

http://www.infoplease.com/ipa/A0762524.html

http://www.citymayors.com/statistics/largest-cities-area-125.html



```python

```
