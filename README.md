# NFE UMT - National Federation of Education Management System

## Overview
This system manages members, membership cards, and organizational structures for the National Federation of Education. It provides functionality for:
- Member management with detailed profiles
- Membership card tracking
- Organizational structure management
- Financial tracking (income/expenses)

## Setup
1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

## Project Structure
- `core/` - Core application settings and configurations
- `members/` - Member management functionality
- `cards/` - Membership card management
- `organization/` - Organizational structure management
- `finance/` - Financial management

## Features
1. Member Management
   - Complete member profiles
   - Educational and professional information
   - Contact details

2. Membership Cards
   - Card issuance and renewal
   - Status tracking
   - Payment management

3. Organizational Structure
   - Executive office management
   - Regional and local office management
   - Committee management

4. Financial Management
   - Income tracking
   - Expense management
   - Financial reporting
