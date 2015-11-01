#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"

using namespace std;
using namespace cv;

Mat src; Mat dst;
char window_name1[] = "Unprocessed Image";
char window_name2[] = "Processed Image";

int main( int argc, char** argv )
{
    IplImage * pInpImg = 0;
    
    // Load an image from file - change this based on your image name
    pInpImg = cvLoadImage("cat.jpg", CV_LOAD_IMAGE_UNCHANGED);
    if(!pInpImg)
    {
        fprintf(stderr, "failed to load input image\n");
        return -1;
    }
    
    // Write the image to a file with a different name,
    // using a different image format -- .png instead of .jpg
    if( !cvSaveImage("my_image_copy.png", pInpImg) )
    {
        fprintf(stderr, "failed to write image file\n");
    }
    
    // Remember to free image memory after using it!
    cvReleaseImage(&pInpImg);
    
    return 0;
}