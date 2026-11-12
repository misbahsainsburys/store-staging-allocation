import json
import re
from copy import deepcopy
from pathlib import Path

from inputs import (
    GATEWAY,
    HOSTNAME,
    IP_ADDRESS,
    LAN_MAC,
    SERIAL,
    STACK_SIZE,
    STACK_MEMBERS,
    STACK_PRIORITIES,
    REFERENCE_VARIABLES,
)

OUTPUT_FILE = Path(__file__).with_name("variable_file.json")


def normalize_mac(mac: str) -> str:
    """Return a validated 12-hex-character MAC address."""
    clean = re.sub(r"[^0-9A-Fa-f]", "", mac or "")
    if len(clean) != 12:
        raise ValueError(f"Invalid MAC address: {mac!r}")
    return clean.lower()


def format_vsf_mac(mac: str) -> str:
    """Convert 88:3a:30:45:cb:80 -> 883a30-45cb80 for VSF."""
    clean = normalize_mac(mac)
    return f"{clean[:6]}-{clean[6:]}"


def validate_inputs() -> None:
    if STACK_SIZE not in (1, 2, 3, 4):
        raise ValueError("STACK_SIZE must be 1, 2, 3, or 4")

    required = {
        "GATEWAY": GATEWAY,
        "HOSTNAME": HOSTNAME,
        "LAN_MAC": LAN_MAC,
        "SERIAL": SERIAL,
    }
    missing = [name for name, value in required.items() if not str(value).strip()]
    if missing:
        raise ValueError(f"Missing required input(s): {', '.join(missing)}")

    normalize_mac(LAN_MAC)

    if STACK_SIZE == 1:
        if STACK_MEMBERS:
            raise ValueError("STACK_MEMBERS must be empty when STACK_SIZE = 1")
        return

    if len(STACK_MEMBERS) != STACK_SIZE:
        raise ValueError(
            f"STACK_SIZE is {STACK_SIZE}, but {len(STACK_MEMBERS)} STACK_MEMBERS were provided"
        )

    if len(STACK_PRIORITIES) < STACK_SIZE:
        raise ValueError("Not enough values in STACK_PRIORITIES")

    for index, member in enumerate(STACK_MEMBERS, start=1):
        if not member.get("part_number"):
            raise ValueError(f"Member {index}: part_number is required")
        if not member.get("mac"):
            raise ValueError(f"Member {index}: mac is required")
        normalize_mac(member["mac"])


def generate_stack_command() -> str:
    """Create _sys_stack_command from STACK_SIZE and STACK_MEMBERS."""
    if STACK_SIZE == 1:
        return ""

    lines = ["vsf", "   enable domain 1"]

    for member_number, member in enumerate(STACK_MEMBERS, start=1):
        part_number = member["part_number"].strip()
        mac = format_vsf_mac(member["mac"])
        priority = STACK_PRIORITIES[member_number - 1]

        lines.extend(
            [
                f"   member {member_number}",
                f'      type "{part_number}" mac-address {mac}',
                f"      priority {priority}",
                f"      link 1 {member_number}/49-{member_number}/50",
                f'      link 1 name "I-Link{member_number}_1"',
                f'      link 2 name "I-Link{member_number}_2"',
                "      exit",
            ]
        )

    lines.extend(["   port-speed 10g", "   exit"])
    return "\n".join(lines) + "\n"


def create_variable_file() -> dict:
    """Copy reference variables and replace only approved dynamic fields."""
    validate_inputs()

    variables = deepcopy(REFERENCE_VARIABLES)

    variables["_sys_gateway"] = GATEWAY
    variables["_sys_hostname"] = HOSTNAME
    variables["_sys_ip_address"] = IP_ADDRESS
    variables["_sys_lan_mac"] = LAN_MAC
    variables["_sys_serial"] = SERIAL
    variables["_sys_stack_command"] = generate_stack_command()

    return {SERIAL: variables}


def main() -> None:
    result = create_variable_file()

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
        file.write("\n")

    print(f"Variable file created successfully: {OUTPUT_FILE}")
    print(f"Hostname   : {HOSTNAME}")
    print(f"Serial     : {SERIAL}")
    print(f"Stack size : {STACK_SIZE}")


if __name__ == "__main__":
    main()
