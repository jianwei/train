python3 format.py

./opencv_createsamples -vec pos.vec  -info pos.txt -num 828 -w 40 -h 40

./opencv_traincascade -data xml -vec pos.vec -bg neg.txt -numPos 800 -numNeg 1000 -numStages 100 -w 40 -h 40 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -mode ALL


git fetch --all &&  git reset --hard origin/main && git pull