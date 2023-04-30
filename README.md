# MyChessCalibration
체스보드 영상에 학번을 출력하는 간단한 AR 기법 실습입니다.   
Camera Calibration을 video~video3 로 수행하려고 했지만 수동 포커스에서도 인식되지 않아 부득이하게 chessboard.avi 예제파일을 그대로 사용했습니다.   
간단한 박스대신 학번을 출력하는것으로 변경했습니다.   ![image](https://user-images.githubusercontent.com/74591896/235347727-5fcdf681-d570-4087-ad35-65caebeb30a2.png)   
camera_calibration.py 에서 캘리브레이션 결과 K =   
[[434.20154504, 0, 476.69359916],   
[0, 432.83771324, 290.20247331],   
[0, 0, 1]]   
Distortion coefficient = [-2.88706447e-01, 1.04936709e-01, -3.03034020e-04, 2.50615605e-04, -1.90077401e-02]   
해당 값을 pose_estimation_chessboard.py 에 입력해 사용했습니다.   
학번을 출력하기위해 np.array 8개를 생성했고 이에 상응하는 upper도 8개 생성한 다음, Draw에서도 같은 작업을 8번 하도록 변경했습니다.   
![test](https://github.com/SeukCho/MyChessCalibration/blob/main/result.gif)   
실행 결과의 일부를 gif로 첨부했습니다.
