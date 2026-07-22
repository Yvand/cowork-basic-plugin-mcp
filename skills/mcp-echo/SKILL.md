---
name: mcp-echo
description: |
  Demonstrates how to connect to an external MCP (Model Context Protocol) server from a Copilot skill.
  Use when user asks to "test the echo server", "send a message to the MCP server", or "verify MCP connectivity".
license: MIT
metadata:
  author: Yvand
  version: "1.0"
---

# MCP Echo Skill

This skill demonstrates how to connect to an external MCP (Model Context Protocol) server from a Copilot skill. It calls tools from a configured test MCP server.

## When to use this skill

Use this skill when:
- The user asks to test the MCP echo server
- The user wants to send a message to an MCP server
- The user asks to verify MCP connectivity
- The user mentions "echo" and "MCP" together

## MCP Echo tools

- **`test_mcp_echo`** — Test the MCP echo server. Inputs: text to echo back. Returns the echoed text.

## Instructions

When invoked, you should:

1. **Call the tool** -  Use `test_mcp_echo` with the user's input as the parameter. The tool will return a response from the MCP echo server.

2. **Return the result** - Present the response to the user

## Example usage

If the user says "test the echo server with hello world", you should:
1. Call the tool `test_mcp_echo` with the parameter "hello world". The tool will return "hello world" from the MCP echo server.
2. Return the response
