# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..minc import NlpFit


def test_NlpFit_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        clobber=dict(
            argstr="-clobber",
            usedefault=True,
        ),
        config_file=dict(
            argstr="-config_file %s",
            extensions=None,
            mandatory=True,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        init_xfm=dict(
            argstr="-init_xfm %s",
            extensions=None,
            mandatory=True,
        ),
        input_grid_files=dict(),
        output_xfm=dict(
            argstr="%s",
            extensions=None,
            genfile=True,
            position=-1,
        ),
        source=dict(
            argstr="%s",
            extensions=None,
            mandatory=True,
            position=-3,
        ),
        source_mask=dict(
            argstr="-source_mask %s",
            extensions=None,
            mandatory=True,
        ),
        target=dict(
            argstr="%s",
            extensions=None,
            mandatory=True,
            position=-2,
        ),
        verbose=dict(
            argstr="-verbose",
        ),
    )
    inputs = NlpFit.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_NlpFit_outputs():
    output_map = dict(
        output_grid=dict(
            extensions=None,
        ),
        output_xfm=dict(
            extensions=None,
        ),
    )
    outputs = NlpFit.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
