import pathlib
import pydantic
import unittest
from pydantic import BaseModel

from pivmetalib import typing

__this_dir__ = pathlib.Path(__file__).parent


class TestTyping(unittest.TestCase):

    def test_camera_resolution_type(self):
        class Camera(BaseModel):
            res: typing.ResolutionType

        cam = Camera(res='123x123')
        self.assertEqual(cam.res, '123x123')
        with self.assertRaises(pydantic.ValidationError):
            Camera(res='1')
        with self.assertRaises(pydantic.ValidationError):
            Camera(res='10x30')
        with self.assertRaises(pydantic.ValidationError):
            Camera(res='10x3000')
        with self.assertRaises(pydantic.ValidationError):
            Camera(res=1.2)

        cam = Camera(res='1000x3000')
        self.assertEqual(cam.res, '1000x3000')
