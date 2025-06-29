# GIFGen

Simple tool to create GIFs from image files.

## Getting Started

You can setup this on your Python 3 environment as easy as possible.

### Prerequisites

- Python 3
- Pip
- Pillow (PIL)

### Installing

```bash
pip install git+https://github.com/hnthap/gifgen.git
```

After installing, you can simply use it in your code as

```python
from gifgen import create_gif

image_paths = ['a.png', 'b.jpg']
output = 'out'  # Save as out.gif

create_gif(image_paths, output, width=512, height=512, duration=100)  # Duration in ms
```

Or you can run in CLI (see [cli.py](./cli.py)):

```bash
# Make out.gif from image files from the folder "images"
# You need to replace "./cli.py" with the actual path to "cli.py"
python ./cli.py images/ out.gif -d 500 --width 512 --height 512
```

## Contributing

Please contribute if you want to improve it! You just need to fork, commit your edit and make a pull request.

## Versioning

We use [Semantic Versioning](http://semver.org/) for versioning. For the versions
available, see the [tags on this
repository](https://github.com/hnthap/gifgen/tags).

## Authors

See the list of
[contributors](https://github.com/hnthap/gifgen/contributors)
who participated in this project.

## License

This project is licensed under the [CC0 1.0 Universal](LICENSE) Creative Commons License - see the [LICENSE.md](LICENSE) file for details.

<!-- ## Acknowledgments -->
