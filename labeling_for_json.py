from PIL import Image, ImageDraw
import json

def draw_bounding_boxes(json_file_path, image_file_path, output_image_path):
    # JSON 파일 읽기
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    # 이미지 열기
    image = Image.open(image_file_path)
    draw = ImageDraw.Draw(image)

    # JSON 데이터의 "row" 항목 반복
    for item in json_data["row"]:
        # 바운딩 박스 정보 추출
        points1 = [int(point) for point in item["points1"].split(",")]
        points2 = [int(point) for point in item["points2"].split(",")]
        points3 = [int(point) for point in item["points3"].split(",")]
        points4 = [int(point) for point in item["points4"].split(",")]
        
        # 바운딩 박스 그리기
        draw.polygon(points1 + points2 + points3 + points4, outline="red")

    # 바운딩 박스가 그려진 이미지 저장
    image.save(output_image_path)

    print(f"바운딩 박스가 그려진 이미지 저장 완료: {output_image_path}")

json_file_path = "C:/Users/gjaischool/study_is_good/final_project/adas_data/validation_data/라벨링데이터/주간/주간_성남02/성남_주간_2021-10-14-17-15-59/Front_View_CMR/2021-10-14-17-15-59_Front_1634199385350.png.json"
image_file_path = "C:/Users/gjaischool/study_is_good/final_project/adas_data/validation_data/원천데이터/주간/주간_성남02/성남_주간_2021-10-14-17-15-59/Front_View_CMR/2021-10-14-17-15-59_Front_1634199385350.png"
output_image_path = "./test4.png"

draw_bounding_boxes(json_file_path, image_file_path, output_image_path)
