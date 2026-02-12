# DSLExamples

Python data package with examples of DSL command translations and workflow separators.

## Installation (editable)

```bash
pip install -e .
```

## Usage

```python
from DSLExamples import dsl_examples, dsl_workflow_separators

all_examples = dsl_examples()
python_lsa = dsl_examples("Python", "LSAMon")
separators = dsl_workflow_separators("WL", "LSAMon")
```
