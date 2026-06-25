# ProxyLens

**ProxyLens** is a full-stack SEO, proxy rotation, and web scraping monitoring platform designed to help developers monitor public web pages, manage proxy pools, run SEO audits, track scraping jobs, analyze request performance, and export useful reports.

The project is built as a developer-focused SaaS-style tool for understanding and managing responsible web scraping workflows. It combines scraping automation, proxy health monitoring, job queues, request logging, SEO analysis, and dashboard analytics in one platform.

## Overview

Web scraping becomes more complex as request volume increases. Developers need more than a simple script; they need visibility into request behavior, proxy performance, failed jobs, response times, SEO issues, and ethical scraping checks.

ProxyLens solves this by providing a structured platform where users can create projects, add target URLs, run scraping jobs, monitor proxy health, review request logs, perform SEO audits, and export reports for further analysis.

The goal of ProxyLens is not to encourage aggressive or abusive scraping. Instead, it focuses on responsible data collection, clear monitoring, rate-aware workflows, and practical SEO insights.

## Key Features

* User authentication and project management
* URL and scraping job creation
* Proxy pool management
* Proxy health checks
* Background scraping workers
* Job queue system
* Request logging and monitoring
* SEO audit checks
* Proxy health dashboard
* SEO analytics dashboard
* Charts and performance insights
* Ethical scraping checklist
* CSV report export

## SEO Monitoring Features

ProxyLens includes SEO-focused checks to help users analyze public web pages and identify common technical SEO issues.

Planned SEO checks include:

* Page title detection
* Meta description detection
* H1, H2, and H3 heading structure
* Canonical URL detection
* Internal and external link analysis
* Broken link detection
* Image alt text checks
* HTTP status code tracking
* Redirect tracking
* Robots.txt availability
* Robots meta tag detection
* Page response time analysis

## Proxy Monitoring Features

ProxyLens allows users to manage and monitor proxy performance across scraping workflows.

Planned proxy features include:

* Add and manage proxy providers
* Store proxy host, port, protocol, country, and credentials
* Track proxy status
* Monitor average response time
* Track success and failure rates
* Detect slow, failing, or blocked proxies
* Rotate proxies during scraping jobs
* Log which proxy was used for each request

## Responsible Scraping

ProxyLens is designed with responsible scraping principles in mind.

Before creating scraping jobs, users are encouraged to review an ethical scraping checklist, including:

* Whether the target data is publicly accessible
* Whether the website provides an official API
* Whether robots.txt has been reviewed
* Whether request limits are reasonable
* Whether personal or sensitive data is being avoided
* Whether the website’s terms and policies have been considered

## Tech Stack

### Frontend

* Next.js
* TypeScript
* Tailwind CSS
* Shadcn UI
* TanStack Query
* Recharts

### Backend

* Django
* Django REST Framework
* PostgreSQL
* Celery
* Redis

### Scraping and SEO

* Playwright Python
* BeautifulSoup or selectolax
* Requests or HTTPX
* Robots.txt checker
* CSV export

### Deployment

* Docker
* Docker Compose
* PostgreSQL
* Redis

## Core Modules

### Authentication

Handles user registration, login, logout, and user-specific access to projects, jobs, and reports.

### Projects

Allows users to group URLs, jobs, audits, and reports under separate monitoring projects.

### URL and Job Management

Allows users to add public URLs, configure scraping jobs, set job status, and run jobs manually or on a schedule.

### Proxy Pool Management

Allows users to add, test, and monitor proxies used during scraping workflows.

### Scraping Worker

Runs scraping jobs in the background, selects proxies, sends requests, validates responses, performs SEO checks, and stores results.

### Job Queue

Uses Redis and Celery to process scraping jobs, proxy health checks, SEO audits, and report exports asynchronously.

### Request Logs

Stores detailed request information such as target URL, proxy used, response status, response time, retry count, error message, and timestamp.

### Proxy Health Dashboard

Displays proxy performance metrics, including healthy proxies, failed proxies, slow proxies, average latency, and success rate.

### SEO Dashboard

Displays SEO audit results, missing metadata, broken links, heading issues, response problems, and page performance insights.

### Reports

Allows users to export request logs, proxy health data, SEO audits, and job performance summaries as CSV files.

## Project Goals

The main goals of ProxyLens are to:

* Build a realistic full-stack developer tool
* Explore proxy rotation from both backend and frontend perspectives
* Understand scraping workflows beyond simple scripts
* Practice background jobs and queue-based architecture
* Build dashboards for technical monitoring
* Add SEO analysis to make the tool more commercially useful
* Promote responsible and ethical scraping practices
* Create a strong portfolio project for full-stack development and technical writing

## Planned Architecture

```text
Next.js Frontend
        ↓
Django REST API
        ↓
PostgreSQL Database
        ↓
Redis Queue
        ↓
Celery Workers
        ↓
Scraping, SEO Audits, Proxy Checks, Report Exports
```

## Development Roadmap

### Phase 1: Foundation

* Set up Django backend
* Set up PostgreSQL
* Configure Django REST Framework
* Create authentication flow
* Create project and target URL models
* Build initial frontend dashboard layout

### Phase 2: Jobs and Logs

* Create scraping job model
* Add manual job execution
* Store request logs
* Display logs on the frontend
* Add basic status tracking

### Phase 3: Proxy Management

* Add proxy provider model
* Add proxy model
* Implement proxy health checks
* Add basic proxy rotation
* Build proxy health dashboard

### Phase 4: SEO Auditing

* Extract page title
* Extract meta description
* Analyze headings
* Detect canonical tags
* Analyze links
* Track status codes and response time
* Store SEO audit results

### Phase 5: Analytics and Reports

* Add dashboard charts
* Show job success and failure rates
* Show proxy performance metrics
* Show SEO issue summaries
* Export reports as CSV

### Phase 6: Advanced Features

* Scheduled scraping jobs
* Real-time job updates
* PDF report export
* Team accounts
* API keys
* Webhooks
* Subscription and usage limits
* Multi-provider proxy failover

## Project Status

ProxyLens is currently in the early development stage. The first milestone is to build the backend foundation, create the core database models, and allow users to create projects and add target URLs.

## Disclaimer

ProxyLens is intended for learning, monitoring, and responsible analysis of publicly accessible web pages. Users should respect website terms, robots.txt directives, applicable laws, and ethical data collection practices.
