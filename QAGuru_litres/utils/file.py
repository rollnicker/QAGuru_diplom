def abs_path_from_project(relative_path: str):
    import QAGuru_litres
    from pathlib import Path

    return (
        Path(QAGuru_litres.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
