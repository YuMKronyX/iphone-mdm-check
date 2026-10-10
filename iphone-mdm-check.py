#!/usr/bin/env python3
“”“iPhone MDM Check — diagnostic local uniquement.”””

import shutil
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox

def diagnostic():
result = []

for tool in ("idevice_id", "ideviceinfo", "idevicepair"):
    path = shutil.which(tool)
    result.append(f"{tool}: {path or 'non installé'}")
tool = shutil.which("idevice_id")
if tool:
    try:
        p = subprocess.run(
            [tool, "-l"],
            capture_output=True,
            text=True,
            timeout=5
        )
        devices = p.stdout.strip()
        result.append(
            "\nAppareils détectés :\n" +
            (devices or "Aucun appareil détecté")
        )
    except (OSError, subprocess.TimeoutExpired):
        result.append("\nErreur pendant la détection USB.")
result.append(
    "\nImportant : ce programme ne retire pas le MDM. "
    "La libération doit être demandée à l'organisation "
    "qui gère l'appareil."
)
output.config(state="normal")
output.delete("1.0", "end")
output.insert("1.0", "\n".join(result))
output.config(state="disabled")

app = tk.Tk()
app.title(“iPhone MDM Check”)
app.geometry(“600x420”)

ttk.Label(
app,
text=“iPhone MDM Check”,
font=(“TkDefaultFont”, 18, “bold”)
).pack(pady=12)

ttk.Label(
app,
text=“Diagnostic USB pour Linux — sans contournement MDM”,
wraplength=550
).pack(pady=5)

ttk.Button(
app,
text=“Lancer le diagnostic”,
command=diagnostic
).pack(pady=12)

output = tk.Text(app, wrap=“word”, height=14, width=65)
output.pack(padx=12, pady=8, fill=“both”, expand=True)
output.insert(
“1.0”,
“Clique sur « Lancer le diagnostic » pour commencer.”
)
output.config(state=“disabled”)

app.mainloop()