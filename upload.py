from azure.storage import *

storage_account_name = 'azuremap' # storage key in file in parent directory called <storage_account_name>.storagekey
storage_account_key = open(r'../%s.storagekey' % storage_account_name, 'r').read() 
//print(storage_account_key)

blob_service = BlobService(account_name=storage_account_name, account_key=storage_account_key)
storage_container_name = 'maps'
blob_service.create_container(storage_container_name)
blob_service.set_container_acl(storage_container_name, x_ms_blob_public_access='container')

for file_name in [r'azuremap.geojson', r'azuremap.topojson']:
	myblob = open(file_name, 'r').read()
	blob_name = file_name
	blob_service.put_blob(storage_container_name, blob_name, myblob, x_ms_blob_type='BlockBlob')
	blob_service.set_blob_properties(storage_container_name, blob_name, x_ms_blob_content_type='application/json', x_ms_blob_cache_control='public, max-age=3600')

# Show a blob listing which now includes the blobs just uploaded
blobs = blob_service.list_blobs(storage_container_name)
print("Directory listing of all blobs in container '%s'" % storage_container_name)
for blob in blobs:
    print(blob.url)

# format for blobs is: <account>.blob.core.windows.net/<container>/<file>
# example blob for us: pytool.blob.core.windows.net/pyfiles/clouds.jpeg
