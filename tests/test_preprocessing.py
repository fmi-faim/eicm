from unittest import TestCase

from src.eicm.preprocessing.yokogawa import get_metadata, parse_filename


class Yokogawa(TestCase):
    def test_get_metadata(self):
        acq_date, px_size, px_size_unit, channels = get_metadata("../resources/")

        assert acq_date == "2022-12-21"
        assert px_size == 0.10833333333333334
        assert px_size_unit == "micron"
        assert channels == {
            "1": {
                "pixel_size": "0.10833333333333334",
                "cam_index": "2",
                "objective": "60x-W",
                "filter": "BP445-45",
                "laser": "405nm",
            },
            "2": {
                "pixel_size": "0.10833333333333334",
                "cam_index": "2",
                "objective": "60x-W",
                "filter": "BP525-50",
                "laser": "488nm",
            },
            "3": {
                "pixel_size": "0.10833333333333334",
                "cam_index": "1",
                "objective": "60x-W",
                "filter": "BP600-37",
                "laser": "561nm",
            },
            "4": {
                "pixel_size": "0.10833333333333334",
                "cam_index": "1",
                "objective": "60x-W",
                "filter": "BP676-29",
                "laser": "640nm",
            },
            "5": {
                "pixel_size": "0.10833333333333334",
                "cam_index": "2",
                "objective": "60x-W",
                "filter": "BP525-50",
                "laser": "Lamp",
            },
            "6": {
                "pixel_size": "0.10833333333333334",
                "cam_index": "2",
                "objective": "60x-W",
                "filter": "BP525-50",
                "laser": "488nm",
            },
        }

    def test_parse_file_name(self):
        plate_name = "Test-plate"
        well = "A01"
        time_point = "T0001"
        field = "F010"
        l01 = "L01"
        action = "A01"
        z = "Z32"
        channel = "C01"
        file_name = (
            f"{plate_name}_{well}_{time_point}{field}{l01}{action}{z}{channel}.tif"
        )

        p, w, tp, f, l_, a, z_, ch = parse_filename(file_name, plate_name)

        assert p == plate_name
        assert w == well
        assert tp == time_point
        assert f == 10
        assert l_ == l01
        assert a == action
        assert z_ == 32
        assert ch == channel
