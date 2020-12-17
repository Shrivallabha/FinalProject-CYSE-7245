# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import ExtractROI


def test_ExtractROI_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        crop_list=dict(
            argstr="%s",
            position=2,
            xor=[
                "x_min",
                "x_size",
                "y_min",
                "y_size",
                "z_min",
                "z_size",
                "t_min",
                "t_size",
            ],
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr="%s",
            extensions=None,
            mandatory=True,
            position=0,
        ),
        output_type=dict(),
        roi_file=dict(
            argstr="%s",
            extensions=None,
            genfile=True,
            hash_files=False,
            position=1,
        ),
        t_min=dict(
            argstr="%d",
            position=8,
        ),
        t_size=dict(
            argstr="%d",
            position=9,
        ),
        x_min=dict(
            argstr="%d",
            position=2,
        ),
        x_size=dict(
            argstr="%d",
            position=3,
        ),
        y_min=dict(
            argstr="%d",
            position=4,
        ),
        y_size=dict(
            argstr="%d",
            position=5,
        ),
        z_min=dict(
            argstr="%d",
            position=6,
        ),
        z_size=dict(
            argstr="%d",
            position=7,
        ),
    )
    inputs = ExtractROI.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ExtractROI_outputs():
    output_map = dict(
        roi_file=dict(
            extensions=None,
        ),
    )
    outputs = ExtractROI.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
