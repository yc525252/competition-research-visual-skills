# Competition · Research · Visual Skills

31 lightweight Agent Skills for competition projects, academic work, and document or visual production.

[中文](README.md) · [MIT License](LICENSE) · [Sources and scope](SOURCES.md)

Each `crv-` entry defines its inputs, workflow, outputs, tool requirements, and example request. Most detailed guidance is currently in Chinese.

|Category|Count|Guide|
|---|---:|---|
|Competition and business|6|[Guide](docs/competition.md)|
|Academic research|5|[Guide](docs/academic.md)|
|Documents, presentations, and visuals|20|[Guide](docs/documents.md)|

## Quick start

Read an individual `skills/<name>/SKILL.md` directly, or install selected entries into a compatible Agent environment. Discovery and `$skill-name` support depend on the host.

```bash
git clone https://github.com/yc525252/competition-research-visual-skills.git
cd competition-research-visual-skills
python scripts/list_skills.py
python scripts/install.py --category competition --dry-run
python scripts/install.py --category competition
```

Management scripts require Python 3.10+ and use only the standard library. The default destination is `CODEX_HOME/skills`, or `~/.codex/skills` if `CODEX_HOME` is unset. Use `--target` for another compatible directory. Existing destinations are never overwritten.

```text
$crv-research-writing
Use the supplied methods and experiment records to draft the Methods section.
Preserve conditions and parameters, and list missing reproducibility information.
```

These are original lightweight workflows, not copies of the previously installed third-party implementations listed in `SOURCES.md`. No vendor document engine, external slide pipeline, model, font, image, or template is bundled. Actual file editing, image generation, plotting, and rendering require suitable tools in the host environment.

## Validation

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
```

Checks cover repository structure, metadata, links, content scope, and installer behavior. They do not claim end-to-end execution of all 31 use cases or validate external services.

See [capability boundaries](docs/capabilities.md) and [contributing](CONTRIBUTING.md).
