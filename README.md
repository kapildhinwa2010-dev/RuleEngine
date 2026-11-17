# RuleEngine

RuleEngine is a small Python library for storing subject–predicate–object facts and deriving additional facts with simple transitive rules. The project metadata identifies it as version `0.1.0`; the implementation and test suite are compact, so treat it as an early-stage utility rather than a general-purpose or production-validated rule system.

## Features

- `Fact` represents a triple of non-empty strings, supports tuple conversion, equality, hashing, and readable representation.
- `KnowledgeNet` stores unique facts, returns a sorted fact list, reports its size, and queries facts by optional subject, predicate, and object filters.
- `chain()` follows a predicate from a starting subject for up to a configurable number of hops.
- `derive_aliases()` finds connected components of `same_as` facts and maps each participating value to the lexicographically smallest value in its component.
- `transitive_closure()` returns reachable objects by subject for a predicate, with a configurable hop bound.
- `add_rule(base_predicate, derived_predicate)` and `forward_chain()` add derived facts for reachable pairs under registered transitive rules. Derived facts are kept in the store; repeating the operation does not add duplicates.

## Requirements and installation

The package metadata requires Python 3.9 or later and declares `numpy>=1.24`. Install from the repository root with:

```bash
python -m pip install .
```

To install the dependencies listed for the project and its tests from a checkout instead, use:

```bash
python -m pip install -r requirements.txt
```

There is no command-line interface; use the Python module API.

## Example

```python
from ruleengine import KnowledgeNet

net = KnowledgeNet()
net.add("a", "parent", "b")
net.add("b", "parent", "c")
net.add_rule("parent", "ancestor")

derived = net.forward_chain()
print([fact.as_tuple() for fact in derived])
# [('a', 'ancestor', 'b'), ('a', 'ancestor', 'c'), ('b', 'ancestor', 'c')]
print(len(net))  # 5 facts total: 2 input facts + 3 derived facts
```

## Tests and CI

Run the test suite from the repository root with:

```bash
python -m pytest -q
```

On the checked-out commit, this command completed successfully: **11 tests passed**. The GitHub Actions CI workflow is configured to run pytest and compile/smoke checks on Python 3.10, 3.11, and 3.12. This local test result does not establish the status of remote CI runs.

## Scope and limitations

This is a small in-memory fact store with a limited transitive-rule mechanism, not a full logic-programming engine. It does not implement conjunctions, negation, defaults, explanations/provenance, persistence, or fact retraction. `chain()` chooses the first matching next fact at each hop rather than enumerating alternative paths. `transitive_closure()` defaults to a maximum of 16 hops, which also bounds the reachability used by `forward_chain()`. Rule registration stores one derived predicate per base predicate; registering another rule for the same base replaces the earlier mapping. No benchmark results are supplied by the repository.

## License

The repository includes an MIT License, copyright © 2026 Kapildhinwa2010-dev. See [LICENSE](LICENSE) for the full terms.
