"""DSLExamples: DSL command translation examples and workflow separators."""

from __future__ import annotations

from importlib import resources
import json
from typing import Any, Dict


ANY: object = object()

_DSL_EXAMPLES_CACHE: Dict[str, Any] | None = None
_DSL_WORKFLOW_SEPARATORS_CACHE: Dict[str, Any] | None = None


def resources_map() -> Dict[str, str]:
    """Return a mapping of resource names to package-relative paths."""
    return {
        "dsl-examples-bulgarian.json": "resources/dsl-examples-bulgarian.json",
        "dsl-examples-english.json": "resources/dsl-examples-english.json",
        "dsl-examples-portuguese.json": "resources/dsl-examples-portuguese.json",
        "dsl-examples-russian.json": "resources/dsl-examples-russian.json",
        "dsl-workflow-separators.json": "resources/dsl-workflow-separators.json",
    }


def _load_json(resource_name: str) -> Dict[str, Any]:
    path = resources.files(__package__).joinpath("resources", resource_name)
    return json.loads(path.read_text(encoding="utf-8"))


def _get_dsl_examples(from_lang: str = 'English') -> Dict[str, Any]:
    from_lang_local = from_lang.lower()
    known_langs = {"bulgarian", "english", "portuguese", "russian"}
    if from_lang_local not in known_langs:
        raise ValueError(
             f"The value of from_lang is expected to be one of '{"', '".join(known_langs)}'."
        )
    global _DSL_EXAMPLES_CACHE
    if _DSL_EXAMPLES_CACHE is None:
        _DSL_EXAMPLES_CACHE = {}
    if from_lang not in _DSL_EXAMPLES_CACHE:
        _DSL_EXAMPLES_CACHE[from_lang_local] = _load_json("dsl-examples-" + from_lang_local + ".json")
    return dict(_DSL_EXAMPLES_CACHE[from_lang_local])


def _get_dsl_workflow_separators() -> Dict[str, Any]:
    global _DSL_WORKFLOW_SEPARATORS_CACHE
    if _DSL_WORKFLOW_SEPARATORS_CACHE is None:
        _DSL_WORKFLOW_SEPARATORS_CACHE = _load_json("dsl-workflow-separators.json")
    return dict(_DSL_WORKFLOW_SEPARATORS_CACHE)


def _dsl_retrieve(*, lang: Any = ANY, workflow: Any = ANY, dsl_data: Dict[str, Any]) -> Any:
    if lang is not ANY and not isinstance(lang, str):
        langs = "', '".join(dsl_data.keys())
        raise TypeError(
            f"The value of lang is expected to be None or one of '{langs}'."
        )

    if lang is not ANY and lang not in dsl_data:
        langs = "', '".join(dsl_data.keys())
        raise ValueError(
            f"The value of lang is expected to be None or one of '{langs}'."
        )

    if workflow is not ANY and not isinstance(workflow, str):
        raise TypeError("The value of workflow is expected to be a string or None.")

    if lang is ANY and workflow is ANY:
        return dsl_data
    if isinstance(lang, str) and workflow is ANY:
        return dsl_data[lang]
    if lang is ANY and isinstance(workflow, str):
        return {k: v.get(workflow) for k, v in dsl_data.items()}
    if isinstance(lang, str) and isinstance(workflow, str):
        return dsl_data[lang][workflow]

    return dsl_data


def dsl_examples(lang: Any = ANY, workflow: Any = ANY, from_lang: str = 'English') -> Any:
    """Return DSL examples for a language/workflow or all examples."""
    if lang is None:
        lang = ANY
    if workflow is None:
        workflow = ANY
    dsl_data = _get_dsl_examples(from_lang=from_lang)
    return _dsl_retrieve(lang=lang, workflow=workflow, dsl_data=dsl_data)


def dsl_workflow_separators(lang: Any = ANY, workflow: Any = ANY) -> Any:
    """Return DSL workflow separators for a language/workflow or all separators."""
    if lang is None:
        lang = ANY
    if workflow is None:
        workflow = ANY
    dsl_data = _get_dsl_workflow_separators()
    return _dsl_retrieve(lang=lang, workflow=workflow, dsl_data=dsl_data)


__all__ = [
    "ANY",
    "dsl_examples",
    "dsl_workflow_separators",
    "resources_map",
]
