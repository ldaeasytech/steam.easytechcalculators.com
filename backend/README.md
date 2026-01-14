# Water & Steam Property Calculator API

This project provides a web-based water and steam thermodynamic property calculator
based on the **IAPWS Industrial Formulation 1997 (IF97)**.

The backend is implemented using **Python + FastAPI** and exposes a simple REST API
that computes thermodynamic and transport properties of water and steam.

## Features

- Automatic phase determination
  - Subcooled / compressed liquid
  - Saturated water / vapor
  - Superheated steam
- Thermodynamic properties
  - Density
  - Specific volume
  - Enthalpy
  - Entropy
  - Cp and Cv
- Transport properties
  - Dynamic viscosity
  - Thermal conductivity
- Based on IAPWS-IF97 equations
- Suitable for engineering calculations

## API Endpoint

### GET `/api/water`

**Query Parameters**

| Parameter | Description | Unit |
|---------|------------|------|
| `T` | Temperature | °C |
| `P` | Pressure | MPa |

**Example**

