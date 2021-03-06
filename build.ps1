echo "[BEGIN]"
Get-Date

python generate_geojson.py
echo "[writing] azuremap.topojson"
topojson -p -o azuremap.topojson azuremap.geojson

$geo = (Get-Item .\azuremap.geojson).Length
$topo = (Get-Item .\azuremap.topojson).Length
$perc= [Decimal]::Round(($topo/$geo)*100)
echo "TopoJSON file size ($topo) is $perc% of GeoJSON file size ($geo)"

echo "[saving back to azuremap github repo]"
git commit -a -m "update"
git push 

echo "[saving back to blob storage]"
python upload.py

echo "[saving map files back to github gist]"
copy .\azuremap.geojson ..\azuremap.gist
copy .\azuremap.topojson ..\azuremap.gist
copy .\region_meta.json ..\azuremap.gist

pushd ..\azuremap.gist
git commit -a -m "regenerated from source"
git push gist master
echo "Consider 'git pull gist master' if there are conflicts."
popd

Get-Date
echo "[ALL DONE]"
