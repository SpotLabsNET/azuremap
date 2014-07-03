from jinja2 import Environment, FileSystemLoader
import json
import region

###
### PULL REQUESTS ACCEPTED HERE:
###            https://github.com/codingoutloud/azuremap
###
#######################################################################
###     UPDATE THE LIST BELOW AS DATA CENTER INFORMATION EVOLVES    ###
### Any change (pull request) happens in the actual GitHub repo at: ###
###            https://github.com/codingoutloud/azuremap            ###
#######################################################################
# In the Windows Azure terminology relating to data centers, we have:
# - Data centers belong to a Region.
# - Regions belong to a Geo.
# - A Geo is a significant geographic area serviced by one or more Regions.
#
# The names of Regions and Geos are mostly GUESSES while pre-production.
#

##
## REGIONS (which all include a CDN)
## 
def region_hook(d):
    return region.Region(d['Geo'], d['Region'], d['Location'], d['Failover Region'], d['Status'])

with open('region_meta.json') as region_meta_file:
    regions = json.load(region_meta_file, object_hook=region_hook)

# spin through the regions to figure out the region => failover_region pairs
failover_regions = []
for r in regions:
    for fo in regions:
        if r.failover_region == fo.region:
            print("[failover mapping] %s => %s" % (r.region, fo.region))
            fo_region = region.FailoverRegion(r.region, r.latitude, r.longitude, fo.region, fo.latitude, fo.longitude)
            failover_regions.append(fo_region)

print("there are %d regions and %d failover_regions" % (len(regions), len(failover_regions)))


##
## CDN ONLY (don't double-list CDN nodes that match existing data center REGION - for now)
##
def cdn_hook(d):
    return region.CDN(d['Geo'], d['Region'], d['Location'])

with open('cdn_meta.json') as cdn_meta_file:
    cdns = json.load(cdn_meta_file, object_hook=cdn_hook)

# spin through the regions to figure out the region => failover_region pairs
for cdn in cdns:
    if not cdn.region == regions[0].region:
        print "[hello we have a match] %s " % cdn.region


print("there are %d CDNs" % (len(cdns)))

### 
### Build the GeoJSON map
###

# normally we'd use a "./templates" folder, but we only have a single template in top-level folder
env = Environment(loader=FileSystemLoader("."), trim_blocks=True)
template = env.get_template("azuremap.geojson.jinja-template")
regionsGeoJSON = template.render(regions=regions, failover_regions=failover_regions, cdns=cdns)

# write out local file
print("[writing] azuremap.geojson")
f = open('azuremap.geojson', 'w')
f.write(regionsGeoJSON)
f.close()
