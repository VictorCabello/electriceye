#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `electriceye` package."""

import os
from click.testing import CliRunner

from electriceye import electriceye
from electriceye import cli


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "electriceye.cli.main" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output


def test_image_diff_01():
    """ test_image_diff_01
    input: Same img
    output: 1.0
    """
    # Prepare
    img_dir = 'tests/imgs/'
    file_a = os.path.join(img_dir + 'test_1_a.JPG')
    file_b = os.path.join(img_dir + 'test_1_a.JPG')

    # Execute
    result = electriceye.image_diff(file_a, file_b)

    # Verify
    assert result['mssim'] == 1.0

def test_image_diff_02():
    """ test_image_diff_01
    input: Same img
    output: no 1.0
    """
    # Prepare
    img_dir = 'tests/imgs/'
    file_a = os.path.join(img_dir + 'test_1_a.JPG')
    file_b = os.path.join(img_dir + 'test_1_b.JPG')

    # Execute
    result = electriceye.image_diff(file_a, file_b)

    # Verify
    assert result['mssim'] != 1.0
