"""Testing some theories."""

test: dict[str, list[str]] = {"prior_exp": ["none", "some", "none", "none"], "dif": ["1", "2", "1", "1"]}

test["prior_exp"].append("Hello")

test1: dict[str, list[str]] = {}

test1["prior_exp"] = [""] 

print(test1)