# 🔒 SecureStaticSite — Secure Static Website Hosting on AWS

A fully functional static website hosted on Amazon S3 with CloudFront CDN for HTTPS enforcement and reduced global latency. IAM least-privilege policies configured for secure access control.

---

## ☁️ AWS Services Used

| Service | Purpose |
|---|---|
| **S3** | Hosts static website files |
| **CloudFront** | CDN for HTTPS delivery and low latency |
| **IAM** | Least-privilege access policy |

---

## 🏗️ Architecture

```
User → CloudFront (HTTPS) → S3 (Static Website)
                ↑
          IAM Policy (Least Privilege Access)
```

---

## 🔄 How It Works

1. Static website files are stored in an **S3 bucket**
2. **CloudFront** distribution sits in front of S3 for HTTPS and CDN delivery
3. **IAM policy** ensures least-privilege access — only GetObject and ListBucket allowed
4. Users access the website via the **CloudFront HTTPS URL**

---

## 🔐 IAM Policy (Least Privilege)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "S3ReadOnlyAccess",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::securestaticsite-mitesh",
        "arn:aws:s3:::securestaticsite-mitesh/*"
      ]
    },
    {
      "Sid": "CloudFrontReadOnly",
      "Effect": "Allow",
      "Action": [
        "cloudfront:GetDistribution",
        "cloudfront:ListDistributions"
      ],
      "Resource": "*"
    }
  ]
}
```

---

## 📸 Screenshots

### S3 Bucket
![S3](screenshots/s3-bucket.png)

### CloudFront Distribution
![CloudFront](screenshots/cloudfront.png)

### IAM Policy
![IAM](screenshots/iam-policy.png)

### Live Website
![Website](screenshots/live-website.png)

---

## 🚀 Deployment Steps

1. **S3** — Create bucket, disable block public access, enable static website hosting, upload index.html
2. **IAM** — Create least-privilege policy with S3 read-only access
3. **CloudFront** — Create distribution pointing to S3 website endpoint, enable HTTPS
4. **Invalidation** — Create `/*` invalidation to clear cache

---

## 💰 Cost

Runs entirely on **AWS Free Tier** — $0/month!

| Service | Free Tier |
|---|---|
| S3 | 5GB storage |
| CloudFront | 1TB transfer/month |
| IAM | Always free |

---

## 👨‍💻 Author

**Mitesh Baikar**
Cloud & DevOps Enthusiast | Mumbai, India
[LinkedIn](https://linkedin.com/in/your-linkedin) | [GitHub](https://github.com/your-github)
