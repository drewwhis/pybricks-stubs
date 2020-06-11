from unittest import TestCase
from pybricks.media.ev3dev.__stub.__image import Image
from pybricks.media.ev3dev.__stub.__imagefile import ImageFile
from pybricks.parameters.__stub.__color import Color
from pybricks.media.ev3dev.__stub.__font import Font


class TestImage(TestCase):
    def test_constructor(self):
        try:
            Image('test')
            Image(ImageFile.ACCEPT)
            Image(Image('test'))
        except:
            self.fail()

        try:
            Image('test', sub=True, x1=0, y1=0, x2=0, y2=0)
            Image(ImageFile.ACCEPT, sub=True, x1=0, y1=0, x2=0, y2=0)
            Image(Image('test'), sub=True, x1=0, y1=0, x2=0, y2=0)
        except:
            self.fail()

    def test_properties(self):
        image = Image('test')
        self.assertIsInstance(image.width, int)
        self.assertIsInstance(image.height, int)
        self.assertEqual(image.width, 0)
        self.assertEqual(image.height, 0)

    def test_empty(self):
        result = Image.empty()
        self.assertIsInstance(result, Image)

        result = Image.empty(178)
        self.assertIsInstance(result, Image)

        result = Image.empty(178, 128)
        self.assertIsInstance(result, Image)

    def test_draw_text(self):
        image = Image('test')
        self.assertIsNone(image.draw_text(0, 0, "test"))
        self.assertIsNone(image.draw_text(0, 0, "test", Color.GREEN))
        self.assertIsNone(image.draw_text(
            0, 0, "test", Color.GREEN, Color.BLACK))

    def test_print(self):
        image = Image('test')
        self.assertIsNone(image.print())
        self.assertIsNone(image.print('a'))
        self.assertIsNone(image.print('a', 1))
        self.assertIsNone(image.print('a', 1, sep=':'))
        self.assertIsNone(image.print('a', 1, end=':'))
        self.assertIsNone(image.print('a', 1, sep=':', end=','))

    def test_set_font(self):
        image = Image('test')
        self.assertIsNone(image.set_font(Font()))

    def test_draw_image(self):
        image = Image('test')
        self.assertIsNone(image.draw_image(0, 0, 'test'))
        self.assertIsNone(image.draw_image(0, 0, Image('test')))
        self.assertIsNone(image.draw_image(0, 0, ImageFile.ANGRY))
        self.assertIsNone(image.draw_image(0, 0, 'test', Color.GREEN))

    def test_draw_pixel(self):
        image = Image('test')
        self.assertIsNone(image.draw_pixel(0, 0))
        self.assertIsNone(image.draw_pixel(0, 0, Color.RED))

    def test_draw_line(self):
        image = Image('test')
        self.assertIsNone(image.draw_line(0, 0, 0, 0))
        self.assertIsNone(image.draw_line(0, 0, 0, 0, 0))
        self.assertIsNone(image.draw_line(0, 0, 0, 0, 0, Color.PURPLE))

    def test_draw_box(self):
        image = Image('test')
        self.assertIsNone(image.draw_box(0, 0, 0, 0))
        self.assertIsNone(image.draw_box(0, 0, 0, 0, 0))
        self.assertIsNone(image.draw_box(0, 0, 0, 0, 0, True))
        self.assertIsNone(image.draw_box(0, 0, 0, 0, 0, True, Color.GREEN))

    def test_draw_circle(self):
        image = Image('test')
        self.assertIsNone(image.draw_circle(0, 0, 0))
        self.assertIsNone(image.draw_circle(0, 0, 0, True))
        self.assertIsNone(image.draw_circle(0, 0, 0, True, Color.RED))

    def test_clear(self):
        image = Image('test')
        self.assertIsNone(image.clear())

    def test_load_image(self):
        image = Image('test')
        self.assertIsNone(image.load_image('test'))
        self.assertIsNone(image.load_image(Image('test')))
        self.assertIsNone(image.load_image(ImageFile.ANGRY))

    def test_save(self):
        image = Image('test')
        self.assertIsNone(image.save('test'))
