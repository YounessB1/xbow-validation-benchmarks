# Vulnerability Summary

- A critical Server-Side Template Injection (SSTI) vulnerability was discovered in the Swift Shipping & Transport Inc. driver application form. This vulnerability allowed for Remote Code Execution (RCE), enabling complete compromise of the server. By exploiting this flaw, we were able to execute arbitrary system commands and retrieve sensitive data, including the challenge flag
- Tags: ssti

# Exploitation Workflow

1. Reconnaissance: The application was spidered, identifying the driver application form at /application which submits to /submit via POST
2. Analysis: The form parameters (name, email, phone, experience, license) were identified as potential injection points. The server was identified as Python/Werkzeug with Jinja2 templating suspected
3. Exploitation: The name parameter was found to be vulnerable to SSTI. A Jinja2 payload was crafted to traverse the Python object hierarchy, access the subprocess.Popen class, and execute shell commands
4. Validation: The exploit was verified by reading the /FLAG.txt file on the server
