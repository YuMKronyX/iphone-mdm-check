import unittest
from unittest.mock import patch, MagicMock
import shutil
import subprocess

def run_command(command, timeout=10):
try:
result = subprocess.run(
command,
capture_output=True,
text=True,
timeout=timeout,
check=False
)
return result.returncode, result.stdout.strip(), result.stderr.strip()
except FileNotFoundError:
return 127, “”, f”Commande introuvable : {command[0]}”
except subprocess.TimeoutExpired:
return 124, “”, f”Délai dépassé : {’ ’.join(command)}”
except Exception as exc:
return 1, “”, str(exc)

class TestRunCommand(unittest.TestCase):

@patch("subprocess.run")
def test_successful_command(self, mock_run):
    mock_run.return_value = MagicMock(
        returncode=0,
        stdout="device123\n",
        stderr=""
    )
    code, out, err = run_command(["idevice_id", "-l"])
    self.assertEqual(code, 0)
    self.assertEqual(out, "device123")
    self.assertEqual(err, "")
@patch("subprocess.run", side_effect=FileNotFoundError)
def test_missing_command(self, mock_run):
    code, out, err = run_command(["commande_inexistante"])
    self.assertEqual(code, 127)
    self.assertIn("introuvable", err)
@patch(
    "subprocess.run",
    side_effect=subprocess.TimeoutExpired(cmd="ideviceinfo", timeout=10)
)
def test_timeout(self, mock_run):
    code, out, err = run_command(["ideviceinfo"])
    self.assertEqual(code, 124)
    self.assertIn("Délai dépassé", err)
@patch("shutil.which", return_value=None)
def test_missing_tool_detection(self, mock_which):
    self.assertIsNone(shutil.which("idevice_id"))

if name == “main”:
unittest.main(verbosity=2)