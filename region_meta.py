from region import *

### MAKE CHANGES TO THE LIST BELOW AS DATA CENTER INFORMATION EVOLVES ###
# Data centers belong to a Region. Regions belong to a Geo.
# The names of Regions and Geos are mostly GUESSES for the not-yet-production data centers.
regions = [
    # Geo, Region, Location (city), Failover Region, Scope, Status
    Region("Asia Pacific", "East Asia", "Hong Kong", "SE Asia"),
    Region("Asia Pacific", "SE Asia", "Singapore", "East Asia"),
    Region("Asia Pacific", "Shanghai China", "Shanghai China", "Beijing China", status=status_preview),
    Region("Asia Pacific", "Beijing China", "Beijing, China", "Shanghai China", status=status_preview),
    Region("Australia", "Australia East", "Sydney, New South Wales, Australia", "Australia SE", status=status_announced),
    Region("Australia", "Australia SE", "Melbourne, Victoria, Australia", "Australia East", status=status_announced),
    Region("South America", "Brazil South", "Brazil", "US South Central", status=status_preview),
    Region("Europe", "Europe West", "Amsterdam, Netherlands", "Europe North"),
    Region("Europe", "Europe North", "Dublin, Ireland", "Europe West"),
    Region("Japan", "Japan East", "Tokyo, Japan", "Japan West", status=status_announced),
    Region("Japan", "Japan West", "Kansai, Japan", "Japan East", status=status_announced),
    Region("United States", "US North Central", "Chicago, IL, USA", "US South Central"),
    Region("United States", "US South Central", "San Antonio, TX, USA", "US North Central"),
    Region("United States", "US East", "Bristow, Virginia, USA", "US West"),
    Region("United States", "US West", "San Francisco, California, USA", "US East"),
]
