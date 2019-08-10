import os
import sys
from glob import glob

from PIL import Image


def resize_images(images_dir, image_save_dir, image_size):

    os.makedirs(image_save_dir, exist_ok=True)

    image_paths = glob(os.path.join(images_dir, '*'))

    for img_path in image_paths:
        image = Image.open(img_path)
        image = image.convert('RGB')
        image.thumbnail([image_size,image_size])
        back_ground = Image.new("RGB", (image_size,image_size), color=(255,255,255))
        back_ground.paste(image)
        save_path = os.path.join(image_save_dir, os.path.basename(img_path))
        end_index = save_path.rfind('.')
        save_path = save_path[0:end_index]+'.jpg'
        print('save',save_path)
        back_ground.save(save_path,'JPEG')


def _main():
    images_dir = 'image/'  # input directory
    image_save_dir = 'resize_image/'  # output directory
    image_size = 320
    if len(sys.argv) > 1:
        input_shape = (int(sys.argv[1]),int(sys.argv[1]))

    resize_images(images_dir=images_dir, image_save_dir=image_save_dir, image_size=image_size)


if __name__ == '__main__':
    _main()
