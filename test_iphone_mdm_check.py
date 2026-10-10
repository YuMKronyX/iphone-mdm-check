
import shutil
import subprocess
import unittest
from unittest.mock import Mock, patch


def run_command(command, timeout=5):
    """Execute a command and return its result safely."""
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
        return (
            result.returncode,
            result.stdout.strip(),
            result.stderr.strip(),
        )

    except FileNotFoundError:
        return 127, "", f"Commande introuvable : {command[0]}"

    except subprocess.TimeoutExpired:
        return 124, "", f"Commande interrompue après {timeout} secondes"


def tool_exists(command):
    """Check whether a command is available."""
    return shutil.which(command) is not None


class TestRunCommand(unittest.TestCase):

    @patch("subprocess.run")
    def test_successful_command(self, mock_run):
        mock_run.return_value = Mock(
            returncode=0,
            stdout="iPhone connected\n",
            stderr="",
        )

        result = run_command(["idevice_id", "-l"])

        self.assertEqual(result, (0, "iPhone connected", ""))

    @patch("subprocess.run", side_effect=FileNotFoundError)
    def test_command_not_found(self, mock_run):
        result = run_command(["commande_inexistante"])

        self.assertEqual(result[0], 127)
        self.assertEqual(result[1], "")
        self.assertIn("Commande introuvable", result[2])

    @patch(
        "subprocess.run",
        side_effect=subprocess.TimeoutExpired(
            cmd=["ideviceinfo"],
            timeout=5,
        ),
    )
    def test_command_timeout(self, mock_run):
        result = run_command(["ideviceinfo"])

        self.assertEqual(result[0], 124)
        self.assertEqual(result[1], "")
        self.assertIn("interrompue", result[2])

    @patch("shutil.which", return_value="/usr/bin/lsusb")
    def test_tool_exists(self, mock_which):
        self.assertTrue(tool_exists("lsusb"))
        mock_which.assert_called_once_with("lsusb")

    @patch("shutil.which", return_value=None)
    def test_tool_does_not_exist(self, mock_which):
        self.assertFalse(tool_exists("outil_inexistant"))
        mock_which.assert_called_once_with("outil_inexistant")


if __name__ == "__main__":
    unittest.main()
