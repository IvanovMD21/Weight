from PIL import Image, ImageDraw, ImageFont

def nom1():
    def crop_center(pil_img, crop_width: int, crop_height: int) -> Image:
        img_width, img_height = pil_img.size
        return pil_img.crop(((img_width - crop_width) // 2,
                             (img_height - crop_height) // 2,
                             (img_width + crop_width) // 2,
                             (img_height + crop_height) // 2))

    im = Image.open('dr.jpg')
    im_new = crop_center(im, 200, 200)
    im_new.save('dr.jpg', quality=95)
    im_new.show()


def nom2():
    party = {
        "НГ" : "year.jpg",
        "8 марта":"mart.jpg",
        "23 февраля":"feb.jpg"
    }
    x = input("введите праздник: ")
    for key in party:
        if key == x:
            print("Открытка загружается")
            y = Image.open(party[key])
            y.show()

def nom3():
    party = Image.open('mart.jpg')
    imdraw = ImageDraw.Draw(party)
    x = input("введите имя: ")
    text = str(x) + ', поздравляю! '
    font = ImageFont.truetype("SuperWebcomicBros_Rusbyyakustick_-Regular_0.ttf", size = 50)
    y = imdraw.textsize(text, font=font)
    z = party.size
    w = (z[0] // 2) - (y[0] // 2)
    imdraw.text((w, 10), text, font=font, fill=("#ff0000"))
    party.save("newmart.png")
    party.show()

nom3()