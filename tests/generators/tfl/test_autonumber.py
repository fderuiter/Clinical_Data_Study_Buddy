from clinical_data_study_buddy.generators.tfl.autonumber import AutoNumberer
from clinical_data_study_buddy.generators.tfl.models import TFL, Layout, TFLSpec


class TestAutoNumberer:
    def test_assign_numbers_simple(self):
        tfl_spec = TFLSpec(
            version=1.0,
            tfls=[
                TFL(
                    shell_id="T14.1.1",
                    title="Table 1",
                    population="ITT",
                    layout=Layout(orientation="portrait", page_size="A4"),
                ),
                TFL(
                    shell_id="T14.1.2",
                    title="Table 2",
                    population="ITT",
                    layout=Layout(orientation="portrait", page_size="A4"),
                ),
                TFL(
                    shell_id="T14.2.1",
                    title="Table 3",
                    population="ITT",
                    layout=Layout(orientation="portrait", page_size="A4"),
                ),
            ],
        )
        autonumberer = AutoNumberer(tfl_spec)
        new_spec = autonumberer.assign_numbers(prefix="T14")
        assert new_spec.tfls[0].shell_id == "T14.1.1"
        assert new_spec.tfls[1].shell_id == "T14.1.2"
        assert new_spec.tfls[2].shell_id == "T14.2.1"

    def test_assign_numbers_unsorted(self):
        tfl_spec = TFLSpec(
            version=1.0,
            tfls=[
                TFL(
                    shell_id="T14.2.1",
                    title="Table 3",
                    population="ITT",
                    layout=Layout(orientation="portrait", page_size="A4"),
                ),
                TFL(
                    shell_id="T14.1.1",
                    title="Table 1",
                    population="ITT",
                    layout=Layout(orientation="portrait", page_size="A4"),
                ),
                TFL(
                    shell_id="T14.1.2",
                    title="Table 2",
                    population="ITT",
                    layout=Layout(orientation="portrait", page_size="A4"),
                ),
            ],
        )
        autonumberer = AutoNumberer(tfl_spec)
        new_spec = autonumberer.assign_numbers(prefix="T14")
        # The order of tfls in the spec is preserved, but the shell_ids are re-numbered
        assert new_spec.tfls[0].shell_id == "T14.2.1"
        assert new_spec.tfls[1].shell_id == "T14.1.1"
        assert new_spec.tfls[2].shell_id == "T14.1.2"

    def test_assign_numbers_invalid_shell_id(self):
        tfl_spec = TFLSpec(
            version=1.0,
            tfls=[
                TFL(
                    shell_id="invalid-id",
                    title="Table 1",
                    population="ITT",
                    layout=Layout(orientation="portrait", page_size="A4"),
                ),
                TFL(
                    shell_id="T14.1.2",
                    title="Table 2",
                    population="ITT",
                    layout=Layout(orientation="portrait", page_size="A4"),
                ),
            ],
        )
        autonumberer = AutoNumberer(tfl_spec)
        new_spec = autonumberer.assign_numbers(prefix="T14")
        assert new_spec.tfls[0].shell_id == "T14.99.1"
        assert new_spec.tfls[1].shell_id == "T14.1.1"
