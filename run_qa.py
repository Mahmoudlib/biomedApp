import os
import subprocess
import sys


def run_command(command, description):
    print("\n==================================================")
    print(f" Running: {description}")
    print(f" Command: {' '.join(command)}")
    print("==================================================")

    try:
        # Run command and pipe output to stdout/stderr
        subprocess.run(command, check=True, text=True)
        print(f"[PASS] {description}\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[FAIL] {description} (Exit Code: {e.returncode})\n")
        return False
    except FileNotFoundError:
        print(f"[ERROR] Could not find executable for command: {' '.join(command)}")
        print("  Make sure your virtual environment is active and dependencies are installed.\n")
        return False


def main():
    # Make sure we are running in the correct directory
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_root)

    print("Starting Local Quality Assurance & Test Runner...")

    # 1. Install/Verify QA packages
    pip_success = run_command(
        [sys.executable, "-m", "pip", "install", "ruff", "bandit"],
        "Installing QA Tools (ruff, bandit)",
    )
    if not pip_success:
        print("Failed to verify/install QA tools. Exiting.")
        sys.exit(1)

    # 2. Run Ruff Linter
    ruff_lint = run_command([sys.executable, "-m", "ruff", "check", "."], "Ruff Linter Check")

    # 3. Run Ruff Formatter check
    ruff_format = run_command([sys.executable, "-m", "ruff", "format", "--check", "."], "Ruff Formatter Check")

    # 4. Run Bandit Security scan
    bandit_scan = run_command(
        [sys.executable, "-m", "bandit", "-r", "core/", "biomedApp/", "-s", "B101"],
        "Bandit Security Scan",
    )

    # 5. Run Django system check
    django_check = run_command([sys.executable, "manage.py", "check"], "Django System Check")

    # 6. Run Django tests
    django_tests = run_command([sys.executable, "manage.py", "test"], "Django Test Suite")

    # Summary
    print("==================================================")
    print(" QA RUN SUMMARY")
    print("==================================================")
    results = {
        "Ruff Linter": ruff_lint,
        "Ruff Formatter": ruff_format,
        "Bandit Security": bandit_scan,
        "Django Check": django_check,
        "Django Tests": django_tests,
    }

    all_passed = True
    for name, success in results.items():
        status = "PASSED" if success else "FAILED"
        print(f"{name:<20}: {status}")
        if not success:
            all_passed = False

    print("==================================================")
    if all_passed:
        print("SUCCESS: ALL QA CHECKS & TESTS PASSED!")
        sys.exit(0)
    else:
        print("FAILURE: SOME CHECKS FAILED. Please fix the issues before pushing.")
        sys.exit(1)


if __name__ == "__main__":
    main()
