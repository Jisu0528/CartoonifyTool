import cv2
import os

def resize_image(img, max_width=800, max_height=600):
  # 이미지의 가로, 세로 크기를 가져옴
  h, w = img.shape[:2]
  
  # 이미지의 가로, 세로 비율 계산
  aspect_ratio = w / h

  # 이미지의 크기를 조정
  if w > max_width or h > max_height:
    if aspect_ratio > 1:
      new_width = max_width
      new_height = int(new_width / aspect_ratio)
    else:
      new_height = max_height
      new_width = int(new_height * aspect_ratio)
    
    img = cv2.resize(img, (new_width, new_height))
  
  return img

def cartoon_filter(img):
  img = resize_image(img)
  h, w = img.shape[:2]
  img2 = cv2.resize(img, (w//2, h//2))

  blr = cv2.bilateralFilter(img2, -1, 20, 7)
  edge = 255 - cv2.Canny(img2, 80, 120)
  edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

  dst = cv2.bitwise_and(blr, edge)
  dst = cv2.resize(dst, (w, h), interpolation=cv2.INTER_NEAREST)

  return dst

# 이미지 폴더 경로 설정
image_folder = "image"

# 이미지 파일 목록 가져오기
image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

# 이미지 파일 목록에서 확장자가 이미지 파일인 것만 필터링
image_files = [img_file for img_file in image_files if os.path.splitext(img_file)[1].lower() in ['.jpg', '.png', '.jpeg']]

# 처음에는 첫 번째 이미지 파일을 로드하여 시작
current_image_index = 0
current_image = cv2.imread(image_files[current_image_index])

cartoon_mode = False

while True:
  if cartoon_mode:
    current_image = cartoon_filter(current_image)
  else:
    current_image = resize_image(current_image)
  
  cv2.imshow('image', current_image)
  key = cv2.waitKey(0)

  if key == 27:  # ESC 키를 누르면 종료
    break
  elif key == ord(' '):  # 스페이스바를 누르면 다음 이미지로 전환
    current_image_index = (current_image_index + 1) % len(image_files)
    current_image = cv2.imread(image_files[current_image_index])
    cartoon_mode = False  # 이미지를 변경할 때는 카툰 필터 해제
  elif key == ord('1'):  # `1` 키를 누르면 카툰 필터로 변경
    cartoon_mode = not cartoon_mode

cv2.destroyAllWindows()
