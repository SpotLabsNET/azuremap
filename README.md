azuremap
========

This project builds a reusable map of the Windows Azure data center regions around the world.

The maps are currently generated to two formats: GeoJSON (azuremap.geojson) and TopoJSON (azuremap.topojson). Both of these map formats are open standards. With a little help, they can be rendered directly in a Web Browser (such as in [this blog post](http://blog.codingoutloud.com/2014/02/01/mapping-windows-azure-4-years-after-full-general-availability/) and this [GitHub Gist](https://gist.github.com/codingoutloud/8590311)). 


terminology
-----------

The azuremap project copies the terminology used in the [Windows Azure Trust Center](http://www.windowsazure.com/en-us/support/trust-center/privacy/).

There are three core concepts: the __*data center*__, the __*region*__, and the __*geo*__:

- A *data center* is part of a region. Each *region* comprises one or more data centers. Within a region, data centers are assumed to be "near" each other (think "same city").
- A region belongs to a *geo*. A Geo is a significant geographic area comprising one or more Regions.

__NOTE:__ The names of regions and geos, and the locations of regions, are mostly GUESSES while pre-production.


generation technology
-----------

The technology involved in the processing includes use of the Bing Maps Geocoder, some custom Python code, a Jinja template, the Node.js topojson project, and a PowerShell script to build it all. 

The script cannot be run from "anywhere" since it includes updating github repos (to which the general public will not have direct push access). Here is an example of the script running:

![Output from running the AzureMap build.ps1 script](https://raw.github.com/codingoutloud/azuremap/master/azuremap-build-output.png)
