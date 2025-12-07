#!/usr/bin/env python3
"""Comprehensive pre-flight check before running the agent"""

import sys
import os
import socket
import time

# Add project root to path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)
sys.path.insert(0, os.path.join(project_root, 'agent'))

errors = []
warnings = []

def check(condition, error_msg, warning_msg=None):
    """Check a condition and record errors/warnings"""
    if not condition:
        if error_msg:
            print(f"❌ ERROR: {error_msg}")
            errors.append(error_msg)
        elif warning_msg:
            print(f"⚠️  WARNING: {warning_msg}")
            warnings.append(warning_msg)
        return False
    return True

def check_port_connection(port, timeout=2):
    """Check if a port is listening"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex(('127.0.0.1', port))
        sock.close()
        return result == 0
    except:
        return False

def check_file_with_expand(path_var, description):
    """Check if a file exists, expanding user path"""
    path = os.getenv(path_var)
    if not path:
        errors.append(f"{description}: {path_var} not set")
        print(f"❌ ERROR: {description}: {path_var} not set in env/.env")
        return False
    expanded = os.path.expanduser(path)
    if os.path.exists(expanded):
        print(f"✓ {description}: {expanded}")
        return True
    else:
        errors.append(f"{description}: File not found at {expanded}")
        print(f"❌ ERROR: {description}: File not found at {expanded}")
        return False

print("=" * 70)
print("StarDojo Pre-Flight Check")
print("=" * 70)
print()

# Load environment
from dotenv import load_dotenv
env_file = os.path.join(project_root, "env", ".env")
if os.path.exists(env_file):
    load_dotenv(env_file)
    print(f"✓ Loaded .env file: {env_file}")
else:
    print(f"⚠️  .env file not found at: {env_file}")
    warnings.append(".env file not found")

print()
print("1. Environment Variables")
print("-" * 70)
check_file_with_expand("STARDEW_APP_PATH", "StardewModdingAPI executable")
oa_key = os.getenv("OA_OPENAI_KEY")
if oa_key:
    print(f"✓ OA_OPENAI_KEY is set (length: {len(oa_key)})")
else:
    warnings.append("OA_OPENAI_KEY not set - LLM calls will fail")
    print("⚠️  OA_OPENAI_KEY not set - LLM calls will fail")
print()

print("2. Game Server Connection")
print("-" * 70)
port = 10783
if check_port_connection(port):
    print(f"✓ Game server is listening on port {port}")
else:
    errors.append(f"Game server not listening on port {port}")
    print(f"❌ ERROR: Game server not listening on port {port}")
    print(f"   → Make sure Stardew Valley is running with the mod loaded")
    print(f"   → Check the SMAPI console for mod errors")
print()

print("3. Memory Mapped File")
print("-" * 70)
stardew_path = os.getenv("STARDEW_APP_PATH")
if stardew_path:
    stardew_path = os.path.expanduser(stardew_path)
    parent_dir = os.path.dirname(stardew_path)
    mmap_file = os.path.join(parent_dir, f"shared_memory_{port}.bin")
    if os.path.exists(mmap_file):
        print(f"✓ Memory mapped file exists: {mmap_file}")
    else:
        warnings.append(f"Memory mapped file not found: {mmap_file}")
        print(f"⚠️  Memory mapped file not found: {mmap_file}")
        print(f"   → This will be created when the mod starts")
else:
    warnings.append("Cannot check mmap file - STARDEW_APP_PATH not set")
print()

print("4. Configuration Files")
print("-" * 70)
configs = [
    ("agent/conf/env_config_stardew.json", "Environment config"),
    ("agent/conf/openai_config.json", "OpenAI config"),
]
for path, desc in configs:
    full_path = os.path.join(project_root, path)
    check(os.path.exists(full_path), f"{desc} not found: {path}")
print()

print("5. Task Files")
print("-" * 70)
task_file = "env/tasks/task_suite/farming_lite.yaml"
full_path = os.path.join(project_root, task_file)
if os.path.exists(full_path):
    print(f"✓ Task file exists: {task_file}")
    try:
        import yaml
        with open(full_path, 'r') as f:
            task_data = yaml.safe_load(f)
        task_count = len(task_data) if task_data else 0
        print(f"✓ Task file is valid (contains {task_count} tasks)")
        if task_count > 0:
            print(f"  → Task ID 0: {list(task_data.keys())[0]}")
    except Exception as e:
        errors.append(f"Task file invalid: {e}")
        print(f"❌ ERROR: Task file invalid: {e}")
else:
    errors.append(f"Task file not found: {task_file}")
    print(f"❌ ERROR: Task file not found: {task_file}")
print()

print("6. Resource Files")
print("-" * 70)
resources = [
    "agent/res/stardew/prompts/templates/action_planning_cultivation.prompt",
    "agent/res/stardew/prompts/templates/information_gathering_cultivation.prompt",
    "agent/res/stardew/prompts/templates/success_detection.prompt",
    "agent/res/stardew/prompts/inputs/action_planning.json",
]
for resource in resources:
    full_path = os.path.join(project_root, resource)
    check(os.path.exists(full_path), f"Resource file not found: {resource}")
print()

print("7. Game Data Files")
print("-" * 70)
game_data_files = [
    "env/game_data/Objects.json",
    "env/game_data/CraftingRecipes.json",
]
for gdf in game_data_files:
    full_path = os.path.join(project_root, gdf)
    check(os.path.exists(full_path), f"Game data file not found: {gdf}")
print()

print("8. Critical Imports")
print("-" * 70)
imports_to_check = [
    ("cv2", "OpenCV"),
    ("numpy", "NumPy"),
    ("mtm", "MTM package"),
    ("stardojo.config", "StarDojo config"),
    ("agent.stardojo_react_agent", "React agent"),
    ("env.stardew_env", "Stardew environment"),
    ("env.tasks.base", "Task base"),
]
for module, desc in imports_to_check:
    try:
        __import__(module)
        print(f"✓ {desc}")
    except Exception as e:
        errors.append(f"{desc} import failed: {e}")
        print(f"❌ ERROR: {desc} import failed: {e}")
print()

print("9. Module Paths")
print("-" * 70)
try:
    from stardojo.environment.stardew.atomic_skills import basic_skills
    print("✓ Basic skills module can be imported")
except Exception as e:
    errors.append(f"Basic skills module: {e}")
    print(f"❌ ERROR: Basic skills module: {e}")
print()

print("=" * 70)
print("Summary")
print("=" * 70)
if errors:
    print(f"\n❌ Found {len(errors)} CRITICAL ERROR(S):")
    for i, error in enumerate(errors, 1):
        print(f"  {i}. {error}")
    print("\n⚠️  Please fix these errors before running the agent.")
    print("\nMost common issues:")
    print("  1. Game not running → Start Stardew Valley with the mod")
    print("  2. Wrong port → Make sure mod is on port 10783 (or use --port)")
    print("  3. Missing API key → Set OA_OPENAI_KEY in env/.env")
    sys.exit(1)
elif warnings:
    print(f"\n⚠️  Found {len(warnings)} warning(s):")
    for i, warning in enumerate(warnings, 1):
        print(f"  {i}. {warning}")
    print("\n✓ No critical errors. You can proceed, but check warnings above.")
    sys.exit(0)
else:
    print("\n✅ All checks passed! Ready to run the agent.")
    print("\nNext steps:")
    print("  1. Ensure Stardew Valley is running with a game loaded")
    print("  2. Run: python env/llm_env.py --port 10783 --task_name farming_lite --task_id 0")
    sys.exit(0)
