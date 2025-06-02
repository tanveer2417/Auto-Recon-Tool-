# main.py
import os
import sys
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description="Auto Recon Tool - CLI Interface")
    parser.add_argument("module", nargs='?', help="Module to run", choices=[
        "subdomain", "livedomain", "portscan", "dnsenum", "sslanalysis",
        "techdetect", "wafdetect", "screenshot", "osint", "fuzzing",
        "params", "vulnscan", "versions", "webcrawl"
    ])
    parser.add_argument("--target", help="Target domain or IP")

    args = parser.parse_args()

    if not args.module:
        print("""
=== Auto Recon Tool ===

Usage:
    python main.py <module> --target <target>

Modules:
    subdomain       Subdomain Enumeration
    livedomain      Live Domain Checker
    portscan        Port Scanner
    dnsenum         DNS Enumeration
    sslanalysis     SSL/TLS Analysis
    techdetect      Technology Detection
    wafdetect       WAF Detection
    screenshot      Screenshot Capture
    osint           OSINT Reconnaissance
    fuzzing         Path Fuzzer
    params          Parameter Finder
    vulnscan        Vulnerability Scanner
    versions        Detect Outdated Technologies
    webcrawl        Web Crawler

Example:
    python main.py techdetect --target http://example.com
""")
        sys.exit()

    if args.module == "techdetect":
        from modules.tech_detection import detect_technologies
        print(detect_technologies(args.target))

    elif args.module == "wafdetect":
        from modules.waf_detection import detect_waf
        print(detect_waf(args.target))

    elif args.module == "screenshot":
        from modules.visual_scan import capture_screenshot
        capture_screenshot(args.target)

    elif args.module == "osint":
        from modules.osint import gather_osint
        print(gather_osint(args.target))

    elif args.module == "fuzzing":
        from modules.fuzzing import fuzz_target
        print(fuzz_target(args.target))

    elif args.module == "params":
        from modules.find_params import find_parameters
        print(find_parameters(args.target))

    elif args.module == "vulnscan":
        from modules.vuln_scanner import scan_vulnerabilities
        print(scan_vulnerabilities(args.target))

    elif args.module == "versions":
        from modules.old_versions import detect_old_versions
        print(detect_old_versions(args.target))

    elif args.module == "webcrawl":
        from modules.web_crawl import crawl_website
        print(crawl_website(args.target))

    else:
        print("[!] Unknown module or not implemented yet")

if __name__ == "__main__":
    main()

