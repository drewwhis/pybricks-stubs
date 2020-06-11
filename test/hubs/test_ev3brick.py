from unittest import TestCase
from pybricks.hubs.__stub.__ev3brick import EV3Brick
from pybricks.parameters.__stub.__color import Color
from pybricks.media.ev3dev.__stub.__font import Font
from pybricks.media.ev3dev.__stub.__image import Image
from pybricks.media.ev3dev.__stub.__imagefile import ImageFile
from pybricks.media.ev3dev.__stub.__soundfile import SoundFile


class TestEV3Brick(TestCase):
    def test_constructor(self):
        try:
            EV3Brick()
        except:
            self.fail()

    def test_battery_voltage(self):
        brick = EV3Brick()
        value = brick.battery.voltage()
        self.assertIsInstance(value, int)
        self.assertEqual(0, value)

    def test_battery_current(self):
        brick = EV3Brick()
        value = brick.battery.current()
        self.assertIsInstance(value, int)
        self.assertEqual(0, value)

    def test_buttons_pressed(self):
        brick = EV3Brick()
        value = brick.buttons.pressed()
        self.assertIsInstance(value, list)
        self.assertEqual(0, len(value))

    def test_light_on(self):
        brick = EV3Brick()
        self.assertIsNone(brick.light.on(Color.RED))
        self.assertIsNone(brick.light.on(None))

    def test_light_off(self):
        brick = EV3Brick()
        self.assertIsNone(brick.light.off())

    def test_screen_width(self):
        brick = EV3Brick()
        self.assertEqual(178, brick.screen.width)
    
    def test_screen_height(self):
        brick = EV3Brick()
        self.assertEqual(128, brick.screen.height)

    def test_screen_draw_text(self):
        brick = EV3Brick()
        self.assertIsNone(brick.screen.draw_text(0, 0, "test"))
        self.assertIsNone(brick.screen.draw_text(0, 0, "test", Color.GREEN))
        self.assertIsNone(brick.screen.draw_text(0, 0, "test", Color.GREEN, Color.BLACK))

    def test_screen_print(self):
        brick = EV3Brick()
        self.assertIsNone(brick.screen.print())
        self.assertIsNone(brick.screen.print('a'))
        self.assertIsNone(brick.screen.print('a', 1))
        self.assertIsNone(brick.screen.print('a', 1, sep=':'))
        self.assertIsNone(brick.screen.print('a', 1, end=':'))
        self.assertIsNone(brick.screen.print('a', 1, sep=':', end=','))

    def test_screen_set_font(self):
        brick = EV3Brick()
        self.assertIsNone(brick.screen.set_font(Font()))

    def test_screen_load_image(self):
        brick = EV3Brick()
        self.assertIsNone(brick.screen.load_image('test'))
        self.assertIsNone(brick.screen.load_image(Image('test')))
        self.assertIsNone(brick.screen.load_image(ImageFile.ANGRY))

    def test_screen_draw_image(self):
        brick = EV3Brick()
        self.assertIsNone(brick.screen.draw_image(0, 0, 'test'))
        self.assertIsNone(brick.screen.draw_image(0, 0, Image('test')))
        self.assertIsNone(brick.screen.draw_image(0, 0, ImageFile.ANGRY))
        self.assertIsNone(brick.screen.draw_image(0, 0, 'test', Color.GREEN))

    def test_screen_draw_pixel(self):
        brick = EV3Brick()
        self.assertIsNone(brick.screen.draw_pixel(0, 0))
        self.assertIsNone(brick.screen.draw_pixel(0, 0, Color.RED))

    def test_screen_draw_line(self):
        brick = EV3Brick()
        self.assertIsNone(brick.screen.draw_line(0, 0, 0, 0))
        self.assertIsNone(brick.screen.draw_line(0, 0, 0, 0, 0))
        self.assertIsNone(brick.screen.draw_line(0, 0, 0, 0, 0, Color.PURPLE))

    def test_screen_draw_box(self):
        brick = EV3Brick()
        self.assertIsNone(brick.screen.draw_box(0, 0, 0, 0))
        self.assertIsNone(brick.screen.draw_box(0, 0, 0, 0, 0))
        self.assertIsNone(brick.screen.draw_box(0, 0, 0, 0, 0, True))
        self.assertIsNone(brick.screen.draw_box(0, 0, 0, 0, 0, True, Color.GREEN))

    def test_screen_draw_circle(self):
        brick = EV3Brick()
        self.assertIsNone(brick.screen.draw_circle(0, 0, 0))
        self.assertIsNone(brick.screen.draw_circle(0, 0, 0, True))
        self.assertIsNone(brick.screen.draw_circle(0, 0, 0, True, Color.RED))

    def test_screen_save(self):
        brick = EV3Brick()
        self.assertIsNone(brick.screen.save('test'))

    def test_speaker_beep(self):
        brick = EV3Brick()
        self.assertIsNone(brick.speaker.beep())
        self.assertIsNone(brick.speaker.beep(100))
        self.assertIsNone(brick.speaker.beep(100, 200))

    def test_speaker_play_notes(self):
        brick = EV3Brick()
        self.assertIsNone(brick.speaker.play_notes([]))
        self.assertIsNone(brick.speaker.play_notes(()))
        self.assertIsNone(brick.speaker.play_notes([], 200))

    def test_speaker_play_file(self):
        brick = EV3Brick()
        self.assertIsNone(brick.speaker.play_file('test'))
        self.assertIsNone(brick.speaker.play_file(SoundFile.BOING))

    def test_speaker_say(self):
        brick = EV3Brick()
        self.assertIsNone(brick.speaker.say('test'))

    def test_speaker_set_speech_options(self):
        brick = EV3Brick()
        self.assertIsNone(brick.speaker.set_speech_options())
        self.assertIsNone(brick.speaker.set_speech_options('en'))
        self.assertIsNone(brick.speaker.set_speech_options('en', 'f1'))
        self.assertIsNone(brick.speaker.set_speech_options('en', 'f1', 100))
        self.assertIsNone(brick.speaker.set_speech_options('en', 'f1', 100, 50))

    def test_speaker_set_volume(self):
        brick = EV3Brick()
        self.assertIsNone(brick.speaker.set_volume(50))
        self.assertIsNone(brick.speaker.set_volume(50, 'Beep'))
        self.assertIsNone(brick.speaker.set_volume(50, 'PCM'))
        self.assertIsNone(brick.speaker.set_volume(50, '_all_'))
