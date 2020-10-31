import pyzed.sl as sl
import cv2
import sys

# Create a ZED camera object
zed = sl.Camera()

# Enable recording with the filename specified in argument
input_path = "myVideoFile.svo"
err = zed.open()
init_parameters = sl.InitParameters()
init_parameters.set_from_svo_file(input_path)
# err = zed.enable_recording(sl.RecordingParameters("myVideoFile.svo", sl.SVO_COMPRESSION_MODE.H264))

svo_image = sl.Mat()
while True:
    if zed.grab() == sl.ERROR_CODE.SUCCESS:
    # Read side by side frames stored in the SVO
      zed.retrieve_image(svo_image, sl.VIEW.SIDE_BY_SIDE)
      # Get frame count
      svo_position = zed.get_svo_position();
      print(svo_position)
    elif zed.grab() == sl.ERROR_CODE.END_OF_SVOFILE_REACHED:
      print("SVO end has been reached. Looping back to first frame")
      zed.set_svo_position(0)

# Disable recording
zed.disable_recording()