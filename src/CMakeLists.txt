
# 增加PCL库的依赖
FIND_PACKAGE( PCL REQUIRED COMPONENTS common io visualization filters )
list(REMOVE_ITEM PCL_LIBRARIES "vtkproj4") # use this in Ubuntu 16.04

# 增加opencv的依赖
FIND_PACKAGE( OpenCV REQUIRED )

# 添加头文件和库文件
ADD_DEFINITIONS( ${PCL_DEFINITIONS} )
INCLUDE_DIRECTORIES( ${PCL_INCLUDE_DIRS}  )
LINK_LIBRARIES( ${PCL_LIBRARY_DIRS} )

# link_directories( /usr/lib/x86_64-linux-gnu/ )

# 添加g2o的依赖
# 因为g2o不是常用库，要添加它的findg2o.cmake文件
LIST( APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake_modules )
SET( G2O_ROOT /usr/local/include/g2o )
FIND_PACKAGE( G2O REQUIRED )
# CSparse
FIND_PACKAGE( CSparse REQUIRED )
INCLUDE_DIRECTORIES( ${G2O_INCLUDE_DIR} ${CSPARSE_INCLUDE_DIR} )

ADD_LIBRARY( slambase slamBase.cpp )
TARGET_LINK_LIBRARIES( slambase
    ${OpenCV_LIBS} 
    ${PCL_LIBRARIES}
    )

# ADD_EXECUTABLE( slamEnd slamEnd.cpp )
# TARGET_LINK_LIBRARIES( slamEnd
#     slambase
#     ${OpenCV_LIBS}
#     ${PCL_LIBRARIES}
#     g2o_core g2o_types_slam3d g2o_solver_csparse g2o_stuff g2o_csparse_extension ${CSPARSE_LIBRARY})

ADD_EXECUTABLE( slam slam.cpp )
TARGET_LINK_LIBRARIES( slam
    slambase
    ${OpenCV_LIBS}
    ${PCL_LIBRARIES}
    g2o_core g2o_types_slam3d g2o_solver_csparse g2o_stuff g2o_csparse_extension ${CSPARSE_LIBRARY})

ADD_EXECUTABLE( detectFeatures detectFeatures.cpp )
TARGET_LINK_LIBRARIES( detectFeatures 
slambase
${OpenCV_LIBS} 
${PCL_LIBRARIES} )
    
ADD_EXECUTABLE( slamTum slamTum.cpp )
TARGET_LINK_LIBRARIES( slamTum
    slambase
    ${OpenCV_LIBS}
    ${PCL_LIBRARIES}
    g2o_core g2o_types_slam3d g2o_solver_csparse g2o_stuff g2o_csparse_extension ${CSPARSE_LIBRARY})
ADD_EXECUTABLE( test test.cpp )
TARGET_LINK_LIBRARIES( test
    slambase
    ${OpenCV_LIBS}
    ${PCL_LIBRARIES}
    g2o_core g2o_types_slam3d g2o_solver_csparse g2o_stuff g2o_csparse_extension ${CSPARSE_LIBRARY})

