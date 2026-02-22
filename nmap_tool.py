import os
import subprocess
import math

C1 = "\033[34m"
C2 = "\033[94m"
C3 = "\033[38;5;39m"
R  = "\033[0m"

def colorize(text):
    out = ""
    colors = [C1, C2, C3]
    i = 0
    for ch in text:
        if ch == " ":
            out += ch
        else:
            out += colors[i % 3] + ch + R
            i += 1
    return out

def center(text):
    width = os.get_terminal_size().columns
    return text.center(width)

TITLE_LINES = [
    C1 + "██████   █████                                    " + R,
    C2 + "░░██████ ░░███                                     " + R,
    C3 + " ░███░███ ░███  █████████████    ██████   ████████ " + R,
    C1 + " ░███░░███░███ ░░███░░███░░███  ░░░░░███ ░░███░░███" + R,
    C2 + " ░███ ░░██████  ░███ ░███ ░███   ███████  ░███ ░███" + R,
    C3 + " ░███  ░░█████  ░███ ░███ ░███  ███░░███  ░███ ░███" + R,
    C1 + " █████  ░░█████ █████░███ █████░░████████ ░███████ " + R,
    C2 + "░░░░░    ░░░░░ ░░░░░ ░░░ ░░░░░  ░░░░░░░░  ░███░░░   " + R,
    C3 + "                                          ░███      " + R,
    C1 + "                                          █████     " + R,
    C2 + "                                         ░░░░░      " + R
]


COMMANDS = [
    ("nmap -sV", "Version detection"),
    ("nmap -A", "Aggressive scan"),
    ("nmap -sC", "Default scripts"),
    ("nmap -sS", "SYN stealth"),
    ("nmap -O", "OS detection"),
    ("nmap -p 1-65535", "All ports"),
    ("nmap --top-ports 100", "Top ports"),
    ("nmap --script vuln", "Vuln scan"),
    ("nmap -sn", "Ping scan"),
    ("nmap -sU", "UDP scan"),
    ("nmap -sT", "TCP connect"),
    ("nmap -6", "IPv6 scan"),
    ("nmap -T4", "Faster timing"),
    ("nmap -Pn", "No ping"),
    ("nmap -v", "Verbose"),
    ("-p", "Port selection"),
    ("-p-", "All ports"),
    ("-p0-", "From port 0"),
    ("-F", "Fast scan"),
    ("--top-ports 100", "Top ports"),
    ("-sL", "List scan"),
    ("-PS", "TCP SYN ping"),
    ("-PA", "TCP ACK ping"),
    ("-PU", "UDP ping"),
    ("-PR", "ARP ping"),
    ("-n", "No DNS"),
    ("-sV --version-intensity", "Intensity"),
    ("-sV --version-light", "Light scan"),
    ("-sV --version-all", "Full version scan"),
    ("-O --osscan-limit", "Limit OS scan"),
    ("-O --osscan-guess", "Guess OS"),
    ("-O --max-os-tries", "Max tries"),
    ("-iL", "Input list"),
    ("-iR", "Random targets"),
    ("--exclude", "Exclude hosts"),
    ("-T0", "Paranoid"),
    ("-T1", "Sneaky"),
    ("-T2", "Polite"),
    ("-T3", "Normal"),
    ("-T4", "Aggressive"),
    ("-T5", "Insane"),
    ("-f", "Fragment packets"),
    ("--mtu", "Set MTU"),
    ("-D", "Decoy"),
    ("-S", "Spoof IP"),
    ("-g", "Source port"),
    ("--proxies", "Use proxies"),
    ("--data-length", "Random data"),
    ("-oN", "Normal output"),
    ("-oX", "XML output"),
    ("-oG", "Grepable"),
    ("-oA", "All formats"),
    ("--append-output", "Append"),
    ("-d", "Debug"),
    ("--reason", "Show reasons"),
    ("--open", "Show open ports"),
    ("--packet-trace", "Trace packets"),
    ("--iflist", "Interface list"),
    ("--resume", "Resume scan")
]

def print_title():
    for line in TITLE_LINES:
        print(line)

def print_centered_extra():
    print(center(colorize("[ipconfig] shows your ip")))

def print_commands():
    rows = math.ceil(len(COMMANDS) / 3)
    for i in range(rows):
        group = COMMANDS[i*3:(i+1)*3]
        raw_line = ""
        for cmd, desc in group:
            raw_line += f"[{cmd}] {desc}".ljust(45)
        print(colorize(raw_line))

def run(cmd):
    os.system("cls")
    print(C3 + f"Running: {cmd}\n" + R)
    subprocess.run(cmd, shell=True)
    input("\nPress ENTER to return...")
    main()

def main():
    os.system("cls")  # ← FIX: cancella tutto PRIMA
    print_title()
    print_centered_extra()
    print_commands()

    prompt = "\033[35m(nmap@nmap)\033[0m ~\n\033[35m#\033[0m "
    user_cmd = input(prompt).strip()

    if user_cmd:
        run(user_cmd)
    else:
        main()

if __name__ == "__main__":
    main()
