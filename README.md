# MendiGenerativeArt 

A year or so ago I got a Mendi device. It uses fNIRS technology to track brain activity through increased blood flow to certain areas of the brain, basically a mini brain scanner. 

Then a few months ago I started getting interested in Generative Art, not the AI kind, but rather stills and animations created through programs like Processing. I found a lecture on youtube given by Dan Lidral Porter on the De-Jong IFS, an iterated function system which is capable of producing intricate and pretty patterns which change as the four parameters of the function change. In the lecture he shows animations created from varying two of these parameters across a path. 

The purpose of Mendi is to be used as a Neurofeedback device. Neurofeedback is a relatively new technology shown to increase brain function and help with mental health issues through essentially controlling a game with your mind. I wondered if I could use the output from the Mendi device to control an animation of the De Jong IFS in real time. 

Sadly Mendi don't have a public API, so I decided instead to try and use the data they give you in the app to control it instead. This wouldn't allow me to control the animation in real-time, but could still allow for a cool proof of concept.

So I created a python script which could automatically extract the data from the graph through the manipulation of a screenshotted image. I then wrote some code in Processing which would import this data, and use it to control the 'a' parameter.

The result is this!

https://github.com/patrickshortall26/MendiGenerativeArt/assets/60779668/c045bcb1-1e5a-410d-8c88-8cf7262b1437

