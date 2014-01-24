from jinja2 import Environment, FileSystemLoader
import region
import region_meta

# spin through the regions to figure out the region => failover_region pairs
failover_regions = []
for r in region_meta.regions:
    for fo in region_meta.regions:
        if r.failover_region == fo.region:
            print("[failover mapping] %s => %s" % (r.region, fo.region))
            fo_region = region.FailoverRegion(r.region, r.latitude, r.longitude, fo.region, fo.latitude, fo.longitude)
            failover_regions.append(fo_region)

print("there are %d regions and %d failover_regions" % (len(region_meta.regions), len(failover_regions)))

# normally we'd use a "./templates" folder, but we only have a single template in top-level folder
env = Environment(loader=FileSystemLoader("."), trim_blocks=True)
template = env.get_template("azuremap.geojson.jinja-template")
regionsGeoJSON = template.render(regions=region_meta.regions, failover_regions=failover_regions)

# write out local file
print("[writing] azuremap.geojson")
f = open('azuremap.geojson', 'w')
f.write(regionsGeoJSON)
f.close()
