import geocode

scope_full = "All Windows Azure Services"
scope_cdn = "CDN"
scope_default = scope_full
status_production = "Production"
status_preview = "Public Preview"
status_announced = "Announced"
status_default = status_production


class FailoverRegion:
    def __init__(self, region, region_latitude, region_longitude, fo_region, fo_region_latitude, fo_region_longitude):
        self.region = region
        self.region_latitude = region_latitude
        self.region_longitude = region_longitude
        self.fo_region = fo_region
        self.fo_region_latitude = fo_region_latitude
        self.fo_region_longitude = fo_region_longitude


class Region:
    def __init__(self, geo, region, location, failover_region, scope=scope_default, status=status_default):
        self.geo = geo
        self.region = region
        self.location = location
        self.failover_region = failover_region
        self.scope = scope
        self.status = status
        self.latitude, self.longitude = self.geocode()

    def geocode(self):
        return geocode.geocode(self.location)

