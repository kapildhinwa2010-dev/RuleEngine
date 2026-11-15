# RuleEngine

[![CI](https://github.com/kapildhinwa2010-dev/RuleEngine/actions/workflows/ci.yml/badge.svg)](https://github.com/kapildhinwa2010-dev/RuleEngine/actions/workflows/ci.yml)
[![CI](https://github.com/kapildhinwa2010-dev/RuleEngine/actions/workflows/codeql.yml/badge.svg)](https://github.com/kapildhinwa2010-dev/RuleEngine/actions/workflows/codeql.yml)

Rule-based fact derivation with forward chaining over (subject, predicate, object) triples.

**Part of the [Kapildhinwa2010-dev Toolkit](https://github.com/kapildhinwa2010-dev/Kapildhinwa2010-dev).**

## What it does

RuleEngine is the RULES layer of the fact-tool family. On top of the
shared triple store it registers (base_predicate -> derived_predicate)
rules and forward_chain() derives new facts from transitive base
chains: a parent b, b parent c  =>  a ancestor b, a ancestor c.
Storage extras (merge/JSON) live in FactBase; alias derivation in
AliasDeriver; path analysis in ChainReasoner.

## Install

```bash
pip install -r requirements.txt
```

## Quick start

```python
from ruleengine import KnowledgeNet

net = KnowledgeNet()
net.add("a", "parent", "b")
net.add("b", "parent", "c")
net.add_rule("parent", "ancestor")
print(net.forward_chain())   # 2 new ancestor facts
print(len(net))              # 4
```

## API

- add / query / facts / chain / interference - shared triple store
- add_rule(base, derived) - register a transitive rule
- transitive_closure(predicate) - subject -> all reachable objects
- forward_chain() - fire all rules, return newly derived facts

## Honest results and limitations

- Rules are strictly transitive (base implies derived along chains).
  No negation, no conjunction, no default handling - the source
  experiments showed negation is confidently wrong in this family.
- forward_chain() adds derived facts permanently; there is no
  retraction.
- chain() follows only the FIRST match per hop (use ChainReasoner for
  all paths).

## License

MIT - see [LICENSE](LICENSE).
