# Build Order: You are given a list of projects and a list of dependencies
# (which is a list of pairs of projects, where the second project is dependent
# on the first project). All of a project's dependencies must be built before
# the project is. Find a build order that will allow the projects to be built.
# If there is no valid build order, return an error.


# 💡
# Sale de una. La idea es crear un grafo dirigido de dependencias e ir
# agregando al build order los projects sin dependencias.
# Hacerlos SETs para eficiencia, plz, no listas.
# Cada vez que agregás algo al build order, lo quitás de las dependencias.
# Y repetís.
# Cuidarse de circularidades: si en algún momento quedan proyectos pendientes
# pero todos tienen al menos una dependencia, entonces hay una circularidad.


# F -> A -> D -> C
#   -> B ->
# E

projects = "a, b, c, d, e, f".split(", ")
dependencies = [
    ("a", "d"),
    ("f", "b"),
    ("b", "d"),
    ("f", "a"),
    ("d", "c"),
]


def build_order(projects: list[str], dependencies: list[tuple[str, str]]) -> list[str]:
    graph = {project: set() for project in projects}
    for dependency, project in dependencies:
        graph[project].add(dependency)

    build = []

    while len(build) < len(projects):
        something_built = False
        for project, deps in graph.items():
            if not deps and project not in build:
                build.append(project)
                something_built = True

        if not something_built:
            return Exception("No valid order, circularity.")

        for built_project in build:
            for _, deps in graph.items():
                if built_project in deps:
                    deps.remove(built_project)

    return build


print(build_order(projects, dependencies))
