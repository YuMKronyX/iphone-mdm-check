#!/usr/bin/env python3
import shutil
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

APP_NAME = “iPhone MDM Check — V2”

class IPhoneDiagnosticApp:
def init(self, root):
self.root = root
self.root.title(APP_NAME)
self.root.geometry(“720x600”)
self.root.minsize(520, 450)

    self.output = tk.Text(
        root, wrap="word", font=("Courier", 10),
        bg="#15171c", fg="#e6e6e6",
        insertbackground="white"
    )
    self.output.pack(fill="both", expand=True, padx=12, pady=12)
    buttons = ttk.Frame(root)
    buttons.pack(fill="x", padx=12, pady=(0, 12))
    ttk.Button(
        buttons, text="Lancer le diagnostic",
        command=self.run_diagnostics
    ).pack(side="left", padx=(0, 8))
    ttk.Button(
        buttons, text="Copier le rapport",
        command=self.copy_report
    ).pack(side="left", padx=(0, 8))
    ttk.Button(
        buttons, text="Effacer",
        command=self.clear_report
    ).pack(side="left")
    self.log("iPhone MDM Check — V2")
    self.log("Outil de diagnostic USB pour Linux")
    self.log("Aucun contournement du MDM n'est effectué.\n")
def log(self, text):
    self.output.insert("end", text + "\n")
    self.output.see("end")
def run_command(self, command, timeout=10):
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
        return 127, "", f"Commande introuvable : {command[0]}"
    except subprocess.TimeoutExpired:
        return 124, "", f"Délai dépassé : {' '.join(command)}"
    except Exception as exc:
        return 1, "", str(exc)
def check_command(self, name):
    path = shutil.which(name)
    if path:
        self.log(f"[OK] {name} : {path}")
        return True
    self.log(f"[MANQUANT] {name}")
    return False
def run_diagnostics(self):
    self.clear_report()
    self.log(f"Rapport du {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}")
    self.log("=" * 55)
    self.log("\n1. Vérification des outils Linux")
    tools = ["idevice_id", "ideviceinfo", "idevicepair", "lsusb"]
    available = {tool: self.check_command(tool) for tool in tools}
    self.log("\n2. Détection USB")
    if available["lsusb"]:
        code, out, err = self.run_command(["lsusb"])
        if out:
            matches = [
                line for line in out.splitlines()
                if any(word in line.lower() for word in
                       ["apple", "iphone", "ipad", "ipod"])
            ]
            if matches:
                for line in matches:
                    self.log(f"[DÉTECTÉ] {line}")
            else:
                self.log("[INFO] Aucun périphérique Apple identifié dans lsusb.")
                self.log("Vérifie le câble, le port USB et le déverrouillage de l'iPhone.")
        elif err:
            self.log(f"[ERREUR] {err}")
    else:
        self.log("[INFO] Installe usbutils pour utiliser lsusb.")
    self.log("\n3. Recherche de l'iPhone")
    device_id = None
    if available["idevice_id"]:
        code, out, err = self.run_command(["idevice_id", "-l"])
        if code == 0 and out:
            devices = out.splitlines()
            device_id = devices[0]
            self.log(f"[OK] {len(devices)} appareil(s) détecté(s)")
            for device in devices:
                self.log(f"  Identifiant : {device}")
        elif code == 0:
            self.log("[NON DÉTECTÉ] Aucun iPhone reconnu par libimobiledevice.")
        else:
            self.log(f"[ERREUR] {err or out or 'Détection impossible'}")
    self.log("\n4. Informations iOS")
    if device_id and available["ideviceinfo"]:
        code, out, err = self.run_command(
            ["ideviceinfo", "-u", device_id], timeout=15
        )
        if code == 0:
            wanted = {
                "DeviceName", "ProductType", "ProductVersion",
                "BuildVersion", "ModelNumber"
            }
            found = {}
            for line in out.splitlines():
                if ": " in line:
                    key, value = line.split(": ", 1)
                    if key in wanted:
                        found[key] = value
            for key in sorted(found):
                self.log(f"{key} : {found[key]}")
            if not found:
                self.log("[INFO] Informations détaillées indisponibles.")
        else:
            self.log(f"[ERREUR] {err or out}")
            self.log("Déverrouille l'iPhone et accepte « Faire confiance » si proposé.")
    else:
        self.log("[INFO] Informations indisponibles sans appareil détecté et ideviceinfo.")
    self.log("\n5. Vérification du jumelage")
    if device_id and available["idevicepair"]:
        code, out, err = self.run_command(
            ["idevicepair", "-u", device_id, "validate"], timeout=15
        )
        if code == 0:
            self.log("[OK] Jumelage validé.")
        else:
            self.log("[À VÉRIFIER] Jumelage non validé.")
            self.log(err or out or "Aucun détail fourni.")
            self.log("Déverrouille l'iPhone et vérifie l'autorisation de confiance.")
    elif not device_id:
        self.log("[INFO] Jumelage non testé : appareil non détecté.")
    else:
        self.log("[INFO] Jumelage non testé : idevicepair absent.")
    self.log("\n6. Résumé et conseils")
    if not available["idevice_id"]:
        self.log("• Installe libimobiledevice pour obtenir idevice_id.")
    if not available["ideviceinfo"] or not available["idevicepair"]:
        self.log("• Installe les outils libimobiledevice manquants.")
    self.log("• Essaie un câble USB compatible avec le transfert de données.")
    self.log("• Déverrouille l'iPhone et reconnecte-le.")
    self.log("• Si l'iPhone apparaît mais reste géré par une organisation, contacte son administrateur.")
    self.log("• Cet outil ne supprime pas et ne contourne pas un profil MDM.")
    self.log("\nFin du diagnostic.")
def copy_report(self):
    report = self.output.get("1.0", "end-1c")
    self.root.clipboard_clear()
    self.root.clipboard_append(report)
    self.root.update()
    messagebox.showinfo("Rapport", "Rapport copié dans le presse-papiers.")
def clear_report(self):
    self.output.delete("1.0", "end")

def main():
root = tk.Tk()
IPhoneDiagnosticApp(root)
root.mainloop()

if name == “main”:
main()