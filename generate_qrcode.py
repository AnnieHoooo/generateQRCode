import qrcode

# 定义您的网址
url = "https://www.loongspirit.com/"

# 创建qr代码实例
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# 添加网址到二维码
qr.add_data(url)
qr.make(fit=True)

# 创建一个图像并保存
img = qr.make_image(fill='black', back_color='white')
img.save("website_qr.png")
