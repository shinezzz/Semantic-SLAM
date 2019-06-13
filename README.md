### Semantic Map
    这个程序其实并没有过多关注位姿，着重点在Map部分。主要是基于高博的[一起来做RGBD-SLAM](https://www.cnblogs.com/gaoxiang12/p/4633316.html)以及[Mask R-CNN](https://github.com/matterport/Mask_RCNN)进行创造。
 
#### REQUREMENT
    1. 需要安装：`pcl`,`opencv2`,`g2o`。
    2. 原有数据集顺序命名，如果要用TUM数据集，参考`script`生成`associtaion.txt`文件。
    3. 在TUM数据集上，跟踪容易丢失，采用自己用kinect仿照TUM录制数据集。录制参考[我的博客](https://blog.csdn.net/shinef/article/details/90573486)
    4. 处理好数据得到`rgb`,`depth`两个彩色图和深度图像文件夹，和高博提供的数据集用顺序命名，该图像采用时间戳命名。稠密建图的图像输入方式也改了，如`slamTumDesn.cpp`
    5. 利用Mask R-CNN处理`rgb`中的每一帧图像，输出根据类染色的图片`rgb_mask`,[参考Repository](https://github.com/shinezzz/Test_MASK_RCNN)中的`myTest`，在`script/MaskRCNN`也有处理代码，就是调用Mask R-CNN进行相应输出。配置Mask R-CNN[环境参考原文](https://github.com/matterport/Mask_RCNN)
    6. 最终执行的时候修改参数文件`parameters.txt`相应的参数，比如路径等等参数。

#### contribution
    1. 稠密建图的基础上融合语义信息进行稠密语义地图构建:稠密`slamDense.cpp`,语义`slam.cpp`
    2. 支持TUM数据集建图:稠密`slamTumDense.cpp`,语义`slamTum.cpp`，执行这两个文件需要输入参数
    slamTum.cpp 读取处理tum数据集
```bash
    ./bin/slamTum PATH/TO/ASSOCIATE
```
#### TODO
    本来向通过C++程序里直接调用Mask R-CNN，也参考了`Dyna SLAM`等实现一个程序里实现调用的，还是没有成功，如果大佬不吝指教，不慎感激。
