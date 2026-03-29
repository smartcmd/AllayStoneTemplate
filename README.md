# AllayStone Template

Minimal template repository for writing a Python plugin for AllayStone.

## Before You Start

This repository is meant to be copied with GitHub's template feature and then renamed for your plugin.

Update these places first:

1. `pyproject.toml`
2. `src/allaystone_template/`
3. `src/allaystone_template/plugin.py`

## Rename Checklist

1. Change `[project].name` in `pyproject.toml` to `allaystone-<your-plugin-name>`.
2. Change `[project.entry-points.allaystone]` so the key is your plugin name and the value points to your new module and class.
3. Rename `src/allaystone_template/` to your package name.
4. Rename `TemplatePlugin` in `src/allaystone_template/plugin.py` to your real plugin class name.
5. Update `version`, `api_version`, `description`, `authors`, and `website`.

The distribution name must keep the `allaystone-` prefix or AllayStone will not load it.

## Optional Editor Stubs

AllayStone publishes a wheel containing the generated `allay.api` stubs and the `allaystone` helper package.

Install it from an AllayStone release if you want autocomplete and type hints in your editor:

```powershell
python -m pip install https://github.com/smartcmd/AllayStone/releases/download/<tag>/<wheel-file>.whl
```

## Build A Wheel

```powershell
python -m pip wheel . --no-deps --wheel-dir dist
```

Copy the generated wheel from `dist/` into your server's `plugins/` directory.

## GitHub Actions

This template includes [`.github/workflows/build.yml`](.github/workflows/build.yml).

- pushes to `main`, pull requests, and manual runs build a wheel and upload it as a workflow artifact
- published GitHub releases also attach the built wheel to the release assets

If you want a downloadable wheel for each version, create a tag and publish a GitHub release from that tag.

## Install Editable

```powershell
python -m pip install -e . --prefix <server>/plugins/.local
```

For `./gradlew runServer`, the managed prefix is usually `build/run/plugins/.local`.

## Remove Editable

Stop the server first, then uninstall the distribution from the same prefix:

```powershell
$env:PYTHONPATH = "<server>/plugins/.local/Lib/site-packages"
python -m pip uninstall allaystone-<your-plugin-name>
Remove-Item Env:PYTHONPATH
```

## Plugin Layout

`src/allaystone_template/plugin.py` contains the minimal plugin entry class. It shows:

- lifecycle hooks: `on_load()`, `on_enable()`, `on_disable()`
- how to use `self.logger`
- how to write files into `self.data_folder`

## Local Example

After you finish renaming the template, build a wheel and copy it into an Allay server that already has the AllayStone jar installed.

On startup, the example implementation writes a marker file into `plugins/<plugin-name>/`.
