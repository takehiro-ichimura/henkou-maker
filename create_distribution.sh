pyinstaller ./src/main.py --onefile
rm henkou_maker_distribution.zip
mkdir henkou_maker_distribution
cp -r ./dist ./henkou_maker_distribution
cp -r ./input ./henkou_maker_distribution
cp -r ./output ./henkou_maker_distribution
cp -r ./templates ./henkou_maker_distribution
cp ./README.txt ./henkou_maker_distribution
zip -r henkou_maker_distribution.zip henkou_maker_distribution  -x "*.DS_Store" "*__MACOSX*"
rm -r henkou_maker_distribution