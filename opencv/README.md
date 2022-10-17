python3 format.py

./opencv_createsamples -vec pos.vec  -info pos.txt -num 828 -w 40 -h 40

./opencv_traincascade -data xml -vec pos.vec -bg neg.txt -numPos 800 -numNeg 1000 -numStages 32 -w 40 -h 40 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -mode ALL


git fetch --all &&  git reset --hard origin/main && git pull


opencv_traincascade：
-data
训练的分类器的存储目录
-vec
正样本文件，由open_createsamples.exe生成，正样本文件后缀名为.vec
-bg
负样本说明文件，主要包含负样本文件所在的目录及负样本文件名
-numPos
每级分类器训练时所用到的正样本数目，应小于vec文件中正样本的数目，具体数目限制条件为：numPos+（numStages-1）*numPos*（1-minHitRate）<=vec文件中正样本的数目
-numNeg
每级分类器训练时所用到的负样本数目，可以大于-bg指定的图片数目
-numStages
训练分类器的级数，强分类器的个数
-precalcValBufSize
缓存大小，用于存储预先计算的特征值，单位MB
-precalcIdxBufSize
缓存大小，用于存储预先计算的特征索引，单位MB
-baseFormatSave
仅在使用Haar特征时有效，如果指定，级联分类器将以老格式存储



numPos+（numStages-1）*numPos*（1-minHitRate）<=正样本
正负样本比例1:2.5~1:3，曾经有篇文章中说，为了减小false positive ，可以加大负样本数目。


