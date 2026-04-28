# 📊 CloudWatch Monitoring Dashboard — EC2 Health Monitor & Auto Alert System

A real-time cloud monitoring system built on AWS that automatically tracks EC2 CPU utilization and sends instant email alerts when the threshold is breached.

---

## ☁️ AWS Services Used

| Service | Purpose |
|---|---|
| **EC2** | Ubuntu server being monitored |
| **CloudWatch** | Real-time CPU metrics collection + Alarm |
| **SNS** | Instant email notification delivery |
| **IAM** | Least-privilege access policies |

---

## 🏗️ Architecture

```
EC2 Instance (Ubuntu)
        ↓
CloudWatch (monitors CPU every minute)
        ↓
CloudWatch Alarm (triggered when CPU > threshold)
        ↓
SNS Topic
        ↓
📧 Email Alert
```

---

## 🔄 How It Works

1. **EC2** Ubuntu instance is deployed and running
2. **CloudWatch** automatically collects CPU utilization metrics every minute
3. A **CloudWatch Alarm** is configured to trigger when CPU exceeds the threshold
4. When alarm triggers, it publishes a message to **SNS topic**
5. **SNS** instantly delivers an email alert to all subscribed users
6. **IAM** least-privilege policies secure the entire setup

---

## 🧪 How I Tested It

Used the **stress** tool to artificially push EC2 CPU to **98%** to validate the alarm:

```bash
sudo apt install stress -y
stress --cpu 2 --timeout 600
```

Result: CloudWatch detected the CPU spike → Alarm triggered → **Email received within minutes!** ✅

---

## 📸 Screenshots

### CloudWatch Alarm — In Alarm State
![Alarm](screenshots/cloudwatch-alarm.png)

### CPU Utilization Graph — 98% Spike
![CPU Graph](screenshots/cpu-graph.png)

### SNS Email Notification Received
![Email](screenshots/email-notification.png)

### EC2 Instance Running
![EC2](screenshots/ec2-instance.png)

### SNS Topic with Subscription
![SNS](screenshots/sns-topic.png)

---

## 🚀 Deployment Steps

### 1. EC2 Setup
- Launch t2.micro Ubuntu instance (Free Tier)
- Name: `cloudwatch-monitor-server`

### 2. SNS Setup
- Create Standard SNS topic: `cloudwatch-alerts-topic`
- Subscribe email address
- Confirm subscription via email

### 3. CloudWatch Alarm Setup
- Go to CloudWatch → Alarms → Create alarm
- Select EC2 → Per-Instance Metrics → CPUUtilization
- Set threshold (e.g., CPU > 70%)
- Configure action: Send notification to SNS topic

### 4. IAM Policy
- Create least-privilege IAM policy
- Allow only CloudWatch read + SNS publish permissions

### 5. Test
- Connect to EC2 via EC2 Instance Connect
- Install and run stress tool
- Verify email alert received

---

## 💡 Real World Use Case

| Scenario | How This Helps |
|---|---|
| E-commerce sale | Detect server overload before crash |
| Startup | 24/7 server health monitoring |
| Any Company | Get alerted before downtime happens |

---

## 💰 Cost

Runs entirely on **AWS Free Tier** — $0!

| Service | Free Tier |
|---|---|
| EC2 t2.micro | 750 hrs/month |
| CloudWatch | 10 alarms free |
| SNS | 1M notifications free |
| IAM | Always free |

---

## 👨‍💻 Author

**Mitesh Baikar**
Cloud & DevOps Enthusiast | Mumbai, India
[LinkedIn](https://www.linkedin.com/in/mitesh-baikar-3004a22a0/) | [GitHub](https://github.com/Mitesh307)
