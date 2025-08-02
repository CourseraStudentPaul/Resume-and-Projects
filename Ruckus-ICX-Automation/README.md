# Ruckus ICX Switch Configuration Automation
# 🚀 Ruckus ICX Switch Configuration Automation

Automate the generation and deployment of configuration scripts for Ruckus ICX switches using Python, CSV input, and optionally Ansible. This project streamlines switch provisioning based on a standardized Excel-based configuration template.

---

## 📌 Project Goals

- Parse a reusable configuration template
- Generate switch-specific config files from CSV input
- Optionally deploy configs via SSH using Ansible

---

## 📁 Folder Structure

```plaintext
Ruckus-ICX-Automation/
├── ansible/
│   ├── inventory/
│   │   └── hosts.ini
│   └── playbooks/
│       └── deploy_configs.yml
├── data/
│   └── switch_parameters_template.csv
├── scripts/
│   └── generate_configs.py
├── templates/
│   └── ICX-Config-firmware10X-HMA-v6 Original.xlsx
├── generated_configs/  ← (created at runtime)
└── README.md

