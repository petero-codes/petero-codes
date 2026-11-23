# Peter Njuguna

**Python Backend Developer | Full-Stack Engineer | AI Evaluation Specialist**  
Nairobi, Kenya • [Portfolio](https://iam-petero.vercel.app/) • [LinkedIn](https://www.linkedin.com/in/peter-njuguna-13b00a411) • [GitHub](https://github.com/petero-codes) • [Email](mailto:waynelulu6@gmail.com)

---

## About Me

I am a software engineer focused on **Python backend engineering**, **REST API architecture**, and **full-stack web development**, with dedicated experience in **AI model output evaluation**.

My engineering work emphasizes architectural integrity: separating business domain logic from external frameworks, enforcing strict server-side schema validation, and writing code that is verifiable through automated tests. Whether architecting hierarchical approval workflows with Clean Architecture and SQL Server for KenGen ICT, constructing persistent client state with Redux Toolkit for e-commerce storefronts, or building evaluation APIs with FastAPI, I focus on building reliable systems that handle real-world constraints cleanly.

- **Primary Specialization**: Python backend development, REST API design, relational data modeling, and server-side authorization.
- **Full-Stack Competence**: Modern TypeScript/JavaScript, React 18, Next.js (App Router), and Tailwind CSS.
- **AI Evaluation**: Rubric-based LLM response evaluation, factuality verification, hallucination detection heuristics, and automated testing pipelines.
- **Portfolio Website**: [iam-petero.vercel.app](https://iam-petero.vercel.app/)

---

## Technical Skills

### Languages
`Python` • `TypeScript` • `JavaScript (ES6+)` • `SQL` • `Bash`

### Backend Development
- **Frameworks & Runtimes**: FastAPI, Node.js, Express.js, Pydantic, SQLAlchemy
- **API Architecture**: RESTful API design, versioned contracts, error handling middleware, pagination
- **Security & Access Control**: Role-Based Access Control (RBAC), signed session cookies (HMAC-SHA256), JWT authentication, defensive input validation

### Frontend Development
- **Libraries & Frameworks**: React 18, Next.js 14 (App Router), Redux Toolkit
- **Styling & UI**: Tailwind CSS, responsive design systems, Framer Motion micro-interactions
- **Tooling & Build**: Vite, Webpack, PostCSS

### Databases & Persistence
- **Relational Databases**: Microsoft SQL Server (`msnodesqlv8`), PostgreSQL, MySQL, SQLite
- **Document Stores**: MongoDB
- **Data Engineering**: Schema design, foreign key constraints, database migrations, least-privilege database user roles

### Architecture & Engineering Practices
- **Design Patterns**: Clean Architecture (Domain → Application → Infrastructure isolation), Repository Pattern, Service Layer Pattern
- **Workflow Engines**: Multi-tier organizational approval routing, dynamic manager hierarchy traversal
- **Data Integrity**: Immutable audit logging, revision history, idempotent backfill scripts

### AI Evaluation & Quality Assurance
- **Model Evaluation**: Comparative response ranking, multi-step reasoning validation, constraint adherence testing
- **Heuristics & Verification**: Hallucination detection, source grounding verification, prompt rubric construction
- **Testing Suites**: Vitest (Next.js/React), PyTest (Python services), integration testing

### Tools & DevOps
- **Workflow & Environment**: Git, GitHub, Docker, Linux (Ubuntu/Debian), Postman, VS Code, Vercel

---

## Featured Projects

### 1. [KenGen ICT Budgeting Portal](https://github.com/petero-codes/budget-planner)
> **Enterprise Budgeting & Hierarchical Approval Platform**  
> *Next.js 14 (App Router) • TypeScript • SQL Server (`msnodesqlv8`) • Clean Architecture • Vitest • Tailwind CSS*

- **Problem Addressed**: KenGen ICT required a centralized annual budgeting portal to replace fragmented spreadsheets, enforce hierarchical multi-tier organizational approvals without hardcoding job titles, and generate immutable audit logs for financial reporting.
- **My Contribution**: Architected and developed the application end-to-end using Clean Architecture principles.
- **Key Features**:
  - **Clean Architecture Layers**: Strict isolation between Domain entities, Application use cases, and Infrastructure adapters (in-memory mock and SQL Server).
  - **Dynamic Tree-Based Approval Routing**: Traverses organizational manager hierarchies (`Users.managerId`) dynamically without brittle hardcoded executive titles.
  - **Multi-Tier Workflow**: Role-enforced workflow progression (`Staff Submission` → `Line Manager Review` → `General Manager Authorization` → `Finance Validation` → `Finalised`).
  - **Data Immutability & Audit Lineage**: Server-enforced lock preventing modifications once finalized; comprehensive chronological audit trail of all actions and comments.
  - **SAP CSV Export**: Generates validated SAP ERP-compliant CSV exports upon final administrative approval.
  - **Security & Testing**: Least-privilege SQL Server role configuration (`app_budget_ops`), signed session cookies, and unit tests written with Vitest.
- 🔗 [**Repository: budget-planner ↗**](https://github.com/petero-codes/budget-planner)

---

### 2. [AI-Powered Code Review Assistant](https://github.com/petero-codes/AI-Powered-Code-Review-Assistant)
> **Automated Code Quality & Static Evaluation Backend**  
> *Python • FastAPI • SQLAlchemy • SQLite • Pydantic v2 • Docker • REST APIs*

- **Problem Addressed**: Automating static code inspection, defect scoring, and structured quality metrics through high-throughput, containerized REST API endpoints.
- **My Contribution**: Built the complete FastAPI backend service, data models, and containerization.
- **Key Features**:
  - **FastAPI Service Architecture**: Asynchronous API endpoints for code analysis submission, review history retrieval, and score computation.
  - **Schema Validation**: Strict Pydantic models enforcing payload structure, code language parameter validation, and consistent response formats.
  - **Data Persistence**: SQLAlchemy ORM models managing user records, review metadata, static defect findings, and review history.
  - **Containerization**: Packaged with a multi-stage Dockerfile for reproducible local and cloud deployment.
- 🔗 [**Repository: AI-Powered-Code-Review-Assistant ↗**](https://github.com/petero-codes/AI-Powered-Code-Review-Assistant)

---

### 3. [Seekon Sneakerverse E-Commerce](https://github.com/petero-codes/frontend-sneeker-store)
> **Modern Footwear Storefront with Persistent State Management**  
> *React 18 • Redux Toolkit • Tailwind CSS • Vite • Framer Motion • REST APIs*

- **Problem Addressed**: Providing a fast, responsive e-commerce shopping experience for footwear discovery with instant faceted filtering and persistent cart state across sessions.
- **My Contribution**: Architected and built the complete frontend client application (collaborative project; integrated with dedicated backend services).
- **Key Features**:
  - **Faceted Product Filtering**: Client-side filtering by category, release date, and price range with instant visual updates.
  - **State Management**: Centralized Redux Toolkit slices (`cartSlice`, `productSlice`) ensuring cart persistence across page reloads and browser tabs.
  - **Interactive Experience**: Conversational shopping assistant widget, lazy-loaded product imagery, and 60fps micro-interactions with Framer Motion.
  - **Production Deployment**: Automated CI/CD deployment configured on Vercel.
- 🔗 [**Repository: frontend-sneeker-store ↗**](https://github.com/petero-codes/frontend-sneeker-store) • [**Live Storefront Demo ↗**](https://frontend-sneeker-store.vercel.app/)

---

### 4. [Autonomous Systems Automation Engine](https://github.com/petero-codes/automation-)
> **Low-Level Windows Process & Hardware Simulation Platform**  
> *Python • C Interception Driver • Win32 API • PyTest • Process Management*

- **Problem Addressed**: Executing programmatic desktop tasks on Windows systems with natural, human-indistinguishable input physics, multi-window hooks, and crash recovery.
- **My Contribution**: Sole developer of the automation suite, driver wrappers, and integration tests.
- **Key Features**:
  - **Kernel Driver Interface**: Interfaced with the C-based Interception kernel driver to simulate low-level hardware mouse and keyboard events safely.
  - **Bezier Curve Physics**: Formulated non-linear motor trajectory algorithms mimicking human motor pacing and natural deceleration.
  - **Stateful Resumption**: JSON-based session checkpoint manager enabling long-running workflows to resume execution after process restarts.
  - **Automated Test Suite**: Integration test suite (`tests/test_nextgen_suite.py`) validating driver state and window handle bindings before task execution.
- 🔗 [**Repository: automation- ↗**](https://github.com/petero-codes/automation-)

---

### 5. [Finance Club Market Analytics Dashboard](https://github.com/petero-codes/finnanceclub)
> **Real-Time Financial Analytics & Time-Series Data Dashboard**  
> *React • TypeScript • Tailwind CSS • Vite • REST APIs*

- **Problem Addressed**: Visualizing financial asset metrics, time-series market performance, and portfolio distributions smoothly across mobile and desktop devices.
- **My Contribution**: Built the responsive frontend analytics dashboard and charting components.
- **Key Features**:
  - **Interactive Charting**: Modular SVG/Canvas charting primitives rendering asset trends without frame drops during re-renders.
  - **Responsive Analytics Layout**: Dense multi-column financial metrics converted to accessible card layouts on mobile screens.
  - **Client-Side Data Caching**: Cached HTTP data fetching reducing redundant API requests and ensuring sub-100ms dashboard tab switching.
- 🔗 [**Repository: finnanceclub ↗**](https://github.com/petero-codes/finnanceclub) • [**Live Dashboard Demo ↗**](https://finnanceclub.vercel.app/)

---

## Engineering Approach

### 1. Backend Architecture & Clean Boundaries
I structure applications so that business domain logic remains strictly decoupled from external libraries, web frameworks, and database drivers. This makes use cases straightforward to unit-test in isolation, simplifies future database migrations, and prevents framework lock-in.

### 2. Defensive Validation & Data Integrity
I treat all client input as untrusted. In Python backends, request payloads are strictly validated using Pydantic schemas before reaching business logic handlers. In relational databases, data integrity is guaranteed at the persistence layer using explicit foreign keys, check constraints, unique indices, and ACID transactions rather than relying solely on application-level checks.

### 3. Server-Enforced Authorization & Security
Access control logic belongs on the server. I implement multi-tier role checks and workflow transition guards inside backend service handlers, ensuring that unauthorized state transitions (e.g. finalizing a budget without Finance privileges) are rejected regardless of client UI state. Authentication sessions utilize HMAC-signed cookies or scoped JWT tokens with least-privilege runtime access.

### 4. Testing & Verification
Code is only as reliable as its automated verification. I write unit and integration tests using `pytest` for Python services and `Vitest` for TypeScript/React applications, with emphasis on edge cases, authorization boundaries, and failure-handling paths.

### 5. AI Evaluation & Quality Assurance
In AI assessment and evaluation workflows, I apply empirical rubrics rather than subjective impressions. This includes:
- **Instruction Adherence**: Validating that model responses comply with complex multi-constraint system prompts.
- **Factuality & Hallucination Checking**: Cross-referencing generated claims against reference grounding documents.
- **Logical Consistency**: Identifying reasoning leaps, mathematical errors, or contradictory statements across iterative multi-turn dialogues.
- **Automated Validation**: Writing Python scripts to automate format compliance checking, diff analysis, and dataset batch verification.

---

## Contact & Profiles

- **Portfolio**: [iam-petero.vercel.app](https://iam-petero.vercel.app/)
- **GitHub**: [github.com/petero-codes](https://github.com/petero-codes)
- **LinkedIn**: [linkedin.com/in/peter-njuguna-13b00a411](https://www.linkedin.com/in/peter-njuguna-13b00a411)
- **Email**: [waynelulu6@gmail.com](mailto:waynelulu6@gmail.com)
