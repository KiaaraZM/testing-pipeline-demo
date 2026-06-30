# 🧪 CI/CD Testing Management Tools — Practical Comparison

> **Companion repository** for the article:
> *"5 CI/CD Tools Walk Into a Pipeline: Only One Won't Make You Cry"*
> Published on [Dev.to](https://dev.to/kiarazmurillo)

[![GitHub Actions](https://github.com/KiaaraZM/testing-pipeline-demo/actions/workflows/tests.yml/badge.svg)](https://github.com/KiaaraZM/testing-pipeline-demo/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/python-3.11-blue)
![pytest](https://img.shields.io/badge/tested%20with-pytest-orange)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📌 What is this?

This repository compares **5 real CI/CD testing management tools** using the exact same Python project and test suite. Each tool runs the same `pytest` tests through a different pipeline configuration.

| Tool | Config file | Status |
|------|-------------|--------|
| ✅ GitHub Actions | `.github/workflows/tests.yml` | Active |
| ✅ GitLab CI/CD | `.gitlab-ci.yml` | Ready |
| ✅ Jenkins | `Jenkinsfile` | Ready |
| ✅ CircleCI | `.circleci/config.yml` | Ready |
| ✅ Bitbucket Pipelines | `bitbucket-pipelines.yml` | Ready |

---

## 📁 Project Structure

```
testing-pipeline-demo/
├── app/
│   ├── __init__.py
│   └── calculator.py          ← simple Python app
├── tests/
│   ├── __init__.py
│   └── test_calculator.py     ← 7 pytest test cases
├── docs/
│   └── comparison.md          ← detailed tool comparison
├── .github/
│   └── workflows/
│       └── tests.yml          ← GitHub Actions pipeline
├── .gitlab-ci.yml             ← GitLab CI/CD pipeline
├── .circleci/
│   └── config.yml             ← CircleCI pipeline
├── Jenkinsfile                ← Jenkins pipeline
├── bitbucket-pipelines.yml    ← Bitbucket Pipelines
├── requirements.txt
└── README.md
```

---

## 🚀 Run locally

```bash
# Clone the repo
git clone https://github.com/KiaaraZM/testing-pipeline-demo.git
cd testing-pipeline-demo

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ --tb=short -v
```

Expected output:

```
collected 7 items

tests/test_calculator.py::test_add              PASSED
tests/test_calculator.py::test_subtract         PASSED
tests/test_calculator.py::test_multiply         PASSED
tests/test_calculator.py::test_divide           PASSED
tests/test_calculator.py::test_divide_by_zero   PASSED
tests/test_calculator.py::test_add_negative     PASSED
tests/test_calculator.py::test_multiply_by_zero PASSED

7 passed in 0.12s
```

---

## 🔍 Tool Comparison at a Glance

```
SETUP DIFFICULTY
─────────────────────────────────────────
GitHub Actions    ████░░░░░░  Easy
GitLab CI/CD      ████░░░░░░  Easy
CircleCI          █████░░░░░  Medium
Bitbucket         ████░░░░░░  Easy
Jenkins           ██████████  Complex

FLEXIBILITY / CUSTOMIZATION
─────────────────────────────────────────
GitHub Actions    ████████░░  High
GitLab CI/CD      ███████░░░  High
CircleCI          ██████░░░░  Medium
Bitbucket         █████░░░░░  Medium
Jenkins           ██████████  Maximum

FREE TIER (build minutes/month)
─────────────────────────────────────────
GitHub Actions    ██████████  2,000 min
GitLab CI/CD      ████████░░  400 min
CircleCI          ████████░░  6,000 min
Bitbucket         ████░░░░░░  50 min
Jenkins           ██████████  Free (self-hosted)
```

---

## 📊 Detailed Comparison

| Feature | GitHub Actions | GitLab CI/CD | Jenkins | CircleCI | Bitbucket |
|---------|---------------|-------------|---------|----------|-----------|
| Config format | YAML | YAML | Groovy DSL | YAML | YAML |
| Hosting | Cloud | Cloud/Self | Self-hosted | Cloud | Cloud |
| Infrastructure needed | ❌ No | ❌ No | ✅ Yes | ❌ No | ❌ No |
| Free tier | ✅ Generous | ✅ Good | ✅ (self-host) | ✅ Limited | ⚠️ 50 min |
| Docker support | ✅ | ✅ | ✅ (plugin) | ✅ | ✅ |
| Plugin ecosystem | 22,000+ actions | Built-in | 1,800+ plugins | Moderate | Limited |
| GitHub integration | ⭐ Native | Good | Plugin | Good | Plugin |
| GitLab integration | Plugin | ⭐ Native | Plugin | Good | Plugin |
| Jira integration | Plugin | Good | Plugin | Plugin | ⭐ Native |
| Market share (2026) | ~33% | ~19% | ~28% | Declining | Niche |
| Learning curve | Low | Low | High | Medium | Low |

---

## 🧠 When to use each tool

```
You are on GitHub?
  └── ✅ Use GitHub Actions — zero friction, native integration

You are on GitLab?
  └── ✅ Use GitLab CI/CD — built-in, supports self-hosted runners

You need maximum control / enterprise / on-prem?
  └── ✅ Use Jenkins — steep learning curve, but unlimited flexibility

You need fast parallel pipelines in the cloud?
  └── ✅ Use CircleCI — excellent caching and test splitting

You use Jira + Bitbucket?
  └── ✅ Use Bitbucket Pipelines — best Atlassian ecosystem integration
```

---

## 📄 Pipeline configs explained

### GitHub Actions (`.github/workflows/tests.yml`)
Triggers on every push and pull request to `main`. Uses official Python setup action.

### GitLab CI/CD (`.gitlab-ci.yml`)
Runs on merge requests and pushes using a Python Docker image with defined stages.

### Jenkins (`Jenkinsfile`)
Uses declarative pipeline syntax with `post` stages for success/failure reporting. Requires a running Jenkins server.

### CircleCI (`.circleci/config.yml`)
Caches pip dependencies by `requirements.txt` checksum. Restores cache on subsequent runs for faster execution.

### Bitbucket Pipelines (`bitbucket-pipelines.yml`)
Separate pipeline steps for default branch and feature branches. Uses built-in pip caching.

---

## 📚 References

- [JetBrains State of Developer Ecosystem 2026](https://blog.jetbrains.com/teamcity/2026/03/best-ci-tools/)
- [CircleCI vs GitHub Actions at scale](https://circleci.com/blog/ci-cd-at-scale-circleci-vs-github-actions/)
- [CI tools like Jenkins — how they compare in 2026](https://northflank.com/blog/ci-tools-like-jenkins)
- [GitHub Actions official docs](https://docs.github.com/en/actions)
- [GitLab CI/CD docs](https://docs.gitlab.com/ee/ci/)

---

## 👤 Author

**Kiara Holly Zapana Murillo**
[Dev.to](https://dev.to/kiarazmurillo) · [GitHub](https://github.com/KiaaraZM)

---

*This repository is for educational purposes as part of a university software testing course.*
