python generate_geojson.py
echo "[writing] azuremap.topojson"
topojson -p -o azuremap.topojson azuremap.geojson
echo "[saving back to github]"
# git commit azuremap.topojson azuremap.geojson -m "update"
# git push gist master
# git push
echo "[ALL DONE]"

