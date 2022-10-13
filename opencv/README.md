opencv_createsamples -vec pos.vec  -info pos.txt -num 50 -w 40 -h 40

opencv_traincascade -data xml -vec pos.vec -bg neg.txt -numPos 30 -numNeg 100 -numStages 15 -w 40 -h 40 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -mode ALL
