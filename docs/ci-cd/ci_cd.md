# AgroTech AI CI/CD Reference

> Canonical reference for the automated software delivery process. High‑level narrative lives in the main `README.md`; this file is the deep-dive.

---
## 1. Goals
| Objective | Why It Matters |
|-----------|----------------|
| Fast feedback | Fail fast on code quality + tests before building images |
| Reproducible deployments | Immutable image tags & infra templates |
| Environment parity | Staging & prod run the same container artifact |
| Progressive promotion | Staging must succeed before production deploy |
| Observability & traceability | Artifacts + explicit tagging + future metadata export |
| Extensibility | Clear hooks for acceptance tests, approvals, rollbacks |

---
## 2. Workflow Inventory
| File | Purpose | Trigger |
|------|---------|---------|
| `.github/workflows/ci_main.yml` | Continuous integration + auto deploy (staging → prod) | push to `main`, manual dispatch |
| `.github/workflows/production-release.yml` | Manual semantic release + `latest` tagging | manual dispatch with inputs |

---
## 3. `ci_main.yml` Job Breakdown
| Order | Job | Key Actions | Outputs / Artifacts | Fails If |
|-------|-----|-------------|---------------------|----------|
| 1 | test-python | Pytest, coverage, lint/format checks (inside composite) | `python-coverage-reports` | Tests / quality violations |
| 1 | test-javascript | Vitest, coverage, ESLint (composite) | `javascript-coverage-reports` | Tests / lint errors |
| 2 | check-code-statically | SonarCloud analysis ingesting both coverage reports | Quality gate report | Sonar issues / missing artifacts |
| 3 | build-agrotech-app-image | Build & push Docker image tagged with commit SHA | Image in Docker Hub | Build or push error |
| 4 | deploy-cfn-staging | CloudFormation deploy + ECS service update (staging) | Updated ECS tasks | CFN/ECS failure |
| 5 | deploy-cfn-prod | Same image promotion to production | Updated ECS tasks | Prior failure or CFN/ECS error |

Notes:
- Steps 1 jobs run in parallel; downstream waits on both.
- Production deploy strictly depends on staging success (minimal promotion gate).

### 3.1 ECS / CloudFormation Flow
1. Template parameters are resolved (VPC, Subnets, Roles, Image URI)
2. Task Definition registered referencing pushed image tag
3. ECS Service force-new-deployment triggers rolling replacement
4. ALB Target Group health checks `/health`
5. On success: staging considered green → production job starts

---
## 4. Image Tagging & Promotion
| Tag Type | Producer | Format | Use Case |
|----------|----------|--------|----------|
| Immutable build tag | CI pipeline | `<commit-sha>` | Deterministic staging & prod deployment |
| Version tag | Release workflow | `vX.Y.Z` | Human-readable milestone / external consumers |
| Floating convenience | Release workflow | `latest` | Local pulls / exploratory usage |

Future (recommended): also push image digest to an artifact for digest-pinned deployments.

---
## 5. Production Release (`production-release.yml`)
Flow:
1. Manual dispatch with `version`
2. Rebuild (guarantees reproducibility vs re-tagging an old layer set)
3. Push `<version>` and `latest`
4. (Optional future step) Create GitHub Release + attach changelog + SBOM

This workflow intentionally does **not** auto-deploy to AWS — versioning is decoupled from infra updates so you can promote deliberately.

---
## 6. Composite Actions Overview
| Path | Responsibility | Hidden Complexity |
|------|----------------|-------------------|
| `.github/actions/python-tests` | Standardized Python testing/coverage | Virtualenv setup, dependency caching |
| `.github/actions/javascript-tests` | JS tests + coverage + lint | Node version toolchain + test reporter |
| `.github/actions/static-analysis` | SonarCloud invocation | Coverage artifact download + scanner config |
| `.github/actions/docker-push` | Multi-tag image build & push | Login, caching, (future: multi-arch) |
| `.github/actions/aws-deploy` (referenced) | CloudFormation + ECS rollout | Parameter injection, wait logic |

---
## 7. Secrets & Parameters
| Name | Scope | Description |
|------|-------|-------------|
| `DOCKERHUB_USERNAME` | CI / Release | Docker Hub namespace |
| `DOCKERHUB_TOKEN` | CI / Release | Registry auth token |
| `SONAR_TOKEN` | CI | SonarCloud auth |
| `AWS_ACCESS_KEY_ID` | Deploy | AWS credential |
| `AWS_SECRET_ACCESS_KEY` | Deploy | AWS credential |
| `AWS_SESSION_TOKEN` | Deploy (if temp) | Session token |
| `LAB_ROLE_ARN` | Deploy | IAM role for tasks / permissions |
| `VPC_ID` | Deploy | Target VPC |
| `SUBNET_IDS` | Deploy | Private/public subnets (comma separated) |

Infra parameterization ensures infra remains code-defined and reproducible.

---
## 8. Artifacts & Evidence
| Artifact | Producer | Consumption |
|----------|----------|-------------|
| `python-coverage-reports` | test-python | SonarCloud + audit |
| `javascript-coverage-reports` | test-javascript | SonarCloud + audit |
| (future) `deployment-metadata.json` | deploy jobs | Traceability dashboard |
| (future) SBOM (CycloneDX) | build job | Supply chain scanning |

Retention: default GitHub artifact retention (configurable per repo).

---
## 9. Observability & Traceability (Planned)
- Emit deployment summary (commit, image tag, time, stack outputs) to log or artifact
- Persist ECS task definition revision IDs for rollback mapping
- Optional Slack / Teams webhook integration for human visibility

---
## 10. Failure Modes & Triage
| Stage | Typical Failure | First Check | Fast Fix |
|-------|------------------|------------|---------|
| Tests | Import/module errors | Job logs | Missing dep / path fix |
| Static analysis | Sonar coverage missing | Artifact presence | Ensure artifact names align |
| Build | Docker push denied | Auth / token scopes | Refresh token / namespace |
| Staging deploy | CFN stack rollback | CloudFormation events | Fix parameter / IAM issue |
| Prod deploy | Health check fail | ECS service events + target group | Revert to previous task def |
| Release | Version conflict | Existing git tag | Bump semantic version |

---
## 11. Roadmap Enhancements
| Area | Enhancement | Rationale | Effort |
|------|------------|-----------|--------|
| Testing | Add acceptance test job post-staging | Prevent bad prod promotion | Medium |
| Governance | Manual approval before prod | Controlled releases | Low |
| Security | Sign images w/ cosign & verify | Supply chain trust | Medium |
| Deployment | Digest-based ECS task defs | Strong immutability | Low |
| Reliability | Auto rollback on failed health | Faster recovery | Medium |
| Insight | Publish deployment metadata | Audit & debugging | Low |
| Performance | Single multi-tag docker build | Reduce build time | Low |
| Security | SBOM + vulnerability scan | Compliance & risk mgmt | Medium |

---
## 12. Glossary
| Term | Meaning |
|------|--------|
| Immutable Tag | Image reference bound to a specific build (commit SHA) |
| Promotion | Moving the *same* artifact across environments |
| Health Check | ALB → container `/health` request determining readiness |
| Coverage Artifact | Generated report used for quality gates and auditing |
| Composite Action | Reusable step bundle encapsulating logic |

---
## 13. Minimal Mental Model
```
Commit → Parallel Tests → Sonar Gate → Build Image(SHA) → Deploy Staging → Deploy Prod → (Optional) Manual Version Release → Tag vX.Y.Z + latest
```

---
## 14. Quick Commands (Local Reproduction)
```bash
# Rebuild production image locally
docker build -f env-deployment/Dockerfile -t agrotech-ai-app:dev .

# Emulate release tag
docker tag agrotech-ai-app:dev agrotech-ai-app:v1.0.0

# Pull CI-produced image by commit
docker pull $DOCKERHUB_USERNAME/agrotech-ai-app:<commit-sha>
```

---
## 15. FAQ
**Q: Why rebuild on manual release instead of re-tagging?**  
A: Ensures the Dockerfile context still produces identical artifact under current toolchain (protects from hidden base updates unnoticed since CI build).

**Q: Why not deploy automatically after version tagging?**  
A: Separation of versioning and deployment enables staged / approval-driven promotion.

**Q: Why one unified container instead of multiple services in prod?**  
A: Simplicity for early-stage PoC; can evolve to split concerns (model serving, API, static UI) later.

---
## 16. Next Steps Checklist (Adopt Gradually)
- [ ] Add acceptance tests job after staging
- [ ] Require manual approval before `deploy-cfn-prod`
- [ ] Switch ECS task definitions to image digests (`image: repo@sha256:...`)
- [ ] Add image signing (cosign) & verification
- [ ] Publish `deployment-metadata.json` artifact
- [ ] Introduce rollback helper script
- [ ] Generate SBOM & run vulnerability scan (e.g., Trivy + Grype)
- [ ] Consolidate Docker build into multi-tag single step

---
*This document evolves with the pipeline—treat it as living architecture.*
