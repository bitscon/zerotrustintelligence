from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from dev.site.build import build_site, check_build
from zti.demo.export import export_terminal_output


class SiteBuildTests(unittest.TestCase):
    def test_check_build_passes_for_repo_source(self) -> None:
        check_build()

    def test_build_outputs_root_relative_paths_and_hidden_core_nav(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_root = Path(tmp)
            artifact_out = build_site(tmp_root / "artifact")

            index_html = (artifact_out / "index.html").read_text(encoding="utf-8")
            adopt_html = (artifact_out / "adopt" / "index.html").read_text(encoding="utf-8")

            self.assertIn('href="/assets/site.css"', index_html)
            self.assertNotIn('/dev/site/', index_html)
            self.assertIn('href="/adopt/request-access/"', index_html)
            self.assertNotIn('>Core</span>', index_html)
            self.assertNotIn('>Core</span>', adopt_html)
            self.assertIn('href="/core/"', adopt_html)
            self.assertIn('<source src="/assets/zti-demo.mp4" type="video/mp4" />', index_html)
            source_video = Path.cwd() / "resources" / "demo" / "build" / "zti-demo.mp4"
            self.assertEqual((artifact_out / "assets" / "zti-demo.mp4").exists(), source_video.exists())

    def test_build_stages_canonical_transcript_into_output(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_root = Path(tmp)
            project_root = Path.cwd()
            build_site(tmp_root / "artifact", project_root=project_root)
            transcript_asset = (tmp_root / "artifact" / "assets" / "demo-output.txt").read_text(encoding="utf-8")
            canonical = export_terminal_output(project_root).read_text(encoding="utf-8")
            self.assertEqual(transcript_asset, canonical)

    def test_missing_demo_video_does_not_fail_by_default(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_root = Path(tmp)
            project_root = tmp_root / "project"
            project_root.mkdir(parents=True, exist_ok=True)
            with mock.patch.dict(os.environ, {}, clear=False):
                artifact_out = build_site(tmp_root / "artifact", project_root=project_root)
            self.assertFalse((artifact_out / "assets" / "zti-demo.mp4").exists())

    def test_missing_demo_video_fails_in_strict_mode(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_root = Path(tmp)
            project_root = tmp_root / "project"
            project_root.mkdir(parents=True, exist_ok=True)
            with mock.patch.dict(os.environ, {"ZTI_REQUIRE_DEMO_VIDEO": "1"}, clear=False):
                with self.assertRaises(FileNotFoundError):
                    build_site(tmp_root / "artifact", project_root=project_root)

    def test_existing_demo_video_stages_when_present(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_root = Path(tmp)
            project_root = tmp_root / "project"
            video_source = project_root / "resources" / "demo" / "build" / "zti-demo.mp4"
            video_source.parent.mkdir(parents=True, exist_ok=True)
            payload = b"fake-mp4-bytes"
            video_source.write_bytes(payload)
            artifact_out = build_site(tmp_root / "artifact", project_root=project_root)
            self.assertEqual((artifact_out / "assets" / "zti-demo.mp4").read_bytes(), payload)


if __name__ == "__main__":
    unittest.main()
