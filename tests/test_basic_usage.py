from DSLExamples import dsl_examples, dsl_workflow_separators


def test_examples_root_is_dict():
    examples = dsl_examples()
    assert isinstance(examples, dict)


def test_examples_lang_is_dict():
    examples = dsl_examples(lang="WL")
    assert isinstance(examples, dict)


def test_examples_lang_workflow_is_dict():
    examples = dsl_examples(lang="WL", workflow="QRMon")
    assert isinstance(examples, dict)


def test_examples_wrong_lang_type():
    try:
        dsl_examples(lang=3)
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError for wrong lang type")

def test_examples_wrong_from_lang():
    try:
        dsl_examples(lang='Python', from_lang="Afrikaans")
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for wrong from_lang value")

def test_separators_smoke():
    separators = dsl_workflow_separators(lang="Python", workflow="LSAMon")
    assert isinstance(separators, str)
