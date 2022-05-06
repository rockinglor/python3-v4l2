import v4l2
import fcntl
[TODO:]

''' Mode 1
cam = v4l2capture.Camera_device("/dev/video0")
width,height = cam.GetSize()
cam.SetSize(2592, 1944)
cam.SetFmt(v4l2capture.YUV2)
#cam.SetFmt(v4l2capture.MJPG)

cam.Open()
image_data = cam.read()
cam.Close()
'''

''' Mode 2
cam.SetBufferSize()
cam.Run()
image_data = cam.Image
cam.Stop()
'''
