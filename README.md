# LLM-Ops

A CLI tool to distribute standardized AI Agent workflows and memory protocols.

## Installation

The recommended way to install `llm-ops` is using `uv` as a tool. This ensures it runs in an isolated environment and is available globally.

```bash
# Run directly without installing
uv run llm-ops install antigravity

# Or install as a global tool
uv tool install .
```

## Usage

If installed as a tool:

```bash
# For Antigravity
llm-ops install antigravity

# For Augment Code
llm-ops install augment
```

If running from source with `uv`:

```bash
uv run llm-ops install antigravity
```

## Development

When developing locally, `uv tool install .` creates a snapshot of your code. To see your changes immediately without reinstalling, use `uv run`:

```bash
# Run the latest local version of the code
uv run python -m llm_ops.main install antigravity
```

If you want to update the global `llm-ops` command with your latest local changes, use the reload command from your source directory:

```bash
# From your llm-ops source directory
# Clean, rebuild, and reinstall in one step
uv run python -m llm_ops.main reload

# Then apply your changes
llm-ops install antigravity
```

Alternatively, you can manually rebuild and reinstall:

```bash
uv tool install --force .
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
