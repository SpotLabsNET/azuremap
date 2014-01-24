azuremap
========

Generates a map of Windows Azure data centers around the world in two formats: GeoJSON (azuremap.geojson) and TopoJSON (azuremap.topojson).

Both of these formats are designed to describe maps. With a little help, it is also possible to render them directly in a Web Browser. 

The technology involved in the processing  includes use of the Bing Maps Geocoder, some custom Python code, a Jinja template, the Node.js topojson project, and a PowerShell script to build it all. 

For more info on the processing, please see this more detailed blog post: http://blog.codingoutloud.com/

The information about Windows Azure data centers is a __work in progress__ and will change as I learn more. I built the map using only published information, but not all the details have yet been made public, so I made some guesses. For the 8 regions already in production, the data supplied should be reliable. For any that are pre-production, there will be some guesses around exact Region and Geo names, and sometimes even some questions around exactly where the data centers are being built (I try to determine the correct city - no more detailed than that though).
