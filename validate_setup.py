#!/usr/bin/env python3
"""Comprehensive validation script to check all imports and paths before running the agent"""

import sys
import os

# Add project root to path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)
sys.path.insert(0, os.path.join(project_root, 'agent'))

errors = []
warnings = []

def check_import(module_name, description):
    """Check if a module can be imported"""
    try:
        __import__(module_name)
        print(f"✓ {description}")
        return True
    except Exception as e:
        error_msg = f"✗ {description}: {str(e)}"
        print(error_msg)
        errors.append(error_msg)
        return False

def check_file_exists(filepath, description):
    """Check if a file exists"""
    full_path = os.path.join(project_root, filepath)
    if os.path.exists(full_path):
        print(f"✓ {description}: {filepath}")
        return True
    else:
        error_msg = f"✗ {description}: {filepath} not found"
        print(error_msg)
        errors.append(error_msg)
        return False

print("=" * 60)
print("StarDojo Setup Validation")
print("=" * 60)
print()

print("1. Checking critical imports...")
print("-" * 60)
check_import("cv2", "OpenCV")
check_import("numpy", "NumPy")
check_import("PIL", "Pillow")
check_import("mtm", "MTM package")
check_import("stardojo.config", "StarDojo config")
check_import("stardojo.utils.file_utils", "File utilities")
check_import("stardojo.planner.stardew_planner", "Stardew planner")
check_import("agent.stardojo_react_agent", "React agent")
check_import("agent.log_processor", "Log processor")
check_import("env.stardew_env", "Stardew environment")
check_import("env.tasks.base", "Task base")
check_import("env.tasks.utils.load_task", "Task loader")
print()

print("2. Checking config files...")
print("-" * 60)
check_file_exists("agent/conf/env_config_stardew.json", "Environment config")
check_file_exists("agent/conf/openai_config.json", "OpenAI config")
print()

print("3. Checking resource files...")
print("-" * 60)
check_file_exists("agent/res/stardew/prompts/templates/action_planning_cultivation.prompt", "Action planning template")
check_file_exists("agent/res/stardew/prompts/templates/information_gathering_cultivation.prompt", "Info gathering template")
check_file_exists("agent/res/stardew/prompts/templates/success_detection.prompt", "Success detection template")
check_file_exists("agent/res/stardew/prompts/inputs/action_planning.json", "Action planning input")
print()

print("4. Checking task files...")
print("-" * 60)
check_file_exists("env/tasks/task_suite/farming_lite.yaml", "Farming lite task")
print()

print("5. Checking environment setup...")
print("-" * 60)
env_file = os.path.join(project_root, "env", ".env")
if os.path.exists(env_file):
    print(f"✓ .env file exists: env/.env")
    # Check if STARDEW_APP_PATH is set
    try:
        from dotenv import load_dotenv
        load_dotenv(env_file)
        stardew_path = os.getenv("STARDEW_APP_PATH")
        if stardew_path:
            if os.path.exists(stardew_path):
                print(f"✓ STARDEW_APP_PATH is set and file exists: {stardew_path}")
            else:
                warnings.append(f"⚠ STARDEW_APP_PATH is set but file doesn't exist: {stardew_path}")
                print(f"⚠ STARDEW_APP_PATH is set but file doesn't exist: {stardew_path}")
        else:
            warnings.append("⚠ STARDEW_APP_PATH not set in .env file")
            print("⚠ STARDEW_APP_PATH not set in .env file")
    except Exception as e:
        warnings.append(f"⚠ Could not check .env: {e}")
        print(f"⚠ Could not check .env: {e}")
else:
    warnings.append("⚠ .env file not found at env/.env")
    print("⚠ .env file not found at env/.env")
print()

print("6. Checking module paths...")
print("-" * 60)
try:
    from stardojo.environment.stardew.atomic_skills import basic_skills
    print("✓ Basic skills module can be imported")
except Exception as e:
    errors.append(f"✗ Basic skills module: {str(e)}")
    print(f"✗ Basic skills module: {str(e)}")
print()

print("7. Testing path resolution...")
print("-" * 60)
try:
    from stardojo.utils.file_utils import assemble_project_path, read_resource_file
    test_path = assemble_project_path("agent/res/stardew/prompts/templates/action_planning_cultivation.prompt")
    if os.path.exists(test_path):
        print(f"✓ Path resolution works: {test_path}")
    else:
        errors.append(f"✗ Path resolution failed: {test_path} doesn't exist")
        print(f"✗ Path resolution failed: {test_path} doesn't exist")
except Exception as e:
    errors.append(f"✗ Path resolution test failed: {str(e)}")
    print(f"✗ Path resolution test failed: {str(e)}")
print()

print("=" * 60)
print("Summary")
print("=" * 60)
if errors:
    print(f"\n❌ Found {len(errors)} error(s):")
    for error in errors:
        print(f"  {error}")
    print("\n⚠️  Please fix these errors before running the agent.")
    sys.exit(1)
elif warnings:
    print(f"\n⚠️  Found {len(warnings)} warning(s):")
    for warning in warnings:
        print(f"  {warning}")
    print("\n✓ No critical errors found. You may proceed, but check warnings above.")
    sys.exit(0)
else:
    print("\n✅ All checks passed! You're ready to run the agent.")
    sys.exit(0)
