
import numpy as np
import cv2 as cv

# The given video and calibration data
input_file = '../data/chess_board.mp4'
K = np.array([[700.5974796, 0., 629.0148821],
              [0., 700.8386952, 351.17970152],
              [0., 0., 1.]])
dist_coeff = np.array([3.52867762e-02, -1.45016454e-01, -1.13961659e-05, 4.40823950e-03, 2.21966160e-01])
board_pattern = (10, 7)
board_cellsize = 0.025
board_criteria = cv.CALIB_CB_ADAPTIVE_THRESH + cv.CALIB_CB_NORMALIZE_IMAGE + cv.CALIB_CB_FAST_CHECK

# Open a video
video = cv.VideoCapture(input_file)
assert video.isOpened(), 'Cannot read the given input, ' + input_file

# Prepare a 3D box for simple AR
box_lower = board_cellsize * np.array([[2, 1,  0], [2, 2,  0], [5, 2,  0], [5, 3,  0], 
                                       [2, 3,  0], [2, 6,  0], [6, 6,  0], [6, 5,  0], 
                                       [3, 5,  0], [3, 4,  0], [6, 4,  0], [6, 1,  0], 
                                       [2, 1,  0]])
box_upper = board_cellsize * np.array([[2, 1, -1], [2, 2, -1], [5, 2, -1], [5, 3, -1], 
                                       [2, 3, -1], [2, 6, -1], [6, 6, -1], [6, 5, -1], 
                                       [3, 5, -1], [3, 4, -1], [6, 4, -1], [6, 1, -1], 
                                       [2, 1, -1]])

# Prepare 3D points on a chessboard
obj_points = board_cellsize * np.array([[c, r, 0] for r in range(board_pattern[1]) for c in range(board_pattern[0])])

# Run pose estimation
while True:
    # Read an image from the video
    valid, img = video.read()
    if not valid:
        break

    # Estimate the camera pose
    complete, img_points = cv.findChessboardCorners(img, board_pattern, board_criteria)
    if complete:
        ret, rvec, tvec = cv.solvePnP(obj_points, img_points, K, dist_coeff)

        # Draw the box on the image
        line_lower, _ = cv.projectPoints(box_lower, rvec, tvec, K, dist_coeff)
        line_upper, _ = cv.projectPoints(box_upper, rvec, tvec, K, dist_coeff)
        cv.polylines(img, [np.int32(line_lower)], True, (255, 0, 0), 2)
        cv.polylines(img, [np.int32(line_upper)], True, (0, 0, 255), 2)
        for b, t in zip(line_lower, line_upper):
            cv.line(img, np.int32(b.flatten()), np.int32(t.flatten()), (0, 255, 0), 2)

        # Print the camera position
        R, _ = cv.Rodrigues(rvec) # Alternative) scipy.spatial.transform.Rotation
        p = (-R.T @ tvec).flatten()
        info = f'XYZ: [{p[0]:.3f} {p[1]:.3f} {p[2]:.3f}]'
        cv.putText(img, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))

    # Show the image and process the key event
    cv.imshow('Pose Estimation (Chessboard)', img)
    key = cv.waitKey(10)
    if key == ord(' '):
        key = cv.waitKey()
    if key == 27: # ESC
        break

video.release()
cv.destroyAllWindows()
