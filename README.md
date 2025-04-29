

 CTF Challenge - Encoding, Encryption & Web Forensics (Levels 1-10)

Welcome to my custom-built  **Capture The Flag (CTF) challenge** focused on **encoding**, **encryption**, and **web forensics** concepts.

Test your technical skills, logical thinking, and investigative instincts across **10 carefully designed levels**!


## 📜 Levels Overview

| Level | Challenge Type                   | Hint                                                      |
|:-----:|:---------------------------------:|:----------------------------------------------------------:|
| 1     | Base64 Hidden Flag                | Inspect developer tools carefully.                        |
| 2     | Caesar Cipher                     | Rotate and reveal the hidden flag.                        |
| 3     | ROT13 Cipher                      | A simple shift-based encryption (special rotation).       |
| 4     | HTML Comment Trap                 | Secrets hidden inside HTML comments.                      |
| 5     | Image Steganography (Metadata)    | Right-click → Download → Inspect EXIF metadata.           |
| 6     | CSS Hidden Flag                   | Dig into the stylesheets (CSS)!                           |
| 7     | HTTP Response Headers             | Use Network tab to find hidden server whispers.           |
| 8     | Base64 Data in URL                 | Decode data hidden inside URL parameters.                 |
| 9     | URL Encoding Trap                 | Decode URL percent-encoded flag.                          |
| 10    | JavaScript Console Puzzle         | Use Console commands to reveal deeply buried secrets.     |



🚀 How to Play

1. Clone the repository:
   ```bash
   git clone https://github.com/Yuvaraj-019/ctf-challenge.git
   cd ctf-challenge
   ```

2. Install required Python packages:
   ```bash
   pip install flask
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

4. Open your browser:
   ```
   http://localhost:5000
   ```
   or if hosted publicly:
   ```
   http://your-ip-address:5000
   ```

---

## 📂 Project Structure

```
├── app.py               # Main Flask application
├── templates/           # All Level HTML templates (index.html, level1.html, ..., level10.html)
├── static/
│   ├── style.css        # Common CSS file for styling
│   ├── secret.png       # Image for Steganography level
│   └── extra/           # Additional hidden files if needed
├── README.md            # (You're here!)
```

---

## 🛡️ Tech Stack

- **Python 3**
- **Flask**
- **HTML / CSS**
- **Web Developer Tools** (Inspect Element, Network tab, Console)

---

## 🎯 Goal

Find the hidden flags in each level and progress through all 10 stages!  
This CTF will test your ability to:
- Use browser tools effectively
- Decode/Decrypt hidden information
- Think like a hacker 🕵️‍♂️

---

## ⚠️ Rules

- **No source code cheating** (unless that's part of the challenge 😉).
- **Use logical solving** — not brute force.
- **Respect the challenge's intended difficulty.**

---

## 🏆 Completion Message

At the end of all 10 levels, you will be greeted with a **Congratulations! 🎉**  
Only the true cyber sleuths make it!

