# ZeeUI

ZeeUI is an Odoo module that provides a **dynamic UI and dashboard management** experience.  
It improves usability and navigation with customizable menus, icons, and dashboard views.  

## Features
- Dynamic dashboards with configurable widgets
- UI/UX enhancements (icons, menus, layouts)
- Integrated **Chart.js** for interactive charts
- Built-in **Font Awesome** support for icons
- Backend and website compatibility

## Installation
1. Copy the module folder `zee_ui` into your Odoo custom addons directory.
2. Update your Odoo apps list:
   ```bash
   ./odoo-bin -u zee_ui -d <your-database>
    ```
3. Activate the module from the Odoo Apps menu.

## Requirements

- Odoo 18 (or compatible version)
- Python 3.10+
- Dependencies: Chart.js (bundled), Font Awesome (bundled)

## Configuration

No extra configuration required. Once installed, ZeeUI is ready to use.

## License

This module is licensed under a Commercial License.
See [LICENSE](LICENSE)