import cv2

def resize_frame(frame, max_width=800, max_height=600):
  # 프레임의 가로, 세로 크기를 가져옴
  h, w = frame.shape[:2]
  
  # 프레임의 가로, 세로 비율 계산
  aspect_ratio = w / h

  # 프레임의 크기를 조정
  if w > max_width or h > max_height:
    if aspect_ratio > 1:
      new_width = max_width
      new_height = int(new_width / aspect_ratio)
    else:
      new_height = max_height
      new_width = int(new_height * aspect_ratio)
    
    frame = cv2.resize(frame, (new_width, new_height))
  
  return frame

def cartoon_filter(frame):
  frame = resize_frame(frame)
  h, w = frame.shape[:2]
  frame = cv2.resize(frame, (w//2, h//2))

  blr = cv2.bilateralFilter(frame, -1, 20, 7)
  edge = 255 - cv2.Canny(frame, 80, 120)
  edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

  dst = cv2.bitwise_and(blr, edge)
  dst = cv2.resize(dst, (w, h), interpolation=cv2.INTER_NEAREST)

  return dst

# 비디오 파일 경로 설정
video_path = 'video\bad_sample3.mp4'

# 비디오 로드
cap = cv2.VideoCapture(video_path)

cartoon_mode = False

while True:
  ret, frame = cap.read()
  if not ret:
    break
  
  if cartoon_mode:
    frame = cartoon_filter(frame)
  else:
    frame = resize_frame(frame)
  
  cv2.imshow('video', frame)
  key = cv2.waitKey(30)

  if key == 27:  # ESC 키를 누르면 종료
    break
  elif key == ord('1'):  # '1' 키를 누르면 카툰 필터로 변경
    cartoon_mode = not cartoon_mode

cap.release()
cv2.destroyAllWindows()
