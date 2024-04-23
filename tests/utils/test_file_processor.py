import tempfile
import pytest


from utils.file_processor import (
    process_input_from_user,
    process_input_from_file,
    is_valid_line
)


class TestIsValidLine:
    @pytest.mark.parametrize("line, expected", [
        ("1426828011 abc", False),
        ("1426828011", False),
        ("1426828011 123 456", False),
    ])
    def test_is_valid_line(self, line, expected):
        assert is_valid_line(line) == expected


class TestProcessInputFromUser:
    @pytest.fixture
    def input_list(self):
        return [("1426828011", 10), ("1426828028", 15), ("1426828037", 25)]

    def test_process_input_from_user(self, input_list):
        result = process_input_from_user(input_list, 1)
        assert result == ['1426828037']

    def test_insufficient_input(self):
        result = process_input_from_user([], 4)
        assert result == []

    def test_insufficient_output(self, input_list):
        result = process_input_from_user(input_list, 4)
        assert result == ['1426828011', '1426828028', '1426828037']


class TestProcessInputFromFile:
    @pytest.mark.parametrize("file_content, x, expected_result", [
        ("", 0, []),
        ("1426828011 10\n1426828028 15\n", 2, ['1426828011', '1426828028']),
        ("1426828011 10\n1426828028 15\n1426828037 25\n", 3, ['1426828011', '1426828028',
                                                              '1426828037']),
    ])
    def test_process_input_from_file(self, file_content, x, expected_result):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write(file_content)
            f.flush()
            f.seek(0)
            result = process_input_from_file(f.name, x)
        assert result == expected_result


class TestProcessLargeInputFromFile:

    @pytest.fixture
    def large_file_content_sorted(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            content = "\n".join([f"{i} {i * 10}" for i in range(1, 10001)])
            f.write(content)
            return f.name

    @pytest.fixture
    def large_file_content_unsorted(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            content = "\n".join([f"{i} {i * 10}" for i in range(10000, 0, -1)])
            f.write(content)
            return f.name

    def test_process_input_from_file_sorted(self, large_file_content_sorted):
        result = process_input_from_file(large_file_content_sorted, 5)
        assert result == ['9996', '9997', '9998', '9999', '10000']

    def test_process_input_from_file_unsorted(self, large_file_content_unsorted):
        result = process_input_from_file(large_file_content_unsorted, 5)
        assert result == ['9996', '9997', '9998', '9999', '10000']
