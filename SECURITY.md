# Security policy

## Supported version

Security fixes are applied to the `main` branch. This repository contains MapLibre GL JS frontend patterns; it is not a hosted service.

## Reporting a vulnerability

Email **zqmcomputing@gmail.com** with the subject `maplibre-patterns security` if you find a vulnerability in the example code or workflow configuration. Please do not open a public issue for a sensitive report.

Include the affected file, the impact you observed, and reproduction steps when available.

## API keys

Client-side map code ships to browsers, so anything in it is public. The patterns use placeholder keys and local tile endpoints; never commit a real API key or token into an example here, and treat any committed credential you spot as a security issue to report, not to use.
