# Project Deployment on GCP VM: Comprehensive Guide

## 1. Configure Project Dependencies

### Python Project Dependencies
```bash
# Update package manager
sudo apt update
sudo apt upgrade -y

# Install Python and pip
sudo apt install python3 python3-pip -y

# Navigate to project directory
cd ~/LegAIDK-main

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install project dependencies
pip install -r requirements.txt
```

### Node.js Project Dependencies
```bash
# Install Node.js and npm
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install -y nodejs

# Navigate to project directory
cd ~/LegAIDK-main

# Install project dependencies
npm install
```

## 2. Set Up Runtime Environment

### Environment Variables
```bash
# Create .env file
touch .env

# Edit environment variables
nano .env

# Example .env content
DATABASE_URL=your_database_connection_string
API_KEY=your_api_key
DEBUG=False
```

### Configuration Management
```bash
# Create a config directory
mkdir -p config

# Create configuration files
touch config/production.json
touch config/development.json

# Manage different environment configurations
```

## 3. Expose Necessary Ports

### Firewall Configuration
```bash
# Open specific port (e.g., 8000)
sudo ufw allow 8000/tcp

# Alternative: GCP Firewall Rules
gcloud compute firewall-rules create allow-custom-port \
    --allow=tcp:8000 \
    --source-ranges=0.0.0.0/0 \
    --target-tags=http-server \
    --description="Allow TCP traffic on port 8000"
```

### Nginx as Reverse Proxy (Optional)
```bash
# Install Nginx
sudo apt install nginx -y

# Configure Nginx
sudo nano /etc/nginx/sites-available/myproject

# Sample Nginx configuration
server {
    listen 80;
    server_name your_domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

# Enable site
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## 4. Service Management

### Systemd Service Configuration
```bash
# Create systemd service file
sudo nano /etc/systemd/system/myproject.service

# Example Python Flask service
[Unit]
Description=LegAIDK Project Service
After=network.target

[Service]
User=adnaannazir10
WorkingDirectory=/home/adnaannazir10/LegAIDK-main
ExecStart=/home/adnaannazir10/LegAIDK-main/venv/bin/gunicorn \
    --workers 3 \
    --bind 127.0.0.1:8000 \
    app:app

Restart=always

[Install]
WantedBy=multi-user.target

# Reload systemd, enable and start service
sudo systemctl daemon-reload
sudo systemctl enable myproject.service
sudo systemctl start myproject.service
```

### Process Management Tools
```bash
# Monitor service
sudo systemctl status myproject.service

# View logs
journalctl -u myproject.service

# Alternative: PM2 for Node.js
npm install -g pm2
pm2 start app.js
pm2 startup systemd
```

## 5. SSL/HTTPS Configuration

### Let's Encrypt with Certbot
```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx -y

# Obtain SSL certificate
sudo certbot --nginx -d your_domain.com
```

## 6. Monitoring and Logging

### Basic Monitoring
```bash
# System resource monitoring
top
htop

# Disk usage
df -h

# Memory usage
free -h
```

### Advanced Monitoring
```bash
# Install Prometheus Node Exporter
wget https://github.com/prometheus/node_exporter/releases/download/v*/node_exporter-*.*-amd64.tar.gz
tar xvfz node_exporter-*.*-amd64.tar.gz
cd node_exporter-*.*-amd64
./node_exporter
```

## Troubleshooting Checklist
- Verify all dependencies are installed
- Check service logs for errors
- Ensure correct file permissions
- Validate environment variables
- Test application locally before exposing

## Security Recommendations
- Keep system updated
- Use fail2ban for SSH protection
- Implement firewall rules
- Use strong, unique passwords
- Regularly audit system access

## Backup Strategy
```bash
# Simple backup script
#!/bin/bash
BACKUP_DIR="/home/adnaannazir10/backups"
PROJECT_DIR="/home/adnaannazir10/LegAIDK-main"

mkdir -p $BACKUP_DIR
tar -czvf $BACKUP_DIR/project_backup_$(date +"%Y%m%d_%H%M%S").tar.gz $PROJECT_DIR
```

## Post-Deployment Validation
1. Check application accessibility
2. Verify all services are running
3. Test critical functionalities
4. Monitor system resources
5. Review security configurations
