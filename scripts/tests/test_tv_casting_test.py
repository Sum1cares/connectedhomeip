#!/usr/bin/env -S python3 -B

# Copyright (c) 2026 Project CHIP Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from linux.tv_casting_test_sequence_utils import App, Step
from run_tv_casting_test import (
    TestStepException,
    capture_runtime_values,
    replace_runtime_values,
)


class TestRuntimePasscode(unittest.TestCase):
    def setUp(self):
        self.step = Step(
            app=App.TV_APP,
            output_msg=["Casting passcode:"],
            capture_regex=r"Casting passcode: \[(?P<commissioner_generated_passcode_hex>0x[0-9a-fA-F_]+)\]",
        )

    def test_captures_and_converts_passcode(self):
        values = capture_runtime_values(
            self.step,
            ["Casting passcode: [0x055A_CB2E]. Additional instructions"],
            "commissioner_generated_passcode_test",
        )

        self.assertEqual(values["commissioner_generated_passcode_hex"], "0x055A_CB2E")
        self.assertEqual(values["commissioner_generated_passcode_decimal"], "89836334")

    def test_requires_a_passcode_in_matched_output(self):
        with self.assertRaises(TestStepException):
            capture_runtime_values(
                self.step,
                ["Casting passcode: [not-a-passcode]"],
                "commissioner_generated_passcode_test",
            )

    def test_replaces_runtime_values_in_sequence_text(self):
        value = replace_runtime_values(
            "cast setcommissionerpasscode {commissioner_generated_passcode_decimal}",
            {"commissioner_generated_passcode_decimal": "89836334"},
        )

        self.assertEqual(value, "cast setcommissionerpasscode 89836334")


if __name__ == "__main__":
    unittest.main()
