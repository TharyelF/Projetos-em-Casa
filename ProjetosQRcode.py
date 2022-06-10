import qrcode

imagem = qrcode.make("https://youtube.com.br")
imagem.save("qrcode.jpg")

