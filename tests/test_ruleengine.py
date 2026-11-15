import pytest
import torch
from ruleengine import RuleEngine, create_ruleengine

class TestRuleEngine:
    def test_init(self):
        m = RuleEngine(dim=256, hidden_dim=512)
        assert m.dim == 256
    
    def test_forward(self):
        m = RuleEngine(dim=256)
        x = torch.randn(32, 256)
        assert m(x).shape == (32, 256)
    
    def test_factory(self):
        m = create_ruleengine()
        assert isinstance(m, RuleEngine)

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
