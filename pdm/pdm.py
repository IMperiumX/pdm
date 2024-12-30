class Package:
    """simplified representation of a package"""

    def __init__(self, name, version, dependencies):
        self.name = name
        self.version = version  # Assume a simple string for now
        self.dependencies = dependencies  # Dictionary: {name: version_constraint}


def parse_constraint(constraint_str):
    """basic version constraint parsing"""
    if constraint_str.startswith(">="):
        return lambda v: v >= constraint_str[2:]
    elif constraint_str.startswith("=="):
        return lambda v: v == constraint_str[2:]
    # ... (add more operators as needed)
    else:
        return lambda v: True  # No constraint


def resolve_dependencies(packages, root_package_name, root_constraint=""):
    """simplified resolver (not Pubgrub yet!)"""
    resolved = {}
    to_resolve = [(root_package_name, parse_constraint(root_constraint))]

    while to_resolve:
        name, constraint = to_resolve.pop()

        compatible_versions = [
            p for p in packages if p.name == name and constraint(p.version)
        ]

        if not compatible_versions:
            raise Exception(f"No compatible version found for {name} ({constraint})")

        # Naive: Just pick the latest version (replace with Pubgrub logic later)
        chosen_package = max(compatible_versions, key=lambda p: p.version)

        resolved[name] = chosen_package

        for dep_name, dep_constraint in chosen_package.dependencies.items():
            if dep_name not in resolved:
                to_resolve.append((dep_name, parse_constraint(dep_constraint)))

    return resolved


# Example Usage (very simplified data)
packages = [
    Package("my-package", "1.0.0", {"dep-a": ">=1.0.0", "dep-b": "==2.1.0"}),
    Package("dep-a", "1.0.0", {}),
    Package("dep-a", "1.1.0", {"dep-c": ">=1.0.0"}),
    Package("dep-a", "1.2.0", {}),
    Package("dep-b", "2.1.0", {}),
    Package("dep-c", "1.0.0", {}),
    Package("dep-c", "1.1.0", {}),
]

resolved = resolve_dependencies(packages, "my-package")
for name, package in resolved.items():
    print(f"{name}: {package.version}")
