
cd ./R/

echo "Generating punnet square..."

Rscript ./gameteFreq_to_Punnet.r

cd ../Python/

echo "Collapsing punnet square's gametes..."

python ./punnet_to_collpaseGametes.py

echo "Generating final gamete frequency equations..."

python ./collapseGametes_to_collectPunnetGametes.py

cp ./final_gamete_frequencies.tsv ../data/

