python3 format.py

./opencv_createsamples -vec pos.vec  -info pos.txt -num 828 -w 40 -h 40

./opencv_traincascade -data xml -vec pos.vec -bg neg.txt -numPos 80 -numNeg 250 -numStages 10 -w 40 -h 40 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -mode ALL 


git fetch --all &&  git reset --hard origin/main && git pull


opencv_traincascade：
-data：指定保存训练结果的文件夹；

-vec:指定正样本集；

-bg:指定负样本的描述文件夹;

-numPos：指定每一级参与训练的正样本的数目（要小于正样本总数）；

-numNeg:指定每一级参与训练的负样本的数目（可以大于负样本图片的总数）；

-numStage:训练的级数；

-w:正样本的宽；-h:正样本的高；(必须与opencv_createsample中使用的-w和-h值一致)

-minHitRate:每一级需要达到的命中率（一般取值0.95-0.995）；

-maxFalseAlarmRate:每一级所允许的最大误检率；

-mode:使用Haar-like特征时使用，可选BASIC、CORE或者ALL；(ALL使用垂直和45度角旋转特征。)


正负样本比例1:2.5~1:3，为了减小false positive ，可以加大负样本数目。



cmake \
-D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D WITH_TBB=ON \
-D BUILD_NEW_PYTHON_SUPPORT=ON \
-D WITH_V4L=ON \
-D INSTALL_C_EXAMPLES=ON \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D BUILD_EXAMPLES=ON \
-D WITH_QT=ON \
-D WITH_OPENGL=ON \
-D WITH_CUDA=ON \
-D WITH_CUBLAS=ON \
-D OPENCV_DNN_CUDA=ON \
-D CUDA_NVCC_FLAGS=--expt-relaxed-constexpr \
-D WITH_CUDNN=ON ..


sudo make -j6
