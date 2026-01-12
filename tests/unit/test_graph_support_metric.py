from memory.concept_graph import ConceptGraph


def test_graph_support_score():
    graph = ConceptGraph()

    graph.add_concepts(
        task="Explain Python lists",
        concepts={"python", "list", "sequence"}
    )

    score = graph.support_score(
        task="Explain Python tuples",
        concepts={"python", "tuple", "sequence"}
    )

    assert 0.3 <= score <= 0.7