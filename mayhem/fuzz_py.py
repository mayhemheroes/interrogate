#!/usr/bin/env python3

import atheris
import sys
import fuzz_helpers

with atheris.instrument_imports(include=['interrogate']):
    from interrogate import coverage

def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        with fdp.ConsumeTemporaryFile('.py', as_bytes=True, all_data=True) as f:
            cov = coverage.InterrogateCoverage(paths=[f])
            cov.get_coverage()
    except (IndentationError, ValueError, SyntaxError):
        return -1
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
