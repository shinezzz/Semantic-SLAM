
#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

#include "slamBase.h"

#include <pcl/filters/voxel_grid.h>
#include <pcl/filters/passthrough.h>
FRAME readFrame( int index, ParameterReader& pd );
int main(int argc, char** argv){
    ParameterReader pd;
    int startIndex  =   atoi( pd.getData( "start_index" ).c_str() );
    int endIndex    =   atoi( pd.getData( "end_index"   ).c_str() );
    string rgbDirMask   =   pd.getData("rgb_dir_mask");
    string rgbDirMaskExten = pd.getData("rgb_extension");
    int currIndex = startIndex; // 当前索引为currIndex
    FRAME currFrame = readFrame( currIndex, pd );
    currFrame.rgb = cv::imread(rgbDirMask+to_string(currIndex) + rgbDirMaskExten);
    cv::imshow("test",currFrame.rgb);
    cv::waitKey(0);

    return 0;
}
FRAME readFrame( int index, ParameterReader& pd )
{
    FRAME f;
    string rgbDir   =   pd.getData("rgb_dir");
    string depthDir =   pd.getData("depth_dir");
    
    string rgbExt   =   pd.getData("rgb_extension");
    string depthExt =   pd.getData("depth_extension");

    stringstream ss;
    ss<<rgbDir<<index<<rgbExt;
    string filename;
    ss>>filename;
    f.rgb = cv::imread( filename );

    ss.clear();
    filename.clear();
    ss<<depthDir<<index<<depthExt;
    ss>>filename;

    f.depth = cv::imread( filename, -1 );
    f.frameID = index;
    return f;
}