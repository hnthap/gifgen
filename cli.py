import argparse
import os
import warnings

from gifgen import create_gif


def cli(args):
    folder = args.folder
    output = args.output
    width = args.width
    height = args.height
    duration = args.duration
    image_extensions = ['.avif', '.jfif', '.jpeg', '.jpg', '.png', '.webp']
    image_names = sorted(os.listdir(folder))
    image_paths = []
    for name in image_names:
        if os.path.splitext(name)[-1].lower() in image_extensions:
            image_paths.append(os.path.join(folder, name))
        else:
            warnings.warn(
                'Encountered "%s", which is not recognized as an image.' % name
            )
    image_paths = list(filter(
        lambda path: os.path.splitext(path)[-1].lower() in image_extensions,
        image_paths,
    ))
    if os.path.exists(output):
        os.remove(output)
    create_gif(image_paths, output, width=width, height=height, duration=duration)


def parse_arguments():
    parser = argparse.ArgumentParser(prog='gifgen')
    parser.add_argument('folder', default='.', help='Image folder')
    parser.add_argument(
        'output', default='out', help='Output GIF name, without extension'
    )
    parser.add_argument('--width', type=int, default=512, help='GIF width')
    parser.add_argument('--height', type=int, default=512, help='GIF height')
    parser.add_argument(
        '--duration',
        '-d',
        type=int,
        default=100,
        help='Frame duration in milliseconds',
    )
    return parser.parse_args()


def validate_arguments(args):
    assert os.path.exists(args.folder), 'Input image folder is not exists'
    assert os.path.isdir(args.folder), 'Input image folder is not a folder'
    assert isinstance(args.width, int) and args.width > 0, 'Invalid GIF width'
    assert isinstance(args.height, int) and args.height > 0, \
        'Invalid GIF height'
    assert isinstance(args.duration, int) and args.duration > 0, \
        'Invalid GIF frame duration'


if __name__ == '__main__':
    args = parse_arguments()
    validate_arguments(args)
    cli(args)
