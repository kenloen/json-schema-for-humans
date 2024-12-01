import os
from dataclasses import dataclass
from pathlib import Path
from typing import List

import pytest

from json_schema_for_humans.generation_configuration import GenerationConfiguration
from tests.md_utils_asserts import MdUtilsAsserts

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.dirname(current_dir))
examples_dir = os.path.join(parent_dir, "docs", "examples")


@dataclass
class TestCase:
    name: str
    config: GenerationConfiguration

    __test__ = False


def list_cases() -> List[str]:
    test_cases: List[str] = []
    for case_file_path in (Path(os.path.join(examples_dir, "cases"))).iterdir():
        if not (case_file_path.is_file() and case_file_path.exists() and case_file_path.name.endswith(".json")):
            continue
        test_cases.append(os.path.splitext(case_file_path.name)[0])
    return test_cases


class TestMdGenerate(MdUtilsAsserts):
    @pytest.mark.parametrize("test_case", list_cases())
    @pytest.mark.parametrize("with_badge,trailing_badges", [(True, False), (True, True), (False, False)])
    @pytest.mark.parametrize("nested", [True, False])
    def test_basic(self, test_case: str, with_badge: bool, trailing_badges: bool, nested: bool):
        """Test rendering a basic schema with title"""
        dir_name = "examples_md"
        if nested:
            dir_name = f"{dir_name}_nested"
        if with_badge and trailing_badges and nested:
            dir_name = f"examples_md_nested_with_trailing_html_badges"
        elif with_badge and trailing_badges:
            dir_name = f"examples_md_with_trailing_badges"
        elif with_badge:
            dir_name = f"{dir_name}_with_badges"
        else:
            dir_name = f"{dir_name}_default"

        temp_md_opts = {}
        if trailing_badges:
            temp_md_opts["heading_leading_badges"] = []
            temp_md_opts["heading_trailing_badges"] = ["Required", "Type"]
            if nested:
                temp_md_opts["allow_html"] = True

        self.assert_case_equals(
            examples_dir,
            dir_name,
            test_case,
            GenerationConfiguration(
                template_name="md_nested" if nested else "md",
                template_md_options={"badge_as_image": with_badge, **temp_md_opts},
                deprecated_from_description=True,
                footer_show_time=False,
            ),
        )
