import cv2
import os
import glob

# 'make_video' 폴더 내의 모든 png 이미지를 상대 경로로 가져옵니다.
folder_path = "make_video"
images = glob.glob(os.path.join(folder_path, "*.png"))

# 파일 이름에 따라 정렬합니다.
images.sort()

# 첫 번째 이미지를 읽어서 비디오 프레임의 크기를 결정합니다.
first_image = cv2.imread(images[0])
if first_image is None:
    raise ValueError(f"Cannot read the first image from the folder {folder_path}")

height, width, layers = first_image.shape

# 비디오 코덱과 비디오 라이터를 설정합니다.
video_name = "seoyoung_babo.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(video_name, fourcc, 10, (width, height))

# 각 이미지를 비디오에 씁니다.
for image_file in images:
    img = cv2.imread(image_file)
    if img is not None:
        video.write(img)
    else:
        print(f"Warning: could not read image {image_file} - it's being skipped.")

# 자원을 해제합니다.
video.release()
cv2.destroyAllWindows()

print(f"Video saved as {video_name}")
