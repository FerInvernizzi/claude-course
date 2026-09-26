"""Módulo 11.4 — Servidor MCP mínimo (SDK oficial `mcp` 2.x).

Probalo en Claude Code:
    claude mcp add --transport stdio inventario -- python servidor_inventario.py
"""

from mcp.server.mcpserver import MCPServer

mcp = MCPServer("inventario")

@mcp.tool()
def stock(producto: str) -> int:
    """Devuelve el stock disponible de un producto."""
    return {"yerba": 120, "mate": 35}.get(producto.lower(), 0)

if __name__ == "__main__":
    mcp.run()   # stdio por defecto
