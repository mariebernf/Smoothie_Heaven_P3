# Smoothie_Heaven_P3

## Description

## Project requirements

## User stories

## Design

### Colour scheme

### Typography

### Wireframe

## Features

## Technologies used

## Tools used

## Deployment

## Testing

## Bugs and Fixes

**Issue:** Registration form would not render, 'CSRF Token' error.

**Resolved:** I corrected the error, which was a spelling mistake. I had 'Crsf' instead of 'Csrf'.

---
**Issue:** Base template not found, after setting up registration view. 

**Resolved:** Properly referenced in the templates settings. 
Updated 'DIRS' setting in 'setting.py' to include the correct template.

---

**Issue:** I installed crispy-forms, but it would not work.

**Resolved:** I installed crispy-bootstrap5 for compatibility, and it now works as intended.

---

**Issue:** The logout page was not working and returned a 405 error.

**Resolved:** Resolved by making sure the correct method (POST) was used.

---

**Issue:** Smoothie detail page was returning a 404 error because the URL pattern and view were not correctly set up.

**Resolved:** Updated urls.py with the correct path for smoothie detail view.

---

## Credits
