import pytest

from ruleengine import Fact, KnowledgeNet


def test_fact_basic():
    fact = Fact("alice", "knows", "bob")
    assert fact.as_tuple() == ("alice", "knows", "bob")


def test_fact_rejects_empty():
    with pytest.raises(ValueError):
        Fact("", "knows", "bob")


def test_add_and_len():
    net = KnowledgeNet()
    assert net.add("a", "knows", "b") is True
    assert net.add("a", "knows", "b") is False
    assert len(net) == 1


def test_query_pattern():
    net = KnowledgeNet()
    net.add("a", "knows", "b")
    net.add("a", "likes", "c")
    assert len(net.query(subject="a")) == 2


def test_chain_walk():
    net = KnowledgeNet()
    net.add("a", "next", "b")
    net.add("b", "next", "c")
    assert net.chain("a", "next") == ["b", "c"]


# --- rules / forward chaining (RuleEngine-specific) ---


def test_add_rule_and_forward_chain():
    net = KnowledgeNet()
    net.add("a", "parent", "b")
    net.add("b", "parent", "c")
    net.add_rule("parent", "ancestor")
    derived = net.forward_chain()
    tuples = {f.as_tuple() for f in derived}
    assert ("a", "ancestor", "b") in tuples
    assert ("a", "ancestor", "c") in tuples
    assert ("b", "ancestor", "c") in tuples


def test_forward_chain_idempotent():
    net = KnowledgeNet()
    net.add("a", "parent", "b")
    net.add_rule("parent", "ancestor")
    net.forward_chain()
    assert net.forward_chain() == []


def test_forward_chain_without_rules():
    net = KnowledgeNet()
    net.add("a", "parent", "b")
    assert net.forward_chain() == []


def test_add_rule_rejects_empty():
    net = KnowledgeNet()
    with pytest.raises(ValueError):
        net.add_rule("", "ancestor")


def test_transitive_closure():
    net = KnowledgeNet()
    net.add("a", "parent", "b")
    net.add("b", "parent", "c")
    net.add("c", "parent", "d")
    closure = net.transitive_closure("parent")
    assert closure["a"] == ["b", "c", "d"]
    assert closure["b"] == ["c", "d"]
    assert "d" not in closure


def test_transitive_closure_rejects_bad_hops():
    net = KnowledgeNet()
    with pytest.raises(ValueError):
        net.transitive_closure("p", max_hops=0)