def pytest_assertrepr_compare(op, left, right):
    try:
        import graphviz
    except ImportError:
        return
    from .visualize import visualize
    from .dispatch import Box

    if isinstance(left, Box) and isinstance(right, Box) and op == "==":
        d = graphviz.Digraph()
        seen = set()
        visualize(left, d, seen)
        visualize(right, d, seen)
        d.render(cleanup=True, view=True)

        return [f"{left} != {right}"]