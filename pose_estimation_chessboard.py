import numpy as np
import cv2 as cv

# The given video and calibration data
input_file = 'chessboard.avi'
K = np.array([[434.20154504, 0, 476.69359916], 
              [0, 432.83771324, 290.20247331],   
              [0, 0, 1]] )
dist_coeff = np.array([-2.88706447e-01, 1.04936709e-01, -3.03034020e-04, 2.50615605e-04, -1.90077401e-02])
board_pattern = (10, 7)
board_cellsize = 0.025
board_criteria = cv.CALIB_CB_ADAPTIVE_THRESH + cv.CALIB_CB_NORMALIZE_IMAGE + cv.CALIB_CB_FAST_CHECK

# Open a video
video = cv.VideoCapture(input_file)
assert video.isOpened(), 'Cannot read the given input, ' + input_file


text_lower1 = board_cellsize * np.array([[0, 2, 0], [0, 4, 0]]) # 1
text_upper1 = text_lower1 + board_cellsize * np.array([0, 0, -1])
text_lower2 = board_cellsize *np.array([[1, 2, 0], [1, 4, 0], [2, 4, 0], [2,3, 0], [1, 3, 0]]) # 6
text_upper2 = text_lower2 + board_cellsize *np.array([0, 0, -1])
text_lower3 = board_cellsize *np.array([[3,2,0],[3,4,0]]) # 1
text_upper3 = text_lower3 + board_cellsize *np.array([0, 0, -1])
text_lower4 = board_cellsize *np.array([[4,2,0],[4,4,0],[5,4,0],[5,2,0]]) # 0
text_upper4 = text_lower4 + board_cellsize *np.array([0, 0, -1])
text_lower5 = board_cellsize *np.array([[6,2,0],[6,4,0]]) # 1
text_upper5 = text_lower5 +board_cellsize * np.array([0, 0, -1])
text_lower6 = board_cellsize *np.array([[7,2,0],[7,3,0],[8,3,0],[8,2,0],[8,4,0], [8,3,0],[7,3,0],[7,2,0]])
text_upper6 = text_lower6 + board_cellsize *np.array([0, 0, -1])
text_lower7 = board_cellsize *np.array([[9,2,0],[9,4,0]])
text_upper7 = text_lower7 + board_cellsize *np.array([0, 0, -1])
text_lower8 = board_cellsize *np.array([[10,2,0],[10,4,0]])
text_upper8 = text_lower8 + board_cellsize *np.array([0, 0, -1])

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
        line_lower1, _ = cv.projectPoints(text_lower1, rvec, tvec, K, dist_coeff)
        line_upper1, _ = cv.projectPoints(text_upper1, rvec, tvec, K, dist_coeff)
        cv.polylines(img, [np.int32(line_lower1)], True, (255, 0, 0), 2)
        cv.polylines(img, [np.int32(line_upper1)], True, (0, 0, 255), 2)
        for b, t in zip(line_lower1, line_upper1):
            cv.line(img, np.int32(b.flatten()), np.int32(t.flatten()), (0, 255, 0), 2)
            
        line_lower2, _ = cv.projectPoints(text_lower2, rvec, tvec, K, dist_coeff)
        line_upper2, _ = cv.projectPoints(text_upper2, rvec, tvec, K, dist_coeff)
        cv.polylines(img, [np.int32(line_lower2)], True, (255, 0, 0), 2)
        cv.polylines(img, [np.int32(line_upper2)], True, (0, 0, 255), 2)
        for b, t in zip(line_lower2, line_upper2):
            cv.line(img, np.int32(b.flatten()), np.int32(t.flatten()), (0, 255, 0), 2)
            
        line_lower3, _ = cv.projectPoints(text_lower3, rvec, tvec, K, dist_coeff)
        line_upper3, _ = cv.projectPoints(text_upper3, rvec, tvec, K, dist_coeff)
        cv.polylines(img, [np.int32(line_lower3)], True, (255, 0, 0), 2)
        cv.polylines(img, [np.int32(line_upper3)], True, (0, 0, 255), 2)
        for b, t in zip(line_lower3, line_upper3):
            cv.line(img, np.int32(b.flatten()), np.int32(t.flatten()), (0, 255, 0), 2)
            
        line_lower4, _ = cv.projectPoints(text_lower4, rvec, tvec, K, dist_coeff)
        line_upper4, _ = cv.projectPoints(text_upper4, rvec, tvec, K, dist_coeff)
        cv.polylines(img, [np.int32(line_lower4)], True, (255, 0, 0), 2)
        cv.polylines(img, [np.int32(line_upper4)], True, (0, 0, 255), 2)
        for b, t in zip(line_lower4, line_upper4):
            cv.line(img, np.int32(b.flatten()), np.int32(t.flatten()), (0, 255, 0), 2)
            
        line_lower5, _ = cv.projectPoints(text_lower5, rvec, tvec, K, dist_coeff)
        line_upper5, _ = cv.projectPoints(text_upper5, rvec, tvec, K, dist_coeff)
        cv.polylines(img, [np.int32(line_lower5)], True, (255, 0, 0), 2)
        cv.polylines(img, [np.int32(line_upper5)], True, (0, 0, 255), 2)
        for b, t in zip(line_lower5, line_upper5):
            cv.line(img, np.int32(b.flatten()), np.int32(t.flatten()), (0, 255, 0), 2)
            
        line_lower6, _ = cv.projectPoints(text_lower6, rvec, tvec, K, dist_coeff)
        line_upper6, _ = cv.projectPoints(text_upper6, rvec, tvec, K, dist_coeff)
        cv.polylines(img, [np.int32(line_lower6)], True, (255, 0, 0), 2)
        cv.polylines(img, [np.int32(line_upper6)], True, (0, 0, 255), 2)
        for b, t in zip(line_lower6, line_upper6):
            cv.line(img, np.int32(b.flatten()), np.int32(t.flatten()), (0, 255, 0), 2)
            
        line_lower7, _ = cv.projectPoints(text_lower7, rvec, tvec, K, dist_coeff)
        line_upper7, _ = cv.projectPoints(text_upper7, rvec, tvec, K, dist_coeff)
        cv.polylines(img, [np.int32(line_lower7)], True, (255, 0, 0), 2)
        cv.polylines(img, [np.int32(line_upper7)], True, (0, 0, 255), 2)
        for b, t in zip(line_lower7, line_upper7):
            cv.line(img, np.int32(b.flatten()), np.int32(t.flatten()), (0, 255, 0), 2)
            
        line_lower8, _ = cv.projectPoints(text_lower8, rvec, tvec, K, dist_coeff)
        line_upper8, _ = cv.projectPoints(text_upper8, rvec, tvec, K, dist_coeff)
        cv.polylines(img, [np.int32(line_lower8)], True, (255, 0, 0), 2)
        cv.polylines(img, [np.int32(line_upper8)], True, (0, 0, 255), 2)
        for b, t in zip(line_lower8, line_upper8):
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