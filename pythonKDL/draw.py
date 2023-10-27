from PIL import Image, ImageDraw, ImageFont

def draw_(text_data: str, file: str) -> None:



# Kích thước hình ảnh 
    image_width = 65
    image_height = 84

# Tạo một hình ảnh đen
    image = Image.new('RGB', (image_width, image_height), color='black')

# Tạo một đối tượng vẽ
    draw = ImageDraw.Draw(image)

# Chọn một phông chữ (font) và kích thước
    font = ImageFont.load_default()
    font_size = 18

# Tạo một biến để theo dõi vị trí hiện tại trong hình ảnh
    current_x = 10
    current_y = 10

# Tách dữ liệu văn bản thành các dòng và vẽ chúng lên hình ảnh
    for line in text_data.splitlines():
        draw.text((current_x, current_y), line, fill='green' , font=font)
        current_y += font_size

# Lưu hình ảnh thành tệp PNG
    image.save(file)


# print("So buoc giai la:",len(result) - 1) 
#     for i in range(len(result)):
#         #print("Buoc:",i)
#         kq = convert_list(result[i])
#         dt = f"STEP {i} :\n"
#         for u in range(len(kq)):
#             for v in range(len(kq)):
#                 #print(kq[u][v],end=" ")
#                 dt += str(kq[u][v]) + " "
#             dt += '\n'
#         file = "Buoc" + str(i) + ".png"
#         draw.draw_(dt,file)