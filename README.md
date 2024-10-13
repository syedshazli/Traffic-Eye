# HarvardHack2024
Leveraging sensor technology & computer vision, our project creates a real-time alert system to  alert drivers, pedestrians, and cyclists of hazardous situations at traffic lights & intersections. This was built on top of a repository named Car-Speed_detection. This repository proviuded us with classification of a car as well as the coordinates of the car in the frame. https://github.com/creativekids11/Car-Speed-Detection-Python

From this, we used mathematics to estimate direction and speed in the frame, then we added an algorithm to detect if estimated paths crossed, then added support so that it works with hardware, as well as building the stand-alone device. 


# To run (MacOS Version):
<pre>Clone the repository</pre>
<pre>cd 'working model'</pre>
<pre>pip install requirements.txt</pre>
<pre>python main.py</pre>

# To Run (Windows OS Version):
<pre>Clone the repository</pre>
<pre>cd 'working model'</pre>
<pre>Edit file alarm.py</pre>
<pre>Go into alarm.py</pre>
<pre>Replace the import statements and soundAlarm function with the following</pre>
<pre>import winsound</pre>
def soundAlarm():
<pre>duration = 3000</pre>
<pre>freq = 440</pre>
<pre>winsound.Beep(freq,duration)</pre>
<pre>...Keep the rest of the code in alarm.py the same/pre>
  
<pre>pip install requirements.txt</pre>
<pre>python main.py</pre>
