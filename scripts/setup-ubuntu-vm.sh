#!/bin/bash
echo "=== IntelliFlow CRM Ubuntu VM Setup ==="
apt update && apt upgrade -y
apt install -y curl git docker.io docker-compose-plugin
systemctl enable --now docker

# Clone repo
git clone https://github.com/YOUR-USERNAME/intelliflow-crm.git /opt/intelliflow-crm
cd /opt/intelliflow-crm

echo "Setup complete! Now edit .env and run:"
echo "docker compose -f docker-compose.prod.yml up -d --build"