"""Verify that local Python and container development-tool versions stay aligned."""

import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


def read_env(path: Path) -> dict[str, str]:
    """Read simple KEY=VALUE entries from a dotenv file, ignoring comments and blanks."""
    values = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line and not line.startswith("#"):
            key, value = line.split("=", maxsplit=1)
            values[key] = value
    return values


class DevcontainerVersionTests(unittest.TestCase):
    """Check version pins shared by the local setup and development container."""

    def test_local_tool_versions_match_the_container_build_inputs(self):
        """Keep local version pins wired through Compose to Docker build arguments."""
        local_version = (ROOT / ".python-version").read_text(encoding="utf-8").strip()
        versions = read_env(ROOT / ".devcontainer" / ".env")
        container_version = versions["PYTHON_VERSION"]

        self.assertRegex(local_version, r"^\d+\.\d+\.\d+$")
        self.assertEqual(local_version, container_version)

        version_names = ("PYTHON_VERSION", "UV_VERSION", "JUST_VERSION", "DEBIAN_CODENAME")
        dockerfile = (ROOT / ".devcontainer" / "Dockerfile").read_text(encoding="utf-8")
        compose = (ROOT / ".devcontainer" / "compose.yaml").read_text(encoding="utf-8")
        dockerfile_args = set(re.findall(r"^ARG (\w+)(?:=\S+)?$", dockerfile, re.MULTILINE))

        for name in version_names:
            with self.subTest(name=name):
                self.assertIn(name, dockerfile_args)
                self.assertIn(f"{name}: ${{{name}:?", compose)

    def test_docker_feature_and_cli_versions_are_pinned(self):
        """Require explicit Docker feature and CLI versions instead of floating tags."""
        config = (ROOT / ".devcontainer" / "devcontainer.json").read_text(encoding="utf-8")
        self.assertIn("docker-outside-of-docker:1.10.1", config)
        self.assertRegex(config, r'"version"\s*:\s*"29\.9\.3"')
        self.assertRegex(config, r'"dockerDashComposeVersion"\s*:\s*"v2"')
        self.assertNotIn('"version": "latest"', config)

    def test_feature_lock_pins_the_resolved_artifact_and_integrity(self):
        """Verify the Docker feature lock records a version and matching digest."""
        lock_path = ROOT / ".devcontainer" / "devcontainer-lock.json"
        lock = json.loads(lock_path.read_text(encoding="utf-8"))
        feature = lock["features"]["ghcr.io/devcontainers/features/docker-outside-of-docker:1.10.1"]

        self.assertRegex(feature["version"], r"^\d+\.\d+\.\d+$")
        self.assertRegex(feature["resolved"], r"@sha256:[0-9a-f]{64}$")
        self.assertEqual(feature["integrity"], "sha256:" + feature["resolved"].rsplit(":", 1)[1])


if __name__ == "__main__":
    unittest.main()
