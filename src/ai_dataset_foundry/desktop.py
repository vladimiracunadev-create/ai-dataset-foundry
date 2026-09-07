from __future__ import annotations

import socket
import threading
import time

from ai_dataset_foundry.webapp import create_app


def _free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def main() -> None:
    try:
        import uvicorn
        import webview
    except ImportError as exc:
        raise RuntimeError("Desktop support requires: uv sync --extra desktop") from exc

    port = _free_port()
    server = uvicorn.Server(
        uvicorn.Config(create_app(), host="127.0.0.1", port=port, log_level="warning")
    )
    thread = threading.Thread(target=server.run, daemon=True, name="foundry-local-server")
    thread.start()
    for _ in range(50):
        if server.started:
            break
        time.sleep(0.1)
    if not server.started:
        raise RuntimeError("The local interface did not start")
    webview.create_window(
        "AI Dataset Foundry",
        f"http://127.0.0.1:{port}",
        width=1120,
        height=760,
        min_size=(820, 620),
    )
    webview.start()
    server.should_exit = True


if __name__ == "__main__":
    main()
