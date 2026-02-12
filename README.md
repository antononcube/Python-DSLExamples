# DSLExamples

Python data package with examples of Domain Specific Language (DSL) command translations.

The package closely follows the Raku package 
["DSL::Examples"](https://raku.land/zef:antononcube/DSL::Examples), [AAp1], and
Wolfram Language paclet ["DSLExamples"](https://resources.wolframcloud.com/PacletRepository/resources/AntonAntonov/DSLExamples), [AAp2],
and has (or should have) the same DSL examples data.

-----

## Installation (editable)

```
pip install DSLExamples
```

-----

## Usage

```python
from DSLExamples import dsl_examples, dsl_workflow_separators

all_examples = dsl_examples()
python_lsa = dsl_examples("Python", "LSAMon")
separators = dsl_workflow_separators("WL", "LSAMon")
```

-----

## References

[AAp1] Anton Antonov
[DSL::Examples, Raku package](https://github.com/antononcube/Raku-DSL-Examples),
(2025-2026),
[GitHub/antononcube](https://github.com/antononcube).

[AAp2] Anton Antonov
[DSLExamples, Wolfram Language paclet](https://resources.wolframcloud.com/PacletRepository/resources/AntonAntonov/DSLExamples/),
(2025-2026),
[Wolfram Language Paclet Repository](https://resources.wolframcloud.com/publishers/resources?PublisherID=AntonAntonov).