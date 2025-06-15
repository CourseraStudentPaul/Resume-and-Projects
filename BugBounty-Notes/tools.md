# 🧰 Recon & Testing Toolkit

This is a running list of tools and commands I use for bug bounty testing and recon.

## 🌐 Passive Recon
- `amass enum -d example.com` — Subdomain discovery
- `crt.sh` — Certificate Transparency logs
- `builtwith.com` — Tech stack fingerprinting

## 🛠️ Active Recon
- `nmap -sC -sV -Pn target.com` — Port scan + service detection
- `ffuf -u https://target.com/FUZZ -w wordlist.txt` — Directory fuzzing
- Burp Suite — Interception, repeater, scanner

## 💣 Exploitation / Testing
- `sqlmap -u "https://target.com?id=1" --dbs` — SQL injection
- `wfuzz -c -z file,payloads.txt -u "https://target.com/search?q=FUZZ"` — Parameter fuzzing
- `XSStrike`, `ParamSpider`, `httpx`, `Waybackurls` — Additional tools for XSS and recon

## 🔐 Authentication & Session Testing
- Inspect cookies, headers, CSRF tokens via browser dev tools
- Burp Suite’s session handling rules
