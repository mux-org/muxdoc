import json
import sys
import yaml
from uvicorn.importer import import_from_string


def dump_openapi(app='main:app', app_dir=None, out='openapi.yaml'):
    # https://www.doctave.com/blog/python-export-fastapi-openapi-spec
    if app_dir is not None:
        print(f"adding {app_dir} to sys.path")
        sys.path.insert(0, app_dir)

    print(f"importing app from {app}")
    app = import_from_string(app)
    openapi = app.openapi()
    version = openapi.get("openapi", "unknown version")

    print(f"writing openapi spec v{version}")
    with open(out, "w") as f:
        if out.endswith(".json"):
            json.dump(openapi, f, indent=2)
        else:
            yaml.dump(openapi, f, sort_keys=False)

    print(f"spec written to {out}")
