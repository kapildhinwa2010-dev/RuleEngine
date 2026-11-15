# RuleEngine

[![CI](https://github.com/kapildhinwa2010-dev/RuleEngine/actions/workflows/ci.yml/badge.svg)](https://github.com/kapildhinwa2010-dev/RuleEngine/actions/workflows/ci.yml)
[![CodeQL](https://github.com/kapildhinwa2010-dev/RuleEngine/actions/workflows/codeql.yml/badge.svg)](https://github.com/kapildhinwa2010-dev/RuleEngine/actions/workflows/codeql.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch 2.0+](https://img.shields.io/badge/pytorch-2.0+-red.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

**Rule-based reasoning engine**

Professional implementation of RuleEngine for research and production use.

## Installation

```bash
pip install RuleEngine
```

## Usage

```python
import torch
from ruleengine import RuleEngine

module = RuleEngine(dim=256, hidden_dim=512)
output = module(torch.randn(32, 256))
```

## License

MIT License
