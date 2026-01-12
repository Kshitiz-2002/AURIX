from memory.concept_graph import ConceptGraph


def test_graph_learns_concepts():
    g = ConceptGraph()
    g.add_task("Explain Python programming")

    assert "python" in g.nodes
    assert g.nodes["python"].frequency == 1


def test_graph_support_score():
    g = ConceptGraph()
    g.add_task("Explain Python")

    score = g.graph_support_score("Explain Python basics")
    assert 0.3 <= score <= 1.0
