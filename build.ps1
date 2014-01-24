echo "[BEGIN]"

python generate_geojson.py
echo "[writing] azuremap.topojson"
topojson -p -o azuremap.topojson azuremap.geojson

$geo = (Get-Item .\azuremap.geojson).Length
$topo = (Get-Item .\azuremap.topojson).Length
$perc= [Decimal]::Round(($topo/$geo)*100)
echo "TopoJSON file size ($topo) is $perc% of GeoJSON file size ($geo)"

echo "[saving back to github]"
git commit -a -m "update"
git push gist master
git push github master

echo "[ALL DONE]"
