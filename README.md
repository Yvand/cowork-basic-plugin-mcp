# Basic tests plugin for Copilot Cowork

This repository is a minimal example of a GitHub Copilot plugin that exposes both:

- custom agent skills for Copilot to run locally
- an external MCP (Model Context Protocol) server connection for tools

The project is designed to help test and validate how a small plugin is packaged and consumed inside the Copilot Cowork environment.

## What this repo contains

- `manifest.json` — plugin manifest that declares the skill folders and MCP connector
- `skills/` — reusable Copilot skills
  - `test-python-echo` — runs a bundled Python script that echoes user text
  - `test-mcp-echo` — demonstrates how a skill can call a remote MCP tool
- `mcp-echo-tools.json` — tool metadata for the remote echo MCP server
- `color.png` and `outline.png` — plugin branding assets
- `.github/workflows/build-archive.yml` — builds and packages the plugin as a ZIP artifact for release

## Purpose

The repo serves as a lightweight sample for:

- building a Copilot plugin package
- registering skills that an agent can invoke
- connecting to an external MCP server
- validating the packaging and distribution flow for plugin-based experiences

In practice, it is intended for experimentation and learning rather than production use.

## Skills in this plugin

### `test-python-echo`

This skill runs a local Python script and returns the same text the user passed in. It is useful as a simple smoke test for a skill implementation.

### `test-mcp-echo`

This skill demonstrates connecting to an external MCP server and invoking an MCP tool. The connector points to a public echo MCP server used for testing connectivity and tool calling behavior.

## MCP connector

The plugin registers an anonymous MCP server named `mcp-echo-anonymous` using the URL:

https://mcpplaygroundonline.com/mcp-echo-server

This lets a Copilot skill invoke an echo tool from a remote MCP service without needing a custom backend implementation in this repo.

## Build and packaging

The repository includes a GitHub Actions workflow that:

1. zips the plugin contents into a release artifact
2. uploads that archive as a build artifact
3. creates a draft GitHub release when a `releases/*` tag is pushed

## Typical use case

This repo is useful for someone who wants to:

- prototype a Copilot plugin
- create a minimal skill-based extension
- learn how Copilot skills and MCP connectors are wired together
- validate that a packaged plugin can be built and distributed

## Notes

This is a sample project and is intentionally small and easy to inspect. It is best treated as a starting point for custom Copilot integrations or experiments with MCP-based tool access.
