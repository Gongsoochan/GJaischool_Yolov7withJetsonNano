import cv2
import json
import numpy as np

def json_to_rle(json_file_path, result_path):
    # JSON 데이터를 읽어서 이진 마스크 생성
    with open(json_file_path, 'r', encoding = 'utf-8') as json_file:
        json_data = json.load(json_file)

    shapes = json_data.get('shapes', [])
    image_width = json_data.get('imageWidth', 0)
    image_height = json_data.get('imageHeight', 0)

    if image_width <= 0 or image_height <= 0:
        print("Invalid image dimensions.")
        return

    # Create a binary mask as a NumPy array
    binary_mask = np.zeros((image_height, image_width), dtype=np.uint8)

    for shape in shapes:
        label = shape.get('label', '')
        if label == 'building':
            points = shape.get('points', [])
            if points:
                polygon = np.array(points, dtype=np.int32)
                cv2.fillPoly(binary_mask, [polygon], 1)

    # # Display the binary mask
    # plt.imshow(binary_mask, cmap='gray')
    # plt.title('Binary Mask')
    # plt.axis('off')
    # plt.show()

    # Save the binary mask as a PNG file
    binary_mask_filepath = result_path + json_file_path.replace("./TRAIN","RLE_from_json")
    binary_mask_filepath = binary_mask_filepath.replace(".json",".png")
    # print(binary_mask_filepath)

    cv2.imwrite(binary_mask_filepath, binary_mask * 255)  # Save as a binary mask (0 or 255)

    print("Json File To RLE Mask 변환 완료")

json_file_path = "C:/Users/gjaischool/study_is_good/final_project/091.승용 자율주행차 야간 자동차 전용도로 데이터/01.데이터/Training/01.원천데이터/18_200235_220616_meta_data.json"
result_path = "./"

json_to_rle(json_file_path, result_path)