import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


def read_env(path: Path) -> dict[str, str]:
    values = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line and not line.startswith("#"):
            key, value = line.split("=", maxsplit=1)
            values[key] = value
    return values


class DevcontainerVersionTests(unittest.TestCase):
    def test_local_python_version_matches_the_container_image_pin(self):
        local_version = (ROOT / ".python-version").read_text(encoding="utf-8").strip()
        versions = read_env(ROOT / ".devcontainer" / ".env")
        container_version = versions["PYTHON_VERSION"]

        self.assertRegex(local_version, r"^\d+\.\d+\.\d+$")
        self.assertEqual(local_version, container_version)

        dockerfile = (ROOT / ".devcontainer" / "Dockerfile").read_text(encoding="utf-8")
        dockerfile_versions = dict(
            re.findall(
                r"^ARG (PYTHON_VERSION|UV_VERSION|JUST_VERSION)=(\S+)$",
                dockerfile,
                re.MULTILINE,
            )
        )
        self.assertEqual(
            dockerfile_versions,
            {name: versions[name] for name in ("PYTHON_VERSION", "UV_VERSION", "JUST_VERSION")},
        )

    def test_docker_feature_and_cli_versions_are_pinned(self):
        config = (ROOT / ".devcontainer" / "devcontainer.json").read_text(encoding="utf-8")
        self.assertIn("docker-outside-of-docker:1.10.1", config)
        self.assertRegex(config, r'"version"\s*:\s*"29\.9\.3"')
        self.assertRegex(config, r'"dockerDashComposeVersion"\s*:\s*"v2"')
        self.assertNotIn('"version": "latest"', config)

    def test_feature_lock_pins_the_resolved_artifact_and_integrity(self):
        lock_path = ROOT / ".devcontainer" / "devcontainer-lock.json"
        lock = json.loads(lock_path.read_text(encoding="utf-8"))
        feature = lock["features"]["ghcr.io/devcontainers/features/docker-outside-of-docker:1.10.1"]

        self.assertRegex(feature["version"], r"^\d+\.\d+\.\d+$")
        self.assertRegex(feature["resolved"], r"@sha256:[0-9a-f]{64}$")
        self.assertEqual(feature["integrity"], "sha256:" + feature["resolved"].rsplit(":", 1)[1])


if __name__ == "__main__":
    unittest.main()
