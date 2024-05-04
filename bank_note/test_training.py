from ml.training import read_bank_note_data


def test_read_bank_note_data():
    data = read_bank_note_data()
    assert len(data) == 1372

