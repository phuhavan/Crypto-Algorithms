import re
from pathlib import Path
import sys
import os

# Add the algorithms directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../algorithms/hashing')))

from shake256 import shake256  # Now we can import shake256


def parse_rsp_file(filepath):
    """Parses an .rsp file and extracts test vectors."""
    test_vectors = []
    with open(filepath, 'r') as f:
        data = f.read()

    # Find all test cases using regex
    test_cases = re.findall(
        r'COUNT = (\d+)\nOutputlen = (\d+)\nMsg = ([0-9a-f]*)\nOutput = ([0-9a-f]*)',
        data, re.IGNORECASE
    )

    for count, outlen, msg, expected_output in test_cases:
        count = int(count)
        outlen = int(outlen) // 8  # Convert bits to bytes
        msg_bytes = bytes.fromhex(msg)
        expected_bytes = bytes.fromhex(expected_output)
        test_vectors.append((count, msg_bytes, outlen, expected_bytes))

    return test_vectors

def test_shake256_from_rsp(rsp_file):
    """Tests SHAKE256 implementation using vectors from an .rsp file."""
    test_vectors = parse_rsp_file(rsp_file)

    for count, msg, outlen, expected in test_vectors:
        result = shake256(outlen, msg)
        assert result == expected, f"Test {count} failed!\nExpected: {expected.hex()}\nGot: {result.hex()}"

    print(f"All tests passed for {rsp_file} ✅")

if __name__ == "__main__":
    rsp_files = [
        "SHAKE256VariableOut.rsp",
        "SHAKE256ShortMsg.rsp",
        "SHAKE256Monte.rsp",
        "SHAKE256LongMsg.rsp"
    ]

    for rsp in rsp_files:
        if Path(rsp).exists():
            test_shake256_from_rsp(rsp)
        else:
            print(f"Warning: {rsp} not found, skipping.")
