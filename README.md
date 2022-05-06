功能敘述:
Forked from [aspotton/python-v4l2](https://github.com/aspotton/python-v4l2) <br>
For Linux OS - OpenCV 使用Camera的臨時替代方案


python-v4l2
===========

V4l2 (video4linux2) API,

基本範例: 開啟Video裝置撈裝置資訊:

    #python3
    >>> import v4l2
    >>> import fcntl
    >>> vd = open('/dev/video0', 'w')
    >>> cp = v4l2.v4l2_capability()
    >>> fcntl.ioctl(vd, v4l2.VIDIOC_QUERYCAP, cp)
    0
    >>> cp.driver
    'uvcvideo'
    >>> cp.card
    'USB 2.0 Camera'
