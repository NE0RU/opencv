import cv2, sys

# 입력 파일 지정
if len(sys.argv) <= 1:
    print("no input file")
    quit()
image_file = sys.argv[1]

# 출력 파일 이름
output_file = "./" + image_file.split('.')[0] + '-mosaic.' + image_file.split('.')[1]
mosaic_rate = 30

print(output_file)