# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import CARegister


def test_CARegister_inputs():
    input_map = dict(
        A=dict(
            argstr="-A %d",
        ),
        align=dict(
            argstr="-align-%s",
        ),
        args=dict(
            argstr="%s",
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr="%s",
            extensions=None,
            mandatory=True,
            position=-3,
        ),
        invert_and_save=dict(
            argstr="-invert-and-save",
            position=-4,
        ),
        l_files=dict(
            argstr="-l %s",
        ),
        levels=dict(
            argstr="-levels %d",
        ),
        mask=dict(
            argstr="-mask %s",
            extensions=None,
        ),
        no_big_ventricles=dict(
            argstr="-nobigventricles",
        ),
        num_threads=dict(),
        out_file=dict(
            argstr="%s",
            extensions=None,
            genfile=True,
            position=-1,
        ),
        subjects_dir=dict(),
        template=dict(
            argstr="%s",
            extensions=None,
            position=-2,
        ),
        transform=dict(
            argstr="-T %s",
            extensions=None,
        ),
    )
    inputs = CARegister.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_CARegister_outputs():
    output_map = dict(
        out_file=dict(
            extensions=None,
        ),
    )
    outputs = CARegister.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
