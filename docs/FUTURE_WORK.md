# Security & Compliance

## Current Security Measures

### 1. Storage Security
- Azure Blob Storage with public access disabled
- Files accessible only via authenticated services

---

### 2. Secrets Management
- All secrets stored in environment variables
- `.env` file excluded from version control
- No secrets hardcoded in codebase

---

### 3. Data Privacy
- Documents are processed locally after secure upload
- No document content is exposed publicly
- No external APIs receive raw documents

---

## Planned Security Enhancements

### Role-Based Access Control (RBAC)
- Azure RBAC for user and service permissions
- Fine-grained access control per role

---

### Managed Identity
- Replace connection strings with Managed Identity
- Eliminate long-lived credentials

---

### Network Security
- Private Endpoints for Blob Storage and Azure OpenAI
- VNet integration for backend services

---

### Encryption
- Encryption at rest (Azure-managed keys)
- Encryption in transit (HTTPS/TLS)

---

## Compliance Considerations

- Architecture suitable for enterprise and regulated environments
- Designed to support auditability and access logging
