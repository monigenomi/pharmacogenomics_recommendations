from aldy import get_result_from_aldy_file, create_openpgx_input_dict, GENES


def test_get_result_from_aldy_file_cyp2a6():
    assert get_result_from_aldy_file("./wdl/aldy/test/CYP2A6.aldy") == (
        "CYP2A6",
        "*1/*1",
    )


def test_get_result_from_aldy_file_cyp2d6():
    assert get_result_from_aldy_file("./wdl/aldy/test/CYP2D6.aldy") == (
        "CYP2D6",
        "*16/*79",
    )


def test_create_openpgx_input_dict():
    aldy_files = [f"./wdl/aldy/test/aldy_results/{gene}.aldy" for gene in GENES]
    assert create_openpgx_input_dict(aldy_files) == {
        "CYP1A1": "*1/*1",
        "CYP1A2": "*1/*1",
        "CYP2A6": "*1/*1",
        "CYP2B6": "*1/*1",
        "CYP2C19": "*1/*2",
        "CYP2C8": "*1/*1",
        "CYP2C9": "*1/*2",
        "CYP2D6": "*16/*79",
        "CYP2E1": "*1/*1",
        "CYP3A4": "*1/*36",
        "CYP3A43": "*1/*1",
        "CYP3A5": "*1/*3",
        "CYP4F2": "*1/*1",
        "DPYD": "*5/*6",
        "SLCO1B1": "*1/*20",
        "TPMT": "*1/*1",
    }
