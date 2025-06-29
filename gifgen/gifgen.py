import contextlib

from PIL import Image, ImageOps


def create_gif(
        image_paths, 
        output_gif_path,
        *,
        duration=100,
        loop=0,
        stretch=False,
        width=512,
        height=512,
        ):
    '''
    Create a GIF from a list of image paths.

    Args:
        image_paths (list): A list of image paths.
        output_gif_path (str): The path where the output GIF will be saved to.
        duration (int): Duration of each frame in milliseconds.
        loop (int): Number of times the GIF should loop.
        stretch (bool): Whether to stretch images to fit the frame size.
        width (int): Width of the output GIF.
        height (int): Height of the output GIF.
    '''
    with contextlib.ExitStack() as stack:
        images = [stack.enter_context(Image.open(image_path))
                  for image_path in image_paths]
        if not images:
            raise Exception('No images was fed to create GIF.')
        if stretch:
            images = [image.resize((width, height)) for image in images]
        else:
            images = list(map(
                lambda im: fit_image(im, width=width, height=height),
                images,
            ))
        images[0].save(
            output_gif_path,
            save_all=True,
            append_images=images[1:],
            duration=duration,
            loop=loop,
        )


def fit_image(image: Image.Image, *, width, height):
    '''
    Fit image to frame before generating GIF.
    
    Args:
        image (PIL.Image.Image): Original image.
        width (int): Width of the new image.
        height (int): Height of the new image.
    
    Returns:
        (Image): new image.
    '''
    w, h = image.size
    orig_ratio = w / h
    new_ratio = width / height
    if orig_ratio == new_ratio:
        return image.resize((width, height))
    if orig_ratio < new_ratio:
        image_width = round(w * height / h)
        left = round((width - image_width) / 2)
        top = 0
        image_width = width - 2 * left
        image = image.resize((image_width, height)) # * height / h
    else:
        image_height = round(h * width / w)
        left = 0
        top = round((height - image_height) / 2)
        image_height = height - 2 * top
        image = image.resize((width, image_height)) # * width / w
    result = Image.new(image.mode, (width, height))
    result.paste(image, (left, top))
    return result
